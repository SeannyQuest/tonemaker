# POD Go Tones

Build and edit Line 6 POD Go guitar tones as data. POD Go Edit has no API, but
its preset files (`.pgp`) are editable JSON, so tones can be described in plain
language and dialed in by editing parameters directly.

## How it works
A POD Go preset has 10 blocks (`block0`..`block9`) on signal path `dsp0`, ordered
by each block's `@position`. Six blocks are dedicated + movable + always present
(Volume, Wah, Amp, Cab, EQ, FX Loop); up to four are user-assignable effects.
`dsp0.input` holds the noise gate; `dsp0.output` holds master pan/gain. Snapshots
(`snapshot0`..`3`) store per-block bypass — enabling a block in `dsp0` is not
enough, it must also be on in the active snapshot.

- **Your own exports are editable** (`encryption: None`).
- **Commercial packs are DRM** (`encryption.type: hxmp`) — cannot be edited.

## Usage
```bash
# inspect a preset's full signal chain + params
python3 podgo.py inspect "presets/Loathe Fangs.pgp"

# edit parameters in place (or with --out)
python3 podgo.py set "presets/Loathe Fangs.pgp" block2.Drive=0.62 output.gain=8
python3 podgo.py set "presets/x.pgp" block5.Mix=0.3 --out "presets/y.pgp"

# list verified model IDs
python3 podgo.py models
```
Then import the `.pgp` into POD Go Edit (drag onto a slot, or right-click → Import).

## Adding new models (calibration)
POD Go uses a **subset** of Helix models, and its internal IDs carry `Mono`/`Stereo`
suffixes the public Helix lists omit — so guessed IDs fail to import (POD Go rejects
the whole preset if any one block is unrecognized). The reliable way to add a model:
1. In POD Go Edit, add the block you want, export the preset.
2. `python3 podgo.py inspect <that file>` to read its exact `@model` + param keys.
3. Add the entry to `models.json`.

`models.json` is the verified library; `reference/` holds the ground-truth device
exports it was built from (`logic.pgp`, `Test.pgp`).

## Files
- `pgp_tool.py` — load/save/inspect engine (lossless round-trip)
- `podgo.py` — CLI
- `models.json` — verified POD Go model IDs + parameter keys
- `reference/` — real device exports (ground truth)
- `presets/` — built tones

## Tones
- **Loathe Fangs** — downtuned / shoegaze / fuzz (Loathe "Fangs" vibe):
  Gate → Triangle Fuzz → Cali Rectifire → 4x12 V30 → Parametric EQ → 70s Chorus → Ganymede reverb.
