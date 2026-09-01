# Intuitive Systems Doctrine

**Version:** v0.1  
**Date:** 2026-09-01  
**Status:** Canonical cross-project design doctrine  
**Scope:** Small Systems Lab and projects that explicitly adopt this doctrine

## Core proposition

> The more advanced the system, the more intuitive the interface should become.

Small Systems Lab uses this proposition as a design hypothesis and engineering doctrine, not as a claim that technological sophistication automatically produces good interfaces.

The doctrine asks a specific question: **Can a system become substantially more capable while exposing less unnecessary complexity to the person using it?**

Its central rule is:

> **Reduce operational complexity without reducing epistemic transparency.**

A system may simplify interaction, but it must not simplify away uncertainty, provenance, competing evidence, consent, human judgment, or the ability to inspect how a recommendation was produced.

## Canonical rules

### SSL-IF-001 — Complexity underneath, clarity at the surface

Internal complexity may increase as capabilities increase. The primary interface should expose only the information needed for the immediate human task.

### SSL-IF-002 — Progressive disclosure

Critical information should be available in a sequence such as:

**WHAT YOU NEED TO KNOW → NEXT ACTION → WHY → EVIDENCE → INVESTIGATE**

Deeper complexity is available when requested rather than imposed at first contact.

### SSL-IF-003 — Simplicity must not become authority

A concise output must not imply unquestionable truth. Systems should be able to say that evidence is insufficient, request another observation, or present multiple plausible interpretations.

### SSL-IF-004 — Uncertainty remains inspectable

The user must be able to inspect uncertainty, provenance, source material, assumptions, contradictions, and unresolved questions where relevant.

### SSL-IF-005 — Accessibility is intrinsic

Accessibility is not a separate mode. Critical information should be capable of reaching people through appropriate combinations of text, speech, sound, vibration, tactile patterns, light, directional cues, physical controls, and other documented representations.

### SSL-IF-006 — The system adapts to the human

The person should not be forced to learn unnecessary machine complexity in order to accomplish a critical task. Adaptation must remain consent-aware and overrideable.

### SSL-HW-001 — Form follows usefulness

Every visible hardware component should have an understandable purpose. Future-facing design is not justification for decorative complexity.

### SSL-HW-002 — Capability may expand without interaction complexity expanding

New sensors, modules, data sources, or reasoning capabilities should not automatically produce a more complicated primary interface.

### SSL-HW-003 — Critical functions survive failure

Where the application warrants it, critical functions should not depend exclusively on a pristine screen, continuous network connection, or a single sensory channel.

### SSL-HW-004 — Physical systems should be legible and repairable

Field and public-interest hardware should favor modularity, understandable components, maintainability, replaceability, and documented failure states.

### SSL-GOV-001 — Human judgment remains final

Automation may assist, translate, compare, prioritize, or recommend. It must not erase the human ability to question, override, defer, or decline a determination.

## Research pathway: fiction to evidence

Small Systems Lab may use speculative fiction and cultural artifacts as **research stimuli**. A fictional work may articulate a technological relationship clearly enough to help formulate a design question, but it is not treated as technical validation.

The pathway is:

**FICTION / CULTURAL OBSERVATION → QUESTION → DESIGN PRINCIPLE → RESEARCH → PROTOTYPE → TESTING → EVIDENCE**

This distinction is mandatory. Inspiration and validation are not interchangeable.

## Cultural and design stimuli recorded for v0.1

### Green Lantern: Beware My Power (2022)

At approximately the 16-minute mark, Green Arrow refers to an idea attributed to Hal Jordan about advanced interfaces becoming more intuitive. The exact dialogue has **not yet been verified against an authoritative subtitle or transcript**, so the wording should not be presented as a direct quotation until verified.

The scene is retained as a cultural/design stimulus for the research question: **Does greater system sophistication allow interaction complexity to decrease?**

### Aliens (1986)

The film's industrial machinery, including its rescue and material-handling equipment, is retained as a visual/design stimulus for the principle that machinery can communicate usefulness through form. It is not technical evidence for the doctrine.

## Omoluabi translation

Omoluabi is the real-world research environment in which this doctrine can be prototyped and evaluated.

Its interface hypothesis is:

**ASK / SHOW / LISTEN → UNDERSTAND → ACT → WHY → EVIDENCE**

A field or civic assessment may initially provide a concise human-scale statement, while preserving access to sources, provenance, contradictions, timelines, sensor readings, uncertainty, and competing interpretations.

A canonical example is not “the system knows,” but:

> **Collect another reading before making a determination.**

## Luabi translation

Luabi is the fictional UMADA descendant / extrapolation of the Omoluabi research lineage. Fiction may explore capabilities beyond present engineering, but should preserve the doctrine's core relationship between capability, usefulness, accessibility, inspectability, and human agency unless canon explicitly establishes otherwise.

**Omoluabi and Luabi are not the same artifact.**

- **Omoluabi:** present-day real-world research system and prototype environment.
- **Luabi:** fictional future device within UMADA, informed by but not automatically identical to Omoluabi.

## Earth Sensors Lab translation

Scientific simplification must never erase scientific meaning. A plain-language observation may sit above raw readings, but calibration, units, uncertainty, transformation rules, provenance, and original measurements remain available for inspection.

## Accessibility translation

The doctrine treats accessibility as a sign of system sophistication: a capable system should be able to communicate critical meaning through multiple documented channels without requiring a separate “normal” interface first.

## Research status

This doctrine is a **design and research framework**. Individual claims about usability, comprehension, cognitive load, safety, accessibility, or performance require testing. Future prototypes should record where the doctrine succeeds, where it fails, and where simplification introduces new risks.

## Versioning rule

Future revisions must preserve the distinction between:

1. cultural/design stimulus;
2. design hypothesis;
3. engineering decision;
4. tested evidence;
5. fictional extrapolation.

No item may silently move from one category to another without documentation and human review.
