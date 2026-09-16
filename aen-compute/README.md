# AEN Compute Infrastructure

**Status:** LOCKED v0.1 research baseline / active prototype  
**Branch:** `aen-compute-infrastructure`  
**Small Systems Lab**  
**Physical machine specification:** [`PHYSICAL-CONSTRUCTION-SPEC-V0.1.md`](./PHYSICAL-CONSTRUCTION-SPEC-V0.1.md)  
**Authoritative baseline:** [`LOCKED-BASELINE-V0.1.md`](./LOCKED-BASELINE-V0.1.md)  
**Build sequence:** [`BUILD-PLAN-V0.1.md`](./BUILD-PLAN-V0.1.md)  
**Compute boundary research:** [`RESEARCH-CENTRALIZATION-BOUNDARY.md`](./RESEARCH-CENTRALIZATION-BOUNDARY.md)

## What AEN-CB01 physically is

AEN-CB01 is a three-module machine plus a separate solar source:

- **AEN-E:** a powder-coated steel battery/power cabinet containing certified LFP rack modules, BMS, disconnects, protection, inverter/charger, solar charge interface, and telemetry.
- **AEN-C:** a steel 19-inch compute rack containing a GPU compute node, CPU, memory, NVMe storage, networking, filters, controls, and electrical/thermal instrumentation.
- **AEN-T:** an insulated steel thermal cabinet containing copper/aluminum heat-transfer hardware, a sealed heat-transfer loop or contained hot-air path, temperature/flow/leak sensors, replaceable thermal-storage media, and a dry radiator for heat that cannot be reused.
- **Solar source:** a separate approximately 3 kW v0.1 PV research array using commercial framed modules, aluminum mounting rails, weather-rated DC protection, and an MPPT/hybrid charge interface.

The battery, compute, and thermal systems are intentionally **not placed in one enclosure**. They have different fire, service, cooling, and maintenance requirements. See the physical construction specification for materials, preliminary dimensions, interfaces, sensors, cooling loop, thermal storage, and assembly sequence.

## Mission

AEN Compute is infrastructure for **expanding AI capability in Africa without requiring Africa to inherit the most resource-intensive assumptions of conventional data-center growth**.

The problem is not AI growth itself. AI can expand education, research, healthcare, agriculture, creative practice, public services, scientific capacity, local industry, and economic participation across the continent.

The infrastructure bottleneck is that modern AI is often tied to data-center models that assume abundant grid electricity, large concentrated power loads, intensive heat rejection, and in some designs substantial water use.

AEN asks:

> How can Africa scale AI compute aggressively while redesigning the energy and thermal infrastructure underneath it?

The aim is **more African compute capacity, not less**.

## Core proposition

AEN Compute investigates a distributed, solar-first compute architecture in which electrical storage, compute hardware, heat recovery, thermal storage, networking, and governance are designed as one system.

```text
SUN
  |
  v
SOLAR PV
  |
  v
AEN-E: ELECTRICAL STORAGE
LFP cassettes + protected DC bus
  |
  v
AEN-C: COMPUTE
GPU / CPU / accelerator clusters
  |
  +------------------------+
  |                        |
  v                        v
AI WORK                  RECOVERABLE HEAT
                           |
                           v
                    AEN-T: THERMAL STORAGE
                           |
                           v
                     USEFUL SECOND LOAD
```

The long-term architecture is not limited to one workstation. AEN Compute should be able to scale from edge systems and university research nodes to interconnected regional compute fabrics where the engineering supports it.

## The data-center problem AEN addresses

Conventional AI infrastructure concentrates enormous quantities of computation into a small number of physical sites. That concentration creates corresponding requirements for continuous high-capacity electricity, transmission and grid infrastructure, large thermal-management systems, water in cooling architectures that depend on it, backup generation, land, capital concentration, and dependence on distant cloud providers.

AEN does not assume these constraints are inevitable properties of AI. They are partly properties of **how compute infrastructure has been architected**.

The research question is therefore not "How little AI can Africa afford to run?"

It is:

> **What infrastructure would allow Africa to run far more AI without reproducing the same electricity, water, and centralization bottlenecks?**

## AEN-E — Electrical infrastructure

AEN-E supplies compute through modular electrical storage and solar-first generation. Research goals include scalable solar generation, modular LFP storage, protected DC distribution, DC-first pathways where technically advantageous, grid connection as supplemental resilience rather than a prerequisite where possible, transparent energy measurement and provenance, modular expansion from one block to many blocks, and hardware safety independent of AI/software control.

## AEN-C — Compute infrastructure

AEN-C is the compute layer.

```text
EDGE NODE
    -> single accelerator

AEN COMPUTE BLOCK
    -> workstation / multi-GPU node

AEN COMPUTE CLUSTER
    -> multiple networked blocks

AEN COMPUTE FABRIC
    -> geographically distributed regional capacity
```

AEN does **not** assume every frontier-model workload can be decomposed across widely separated nodes. Some workloads require tightly coupled accelerators and very high-bandwidth interconnects. Those limits should be measured rather than ignored.

## AEN-T — Heat as infrastructure

Almost all electrical energy consumed by compute ultimately becomes heat. Conventional facilities primarily treat this as something to remove. AEN-T asks how much of it can instead be captured, buffered, stored, transported, or reused before final dissipation.

AEN-T is an energy-cascading system, not a perpetual-energy system. Low-temperature waste heat cannot be reconverted to electricity without significant thermodynamic losses.

## Scale, rather than restriction

AEN should use environmental information to **increase usable compute capacity**, not merely to throttle it. Instead of one facility hitting an electricity or cooling ceiling, additional AEN blocks can contribute capacity to the network.

> **Make renewable generation, storage, heat recovery, and distributed orchestration tools for scaling compute.**

## Ethical AI growth

AEN supports rapid AI development while making infrastructure costs visible and governable. Ethical growth does not mean artificially restricting useful African AI capability. It means avoiding a development model in which the benefits of AI grow while energy, water, land, data, labor, or environmental costs are externalized onto host communities.

## African infrastructure context

Africa is not one climate, energy market, network environment, or political jurisdiction. AEN Compute must therefore be locally engineered. Climate adaptations may differ substantially between humid coastal environments, Sahelian regions, high-altitude locations, and temperate zones.

Nigeria is a strong candidate for an initial research program because AEN originated from questions of distributed energy resilience, modular storage, solar input, and reduced generator dependence.

## v0.1 — proof of architecture

**AEN-CB01** is intentionally small because its job is to validate the architecture, not define the final scale.

Initial research target: approximately 1.2 kW compute design load, 12 kWh nominal LFP storage, 3 kW preliminary solar, instrumented electrical and thermal flows, zero operational cooling-water target for the prototype, heat recovery, workload scheduling, and hardware safety independent of the scheduler.

## Central research question

> **Can Africa build substantially more AI compute capacity by redesigning the data center itself — using distributed solar generation, modular storage, heat recovery, climate-adaptive cooling, and networked compute blocks as a new infrastructure model?**

That is the thesis of AEN Compute.
