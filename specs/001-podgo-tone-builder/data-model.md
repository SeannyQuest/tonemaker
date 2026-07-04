# Phase 1 Data Model: POD Go Tone Builder

Entities are derived from the spec and from the observed `.pgp` contract. "Observed contract" means
these shapes come from real device exports, not a published spec.

## Preset

The top-level tone. On disk in one of two forms; the engine normalizes to the inner preset.

- **format**: `raw` (`{data, meta, schema, version}`) or `wrapped` (`{encoded_data, compression,
  encryption, ...}` where `encoded_data = base64(zlib(inner))`).
- **encryption**: if `type == "hxmp"` → DRM; engine MUST refuse (Principle II).
- **data.meta.name**: display name.
- **data.tone.dsp0**: the signal path (see Block, plus `input` and `output`).
- **data.tone.global.@current_snapshot**: index (0–3) of the active snapshot.
- **data.tone.snapshot0..3**: Snapshot entries.
- **data.tone.controller.dsp0**: per-block param → `{@min,@max,@controller}` snapshot-control wiring.

**Rules**: load→save is lossless (Principle I). A preset is "valid" only if it passes `validate` (III).

## Block

One position in `dsp0`, keyed `block0`..`block9`.

- **@position** (int 0..9): chain order; block-key index MUST equal `@position`.
- **@model** (string): POD Go internal id, e.g. `HD2_AmpCaliRectifire`; MUST exist in the library (V).
- **@type** (int): 0=effect/EQ/dyn/wah/vol, 1=amp, 2=legacy cab, 5=FX-loop/verb/delay (trails).
- **@enabled** (bool): on/off in `dsp0`.
- **type-specific required fields**: amp→`@bypassvolume`; cab→`@mic`; reverb/delay/FX-loop→`@trails`.
- **params**: non-`@` keys — normalized 0.0–1.0 for amp/drive/mix knobs; Hz for freq/cut; dB for
  gain/level; per the model's entry in the library.
- Six blocks are dedicated (Volume, Wah, Amp, Cab, EQ, FX Loop); up to four are user effects. An empty
  slot is just `{"@position": N}`.

## Input gate & Output (`dsp0.input`, `dsp0.output`)

- **input**: `noiseGate` (bool), `threshold` (dB, e.g. -56), `decay` (0–1).
- **output**: `pan` (0–1, 0.5=center), `gain` (dB).

## Snapshot

`data.tone.snapshot0..3` — a saved variation inside one preset.

- **@name**, **@tempo**, **@valid**.
- **blocks.dsp0.{blockKey: bool}**: per-block bypass override. Enabling a block requires enabling it
  here too (the gotcha `set_enabled` already handles).
- **controllers.dsp0.{blockKey}.{param}: {@fs_enabled, @value}**: snapshot-held parameter values,
  paired with a `controller.dsp0` entry using `@controller: 11` (11 = snapshots).

## Model library (`models.json`)

Verified catalog, grouped by category (amp, cab, distortion, modulation, delay, reverb, eq, pitch,
dynamics, utility, filter). Each entry:

- **key**: the exact `@model` id.
- **name**: human-readable gear name (auto-harvested entries start `(auto-harvested)` and get curated).
- **type**: the `@type` int.
- **params**: ordered list of parameter keys.
- **extra_fields** (optional): required `@`-fields (`@bypassvolume`/`@mic`/`@trails`).
- **units**/**bool_params** (optional): units and boolean params where known.

**Rules**: entries only from real exports/app data (V); this file is the single source of truth for
the knowledge pack (IV).

## Tone spec (build input)

Declarative description the builder turns into a Preset. Governed by
`contracts/tone-spec.schema.json`.

- **name** (string)
- **blocks**: `[{model, position, enabled?, params?}]`
- **input?**, **output?**: overrides for the gate/output
- **snapshots?**: `[{name, bypass?:{blockKey:bool}, params?:{blockKey:{param:value}}}]`

The builder resolves `blockN` from `position`, fills required `@`-fields from the library, wires
snapshot params via controller 11, then runs `validate` before writing.

## Knowledge pack (`context` output)

Generated from the library + curated preamble. Contains: the `.pgp` schema summary, the 10-block
architecture + snapshot gotchas, the full model library (ids/params/units), the CLI vocabulary, and
one worked example. Invariant: every model it names exists in `models.json` (IV).
