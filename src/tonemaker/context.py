#!/usr/bin/env python3
"""Generate the LLM knowledge pack from the verified model library.

`tonemaker context` prints this so a user can paste it into ANY LLM (Claude, ChatGPT,
local) and have it produce importable POD Go tones. It is GENERATED from models.json
(Principle IV) — every model it names is one the tool actually supports, so it can
never drift into describing gear that would fail to import.
"""
import json

from ._resources import load_models, data_path

_PREAMBLE = """\
# POD Go Tone Builder — LLM Knowledge Pack

> Generated from the verified model library. Do not hand-edit. Paste this whole
> document into your LLM, then describe the guitar tone you want.

You are helping design a tone for the **Line 6 POD Go** by producing data the
`tonemaker` command-line tool can turn into an importable `.pgp` preset. Respond with
**either** of these, and nothing that can't be run:

1. **A tone spec** — a JSON object conforming to the schema below — which the user
   saves as `tone.json` and builds with: `tonemaker build tone.json --out tone.pgp`
2. **A sequence of `tonemaker set` / `tonemaker add` commands** against a named `.pgp` file.

Either way, finish by telling the user to run `tonemaker validate tone.pgp` — this
catches any wrong model id before they try to import it.

## The `.pgp` model (what you're editing)

- A preset is a signal chain of **10 blocks** (`block0`..`block9`) plus an input
  noise gate and a master output. Chain order = each block's `position`.
- Six blocks are dedicated and always present (Volume, Wah, Amp, Cab, EQ, FX Loop);
  up to four are user-assignable effects (distortion, modulation, delay, reverb, ...).
- **Model ids are exact.** Use only the ids listed below (they carry `Mono`/`Stereo`
  suffixes). If ANY block's model id is unrecognized, POD Go rejects the WHOLE preset.
- **Parameter ranges**: amp/drive/fuzz/mix knobs are normalized `0.0`–`1.0`; EQ/cab
  frequencies and cuts are in Hz; gains and levels are in dB; the noise-gate threshold
  is in dB (e.g. `-56`).
- **Snapshots**: a preset can hold up to 4 snapshots (e.g. Clean / Rhythm / Lead /
  Breakdown). Each snapshot overrides which blocks are on (`bypass`) and the values of
  designated parameters (`params`). Keep the active snapshot consistent with which
  blocks you leave enabled.

## Model library (verified — use these ids exactly)
"""

_EXAMPLE = """\
## Worked example

Request: *"A doomy, downtuned tone — heavy fuzz into a mid-scooped Recto, big cave reverb."*

A valid tone spec:

```json
{
  "name": "Doom Cave",
  "blocks": [
    {"model": "HD2_VolPanVolStereo", "position": 0},
    {"model": "HD2_DistTriangleFuzzMono", "position": 1, "params": {"Sustain": 0.6, "Tone": 0.45, "Level": 0.7}},
    {"model": "HD2_AmpCaliRectifire", "position": 2, "params": {"Drive": 0.55, "Bass": 0.6, "Mid": 0.3, "Treble": 0.55, "Presence": 0.4, "Master": 0.5, "ChVol": 0.85}},
    {"model": "HD2_CabMicIr_4x12CaliV30", "position": 3, "params": {"LowCut": 85, "HighCut": 7000, "Level": 0}},
    {"model": "HD2_EQ_STATIC_ParametricStereo", "position": 4, "params": {"MidFreq": 500, "MidGain": -3, "Level": 0}},
    {"model": "HD2_ReverbGanymedeStereo", "position": 7, "params": {"Mix": 0.4, "Decay": 0.8, "Level": 0}}
  ],
  "input": {"noiseGate": true, "threshold": -58, "decay": 0.3},
  "output": {"gain": 6},
  "snapshots": [
    {"name": "Rhythm", "bypass": {"block1": false}, "params": {"block2": {"Drive": 0.55}, "block7": {"Mix": 0.2}}},
    {"name": "Lead",   "bypass": {"block1": true},  "params": {"block2": {"Drive": 0.7},  "block7": {"Mix": 0.5}}}
  ]
}
```

Then: `tonemaker build doom.json --out doom.pgp && tonemaker validate doom.pgp`, and import
`doom.pgp` into POD Go Edit.

## CLI vocabulary
"""

_CLI = """\
- `tonemaker inspect <file>` — print the chain + params (add `--json` for structured output)
- `tonemaker set <file> block2.Drive=0.62 output.gain=8 [--out <file>]` — edit params (validates first)
- `tonemaker add <file> block1=HD2_DistScream808Mono [--out <file>]` — add/replace a block
- `tonemaker build <spec.json> [--out <file>]` — build a full preset from a tone spec (validates first)
- `tonemaker new [--template metal-4snapshot] [--out <file>]` — start from blank/template
- `tonemaker validate <file>` — confirm it will import (run this before importing)
- `tonemaker models [--category amp]` — list available model ids
"""


def _library_markdown(models):
    lines = []
    for cat, entries in models.items():
        if cat.startswith("_") or not isinstance(entries, dict):
            continue
        model_ids = [m for m in entries if isinstance(m, str) and m.startswith("HD2_")]
        if not model_ids:
            continue
        lines.append(f"\n### {cat}\n")
        for mid in model_ids:
            info = entries[mid]
            name = info.get("name", "")
            params = ", ".join(info.get("params", []))
            extra = info.get("extra_fields", [])
            bits = [f"- **`{mid}`** — {name}", f"  - params: {params}" if params else ""]
            if extra:
                bits.append(f"  - required fields: {', '.join(extra)}")
            if info.get("units"):
                bits.append(f"  - units: {json.dumps(info['units'])}")
            if info.get("bool_params"):
                bits.append(f"  - boolean params: {', '.join(info['bool_params'])}")
            lines.extend(b for b in bits if b)
    return "\n".join(lines)


def generate(models=None):
    """Return the full knowledge pack as Markdown, generated from the model library."""
    models = models or load_models()
    schema = data_path("knowledge", "schema.json").read_text(encoding="utf-8")
    return (
        _PREAMBLE
        + _library_markdown(models)
        + "\n\n## Tone spec schema\n\n```json\n" + schema.rstrip() + "\n```\n\n"
        + _EXAMPLE
        + _CLI
    )


def model_ids_in_pack(text):
    """Extract the HD2_ ids referenced in a generated pack (for the drift test)."""
    import re
    return set(re.findall(r"HD2_[A-Za-z0-9_]+", text))
