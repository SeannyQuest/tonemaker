# Contract: `podgo` CLI Commands

The command surface the tool exposes and that the knowledge pack instructs an LLM to emit. Human-
readable output by default; `--json` where noted. Non-zero exit on error, with the offending block
named. All commands operate only on the user's own unencrypted exports; `hxmp` DRM presets are refused.

## `podgo inspect <file>`

Print the preset name, format (raw/wrapped), input gate, output, and every non-empty block in signal
order with model, `@enabled`, and params. `--json` emits the structured chain.
- **Exit**: 0 on success; error if file is DRM or unreadable.

## `podgo set <file> <addr>=<value> [<addr>=<value> ...] [--out <file>]`

Set one or more parameters. `addr` = `blockN.Param` | `output.gain` | `output.pan` |
`input.threshold` | `input.decay` | `input.noiseGate`. Values parse as int/float/bool automatically.
Writes in place unless `--out`. Runs `validate` before writing.
- **Exit**: 0 on success; error (no write) if the result would fail validation.

## `podgo models [--json] [--category <cat>]`

List verified library models (id + human name), optionally filtered by category. `--json` emits full
entries (type, params, units).

## `podgo validate <file>`

Check a preset will import. Fails, naming the block, on: unknown `@model`; missing required `@`-field
for the block `@type`; non-contiguous `@position` or key/position mismatch; block enabled in `dsp0`
but not the active snapshot (or vice-versa). Unknown param keys are warnings.
- **Exit**: 0 if valid; non-zero with a diagnostic list otherwise.

## `podgo build <spec.json> [--out <file>]`

Build a complete preset from a tone spec (see `tone-spec.schema.json`). Resolves block positions,
fills required `@`-fields from the library, wires snapshot-controlled params (controller 11), runs
`validate`, then writes the `.pgp`.
- **Exit**: 0 on success; error (no write) if the spec is invalid or the result fails validation.

## `podgo new [--template <name>] [--out <file>]`

Create a starter preset — blank or from a bundled template (e.g. `metal-4snapshot`).

## `podgo add <file> block<N>=<modelId> [--out <file>]`

Add/replace a block at position N with a library model, filling its required `@`-fields and rebuilding
snapshot bypass + positions so the result still imports. Runs `validate` before writing.

## `podgo harvest [<path> ...]`

Scan `.pgp` files/folders and add unique verified models (id, type, params) to the library, skipping
DRM and `P34_` I/O blocks. Defaults to `reference/` + `~/Downloads`.

## `podgo context [--out <file>]`

Emit the LLM knowledge pack (schema + full model library + rules + CLI vocabulary + worked example),
generated from `models.json`. Prints to stdout (pipe to a file or clipboard) or writes `--out`.

## LLM output contract

The knowledge pack instructs the user's LLM to respond with **either**:
1. a `build` **tone spec** (JSON conforming to `tone-spec.schema.json`), to be saved and built; **or**
2. a sequence of **`podgo set`/`podgo add`** commands against a named file.

Both paths end by running `podgo validate`, so any hallucinated model id is caught before import.
