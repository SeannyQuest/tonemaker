# Quickstart & Validation Guide: POD Go Tone Builder

Runnable scenarios that prove the feature works end-to-end. Assumes the package is installed
(`pip install -e .` from the repo during development, or `pip install podgo-tones` once published).

## Prerequisites

- Python 3.9+
- POD Go Edit (for the final import check) — `/Applications/Line6/POD Go Edit.app` on macOS
- Reference exports present under `reference/` (dev) — used by the round-trip test

## Scenario A — Inspect & edit (US2, Principles I–III)

```bash
podgo inspect reference/logic.pgp                 # prints chain + params
podgo set reference/logic.pgp block2.Drive=0.62 --out /tmp/edited.pgp
podgo inspect /tmp/edited.pgp                      # only Drive changed
podgo validate /tmp/edited.pgp                     # exit 0
```
**Expected**: chain matches POD Go Edit; only the intended value changed; validation passes.

## Scenario B — DRM refusal (Principle II)

```bash
podgo inspect "path/to/a/commercial-pack.pgp"      # if hxmp-encrypted
```
**Expected**: clear refusal, non-zero exit, no decryption attempted.

## Scenario C — Build from a tone spec (US3)

```bash
podgo build examples/specs/doom.json --out /tmp/doom.pgp   # spec conforms to tone-spec.schema.json
podgo inspect /tmp/doom.pgp                                 # chain + snapshots match the spec
podgo validate /tmp/doom.pgp                                # exit 0
```
**Expected**: built preset matches the spec; validation passes before the file is written.

## Scenario D — Validation catches a bad model (Principle III)

```bash
# a spec referencing a non-existent model id, or a hand-broken preset
podgo validate /tmp/broken.pgp
```
**Expected**: non-zero exit; message names the offending block and the unknown `@model`.

## Scenario E — Knowledge pack ⊆ library (Principle IV, US1)

```bash
podgo context --out /tmp/PODGO_LLM_CONTEXT.md
```
**Expected**: a self-contained pack (schema + full model library + rules + worked example); every
model it names exists in `models.json` (guarded by `tests/test_context.py`).

## Scenario F — Extend the library from your own export (US4)

```bash
podgo models | wc -l                               # baseline count
podgo harvest ~/Downloads/MyExport.pgp             # adds any new verified models
podgo models | wc -l                               # count increased for new models
```
**Expected**: models from a real export are added with exact ids/params.

## Scenario G — End-to-end acceptance (SC-002)

1. Build or edit a preset (Scenario A or C).
2. In POD Go Edit, import the `.pgp` (drag onto a slot or right-click → Import).
3. **Expected**: it loads with the intended chain and **no** "unrecognized models" error.

## Automated tests

```bash
pytest            # round-trip (I), validate (III), build (US3), context⊆library (IV)
```
