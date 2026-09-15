# AEN Compute v0.1 — Build Plan

**Goal:** Demonstrate that two compute blocks can route real AI workloads according to live energy and thermal conditions before building a larger physical system.

## Principle

Do not start by building a data center. Start by proving the control architecture.

The first success criterion is simple:

> Given two GPU-capable nodes with different energy and thermal conditions, the AEN scheduler chooses the better node for a non-urgent workload, records why, and can switch future jobs when conditions change.

This is workload placement, not live migration of a running GPU process.

---

## Phase 0 — Digital twin

Build a software-only simulator for two AEN blocks.

Each block exposes:

- solar generation estimate (W)
- battery state of charge (%)
- battery reserve threshold (%)
- GPU power draw (W)
- GPU temperature (C)
- ambient temperature (C)
- thermal-store headroom (%)
- network availability
- workload queue

The scheduler assigns jobs using transparent rules and logs the decision.

**Pass condition:** changing solar, battery, or thermal conditions changes which node receives a job in the expected direction.

---

## Phase 1 — Two real compute nodes on ordinary power

Use two Linux machines with NVIDIA GPUs. They do not need to be identical.

Recommended prototype topology:

```text
AEN CONTROLLER
    |
    +---- Ethernet ---- AEN NODE A (GPU)
    |
    +---- Ethernet ---- AEN NODE B (GPU)
```

The controller may run on one of the nodes for the first prototype, but a separate low-power machine is cleaner later.

### GPU telemetry

Use NVIDIA DCGM / DCGM Exporter on each Linux GPU node. Capture at least:

- GPU utilization
- GPU temperature
- board power
- total energy consumption where supported
- memory utilization
- enforced power limit

Prometheus stores time-series telemetry. Grafana can be added for visualization, but the scheduler should read machine-readable metrics directly.

### Workload layer

Use Ray for the first distributed runtime.

Why Ray:

- native CPU/GPU resource scheduling;
- multiple machines can join one cluster;
- jobs can be submitted programmatically;
- node labels and affinity allow the AEN controller to choose a specific eligible node;
- it scales from a small research prototype to larger clusters.

Important design choice: dynamic energy conditions should live in the AEN controller, not be encoded as static Ray resources. Ray resources are excellent for GPU/CPU availability, while AEN continuously evaluates battery and thermal state and then targets an eligible node.

### First real workload

Use a workload that can run independently on either node, such as:

- batch image inference;
- embedding generation;
- transcription;
- small/medium LLM inference;
- document processing;
- parameter-efficient fine-tuning that fits one node.

Do **not** use multi-node synchronous training as the first test.

**Pass condition:** the same job can be executed on Node A or Node B, and AEN selects the node from telemetry rather than by a hard-coded round-robin rule.

---

## Phase 2 — Real electrical telemetry

Before connecting AEN solar/storage hardware, measure each compute node's actual wall energy with a certified external meter or professionally integrated power monitor.

Add:

- node electrical input power (W)
- cumulative electrical energy (Wh/kWh)
- peak demand

Compare wall input against GPU-only DCGM readings. The difference includes CPU, memory, storage, networking, PSU losses, and cooling.

**Pass condition:** every completed workload has an energy record: start time, finish time, node, GPU energy estimate, whole-node electrical energy, and thermal profile.

---

## Phase 3 — Integrate certified AEN storage

Only after the scheduler and telemetry work, connect a certified battery-energy-storage / inverter system through a qualified electrical design.

Do not prototype with loose lithium cells, improvised high-voltage packs, or backfeeding building circuits.

Expose battery-system telemetry to the controller using a supported interface such as a documented API, Modbus, CAN gateway, or vendor telemetry interface.

Minimum fields:

- state of charge
- charge/discharge power
- pack temperature
- available discharge energy
- battery fault state
- inverter fault state

**Pass condition:** the scheduler avoids assigning a discretionary workload to a node whose battery reserve would be violated.

---

## Phase 4 — Add solar input

Connect AEN storage to a professionally designed solar array and MPPT / inverter architecture.

Add telemetry for:

- current PV output
- cumulative PV energy
- forecast or near-term expected PV generation
- battery charging power

Scheduler behavior now distinguishes between:

- renewable surplus;
- battery-supported operation;
- protected reserve;
- supplemental grid energy if present.

**Pass condition:** a flexible job is preferentially scheduled when/where renewable energy is available without compromising reserved services.

---

## Phase 5 — Thermal instrumentation

Instrument the compute node and its heat path.

Measure:

- GPU and CPU temperatures
- inlet air temperature
- exhaust / heat-transfer temperature
- thermal-store inlet/outlet temperature where applicable
- thermal-store state / estimated headroom
- fan or pump electrical consumption if used

The objective is not to claim that heat has disappeared. The objective is to account for where it goes and how much can be reused.

**Pass condition:** a compute job has both an electrical-energy record and a corresponding thermal-energy estimate / heat-flow record.

---

## Phase 6 — AEN-T heat capture prototype

Add one safe, engineered heat-recovery pathway.

Candidate research directions include:

- air-to-solid thermal storage;
- heat pipe / thermosyphon transfer;
- closed-loop heat exchanger;
- phase-change thermal buffer;
- low-temperature secondary heat use.

A thermal engineer should validate temperatures, materials, containment, fire behavior, service access, and failure modes before fabrication.

**Pass condition:** recover a measurable fraction of compute heat into a secondary thermal store or useful load without exceeding processor, battery, enclosure, or ambient safety limits.

---

## Phase 7 — Multi-block AEN Fabric

Once two local nodes work, add more nodes/sites.

The architecture becomes hierarchical:

```text
TIGHTLY COUPLED LOCAL POD
  GPUs connected by high-speed local fabric
           |
           v
AEN SITE CONTROLLER
           |
           v
AEN REGIONAL FABRIC
  loosely coupled jobs / inference / batch work
```

Do not attempt to replace NVLink/InfiniBand-class local communication with ordinary wide-area Internet for workloads that need synchronous high-bandwidth exchange.

Instead, move the workloads that are naturally mobile:

- inference replicas;
- batch inference;
- embeddings;
- document/media processing;
- independent fine-tunes;
- evaluation;
- rendering;
- scientific jobs with coarse-grained parallelism;
- federated or asynchronous training designs.

---

## AEN scheduler v0.1

A simple first scoring model is enough:

```text
eligible =
    hardware_ok
    AND network_ok
    AND battery_soc > protected_reserve
    AND gpu_temp < thermal_limit
    AND thermal_headroom > minimum_headroom

score =
    renewable_surplus_weight
  + battery_headroom_weight
  + thermal_headroom_weight
  - gpu_temperature_penalty
  - queue_delay_penalty
```

Priority services may bypass ordinary ranking while still respecting hardware safety.

The scheduler should log the inputs, score, selected node, and reason for every decision.

---

## Minimal software stack

```text
Linux on each GPU node
NVIDIA driver + DCGM
DCGM Exporter
Prometheus
Ray
AEN scheduler service (Python)
AEN telemetry adapters
Optional Grafana dashboard
```

NVIDIA DCGM provides GPU power and thermal telemetry. Ray provides the distributed compute substrate. AEN's novel layer is the energy/thermal-aware orchestration and accounting above them.

---

## What we need physically for the first real test

1. Two GPU-capable Linux computers.
2. Wired local network.
3. One controller machine or one node acting as controller.
4. Certified external electrical measurement for each node.
5. Temperature sensors for ambient/inlet/exhaust validation.
6. Later: certified LFP storage / inverter system.
7. Later: professionally designed solar input.
8. Later: engineered thermal-store prototype.

The first software prototype does **not** require batteries, solar panels, or custom cooling hardware.

---

## First demonstration

Run the same batch inference job under three controlled scenarios:

### Scenario A
Node A: high simulated/real solar surplus, cool, battery healthy.  
Node B: low reserve, warmer.

**Expected:** AEN schedules Node A.

### Scenario B
Conditions reverse.

**Expected:** AEN schedules Node B.

### Scenario C
Both blocks below reserve / thermal limits.

**Expected:** AEN queues a discretionary job rather than violating the reserve policy.

The demo dashboard should show:

- incoming job;
- live state of each block;
- scheduler decision;
- workload execution;
- energy consumed;
- heat produced / estimated;
- reason for placement.

That is the smallest convincing proof of the AEN Compute thesis.
