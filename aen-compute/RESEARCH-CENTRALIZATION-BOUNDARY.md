# AEN Compute — What Must Be Centralized, What Can Be Distributed

**Status:** Research note / architecture boundary map  
**Date:** 2026-09-15  
**Branch:** `aen-compute-infrastructure`

## Core finding

AEN should **not** assume that all AI computation can be broken into small, geographically separated blocks.

The technically stronger architecture is **hierarchical**:

1. tightly coupled GPUs stay physically close when a workload requires constant high-bandwidth synchronization;
2. independent or loosely coupled workloads move between AEN sites according to energy, thermal capacity, latency, sovereignty, and local demand;
3. geographically distributed sites operate as a larger AEN Compute Fabric without pretending ordinary wide-area networking behaves like an NVLink/InfiniBand fabric.

This means AEN can support aggressive AI growth while avoiding the claim that every AI workload must fit inside a tiny edge device.

The central research question becomes:

> **How much AI capability can be moved out of conventional hyperscale data-center architecture while preserving the tightly coupled compute islands that genuinely require proximity?**

---

## 1. Why frontier pretraining still wants local concentration

Large synchronous training jobs repeatedly exchange parameters, gradients, activations, or optimizer state between GPUs. Communication is not occasional overhead; for many parallelization strategies it is part of every training step.

Meta reported that Llama 3 training combined data, model, and pipeline parallelism and used **16,000 GPUs simultaneously**, with training runs on two custom 24,000-GPU clusters. That is evidence that frontier-scale pretraining today depends on large, tightly coordinated GPU systems rather than arbitrary geographically scattered machines.

Source: https://ai.meta.com/blog/meta-llama-3/

Microsoft's DeepSpeed work explains the systems reason. Data-parallel training must aggregate gradients; model parallelism requires frequent activation transfers; and communication overhead becomes a limiting factor when bandwidth is low or latency is high. ZeRO and ZeRO++ reduce this communication burden, but do not remove the need for communication.

Sources:

- https://www.microsoft.com/en-us/research/blog/deepspeed-extreme-scale-model-training-for-everyone/
- https://www.microsoft.com/en-us/research/blog/deepspeed-zero-a-leap-in-speed-for-llm-and-chat-model-training-with-4x-less-communication/

NVIDIA's NVSwitch exists specifically to provide high-bandwidth, low-latency GPU-to-GPU communication inside a system. NVIDIA's current AI networking stack extends that idea outward through InfiniBand and Spectrum-X Ethernet for large clusters.

Sources:

- https://docs.nvidia.com/ai-enterprise/release-7/latest/infra-software/vgpu/features/nvswitch.html
- https://www.nvidia.com/en-us/networking/spectrumx/

### AEN implication

**Frontier pretraining should remain a locally concentrated workload.**

AEN should therefore support **AEN Compute Clusters**: multiple pods co-located on one campus with high-speed local interconnect. The innovation is not to scatter a synchronous training job across weak links. The innovation is to redesign the **energy, cooling, storage, modularity, ownership, and environmental architecture around the local cluster.**

---

## 2. Geographic separation is becoming technically possible — but only with specialized networking

NVIDIA now describes a third networking layer, "scale-across," intended to connect multiple data centers into one AI system. Spectrum-XGS is explicitly designed for geographically separated facilities and modifies congestion control and collective communication for inter-site distance.

Sources:

- https://nvidianews.nvidia.com/news/nvidia-introduces-spectrum-xgs-ethernet-to-connect-distributed-data-centers-into-giga-scale-ai-super-factories
- https://developer.nvidia.com/blog/how-to-connect-distributed-data-centers-into-large-ai-factories-with-scale-across-networking/

This is important for AEN because it demonstrates that **a data center does not have to be one building**. However, it does **not** mean arbitrary solar blocks connected by normal Internet links can efficiently train a frontier model as one synchronous job.

### AEN implication

A future AEN Compute Fabric can contain multiple sites, but workloads must be classified by coupling requirement.

---

## 3. Inference is much more distributable than frontier training

Inference serving frequently allows independent requests to be routed to independent model replicas. vLLM explicitly supports data-parallel deployment where model weights are replicated across separate GPUs/instances to process independent batches.

Source: https://docs.vllm.ai/en/stable/serving/data_parallel_deployment/

For a model that fits on one GPU, vLLM recommends using one GPU rather than distributed inference. If it fits within one multi-GPU node, tensor parallelism can remain local. Multi-node inference is required only when the model or throughput target exceeds one node.

Source: https://docs.vllm.ai/en/v0.18.0/serving/parallelism_scaling/

NVIDIA Dynamo goes further by disaggregating inference itself. Prefill and decode can run on separate worker pools, and requests can be routed across multi-node systems. This proves that even one logical AI service can be decomposed into specialized compute stages.

Sources:

- https://www.nvidia.com/en-us/ai/dynamo/
- https://docs.nvidia.com/dynamo/dev/knowledge-base/concepts/system-architecture/disaggregated-serving

### AEN implication

Inference is a primary AEN workload.

The preferred architecture is usually **replication and routing**, not splitting every token generation request across distant locations.

Example:

```text
User in Lagos
    |
    v
AEN Router
    |
    +--> Lagos model replica if available
    |
    +--> Ibadan block if Lagos is energy constrained
    |
    +--> Accra block if policy / latency / capacity permit
```

Each site can contain a local tightly coupled GPU node if the model requires multiple GPUs. Geography is used to route **requests**, not necessarily every tensor operation.

---

## 4. Local agents and many application workloads do not require a hyperscale data center

NVIDIA currently markets DGX Spark as a desktop system for local autonomous agents and large local models, explicitly reducing dependence on cloud token generation. Its software can also cluster multiple units locally.

Sources:

- https://www.nvidia.com/en-us/products/workstations/dgx-spark/
- https://developer.nvidia.com/blog/run-local-ai-agents-with-faster-models-and-multi-node-clustering-on-nvidia-dgx-spark/

This provides direct evidence for an AEN premise: useful generative-AI capability increasingly exists below hyperscale data-center scale.

### Strong AEN candidates

- local agents;
- RAG and document intelligence;
- embeddings;
- speech recognition and translation;
- computer vision;
- local language services;
- education systems;
- healthcare decision-support models where appropriate and governed;
- agricultural models;
- scientific sensor analysis;
- code assistants;
- creative AI;
- public-service inference;
- batch media processing.

These workloads can be colocated with the communities generating the demand and data.

---

## 5. Fine-tuning is much easier to decentralize than pretraining

Parameter-efficient methods dramatically reduce the amount of hardware required to adapt an existing foundation model.

LoRA freezes the base model and trains small low-rank matrices rather than every parameter. The original paper reported large reductions in trainable parameter count and GPU memory requirements.

Source: https://arxiv.org/abs/2106.09685

QLoRA subsequently demonstrated fine-tuning a 65-billion-parameter model on a single 48 GB GPU in its experimental setup. That historical result does not imply every modern model can be tuned on one GPU, but it proves that **model adaptation can occupy a radically different infrastructure class from base-model pretraining.**

Source: https://arxiv.org/abs/2305.14314

### AEN implication

Africa does not need to repeat frontier pretraining every time it needs a new domain, language, institutional, agricultural, educational, or scientific model capability.

AEN blocks can support:

```text
foundation model
      |
      v
local/domain dataset
      |
      v
LoRA / QLoRA / other PEFT
      |
      v
specialized local model
```

This is a high-value path for African compute sovereignty.

---

## 6. Federated learning proves that training itself can sometimes be distributed

Federated learning allows multiple devices or sites to train a shared model without centralizing all underlying data. Google describes federated learning as decoupling collaborative model learning from centralized storage of training data.

Source: https://research.google/blog/federated-learning-collaborative-machine-learning-without-centralized-training-data/

Google research also documents the core limitation: communication cost and heterogeneous client resources become bottlenecks. Techniques such as partial training, compression, layer-wise learning, and depth dropout can reduce these costs, but there are trade-offs.

Sources:

- https://research.google/pubs/efficient-and-private-federated-learning-with-partially-trainable-networks/
- https://research.google/pubs/towards-federated-learning-under-resource-constraints-via-layer-wise-training-and-depth-dropout/

### AEN implication

Federated training is suitable for selected domain models and privacy-sensitive decentralized datasets. It should **not** currently be presented as a straightforward replacement for tightly coupled frontier pretraining.

---

## 7. Batch computation is the easiest workload to move with the sun

Some computation is delay-tolerant and location-flexible. Google has already shifted movable compute tasks across time and geography according to carbon-free energy availability; its examples include media processing workloads.

Sources:

- https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/data-centers-work-harder-sun-shines-wind-blows/
- https://blog.google/company-news/outreach-and-initiatives/sustainability/carbon-aware-computing-location/

Microsoft research describes a related "Virtual Battery" idea: rather than forcing power supply to follow computational demand, move computational demand to where and when renewable power is available.

Source: https://www.microsoft.com/en-us/research/publication/redesigning-data-centers-for-renewable-energy/

A 2026 Microsoft research paper goes further and jointly models AI workload placement, local generation, battery storage, inference routing, and carbon constraints across geographically distributed AI data centers.

Source: https://www.microsoft.com/en-us/research/publication/carbon-aware-compute-power-scheduling-for-ai-data-centers-with-microgrid-prosumer-operations/

### AEN implication

This is one of the strongest validations of the AEN scheduler thesis:

```text
Do not only ask:
"How much electricity must we build for this computation?"

Also ask:
"Which computation can move to the electricity that already exists?"
```

---

# Workload boundary matrix

| Workload | Coupling | Geographic distribution | AEN fit | Recommended AEN level |
|---|---|---|---|---|
| Frontier foundation-model pretraining | Extremely high | Difficult; specialized networking required | Conditional | Cluster / campus |
| Large synchronous distributed training | Very high | Limited | Conditional | Cluster |
| Full-parameter fine-tuning of very large models | High | Limited | Conditional | Pod / cluster |
| LoRA / QLoRA / PEFT | Low–moderate | Good | Strong | Block / pod |
| Independent LLM inference requests | Low between replicas | Excellent | Very strong | Block / fabric |
| Very large single-model inference | High inside replica | Replica placement can distribute geographically | Strong with local pods | Pod + fabric |
| RAG / vector search | Low–moderate | Excellent | Very strong | Block |
| Agents / tool use | Low–moderate | Excellent | Very strong | Block |
| Embeddings | Low | Excellent | Very strong | Block |
| Image/video batch processing | Low | Excellent | Very strong | Block / fabric |
| Scientific batch analysis | Low | Excellent | Very strong | Block / fabric |
| Federated/domain training | Periodic synchronization | Designed for distribution | Strong for selected tasks | Fabric |
| Real-time latency-sensitive local AI | Low if model local | Best near user | Very strong | Edge / block |

---

# Proposed AEN hierarchy

## AEN Edge

One low-power inference device or accelerator.

Use for sensors, field systems, classrooms, local vision/audio, and small models.

## AEN Block

One independent compute module with local electrical and thermal infrastructure.

Typical use:

- one or several GPUs;
- inference;
- RAG;
- agent workloads;
- embeddings;
- batch work;
- PEFT;
- local scientific workloads.

## AEN Pod

Several blocks connected by a local high-bandwidth fabric.

Purpose: allow models or jobs that need tensor, pipeline, expert, or other intra-job parallelism without distributing those communications over ordinary wide-area links.

## AEN Cluster

Multiple pods on one site/campus with shared networking, storage, solar generation, electrical storage, and thermal infrastructure.

This is the level at which AEN can realistically investigate large training systems.

## AEN Fabric

Multiple AEN sites connected geographically.

The Fabric performs:

- request routing;
- workload migration;
- batch scheduling;
- model replication;
- federated learning;
- energy-aware placement;
- thermal-capacity-aware placement;
- regional failover;
- sovereignty/policy-aware routing.

It does **not** assume every GPU across Africa participates in one synchronous job.

---

# Revised thesis

AEN is not a proposal to make African AI smaller.

It is a proposal to separate **AI capability** from the assumption that AI capability must always be delivered by a conventional hyperscale data center.

The architecture preserves concentration **where physics and networking require it**, while distributing everything that does not need that concentration.

Therefore:

> **AEN Compute is a hierarchical solar-first AI infrastructure in which tightly coupled compute is concentrated locally, loosely coupled computation is distributed geographically, and workloads move across time and place according to energy availability, thermal capacity, latency, data sovereignty, and human priorities.**

---

# Prototype consequence

The first AEN-CB01 prototype should not attempt distributed frontier training.

It should validate the pieces that scale upward:

1. solar + battery powered GPU compute;
2. zero-operational-water heat removal target;
3. heat measurement and recovery into AEN-T;
4. local inference;
5. PEFT / small fine-tuning job;
6. batch workload scheduling based on solar and battery state;
7. two-block job routing;
8. model replication between blocks;
9. failover when one block reaches its energy or thermal reserve;
10. energy / thermal / compute telemetry exposed through one governance interface.

Then add a **local high-speed AEN Pod** and measure the boundary where network communication becomes the bottleneck.

That measurement—not ideology—should determine which future workloads stay inside a pod, inside a cluster, or move across the AEN Fabric.
