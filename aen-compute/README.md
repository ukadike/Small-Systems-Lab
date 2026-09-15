# AEN Compute Infrastructure

**Status:** Research / prototype architecture  
**Branch:** `aen-compute-infrastructure`  
**Small Systems Lab**

## Research proposition

AEN Compute investigates whether AI computation can be decomposed into distributed, solar-first compute blocks whose electrical storage, thermal storage, environmental limits, and computational demand are managed as one integrated system.

The project asks a different question from conventional data-center design:

> What if compute capacity were governed by ecological capacity rather than assuming effectively unlimited electricity, cooling, water, and thermal rejection?

AEN Compute does **not** claim to replace all hyperscale data centers. It is a research architecture for workloads that can operate on distributed or edge infrastructure, especially where solar generation, local resilience, water protection, and community ownership are priorities.

## Core architecture

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
GPU / CPU / local ML runtime
  |
  v
RECOVERABLE HEAT
  |
  v
AEN-T: THERMAL STORAGE
phase-change / solid thermal media / other validated storage
  |
  v
SECOND USE
space heating / water preheat / drying / greenhouse / suitable process heat
```

## AEN-E — Electrical layer

AEN-E receives energy from solar-first source infrastructure and stores it in protected modular LFP energy cassettes.

Key requirements:

- solar-first operation;
- battery management and hardware safety independent of AI control;
- modular storage capacity;
- source and energy provenance;
- DC-first pathways where technically appropriate;
- no unsafe backfeeding or improvised building wiring.

## AEN-C — Compute layer

AEN-C turns stored electrical energy into useful computation.

Initial research target:

- one high-end GPU workstation or equivalent research compute node;
- approximately 1.2 kW initial continuous design envelope;
- energy-aware workload scheduling;
- replaceable compute hardware;
- local/offline-capable controls;
- instrumentation for electrical input, computational workload, temperature, and heat output.

The compute layer should not inherit the Silent Core's fanless requirement if doing so compromises safe GPU operation. Energy storage and compute thermal architectures should remain separable.

## AEN-T — Thermal layer

Nearly all electrical energy consumed by compute ultimately appears as heat. AEN-T treats that heat as a recoverable resource rather than immediately rejecting it as waste.

The first objective is **thermal reuse**, not inefficient heat-to-electricity reconversion.

Research areas include:

- heat pipes and thermosyphon systems;
- closed-loop dry cooling;
- phase-change thermal storage;
- ceramic or other solid thermal media;
- thermal buffers that shift heat use across time;
- useful low-temperature secondary loads;
- zero operational cooling-water designs where technically feasible.

## AEN governance layer

AEN Compute treats infrastructure constraints as part of AI governance.

The scheduler may consider:

```text
solar availability
battery state of charge
battery health and temperature
ambient temperature
compute-node temperature
thermal-store capacity
forecast renewable generation
queued workload
workload priority
estimated energy requirement
community-defined reserve requirements
```

Software may schedule, defer, route, meter, log, forecast, and explain. It must never override hardware protection systems.

Example operating logic:

```text
high solar + charged battery + thermal capacity available
    -> permit intensive training workload

low reserve + nonessential workload
    -> queue until renewable capacity returns

high ambient temperature + thermal store near capacity
    -> reduce compute power or route workload elsewhere

priority local service
    -> allocate protected compute reserve
```

## Ethical growth principle

> AI should scale only as fast as the energy, water, materials, labor, and communities supporting it can sustain.

AEN Compute therefore treats the following as design requirements rather than externalities:

- energy accountability;
- water protection;
- transparent environmental accounting;
- local benefit;
- data and infrastructure sovereignty;
- community ownership pathways;
- accessibility by design;
- local maintenance and skills development;
- right-sized models and workloads;
- human authority over machine scheduling priorities.

## African research context

Africa is not treated as a single climate or infrastructure environment. AEN Compute should be climate-adaptive and locally governed.

Potential research questions include:

- How should AEN blocks differ between humid coastal, Sahelian, high-altitude, and temperate African environments?
- Can distributed solar compute reduce dependence on diesel-backed or grid-constrained infrastructure?
- Which local institutions should own and operate compute capacity?
- Which workloads should receive priority when energy is constrained?
- How can recovered thermal energy provide useful local secondary value?
- What parts of enclosure fabrication, integration, maintenance, software, and thermal infrastructure can be developed locally?

Nigeria is a strong candidate for an initial research context because AEN originated around distributed energy resilience, solar input, modular storage, and reduced generator dependence.

## v0.1 research target

**AEN-CB01**

- ~1.2 kW compute design load
- ~12 kWh nominal LFP storage target
- ~3 kW preliminary solar array target
- 8-hour initial ML duty-cycle target
- zero operational cooling-water consumption target
- instrumented heat-recovery pathway
- energy-aware workload scheduler
- hardware safety independent of scheduler

These values are preliminary research targets, not final engineering specifications. They require site-specific solar calculations, thermal engineering, certified components, electrical protection design, and professional safety review before physical deployment.

## Immediate workstreams

1. **Energy model** — solar yield, storage, duty cycle, conversion losses, reserves.
2. **Thermal model** — chip-to-store heat path, storage temperature range, heat rejection/reuse.
3. **Compute model** — workload classes, GPU power limits, networking, distributed scheduling.
4. **Governance model** — priority rules, ecological ceilings, provenance, human override.
5. **African deployment model** — climate adaptation, ownership, maintenance, local benefit.
6. **Accessibility model** — physical, software, documentation, maintenance, and operational access.
7. **Prototype plan** — smallest safe instrumented system capable of testing the thesis.

## Boundary

AEN Compute is not a perpetual-energy system. Stored heat cannot be reconverted to electricity without thermodynamic losses. The research goal is energy cascading: use high-quality electrical energy for computation, then recover useful thermal energy for an appropriate second use before final dissipation.
