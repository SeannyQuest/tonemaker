# Phase 0 Research & Decisions: POD Go Tone Builder

Resolves the open technical choices (the `/clarify` topics) using the user's locked product
direction (Python package on PyPI, comprehensive verified library, LLM-agnostic). No `NEEDS
CLARIFICATION` markers remain.

## D1 — Distribution & packaging backend

- **Decision**: Ship as `podgo-tones` on PyPI, src-layout package `src/podgo/`, single `podgo` console
  entry point, `pyproject.toml` with the **hatchling** build backend. Require Python **3.9+**.
- **Rationale**: Hatchling includes package data (our `data/` tree) with minimal config and handles
  src-layout cleanly. 3.9 is the floor because `importlib.resources.files()` (the clean data-access
  API) is available from 3.9. Zero runtime third-party deps keeps install trivial and audit-free.
- **Alternatives**: setuptools (more boilerplate for data files); flit (weaker data-file story);
  requiring 3.11 (needlessly narrows the audience).

## D2 — Bundled data access

- **Decision**: Load `models.json`, templates, and the knowledge pack via
  `importlib.resources.files("podgo.data") / ...`.
- **Rationale**: Works identically from a source checkout and an installed wheel/zip; no `__file__`
  path hacks that break when zipped.
- **Alternatives**: `__file__`-relative paths (break in zipimport); `pkg_resources` (deprecated).

## D3 — Model-library acquisition order (the comprehensiveness dependency)

- **Decision**: Populate `models.json` in this order, stopping when coverage is comprehensive:
  1. **Harvest on-disk now** — `reference/` exports + the 5 artist presets + the 22 **TDR Djent**
     presets in `~/Downloads/Pod GO Djent & Prog-Metal/` (verified editable, not DRM).
  2. **Factory setlist** — bulk-export from POD Go Edit, then harvest.
  3. **POD Go Edit app-bundle mining** — inspect `/Applications/Line6/POD Go Edit.app` for a bundled
     model database (authoritative full ~250-model list + default params + display names).
  4. **Crowdsource** — users contribute via the harvest workflow + PRs for anything still missing.
- **Rationale**: Each step is strictly cheaper-per-model than the next; (3) is the potential jackpot
  that removes calibration entirely. Guessing is forbidden (Principle V), so every entry traces to a
  real source.
- **Alternatives**: Copying Helix-Native ID lists — rejected: their IDs omit the `Mono`/`Stereo`
  suffixes POD Go requires and fail to import.

## D4 — Tone-spec format for `build`

- **Decision**: A single JSON object: `{name, blocks:[{model, position, enabled, params:{}}],
  input:{}, output:{}, snapshots:[{name, bypass:{blockKey:bool}, params:{blockKey:{param:value}}}]}`.
  Governed by `contracts/tone-spec.schema.json`. The builder resolves `blockN` keys from `position`,
  fills required `@`-fields per model `@type` from the library, and wires snapshot-controlled params
  via controller 11 (reusing the proven logic from `build_artist_presets.py`).
- **Rationale**: A flat, declarative spec is easy for an LLM to emit and for the builder to validate.
  Snapshots-as-overrides matches POD Go's actual model (snapshots gate bypass + hold param values).
- **Alternatives**: Imperative command scripts only (harder to validate as a whole); YAML (adds a dep
  and ambiguity).

## D5 — CLI command surface & LLM output vocabulary

- **Decision**: Commands: `inspect`, `set`, `models`, `validate`, `build`, `harvest`, `context`,
  `new`, `add`. The knowledge pack documents the exact vocabulary and instructs the LLM to emit either
  (a) a `build` tone-spec JSON, or (b) a sequence of `podgo set/add` commands. Human-readable output by
  default; `--json` where a machine-readable form helps.
- **Rationale**: Two output modes cover both "build from scratch" (spec) and "tweak this" (commands).
  Documenting the vocabulary in the generated pack keeps LLM output runnable and in-sync (Principle IV).
- **Alternatives**: A bespoke DSL (needless learning curve); free-form (unparseable/unvalidatable).

## D6 — Validation rules (Principle III made concrete)

- **Decision**: `validate` fails (naming the block) if any of: an `@model` is not in `models.json`; a
  required `@`-field for the block's `@type` is missing (amp→`@bypassvolume`, cab→`@mic`,
  reverb/delay/FX-loop→`@trails`); `@position` values are not contiguous `0..N` or don't match
  block-key order; a block is enabled in `dsp0` but not in the active snapshot (or vice-versa); a
  parameter key is not among the model's known params (warning, not hard-fail, to tolerate firmware
  additions). `build` and `set` invoke `validate` before writing final output.
- **Rationale**: These are exactly the conditions that make POD Go reject a preset; catching them
  pre-import is the whole value of the safety net.
- **Alternatives**: Import-and-see (bad UX, requires the device); schema-only checks (miss the
  cross-field snapshot/position rules).

## D7 — Knowledge-pack generation (no drift)

- **Decision**: `context` generates `PODGO_LLM_CONTEXT.md` (+ `schema.json`) from `models.json` plus a
  small curated prose preamble (schema explanation, gotchas, one worked example). Generated files are
  checked in but carry a "generated — do not edit" header; a test asserts every model named in the
  pack exists in `models.json`.
- **Rationale**: Principle IV — the pack must never describe a model the tool can't build. Generating
  it makes divergence a build/test failure instead of a silent runtime import error.
- **Alternatives**: Hand-written pack (drifts); generating at runtime only (fine, but checking in a
  copy aids discoverability and lets the test guard it).

## D8 — Reuse map (don't rewrite verified logic)

- `pgp_tool.py` → `engine.py`: `load/save` (raw+wrapped, hxmp refusal), `chain`, `set_param`,
  `set_enabled` (snapshot-bypass gating) move ~verbatim.
- `build_artist_presets.py` → `build.py`: extract the block-template assembly, preamp-vs-amp gain
  handling, and controller-11 snapshot wiring into a spec-driven builder.
- `harvest_models.py` → `harvest.py`: category mapping + dedupe + DRM/`P34_` skipping reused as-is.
- `models.json`: moves under `src/podgo/data/` unchanged (then extended per D3).
