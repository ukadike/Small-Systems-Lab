"""AEN Compute v0.1 scheduler simulator.

Software-only proof of the placement idea. No battery or electrical control.
The scheduler chooses between simulated AEN compute blocks using energy and
thermal state, while preserving a protected battery reserve.
"""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class BlockState:
    name: str
    solar_surplus_w: float
    battery_soc_pct: float
    protected_reserve_pct: float
    gpu_temp_c: float
    thermal_headroom_pct: float
    queue_jobs: int
    hardware_ok: bool = True
    network_ok: bool = True


@dataclass
class Job:
    name: str
    priority: str = "discretionary"  # discretionary | priority


def eligible(block: BlockState, job: Job) -> bool:
    if not block.hardware_ok or not block.network_ok:
        return False
    if block.gpu_temp_c >= 85:
        return False
    if block.thermal_headroom_pct < 15:
        return False

    # Priority jobs can consume reserve margin operationally, but this simple
    # simulator still requires a small emergency floor. Hardware protection
    # would remain authoritative in a physical system.
    if job.priority == "priority":
        return block.battery_soc_pct > 10

    return block.battery_soc_pct > block.protected_reserve_pct


def score(block: BlockState) -> float:
    battery_headroom = max(0.0, block.battery_soc_pct - block.protected_reserve_pct)

    # Transparent v0.1 weights; these are research parameters, not optimized
    # production coefficients.
    return (
        0.002 * block.solar_surplus_w
        + 0.08 * battery_headroom
        + 0.06 * block.thermal_headroom_pct
        - 0.05 * max(0.0, block.gpu_temp_c - 50.0)
        - 0.75 * block.queue_jobs
    )


def choose_block(blocks: List[BlockState], job: Job) -> Optional[BlockState]:
    candidates = [block for block in blocks if eligible(block, job)]
    if not candidates:
        return None
    return max(candidates, key=score)


def explain(block: BlockState) -> str:
    return (
        f"{block.name}: score={score(block):.2f}, "
        f"solar_surplus={block.solar_surplus_w:.0f}W, "
        f"battery={block.battery_soc_pct:.0f}%, "
        f"gpu_temp={block.gpu_temp_c:.0f}C, "
        f"thermal_headroom={block.thermal_headroom_pct:.0f}%, "
        f"queue={block.queue_jobs}"
    )


def run_scenario(title: str, blocks: List[BlockState], job: Job) -> None:
    print(f"\n=== {title} ===")
    print(f"Job: {job.name} ({job.priority})")

    for block in blocks:
        state = "ELIGIBLE" if eligible(block, job) else "INELIGIBLE"
        print(f"{state}: {explain(block)}")

    selected = choose_block(blocks, job)
    if selected is None:
        print("DECISION: queue job; no block may safely accept it")
    else:
        print(f"DECISION: run on {selected.name}")


def main() -> None:
    job = Job("batch-embedding-job")

    run_scenario(
        "A: Node A has renewable and thermal headroom",
        [
            BlockState("A", 1600, 78, 30, 58, 80, 0),
            BlockState("B", 100, 34, 30, 73, 35, 1),
        ],
        job,
    )

    run_scenario(
        "B: Conditions reverse",
        [
            BlockState("A", 80, 36, 30, 72, 30, 1),
            BlockState("B", 1500, 82, 30, 57, 84, 0),
        ],
        job,
    )

    run_scenario(
        "C: Both blocks protect reserve / thermal limits",
        [
            BlockState("A", 0, 25, 30, 79, 20, 0),
            BlockState("B", 0, 29, 30, 82, 12, 0),
        ],
        job,
    )


if __name__ == "__main__":
    main()
