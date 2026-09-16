# AEN Compute Block v0.1 — Physical Construction Specification

**Status:** Preliminary engineering specification for review and prototyping  
**Branch:** `aen-compute-infrastructure`  
**System:** AEN-CB01  
**Purpose:** Define what the first AEN Compute Block is physically made of, how its modules are separated, how power and heat move through the system, and what must be validated before fabrication.

> This is a system-level construction specification, not a raw-cell battery-building guide. Certified battery modules, listed power electronics, qualified electrical integration, and professional thermal/mechanical review are required before a physical build.

---

## 1. Physical architecture

AEN-CB01 is **not one enclosure**. It is a three-module system plus an external solar source:

```text
SOLAR ARRAY
    |
    v
SOURCE / POWER INTERFACE
    |
    v
+--------------------+      protected power      +--------------------+
| AEN-E              | ------------------------> | AEN-C              |
| ENERGY MODULE      |                           | COMPUTE MODULE      |
|                    |                           |                    |
| LFP storage        |                           | GPU / CPU / SSD     |
| BMS                |                           | networking         |
| inverter / DC bus  |                           | telemetry          |
+--------------------+                           +---------+----------+
                                                          |
                                                          | heat
                                                          v
                                                +--------------------+
                                                | AEN-T              |
                                                | THERMAL MODULE      |
                                                |                    |
                                                | heat exchanger     |
                                                | thermal store      |
                                                | dry heat rejection |
                                                +--------------------+
```

The modules are physically separated so that battery safety, compute cooling, and thermal storage can be serviced and tested independently.

---

## 2. Module summary

| Module | Physical form | Main construction | Preliminary size class | Function |
|---|---|---|---|---|
| **AEN-E** | lockable floor-standing battery/power cabinet | powder-coated welded steel frame and panels; internal galvanized or coated steel rack rails; insulated cable penetrations | roughly 600–800 mm W × 800–1000 mm D × 1200–1600 mm H | stores electricity and supplies protected power |
| **AEN-C** | 19-inch rack / short-depth compute cabinet | powder-coated steel rack frame; removable perforated steel panels; aluminum internal equipment rails where useful | roughly 600–800 mm W × 800–1000 mm D × 800–1200 mm H | contains GPU compute node, networking, controls, telemetry |
| **AEN-T** | insulated thermal cabinet beside or behind AEN-C | steel outer skin; noncombustible mineral-wool or equivalent high-temperature insulation; aluminum/copper heat-transfer surfaces; removable thermal-storage cartridges | roughly 600–800 mm W × 600–1000 mm D × 800–1200 mm H | receives, stores, rejects, or reuses compute heat |
| **Solar source** | roof/ground canopy or separate array | commercial framed PV modules, aluminum mounting rails, stainless fasteners, weather-rated cable/conduit and disconnect hardware | sized by site; v0.1 nominal research target ~3 kW | primary energy source |

These dimensions are not release drawings. They establish the physical scale and separation needed for the first prototype.

---

## 3. AEN-E — Energy module construction

### 3.1 Cabinet shell

**Preferred prototype material:** 1.2–2.0 mm powder-coated mild steel sheet over a welded or bolted steel frame.

Reason: battery cabinets need mechanical rigidity, impact resistance, grounding continuity, serviceable doors, and the ability to support heavy certified rack modules. Aluminum may be used for nonstructural internal brackets, but the first prototype should not depend on a lightweight consumer-style enclosure.

### 3.2 Battery storage

Use **commercial, closed, certified LFP rack battery modules**, not loose cells.

Target nominal energy for AEN-CB01: **approximately 12 kWh**.

The exact module count and nominal DC voltage are vendor-dependent. For this scale, a **48 V-class rack system** is a practical prototype category because it is widely available and can supply a ~1.2 kW compute load without requiring hyperscale DC distribution. The exact battery architecture must come from the selected certified system integrator.

Each battery module must provide its own BMS or participate in the vendor's system BMS. Required telemetry includes state of charge, module voltage/current, temperature, alarms, cycle count where available, and contactor/fault state.

### 3.3 Internal mechanical mounting

Battery modules mount on steel rack rails or manufacturer-specified shelves. Heavy modules remain in the lower half of the enclosure. The cabinet base must include either:

- forklift/pallet-jack compatible base geometry for installation; or
- locking industrial casters only if the fully loaded mass and stability analysis supports mobility.

Routine service must not require a disabled operator to lift battery modules manually. Slide rails, lift table, cassette trolley, or other no-lift service equipment should be used.

### 3.4 Power hardware

AEN-E contains or interfaces with:

| Component | Construction / mounting requirement |
|---|---|
| main DC disconnect | finger-safe, enclosed, lockable service disconnect |
| overcurrent protection | listed fuse/breaker hardware sized by electrical engineer |
| contactors | enclosed DC-rated contactors under BMS/system control |
| pre-charge | vendor/inverter-compatible pre-charge circuit where required |
| bus conductors | enclosed insulated copper busbar or appropriately rated cable; no exposed energized copper |
| inverter | commercial pure-sine inverter/charger or power-conversion system sized above the compute load |
| solar input | MPPT charger or compatible hybrid inverter interface |
| grounding | bonded steel enclosure and dedicated protective-earth path |
| emergency stop | external mushroom-type physical E-stop that commands safe power isolation |

The first prototype should use commercially integrated power electronics rather than a custom high-voltage inverter design.

### 3.5 Fire and separation boundary

AEN-E should be mechanically separated from AEN-C and AEN-T rather than sharing one internal air volume. Battery enclosure design must be reviewed against applicable energy-storage fire and propagation requirements. UL 9540A is a relevant test methodology for evaluating thermal-runaway propagation and installation behavior of battery energy-storage systems; it is not a substitute for a complete local code and certification review.

---

## 4. AEN-C — Compute module construction

### 4.1 Chassis

Use an industry-standard **19-inch equipment rack** or rack-compatible enclosure rather than a custom computer case.

Preferred materials:

- powder-coated steel outer rack/frame;
- galvanized or plated steel rack rails;
- perforated steel front/rear doors or removable service panels;
- aluminum brackets or cold-plate support parts where weight reduction or heat transfer is useful.

The rack is intentionally modular so GPU servers, networking, storage, sensors, and controller hardware can be changed without redesigning the entire AEN enclosure.

### 4.2 First compute node

AEN-CB01 is sized around **one high-end GPU workstation/server-class node**, with a design allowance of about **1.2 kW continuous system power**.

The physical compute tray should contain:

| Subsystem | Prototype construction target |
|---|---|
| GPU | one high-power accelerator or workstation GPU; removable PCIe/server module |
| CPU | workstation/server CPU matched to workload |
| memory | ECC preferred for research/server use where supported |
| local storage | NVMe SSD for OS + local model/cache storage |
| network | minimum 10 GbE recommended for two-node tests; upgrade path to 25/100 GbE for pods |
| management | low-power controller/BMC or Linux management service |
| telemetry | GPU power/temp, CPU temp, inlet/exhaust temp, whole-node power |

The prototype should avoid exotic proprietary rack-scale hardware at first. NVIDIA's current rack-scale Blackwell systems illustrate why tightly coupled high-density AI hardware uses separate compute trays, power shelves, bus bars, networking, and liquid-cooling manifolds rather than one giant computer enclosure. AEN adopts the same modular engineering principle at much smaller scale.

### 4.3 Power input

For v0.1, AEN-C may receive protected AC from AEN-E through a commercial inverter and standard server PSU. This is deliberately conservative and easy to instrument.

A later revision may test a DC-direct path if there is a measurable efficiency advantage and a standards-compliant power architecture. That is research work, not assumed in v0.1.

### 4.4 Air path

Even if the GPU is liquid-cooled, non-GPU components still require airflow. The compute rack therefore has a defined front-to-rear air path:

```text
filtered cool-side intake
        ->
CPU / memory / SSD / VRM / NIC airflow
        ->
contained warm exhaust
        ->
AEN-T heat-recovery / dry-rejection interface
```

Dust filtration must be removable and washable/replaceable. In humid or dusty African deployment contexts, filters, positive-pressure strategy, corrosion protection, and service intervals must be climate-specific.

---

## 5. AEN-T — Thermal module construction

AEN-T is the most experimental physical subsystem. Its purpose is to take heat away from the processors safely, capture some of it when useful, and reject the rest without an evaporative cooling tower.

### 5.1 Heat capture at the chip

For a 1.2 kW research node, two prototype approaches are acceptable:

**Option A — conventional GPU/CPU cooling with exhaust heat capture.**

This is simplest for the first software/energy prototype but captures lower-grade warm air.

**Option B — direct-to-chip cold plates.**

Use commercial copper or nickel-plated copper cold plates on GPU/CPU hardware supported by the selected compute platform. This provides a more concentrated and useful heat stream.

Current high-density NVIDIA rack systems use liquid cold plates and manifolds for CPUs/GPUs while other components remain air cooled. That is the reference principle for AEN-T, although AEN operates at far smaller scale.

### 5.2 Closed heat-transfer loop

The preferred AEN-CB01 thermal architecture is a **sealed recirculating loop** with no cooling tower and no routine evaporation.

Prototype materials:

- copper or nickel-plated copper cold plates;
- EPDM- or manufacturer-rated flexible coolant hose;
- brass/stainless/aluminum fittings selected for galvanic compatibility;
- quick-disconnect couplings rated for electronics cooling;
- small variable-speed circulation pump;
- plate heat exchanger or finned dry radiator;
- leak tray and electronic leak sensors beneath all wet connections.

The coolant may be a manufacturer-approved water/glycol mixture for the first closed-loop prototype. This does **not** consume water continuously: the loop is sealed. If the project later requires literally water-free coolant, AEN can evaluate refrigerant, dielectric, or other compatible systems as a separate research branch.

### 5.3 Thermal storage cartridge

AEN-T should not begin with a custom chemical formulation. Use **commercially encapsulated phase-change material (PCM)** or another tested solid thermal-storage medium.

Initial target operating band: approximately **45–55 °C phase-transition region**, subject to the actual processor cold-plate outlet temperature and heat-reuse application.

Physical cartridge concept:

```text
steel/aluminum outer cassette
    |
    +-- internal aluminum heat-spreader plates
    +-- sealed commercial PCM packs or solid thermal media
    +-- temperature probes at inlet/core/outlet
    +-- insulated service handle / slide rails
```

The thermal cartridge housing should be metal, replaceable, instrumented, and isolated from electrical components. A PCM supplier must provide flammability, cycling, compatibility, and containment data before use.

### 5.4 Thermal cabinet insulation

Preferred enclosure build:

- powder-coated steel exterior;
- 25–50 mm noncombustible mineral-wool or equivalent high-temperature insulation layer;
- aluminum internal heat-spreader structure;
- removable bolted access panels with high-temperature gasket material;
- drip/leak tray if a liquid heat exchanger is present.

Avoid combustible decorative foams near the thermal core unless a fire engineer explicitly approves them.

### 5.5 Final heat rejection

Heat that cannot be stored or reused goes to an **air-cooled dry radiator/dry cooler** rather than an evaporative cooling tower.

For AEN-CB01, that can be a finned aluminum/copper heat exchanger with EC fans placed outside or in a separated ventilated service area. The dry cooler must be sized for the full compute heat load when thermal storage is full.

The U.S. Department of Energy explicitly recommends reusing waste heat first and rejecting unusable heat through dry coolers when practical to reduce water use. DOE's 2026 COOLERCHIPS 1.5 work is also testing advanced water-free cooling systems for AI data centers at much higher rack heat loads. AEN-CB01 is a small-scale implementation of the same physical objective, not a claim that heat disappears.

---

## 6. Solar source construction

AEN-CB01 research target: approximately **3 kW of PV** for the initial 8-hour-duty-cycle experiment.

Physical source system:

| Item | Construction |
|---|---|
| PV modules | commercial framed crystalline-silicon modules with certified junction boxes |
| mounting rails | extruded anodized aluminum solar rails |
| fasteners | stainless steel outdoor-rated hardware |
| cable | UV-resistant PV-rated cable in protected routing |
| combiner/protection | weather-rated combiner where required, DC disconnect, overcurrent protection, surge protection |
| charge interface | commercial MPPT controller / hybrid inverter compatible with selected AEN-E battery system |
| structure | roof, canopy, or ground frame engineered for local wind, corrosion, and structural loads |

The solar array is physically separate from the compute module. It should be treated as site infrastructure rather than attached directly to the computer cabinet.

---

## 7. Inter-module interfaces

AEN modules must be removable without exposing dangerous energized conductors or opening coolant connections casually.

### Electrical interface

AEN-E to AEN-C should use a protected, keyed, lockable power connector or fixed professional distribution interface appropriate to the selected voltage/current. No loose battery leads, exposed busbars, or consumer extension-cord backfeed arrangements.

### Thermal interface

AEN-C to AEN-T uses either:

- contained hot-air duct interface for the simplest prototype; or
- rated dry-break liquid quick disconnects for direct-to-chip cooling.

### Data interface

Standard Ethernet carries telemetry and control. Safety shutdown remains local in hardware; a network failure must not disable battery protection or thermal shutdown.

---

## 8. Sensors physically installed in v0.1

| Sensor | Placement |
|---|---|
| whole-node power meter | AEN-C electrical input |
| battery current/voltage/SOC | AEN-E via certified BMS telemetry |
| battery temperature | internal battery modules / vendor sensors |
| PV power | source interface / MPPT telemetry |
| GPU telemetry | software/DCGM plus hardware temperature data |
| compute inlet air temp | lower/front rack intake |
| compute exhaust temp | rear/hot-side outlet |
| coolant supply temp | upstream of cold plates if liquid loop used |
| coolant return temp | downstream of cold plates |
| coolant flow | thermal loop |
| leak detection | beneath cold plates, manifolds, quick disconnects, thermal cabinet |
| PCM/store temperature | multiple depths inside AEN-T cartridge |
| ambient temperature/humidity | outside compute enclosure |

---

## 9. First physical assembly sequence

AEN-CB01 should be fabricated in this order:

1. commercial 19-inch AEN-C compute rack with one real GPU node;
2. whole-node electrical metering and temperature instrumentation;
3. separate certified AEN-E LFP/inverter cabinet;
4. protected electrical interface between AEN-E and AEN-C;
5. solar source dock / PV input;
6. contained exhaust heat measurement;
7. AEN-T dry heat-rejection module;
8. direct-to-chip liquid loop only after the compute hardware platform is selected;
9. instrumented thermal-storage cartridge;
10. useful secondary heat-load experiment.

The project therefore becomes progressively more physical without requiring every novel subsystem to succeed on day one.

---

## 10. What v0.1 is literally made of

In plain terms, the first AEN Compute Block is:

**A steel battery cabinet** containing certified LFP rack modules, BMS, disconnects, protection, inverter/charger, MPPT interface, and telemetry;

connected to

**a steel 19-inch compute rack** containing a GPU computer, CPU, memory, NVMe storage, network interface, power supply, sensors, filters, and controller;

connected thermally to

**an insulated steel thermal cabinet** containing copper/aluminum heat-transfer hardware, a sealed pump loop or contained hot-air path, temperature/flow/leak sensors, replaceable thermal-storage cartridges, and an external dry radiator for heat that cannot be reused;

all supplied by

**a separate solar array** built from commercial PV panels on aluminum rails with outdoor-rated DC protection and a commercial solar charge interface.

That is the AEN-CB01 machine.

---

## 11. Construction decisions that remain open

These are engineering decisions, not missing concepts:

- exact certified LFP vendor and module geometry;
- exact battery-system nominal voltage;
- exact inverter/charger topology;
- exact GPU/server platform;
- whether v0.1 thermal capture begins with hot-air recovery or direct-to-chip liquid cooling;
- selected commercial PCM or alternative thermal-storage medium;
- dry-cooler sizing for the selected climate;
- corrosion class and filtration strategy for the first African pilot site;
- final fire separation, venting, suppression, and certification requirements;
- final structural dimensions after equipment selection.

None of those should be guessed before vendor data and site conditions are known.

---

## 12. Engineering references behind the construction direction

- NVIDIA's current GB200/GB300 rack systems physically separate compute trays, power shelves, bus bars, networking, and liquid-cooling manifolds; their direct-to-chip cooling uses liquid cold plates while other components retain air cooling.
- U.S. DOE data-center guidance prioritizes component efficiency, heat reuse, and dry coolers where practical to reduce water use.
- DOE COOLERCHIPS 1.5 is explicitly developing and validating advanced water-free cooling for high-power AI data centers.
- UL 9540A remains a relevant test method for evaluating thermal-runaway propagation and fire behavior in battery energy-storage systems; an AEN battery cabinet must be treated as real BESS equipment, not ordinary furniture.

---

## 13. Design rule

AEN-CB01 is not considered specified until every physical block in the energy path and heat path can be pointed to on a drawing and assigned a material, interface, sensor, service procedure, and safety owner.
