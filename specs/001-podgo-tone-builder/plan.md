# Implementation Plan: POD Go Tone Builder

**Branch**: `001-podgo-tone-builder` | **Date**: 2026-07-04 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `specs/001-podgo-tone-builder/spec.md`

## Summary

Package the existing POD Go `.pgp` tooling into an installable, LLM-drivable CLI (`podgo-tones` on
PyPI, `podgo` entry point). The core is a lossless preset engine plus a pre-import validator; on top
sit a spec-driven preset builder, a model-library harvester, and a `context` command that emits a
knowledge pack generated from the library so any LLM can produce importable tones. Reuse the proven
load/save, snapshot-bypass gating, and controller-11 snapshot wiring already in the repo; add
`validate`, generalize the artist-preset builder into a spec builder, and generate the knowledge pack.

## Technical Context

**Language/Version**: Python 3.9+ (developed on 3.14; standard library only — `json`, `base64`,
`zlib`, `argparse`, `importlib.resources`)

**Primary Dependencies**: None at runtime (zero third-party deps). Dev/build: `pytest`, `build`,
`twine`. Packaging via `pyproject.toml` (setuptools/hatchling backend).

**Storage**: Files only — `.pgp` presets (JSON, raw or `base64(zlib(...))`); bundled package data
(`models.json`, tone-spec templates, generated knowledge pack).

**Testing**: `pytest` — lossless round-trip on reference exports; validation catches known failure
modes; build-from-spec matches spec.

**Target Platform**: Cross-platform (macOS/Windows/Linux) CLI; wherever POD Go Edit users run.

**Project Type**: Single-project Python library + CLI.

**Performance Goals**: N/A (interactive single-file operations; presets are small JSON).

**Constraints**: No network calls to any LLM; no third-party runtime deps; must not mutate preset
data outside the intended edit (lossless); must refuse `hxmp` DRM.

**Scale/Scope**: ~10 blocks per preset, 4 snapshots, a library of up to ~250 stock POD Go models;
single-user desktop usage.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | How this plan complies |
|-----------|------------------------|
| I. Lossless Round-Trip | `engine.load/save` (from `pgp_tool.py`) round-trips raw + wrapped; a pytest asserts reference exports are unchanged. |
| II. Respect Ownership & DRM | `load` refuses `encryption.type: "hxmp"`; only the user's own presets ship as examples; no decryption code. |
| III. Validate Before Import | New `validate.py`; `build` and `set` run it before writing final output; errors name the offending block. |
| IV. Single Source of Truth | `context` generates `PODGO_LLM_CONTEXT.md` + `schema.json` from `models.json`; a test asserts the pack references only library models. |
| V. Verified Library Only | Library entries come only from real exports/app data via `harvest.py`; auto-harvested entries retain exact ids/params and a source trace. |

No violations. Complexity Tracking not required.

## Project Structure

### Documentation (this feature)

```text
specs/001-podgo-tone-builder/
├── plan.md              # This file
├── research.md          # Phase 0 output (decisions + rationale)
├── data-model.md        # Phase 1 output (Preset/Block/Snapshot/Library/ToneSpec entities)
├── quickstart.md        # Phase 1 output (end-to-end validation guide)
├── contracts/
│   ├── cli-commands.md      # CLI command contract (the vocabulary an LLM emits)
│   └── tone-spec.schema.json # JSON Schema for the build tone spec
└── tasks.md             # Phase 2 output (/speckit-tasks — not created here)
```

### Source Code (repository root)

```text
src/podgo/
├── __init__.py
├── engine.py            # from pgp_tool.py — load/save/chain/set_param/set_enabled (reuse ~verbatim)
├── validate.py          # NEW — pre-import checker (Principle III safety net)
├── build.py             # generalized from build_artist_presets.py — tone-spec/template builder
├── harvest.py           # from harvest_models.py — extend library from real exports
├── context.py           # NEW — generate knowledge pack + schema from models.json
├── cli.py               # from podgo.py — argparse dispatch: inspect/set/models/validate/build/harvest/context/new/add
└── data/
    ├── models.json          # verified library (moved from repo root)
    ├── templates/*.json     # tone-spec templates (e.g. metal-4snapshot)
    └── knowledge/
        ├── PODGO_LLM_CONTEXT.md   # generated (do not hand-edit)
        └── schema.json            # generated

examples/                 # the 5 artist presets (user's own work)
reference/                # ground-truth device exports (dev-only; excluded from wheel)
tests/
├── test_roundtrip.py     # Principle I
├── test_validate.py      # Principle III
├── test_build.py         # US3
└── test_context.py       # Principle IV (pack ⊆ library)
pyproject.toml            # entry point: podgo = podgo.cli:main
LICENSE                   # MIT + unofficial/trademark notice
README.md                 # rewritten quickstart (install → context → LLM → import)
.github/workflows/ci.yml  # pytest on push; PyPI publish on tag
```

**Structure Decision**: Single Python package under `src/podgo/` (src-layout for clean packaging).
Bundled data lives under `src/podgo/data/` and is loaded via `importlib.resources` so it works when
pip-installed. Existing top-level scripts are moved (not rewritten) into the package; `reference/` is
kept for tests but excluded from the built wheel; `examples/` (user's own presets) ships with docs.

## Complexity Tracking

No constitution violations; section intentionally empty.
