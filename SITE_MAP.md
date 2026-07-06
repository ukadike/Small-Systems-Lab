# Ecosystem Site Map — Small Systems Lab

A single page indexing every public-facing site and major README across the "ukadike"
GitHub ecosystem. This is the ecosystem-level counterpart to each repo's own local
`INDEX.md`; see those files for a repo's full internal file listing.

Small Systems Lab is the hub. Every branch below links back to it
(`https://ukadike.github.io/small-systems-lab/`) from its own site nav, breadcrumb,
and README footer, as of the `claude/ukadike-github-nav-audit-9yq9ft` navigation pass.

```
/
├── Home / Profile — github.com/ukadike
│
├── Small Systems Lab (hub) — ukadike.github.io/small-systems-lab/
│   ├── About / Method (index.html, README.md)
│   ├── Branches (index.html §Branches)
│   ├── Accessibility as Architecture (docs/accessibility.md)
│   ├── Rule-Based Intelligence (docs/rule-based-intelligence.md)
│   ├── Ancient Geometry (docs/ancient-geometry.md)
│   ├── Sitemap (sitemap/)
│   └── Repository Index (INDEX.md)
│
├── Omoluabi — ukadike.github.io/omoluabi/
│   ├── Overview (index.html, README.md)
│   ├── Start Here (000_START_HERE.md)
│   ├── Governance Loop (governance/)
│   ├── Web Engine (web-engine/)
│   ├── Device (device/)
│   ├── Evidence States (index.html evidence-states block)
│   ├── Accessibility (accessibility/)
│   ├── Schemas (schemas/, cards/)
│   ├── UFO Connection demo — ukadike.github.io/omoluabi/ufo-connection/
│   └── World Layer Sandbox — ukadike.github.io/omoluabi/world-layer-sandbox/p5-coastal-relay/
│
├── Earth Sensors Lab — ukadike.github.io/earth-sensors-lab/
│   ├── Mission (MISSION.md)
│   ├── Research Agenda (RESEARCH_AGENDA.md)
│   ├── Curriculum (curriculum/, CURRICULUM.md)
│   ├── Hardware (hardware/)
│   ├── Software (software/)
│   ├── Accessibility (accessibility/, ACCESSIBILITY.md)
│   ├── Pilots (pilots/, PILOT_MODEL.md)
│   ├── Partnership Model (PARTNERSHIP_MODEL.md)
│   ├── Prototypes (PROTOTYPES.md)
│   └── Schema Card (SCHEMA_CARD.md), full index (INDEX.md)
│
├── Echo — ukadike.github.io/echo/
│   ├── AI Literacy (index.html, README.md)
│   ├── Starter Lessons / lesson roadmap (index.html §Lesson roadmap; README.md §Starter Lessons)
│   ├── Accessibility Baseline (index.html §Accessibility baseline)
│   └── SSL Method (SSL-METHOD.md)
│
├── Umada — ukadike.github.io/umada/
│   ├── Public Welcome (PUBLIC_README.md)
│   ├── Canon (01_canon/)
│   ├── Governance (00_governance/)
│   ├── Characters (sections/characters.html, 02_characters/)
│   ├── Species (04_species/)
│   ├── World (05_world/, sections/places.html)
│   ├── Timelines (sections/timeline.html, 06_timelines/)
│   ├── Languages (sections/language-signage.html, 07_languages/)
│   ├── Technology (08_technology/)
│   ├── Accessibility (sections/accessibility.html, 09_accessibility/)
│   ├── Visual Canon (sections/visual-canon.html, 20_visual_canon_registry/)
│   ├── Episodes (sections/episode-releases.html, 11_episodes/)
│   ├── Seasons (12_seasons/)
│   ├── Fan Archive (sections/fan-archive.html, 18_fan_archive/)
│   └── Structured Data (data/, see SCHEMA_CARD.md)
│
├── Accessible by Design / Accessibility Audit Lab — ukadike.github.io/accessible-by-design-prototyping/
│   ├── No-Code Web Tool (src/site/website-check.html)
│   ├── Audit Methodology (docs/audit-methodology.md)
│   ├── WCAG 2+ Framework (docs/wcag-2-plus-framework.md)
│   ├── Human Review Guide (docs/human-review-guide.md)
│   ├── p5 Accessibility Guide (docs/p5-accessibility-guide.md, src/site/p5-check.html)
│   ├── PDF Accessibility Guide (docs/pdf-accessibility-guide.md, src/site/pdf-check.html)
│   ├── Workshop Guide (docs/workshop-guide.md)
│   ├── Rules (rules/)
│   ├── Schemas (schemas/)
│   ├── Examples (examples/)
│   └── Reports (reports/)
│
└── Alt Text Wiki (legacy/archive) — github.com/ukadike/alt-text-wiki.lnc
    └── Legacy alt-text examples (index.html, guide.html, performers.html,
        headshots.html, stage-images.html, anecdotal.html) — points to
        Accessible by Design for current work; not part of the shared SSL visual
        system.
```

## Not part of the canonical sitemap above

- **Ounjẹ** — named as a sixth SSL branch in `Small-Systems-Lab/README.md` and
  `index.html`, but has no public repository or site yet. Correctly left unlinked
  ("in development") rather than given a fabricated URL.
- **[omoluabi-news](https://github.com/ukadike/omoluabi-news)** — a stub repo for
  "the first live implementation of the Omoluabi model" (an accessible, portable
  newsroom). Not part of the mission scope for this navigation pass and not listed
  in the canonical sitemap that scoped this audit, but it exists, is a satellite of
  Omoluabi, and already links back to both Omoluabi and Small Systems Lab in its own
  README. No live site yet; flagged for a future pass rather than added here.

## Cross-repo link conventions adopted in this pass

- **Primary ecosystem nav** — every public HTML page links to all six live
  branches (Small Systems Lab, Omoluabi, Earth Sensors Lab, Echo, Umada, Accessible
  by Design) plus the `github.com/ukadike` profile, with `aria-current="page"` on
  the current site's own link. Same-tab for all in-ecosystem links; only the
  external GitHub profile link opens in a new tab, with a visible
  "opens in a new tab" cue.
- **Breadcrumb** — `Small Systems Lab → [Branch] → [Page]`, `aria-current="page"`
  on the last (non-linked) item.
- **README footer** — a `## Related SSL Projects` section linking the hub plus
  every sibling branch, added to every repo's `README.md` in this pass.
- **URL casing** — all GitHub Pages URLs use the lowercase form
  (`ukadike.github.io/small-systems-lab/`, `/omoluabi/`, `/earth-sensors-lab/`,
  `/echo/`, `/umada/`, `/accessible-by-design-prototyping/`), matching the
  casing convention already established across the ecosystem before this pass.

See `docs/NAVIGATION_AUDIT.md` for the full audit: what was broken, what was fixed,
and what's still open.
