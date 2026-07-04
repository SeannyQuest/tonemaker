# Tasks: POD Go Tone Builder

**Feature**: `001-podgo-tone-builder` | **Input**: plan.md, spec.md, research.md, data-model.md,
contracts/, quickstart.md

**Tests**: included — the constitution mandates tests for Lossless Round-Trip (I) and Validate-Before-
Import (III), and the spec's success criteria (SC-002/003/005) require them.

**Conventions**: `[P]` = parallelizable (different files, no incomplete deps). `[USn]` maps to the
spec's user stories. Paths are repo-relative. Existing scripts are **moved** (git mv) then adapted,
never rewritten from scratch.

## Phase 1: Setup

- [ ] T001 Create `pyproject.toml` at repo root: hatchling backend, src-layout, project name
  `podgo-tones`, Python `>=3.9`, no runtime deps, console entry point `podgo = "podgo.cli:main"`,
  include package data `podgo/data/**`.
- [ ] T002 Create package skeleton `src/podgo/__init__.py` (version string) and an empty
  `src/podgo/data/` tree with `templates/` and `knowledge/` subdirs.
- [ ] T003 `git mv models.json src/podgo/data/models.json` (move the verified library into the package).
- [ ] T004 Create minimal `src/podgo/cli.py` with an `argparse` dispatcher and a `main()` that
  registers subcommands as they land (start with `inspect`); confirm `pip install -e .` then
  `podgo --help` works.

## Phase 2: Foundational (blocking prerequisites)

- [ ] T005 `git mv pgp_tool.py src/podgo/engine.py`; adjust to load `models.json` via
  `importlib.resources.files("podgo.data")`; keep `load/save` (raw+wrapped, `hxmp` refusal),
  `chain`, `set_param`, `set_enabled` behavior intact.
- [ ] T006 [P] Add `src/podgo/_resources.py` (or a helper in engine) that resolves bundled data paths
  via `importlib.resources` so `models.json`, templates, and knowledge load from an installed wheel.
- [ ] T007 Create `src/podgo/validate.py` implementing the rules in contracts/cli-commands.md &
  research.md D6: unknown `@model`, missing required `@`-field per `@type`, non-contiguous/mismatched
  `@position`, snapshot-bypass inconsistency (hard fails, block-named); unknown param key (warning).
- [ ] T008 [P] `tests/test_roundtrip.py` — load each `reference/*.pgp`, save to a temp path, reload,
  assert the signal chain is identical (Principle I / SC-003).
- [ ] T009 [P] `tests/test_validate.py` — assert a preset with a bogus `@model` and an out-of-order
  `@position` both fail with block-naming diagnostics; a clean reference export passes (Principle III).

**Checkpoint**: engine + validation + data loading work and are tested; stories can build on them.

## Phase 3: User Story 1 — Design a tone with any LLM (Priority: P1) 🎯 MVP

**Goal**: A user hands the generated knowledge pack to their own LLM, describes a tone, and gets
output the tool can turn into an importable preset.

**Independent test**: `podgo context` emits a self-contained pack; feeding it + a tone request to an
LLM yields commands/spec that produce a preset which passes `podgo validate` and imports.

- [ ] T010 [US1] Create `src/podgo/context.py` that generates `PODGO_LLM_CONTEXT.md` from
  `models.json` + a curated prose preamble (schema summary, 10-block architecture, snapshot/controller
  gotchas, CLI vocabulary from contracts/cli-commands.md, one worked example), and generates
  `schema.json` from the tone-spec contract. Files carry a "generated — do not edit" header.
- [ ] T011 [US1] Wire `podgo context [--out]` in `cli.py` (stdout by default) and write the generated
  `src/podgo/data/knowledge/{PODGO_LLM_CONTEXT.md,schema.json}` into the package.
- [ ] T012 [P] [US1] `tests/test_context.py` — assert every model id named in the generated pack
  exists in `models.json` (Principle IV / SC-005), and the pack contains the schema, library, rules,
  and worked-example sections.

**Checkpoint**: US1 independently deliverable — the knowledge pack drives any LLM.

## Phase 4: User Story 2 — Inspect and edit a preset (Priority: P1)

**Goal**: See a preset's full chain and tweak parameters without opening POD Go Edit.

**Independent test**: inspect a real export (matches POD Go Edit); set a param, save, re-inspect —
only that value changed and it still validates.

- [ ] T013 [US2] `git mv podgo.py` content into `cli.py` as the `inspect` command (name, format, gate,
  output, chain) with an optional `--json`.
- [ ] T014 [US2] Add `set <file> <addr>=<value>... [--out]` to `cli.py` reusing `engine.set_param`;
  run `validate` before writing; refuse to write (nonzero exit) if the result would be invalid.
- [ ] T015 [P] [US2] Verify DRM refusal is surfaced by the CLI (engine raises on `hxmp`; `inspect`/`set`
  exit nonzero with a clear message) — add a short test or quickstart assertion.

**Checkpoint**: US1 + US2 together form a usable tool (design + edit + validate).

## Phase 5: User Story 3 — Build a full preset from a tone spec (Priority: P2)

**Goal**: Build a complete, multi-snapshot preset from one structured spec.

**Independent test**: build from a spec; inspect the result; chain/params/snapshots match and it
validates.

- [ ] T016 [US3] Create `src/podgo/build.py` by extracting from `build_artist_presets.py`: block-
  template assembly, required `@`-field filling from the library, preamp-vs-amp handling, and
  controller-11 snapshot wiring; input is a tone spec conforming to contracts/tone-spec.schema.json.
- [ ] T017 [US3] Add `build <spec.json> [--out]` and `new [--template] [--out]` to `cli.py`; both run
  `validate` before writing. Add `src/podgo/data/templates/metal-4snapshot.json`.
- [ ] T018 [P] [US3] `tests/test_build.py` — build from a fixture spec, then assert the produced
  preset's chain, params, and per-snapshot bypass/params match the spec and it passes validation.

## Phase 6: User Story 4 — Comprehensive library, no calibration (Priority: P2)

**Goal**: Stock POD Go models available by verified id; user can extend from their own exports.

**Independent test**: `podgo models` lists stock models with correct ids; a preset using several
imports; harvesting a new export adds its models.

- [ ] T019 [US4] `git mv harvest_models.py src/podgo/harvest.py`; adapt paths to the package library;
  keep category mapping, dedupe, DRM/`P34_` skipping.
- [ ] T020 [US4] Add `models [--json] [--category]`, `harvest [path...]`, and `add <file>
  block<N>=<modelId> [--out]` to `cli.py` (`add` fills required `@`-fields and rebuilds positions +
  snapshot bypass; runs `validate`).
- [ ] T021 [US4] Populate the library (research.md D3 order): harvest `reference/` + the 5 artist
  presets + the 22 editable TDR Djent presets in `~/Downloads/Pod GO Djent & Prog-Metal/`; curate
  human `name` fields for auto-harvested entries. (Factory setlist + app-bundle mining tracked in Polish.)

## Phase 7: User Story 5 — Install and get started in one step (Priority: P3)

**Goal**: One-command install, one-command knowledge pack.

**Independent test**: install the built package in a clean venv; `podgo --help` and `podgo context`
both work.

- [ ] T022 [US5] Rewrite `README.md`: quickstart (`pip install podgo-tones` → `podgo context | pbcopy`
  → paste into any LLM → run commands → import), command reference, calibration/harvest note.
- [ ] T023 [P] [US5] `git mv presets/ examples/` (the 5 artist presets) and reference them from README
  and quickstart; ensure they ship with the sdist.
- [ ] T024 [US5] Build wheel + sdist (`python -m build`), install into a fresh venv, and run
  quickstart Scenarios A/E to confirm packaged data resolves via `importlib.resources`.

## Phase 8: Polish & Cross-Cutting

- [ ] T025 [P] Add `LICENSE` (MIT) + the unofficial/trademark notice (constitution) to README and
  package metadata.
- [ ] T026 [P] Add `.github/workflows/ci.yml`: run `pytest` on push/PR; publish to PyPI on version tag.
- [ ] T027 Configure the wheel to exclude `reference/` (dev-only ground truth) while keeping
  `podgo/data/**` and `examples/`.
- [ ] T028 Library completeness (research.md D3 steps 2–3): export the POD Go factory setlist and
  harvest it; investigate/parse `/Applications/Line6/POD Go Edit.app` for the authoritative model DB;
  merge findings into `models.json` and regenerate the knowledge pack (`podgo context`).
- [ ] T029 End-to-end acceptance (quickstart Scenario G / SC-002): build a preset and import it into
  POD Go Edit; confirm it loads with no "unrecognized models" error. Document the result.

## Dependencies & Execution Order

- **Setup (P1–T004)** → **Foundational (T005–T009)** block everything.
- **User stories** after Foundational: US1 (T010–T012) and US2 (T013–T015) are independent (both P1);
  US3 (T016–T018) depends on engine+validate; US4 (T019–T021) depends on engine+library; US5
  (T022–T024) depends on the CLI existing.
- **Polish (T025–T029)** last; T028/T029 depend on a working `build`/`context` and library.

**MVP scope**: Phases 1–3 (Setup + Foundational + US1) — the knowledge pack + validation loop, the
project's headline capability. Adding Phase 4 (US2) yields a fully usable design+edit tool.

## Parallel Opportunities

- T006, T008, T009 can run together (different files) once T005 lands.
- T012 parallel with T010–T011 wiring; T015 parallel within US2; T018 parallel within US3.
- T023, T025, T026 are independent polish tasks (`[P]`).
