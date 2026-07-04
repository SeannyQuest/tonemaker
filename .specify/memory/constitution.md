<!--
Sync Impact Report
- Version change: (template) → 1.0.0
- Ratification: initial adoption
- Principles defined:
  I. Lossless Round-Trip Integrity
  II. Respect Ownership & DRM (Never Crack)
  III. Validate Before Import (NON-NEGOTIABLE)
  IV. Single Source of Truth (No Knowledge Drift)
  V. Verified Library Only
- Sections added: Distribution & Licensing; Development Workflow; Governance
- Templates reviewed for alignment:
  ✅ .specify/templates/plan-template.md (Constitution Check gate references these principles)
  ✅ .specify/templates/spec-template.md (no mandatory-section conflicts)
  ✅ .specify/templates/tasks-template.md (validation/test task types consistent)
- Deferred TODOs: none
-->

# POD Go Tones Constitution

POD Go Tones (`podgo-tones`) is a Python package and CLI that lets anyone edit Line 6 POD Go
`.pgp` presets as data, and — via a machine-readable knowledge pack — lets them drive that editing
with any large language model of their choice. These principles are non-negotiable and govern every
spec, plan, task, and line of code in the project.

## Core Principles

### I. Lossless Round-Trip Integrity
Loading a preset and saving it back MUST NOT alter any data the operation did not explicitly intend
to change. The engine MUST support both on-disk formats — raw (`{data, meta, schema, version}`) and
wrapped (`base64(zlib(preset_json))`) — and round-trip each without corruption. Every change to the
load/save path MUST be covered by a test that loads a real device export, saves it, and asserts the
re-parsed signal chain is identical. Rationale: a preset that silently mutates is worse than useless
— it destroys the user's work and their trust in the tool.

### II. Respect Ownership & DRM (Never Crack)
The tool operates ONLY on the user's own unencrypted exports. It MUST detect commercial/DRM presets
(`encryption.type: "hxmp"`) and refuse to decode or edit them — never attempt to crack, bypass, or
work around that encryption. The project MUST NOT redistribute third-party commercial preset packs.
Only presets authored by the project (or the user) may ship as examples. Rationale: paid packs are
someone else's livelihood; respecting that is both legally required and ethically non-negotiable.

### III. Validate Before Import (NON-NEGOTIABLE)
POD Go rejects an entire preset if any one block's `@model` is unrecognized. Therefore no preset the
tool emits, builds, or returns is considered valid until it passes validation: every `@model` exists
in the verified library, required `@`-fields are present per block `@type` (amp→`@bypassvolume`,
cab→`@mic`, reverb/delay/FX-loop→`@trails`), `@position` values are contiguous and match block-key
order, and snapshot bypass entries are consistent with `dsp0`. `build` and `set` operations MUST run
validation before writing final output. Rationale: an LLM will occasionally emit a plausible-but-wrong
model ID; validation is the safety net that keeps the "describe a tone" workflow trustworthy.

### IV. Single Source of Truth (No Knowledge Drift)
`models.json` is the one authoritative model library. The LLM knowledge pack (`PODGO_LLM_CONTEXT.md`)
and any machine-readable schema MUST be GENERATED from `models.json` (plus curated docs), never
hand-maintained in parallel. A change to the library MUST regenerate the knowledge pack in the same
change. Rationale: two hand-edited copies of the same facts inevitably diverge, and a stale knowledge
pack produces presets that fail to import.

### V. Verified Library Only
Model entries in `models.json` MUST originate from real POD Go exports or authoritative POD Go
application data — never guessed, never copied from Helix-Native lists (whose IDs omit the `Mono`/
`Stereo` suffixes POD Go requires). Auto-harvested entries MUST be traceable to a source file and
carry their exact `@model` string, `@type`, and parameter keys. Rationale: a single wrong ID poisons
every preset that uses it, and guessed IDs are the most common cause of failed imports.

## Distribution & Licensing

- **Package**: distributed as `podgo-tones` on PyPI; installable with `pip install podgo-tones`;
  exposes a single `podgo` console entry point. Bundled data (library, templates, knowledge pack)
  MUST be shipped as package resources and loaded via `importlib.resources`.
- **LLM-agnostic**: the tool MUST NOT embed API keys, require a specific LLM provider, or make network
  calls to an LLM. Its role is to emit a knowledge pack and to apply/validate the commands or specs a
  user's own LLM produces.
- **License & attribution**: released under the MIT License. All distributions MUST carry the notice:
  "Unofficial — not affiliated with or endorsed by Line 6 / Yamaha Guitar Group. POD Go and Helix are
  trademarks of their respective owners."

## Development Workflow

- **Spec-driven**: work proceeds through the Spec Kit flow — constitution → specify → (clarify) →
  plan → tasks → (analyze) → implement. Code changes trace back to a task, which traces to the spec.
- **Constitution Check**: `plan` MUST include a gate confirming the design honors Principles I–V; any
  deviation MUST be justified in writing or the design MUST change.
- **Tests**: `pytest` is the test runner. Round-trip integrity (I) and validation behavior (III) MUST
  have explicit tests. CI runs the test suite on every push; releases publish to PyPI on a version tag.
- **Reuse over rewrite**: existing verified logic (lossless load/save, snapshot-bypass gating,
  controller-11 snapshot wiring) MUST be reused rather than reimplemented.

## Governance

This constitution supersedes ad-hoc practice. Amendments MUST be made by editing this file with an
updated Sync Impact Report and a semantic version bump: MAJOR for removing or redefining a principle,
MINOR for adding a principle or section, PATCH for clarifications. When a principle changes, dependent
Spec Kit templates and project docs MUST be reviewed for alignment in the same change. Every plan and
review MUST verify compliance with the principles above; unavoidable complexity that touches a
principle MUST be explicitly justified.

**Version**: 1.0.0 | **Ratified**: 2026-07-04 | **Last Amended**: 2026-07-04
