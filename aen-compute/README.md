# AEN Compute Infrastructure

**Status:** LOCKED v0.1 research baseline / active prototype  
**Branch:** `aen-compute-infrastructure`  
**Small Systems Lab**  
**Authoritative baseline:** [`LOCKED-BASELINE-V0.1.md`](./LOCKED-BASELINE-V0.1.md)  
**Build sequence:** [`BUILD-PLAN-V0.1.md`](./BUILD-PLAN-V0.1.md)  
**Compute boundary research:** [`RESEARCH-CENTRALIZATION-BOUNDARY.md`](./RESEARCH-CENTRALIZATION-BOUNDARY.md)

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

Conventional AI infrastructure concentrates enormous quantities of computation into a small number of physical sites. That concentration creates corresponding requirements for:

- continuous high-capacity electricity;
- transmission and grid infrastructure;
- large thermal-management systems;
- water in cooling architectures that depend on it;
- backup generation and resilience systems;
- land and physical infrastructure;
- capital concentration;
- dependence on distant cloud providers.

AEN does not assume these constraints are inevitable properties of AI. They are partly properties of **how compute infrastructure has been architected**.

The research question is therefore not "How little AI can Africa afford to run?"

It is:

> **What infrastructure would allow Africa to run far more AI without reproducing the same electricity, water, and centralization bottlenecks?**

## AEN-E — Electrical infrastructure

AEN-E supplies compute through modular electrical storage and solar-first generation.

Research goals:

- scalable solar generation;
- modular LFP storage;
- protected DC distribution;
- DC-first pathways where technically advantageous;
- grid connection as supplemental resilience rather than a prerequisite where possible;
- transparent energy measurement and provenance;
- modular expansion from one block to many blocks;
- hardware safety independent of AI/software control.

## AEN-C — Compute infrastructure

AEN-C is the compute layer.

It should support progressive scaling:

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

Research areas include:

- local inference;
- model fine-tuning;
- scientific and university computing;
- multimodal AI;
- locally hosted models and services;
- distributed training where network topology makes it practical;
- workload migration between blocks;
- energy-aware and temperature-aware scheduling;
- high-speed interconnect requirements for workloads that cannot be efficiently distributed.

AEN does **not** assume every frontier-model workload can be decomposed across widely separated nodes. Some workloads require tightly coupled accelerators and very high-bandwidth interconnects. Those limits should be measured rather than ignored.

## AEN-T — Heat as infrastructure

Almost all electrical energy consumed by compute ultimately becomes heat.

Conventional facilities primarily treat this as something to remove. AEN-T asks how much of it can instead be captured, buffered, stored, transported, or reused before final dissipation.

Research areas include:

- dry heat rejection;
- heat pipes and thermosyphon systems;
- closed-loop cooling;
- phase-change thermal storage;
- ceramic or solid thermal media;
- modular thermal cassettes;
- water-free or extremely low-water operating modes;
- useful secondary heat loads such as drying, hot-water preheat, greenhouse heat, or suitable process heat.

AEN-T is an energy-cascading system, not a perpetual-energy system. Low-temperature waste heat cannot be reconverted to electricity without significant thermodynamic losses.

## Scale, rather than restriction

AEN should use environmental information to **increase usable compute capacity**, not merely to throttle it.

For example, the orchestration layer can determine where additional compute can run most efficiently:

```text
BLOCK A
high solar surplus
thermal capacity available
    -> accept additional workload

BLOCK B
battery low
thermal store near limit
    -> shift workload elsewhere

BLOCK C
cool ambient conditions
large renewable surplus
    -> accept compute-intensive job
```

Instead of one facility hitting an electricity or cooling ceiling, additional AEN blocks can contribute capacity to the network.

The design goal is therefore:

> **Make renewable generation, storage, heat recovery, and distributed orchestration tools for scaling compute.**

## Ethical AI growth

AEN supports rapid AI development while making infrastructure costs visible and governable.

Ethical growth does not mean artificially restricting useful African AI capability. It means avoiding a development model in which the benefits of AI grow while energy, water, land, data, labor, or environmental costs are externalized onto host communities.

Design principles include:

- **African compute capacity:** increase locally available AI infrastructure.
- **Infrastructure sovereignty:** reduce total dependence on foreign cloud infrastructure where local capacity is practical.
- **Data sovereignty:** support locally controlled storage, models, and services.
- **Water protection:** engineer cooling around minimal operational water consumption where feasible.
- **Renewable expansion:** add generation and storage alongside compute growth.
- **Heat recovery:** seek secondary value from compute heat.
- **Accessibility:** design hardware, software, documentation, education, and employment pathways for disabled users and workers from the beginning.
- **Community benefit:** host communities should receive tangible infrastructure and economic value.
- **Human governance:** people and institutions define priorities; scheduling software executes them.
- **Transparency:** measure energy source, energy use, thermal output, water use, hardware utilization, and local benefit.

## African infrastructure context

Africa is not one climate, energy market, network environment, or political jurisdiction. AEN Compute must therefore be locally engineered.

Potential deployment contexts include:

- universities and research institutions;
- schools and technical education;
- hospitals and health research;
- agricultural and climate computing;
- creative-technology labs;
- locally hosted language and cultural models;
- startups and SMEs;
- public-interest digital infrastructure;
- regional AI and cloud providers.

Climate adaptations may differ substantially between humid coastal environments, Sahelian regions, high-altitude locations, and temperate zones.

Nigeria is a strong candidate for an initial research program because AEN originated from questions of distributed energy resilience, modular storage, solar input, and reduced generator dependence.

## v0.1 — proof of architecture

**AEN-CB01** is intentionally small because its job is to validate the architecture, not define the final scale.

Initial research target:

- ~1.2 kW compute design load;
- ~12 kWh nominal LFP storage target;
- ~3 kW preliminary solar target;
- instrumented electrical and thermal flows;
- zero operational cooling-water target for the prototype;
- heat-recovery pathway;
- workload scheduler;
- hardware safety independent of scheduler.

The next phases should explicitly test **scale-out**:

1. one compute block;
2. multiple blocks on one site;
3. shared solar/storage infrastructure;
4. high-speed local compute cluster;
5. geographically distributed AEN compute fabric;
6. comparison against conventional data-center energy, water, cost, performance, and reliability metrics.

## Central research question

> **Can Africa build substantially more AI compute capacity by redesigning the data center itself — using distributed solar generation, modular storage, heat recovery, climate-adaptive cooling, and networked compute blocks as a new infrastructure model?**

That is the thesis of AEN Compute.
