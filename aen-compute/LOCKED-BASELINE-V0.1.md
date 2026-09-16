# AEN Compute — Locked Baseline v0.1

**Status:** LOCKED RESEARCH BASELINE  
**Date locked:** 2026-09-16  
**Branch:** `aen-compute-infrastructure`

This document records the current AEN Compute baseline. Future work should build from these decisions unless new evidence requires a documented revision.

## 1. Mission

AEN Compute exists to **expand African AI capability without requiring Africa to inherit the most resource-intensive assumptions of conventional data-center growth**.

The project is not about limiting AI growth. It is about redesigning the infrastructure underneath AI so that compute capacity can grow with greater energy resilience, lower water dependence, stronger local ownership, and better environmental accounting.

## 2. Central thesis

> **Can Africa build substantially more AI compute capacity by redesigning the data center itself — using distributed solar generation, modular storage, heat recovery, climate-adaptive cooling, and networked compute blocks as a new infrastructure model?**

This is the governing research question.

## 3. Locked architecture

AEN Compute is hierarchical rather than purely centralized or purely distributed.

```text
AEN EDGE
    -> local sensor / small-model / low-latency compute

AEN COMPUTE BLOCK
    -> single or multi-GPU node

AEN POD
    -> tightly coupled local multi-GPU systems

AEN CLUSTER
    -> multiple pods on one campus / site

AEN COMPUTE FABRIC
    -> geographically distributed sites carrying workloads that tolerate WAN separation
```

### Workloads that may distribute geographically

- inference replicas;
- agent workloads;
- RAG and retrieval;
- embeddings;
- batch inference;
- document, image, audio, and media processing;
- evaluations;
- independent parameter-efficient fine-tunes;
- asynchronous or federated training where appropriate;
- scientific workloads with coarse-grained parallelism.

### Workloads that remain locally concentrated when required

Frontier-scale synchronous pretraining and other tightly coupled workloads remain inside local high-bandwidth compute islands when they require continuous accelerator-to-accelerator communication.

AEN does not assume ordinary wide-area networking can replace NVLink-, NVSwitch-, InfiniBand-, or equivalent-class local fabrics.

## 4. Energy architecture

AEN-E is the electrical layer.

Locked principles:

- solar-first generation;
- modular certified LFP storage;
- protected electrical distribution;
- DC-first pathways where engineering supports them;
- grid as optional/supplemental resilience rather than a mandatory operating assumption where feasible;
- transparent source and energy accounting;
- hardware protection remains independent of AI/software control;
- no unsafe backfeeding, improvised building wiring, or loose-cell battery prototyping.

## 5. Compute architecture

AEN-C is the compute layer.

Locked principles:

- use existing distributed-compute systems rather than reinventing them;
- AEN's novel contribution is energy-, thermal-, and infrastructure-aware orchestration;
- start with workload placement, not live migration of running GPU processes;
- schedule flexible work to the block/site with the strongest available energy and thermal headroom;
- preserve local high-speed clusters where workload physics requires them;
- increase usable compute capacity by routing around energy and thermal bottlenecks rather than treating ecological telemetry only as a throttling mechanism.

## 6. Thermal architecture

AEN-T is the thermal layer.

Locked principles:

- compute heat is accounted for as an energy output;
- recover useful heat where technically and economically practical;
- prefer direct thermal reuse over inefficient heat-to-electricity reconversion;
- investigate dry cooling, heat pipes, thermosyphons, closed-loop systems, phase-change materials, and solid thermal stores;
- prototype target: zero operational cooling-water consumption;
- larger systems may pursue water-free or extremely low-water designs according to climate and engineering evidence;
- AEN-T is an energy-cascading system, not a perpetual-energy system.

## 7. Ethical growth position

AEN supports **more African AI capacity, not artificial scarcity**.

Ethical growth means infrastructure costs are visible, measured, and governed rather than externalized.

Locked principles:

- increase African-owned and locally available compute capacity;
- support infrastructure and data sovereignty;
- protect water resources;
- add renewable generation/storage alongside compute growth;
- seek useful secondary value from compute heat;
- make accessibility foundational across hardware, software, documentation, education, operation, and employment;
- create tangible benefit for host communities;
- keep humans and institutions responsible for priorities;
- measure energy source, electricity use, thermal output, water use, utilization, and local benefit.

## 8. Africa-specific design principle

Africa is not one climatic or infrastructure environment.

AEN must be locally engineered for coastal humidity, salt exposure, dust, extreme heat, altitude, grid conditions, network availability, maintenance capacity, regulation, and local ownership models.

Nigeria remains the leading initial research context, but it is not assumed to represent the continent.

## 9. v0.1 proof target

The first convincing AEN Compute proof is **not a data center**.

It is two GPU-capable nodes under one AEN controller.

The controller receives energy and thermal telemetry and decides where a flexible AI job should run.

### Required demonstration

Scenario A: Node A has superior energy/thermal conditions -> job runs on A.  
Scenario B: conditions reverse -> job runs on B.  
Scenario C: neither node can accept a discretionary job without violating reserve/thermal policy -> job is queued.

The controller must record the decision and its reason.

## 10. Locked implementation sequence

1. **Digital twin** — simulated solar, battery, GPU, thermal, network, and queue state.
2. **Two real GPU nodes** — ordinary electrical supply, real workload dispatch.
3. **Electrical telemetry** — whole-node power and energy measurement.
4. **Certified AEN storage** — battery telemetry integrated into scheduling.
5. **Solar input** — live PV generation becomes a scheduling variable.
6. **Thermal instrumentation** — measure heat production and transfer.
7. **AEN-T prototype** — capture and reuse a measurable fraction of compute heat.
8. **Multi-block scale-out** — pod, cluster, and regional-fabric testing.

Do not purchase custom solar/storage/thermal hardware until the software-only scheduling architecture is proven.

## 11. v0.1 software stack

Initial reference stack:

```text
Linux GPU nodes
NVIDIA DCGM / DCGM Exporter
Prometheus
Ray
AEN scheduler service (Python)
AEN telemetry adapters
Optional Grafana dashboard
```

Ray or an equivalent compute substrate handles ordinary compute scheduling. AEN evaluates dynamic energy and thermal state and determines eligible placement.

## 12. Safety and authority boundary

AEN software may observe, forecast, rank, schedule, defer, route, explain, and log.

AEN software must **not** override:

- BMS protection;
- inverter protection;
- electrical isolation;
- fuses/breakers/contactors;
- processor thermal protection;
- emergency shutdown;
- professionally defined electrical or thermal safety limits.

Hardware safety remains authoritative.

## 13. What remains open

The following are research questions, not locked engineering claims:

- ideal PV/storage ratio at each deployment site;
- exact GPU/accelerator selection;
- preferred thermal-storage medium;
- practical heat-recovery efficiency;
- economics relative to conventional data centers;
- network topology at pod/cluster/fabric scale;
- local manufacturing/integration pathway;
- ownership and financing models;
- regulatory/certification pathway by jurisdiction;
- the maximum workload classes that can move across regional fabrics without unacceptable performance loss.

## 14. Change control

A locked decision may change when testing, engineering review, safety analysis, economics, or new technical evidence contradicts it.

Any major change should be documented with:

1. the previous assumption;
2. the new evidence;
3. the revised decision;
4. its impact on energy, thermal, compute, safety, accessibility, and governance architecture.

Until such a revision is documented, this file is the baseline for AEN Compute v0.1.
