# POD Go Tone Builder — LLM Knowledge Pack

> Generated from the verified model library. Do not hand-edit. Paste this whole
> document into your LLM, then describe the guitar tone you want.

You are helping design a tone for the **Line 6 POD Go** by producing data the
`podgo` command-line tool can turn into an importable `.pgp` preset. Respond with
**either** of these, and nothing that can't be run:

1. **A tone spec** — a JSON object conforming to the schema below — which the user
   saves as `tone.json` and builds with: `podgo build tone.json --out tone.pgp`
2. **A sequence of `podgo set` / `podgo add` commands** against a named `.pgp` file.

Either way, finish by telling the user to run `podgo validate tone.pgp` — this
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

### amp

- **`HD2_AmpCaliRectifire`** — Cali Rectifire (Mesa Dual Rectifier)
  - params: Drive, Bass, Mid, Treble, Presence, Master, ChVol, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpUSDoubleNrm`** — US Double Nrm (Fender Twin)
  - params: Drive, Bass, Mid, Treble, Presence, Master, ChVol, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_PreampPVPanama`** — PV Panama PREAMP (Peavey 5150)
  - params: Drive, Bass, Mid, Treble, Master, ChVol, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampBrit2204`** — Brit 2204 PREAMP (Marshall JCM800)
  - params: Drive, Bass, Mid, Treble, Master, ChVol, Sag, Hum
  - required fields: @bypassvolume

### cab

- **`HD2_CabMicIr_4x12CaliV30`** — 4x12 Cali V30
  - params: Position, LowCut, Mic, Angle, Distance, HighCut, Level
  - units: {"LowCut": "Hz", "HighCut": "Hz", "Angle": "deg", "Distance": "in", "Position": "0-1", "Mic": "index"}
- **`HD2_CabMicIr_4x12BritV30`** — 4x12 Brit V30 (Marshall 1960)
  - params: Position, LowCut, Mic, Angle, Distance, HighCut, Level
  - units: {"LowCut": "Hz", "HighCut": "Hz", "Angle": "deg", "Distance": "in", "Position": "0-1", "Mic": "index"}
- **`HD2_Cab2x12DoubleC12N`** — 2x12 Double C12N (Fender Twin Jensen)
  - params: Level, LowCut, Distance, EarlyReflections, HighCut
  - required fields: @mic

### eq

- **`HD2_EQ_STATIC_ParametricStereo`** — Parametric EQ
  - params: LowCut, HighCut, LowFreq, LowGain, LowQ, MidFreq, MidGain, MidQ, HighFreq, HighGain, HighQ, Level
  - units: {"*Freq": "Hz", "*Cut": "Hz", "*Gain": "dB", "*Q": "~0.707", "Level": "dB"}
- **`HD2_EQ_STATIC_SimpleTiltStereo`** — Simple Tilt EQ
  - params: Tilt, CenterFreq, Level

### distortion

- **`HD2_DistTriangleFuzzMono`** — Triangle Fuzz (Big Muff)
  - params: Sustain, Tone, Level
- **`HD2_DistScream808Mono`** — Scream 808 (Ibanez TS808)
  - params: Gain, Tone, Level
- **`HD2_DistMinotaurMono`** — Minotaur (Klon Centaur)
  - params: Gain, Tone, Level

### modulation

- **`HD2_Chorus70sChorusStereo`** — 70s Chorus (CE-1)
  - params: Mix, ChorusIntensity, VibratoDepth, VibratoRate, Spread, Stereo, Mode, Level, Headroom, SyncSelect1, SyncSelect2, TempoSync1, TempoSync2
  - boolean params: Stereo, Mode, TempoSync1, TempoSync2

### delay

- **`HD2_DelayTransistorTapeStereo`** — Transistor Tape (Maestro EP)
  - params: Time, Feedback, Mix, WowFlutter, Spread, Scale, Level, SyncSelect1, TempoSync1, Headroom
  - required fields: @trails
  - units: {"Time": "0-1", "Feedback": "0-1", "Mix": "0-1", "Level": "dB"}

### reverb

- **`HD2_ReverbGanymedeStereo`** — Ganymede (shimmer)
  - params: Mix, Modulation, Tone, Decay, Predelay, Level
  - required fields: @trails
- **`HD2_ReverbSearchlightsStereo`** — Searchlights (modulated ambient)
  - params: Mix, Intensity, Speed, Modulation, Spread, Decay, Predelay, LowCut, HighCut, Level
  - required fields: @trails
  - units: {"LowCut": "Hz", "HighCut": "Hz"}

### utility

- **`HD2_VolPanVolStereo`** — Volume Pedal
  - params: Pedal, VolumeTaper
- **`HD2_WahThroatyStereo`** — Wah (Throaty)
  - params: FcHigh, FcLow, Pedal, Level, Mix
- **`HD2_WahFasselStereo`** — Wah (Fassel)
  - params: FcHigh, FcLow, Pedal, Level, Mix
- **`HD2_FXLoopStereo1_2`** — Stereo FX Loop
  - params: Return, Send, Mix
  - required fields: @trails
- **`HD2_FXLoopMono1`** — Mono FX Loop
  - params: Return, Send, Mix

## Tone spec schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://github.com/SeannyQuest/podgo-tones/tone-spec.schema.json",
  "title": "POD Go Tone Spec",
  "description": "Declarative description of a POD Go preset that `podgo build` turns into an importable .pgp. Emitted by an LLM from the knowledge pack.",
  "type": "object",
  "required": ["name", "blocks"],
  "additionalProperties": false,
  "properties": {
    "name": {
      "type": "string",
      "description": "Preset display name.",
      "minLength": 1,
      "maxLength": 32
    },
    "blocks": {
      "type": "array",
      "description": "Signal chain. Up to 10 blocks; positions must be contiguous from 0.",
      "minItems": 1,
      "maxItems": 10,
      "items": {
        "type": "object",
        "required": ["model", "position"],
        "additionalProperties": false,
        "properties": {
          "model": {
            "type": "string",
            "description": "Exact POD Go @model id from the library (e.g. HD2_AmpCaliRectifire). Validated against models.json.",
            "pattern": "^HD2_[A-Za-z0-9_]+$"
          },
          "position": {
            "type": "integer",
            "description": "Chain order 0..9; block-key index equals position.",
            "minimum": 0,
            "maximum": 9
          },
          "enabled": {
            "type": "boolean",
            "description": "On/off in dsp0. Default true.",
            "default": true
          },
          "params": {
            "type": "object",
            "description": "Parameter values for this model. Keys must be among the model's known params; amp/drive/mix knobs are 0.0-1.0, freq/cut in Hz, gain/level in dB.",
            "additionalProperties": {
              "type": ["number", "boolean", "integer"]
            }
          }
        }
      }
    },
    "input": {
      "type": "object",
      "description": "Noise gate overrides (dsp0.input).",
      "additionalProperties": false,
      "properties": {
        "noiseGate": { "type": "boolean" },
        "threshold": { "type": "number", "description": "dB, e.g. -56" },
        "decay": { "type": "number", "minimum": 0, "maximum": 1 }
      }
    },
    "output": {
      "type": "object",
      "description": "Master output overrides (dsp0.output).",
      "additionalProperties": false,
      "properties": {
        "pan": { "type": "number", "minimum": 0, "maximum": 1, "description": "0.5 = center" },
        "gain": { "type": "number", "description": "dB" }
      }
    },
    "snapshots": {
      "type": "array",
      "description": "Up to 4 snapshots. Each overrides per-block bypass and snapshot-controlled params (wired via controller 11).",
      "maxItems": 4,
      "items": {
        "type": "object",
        "required": ["name"],
        "additionalProperties": false,
        "properties": {
          "name": { "type": "string", "maxLength": 16 },
          "bypass": {
            "type": "object",
            "description": "blockKey -> on/off for this snapshot.",
            "patternProperties": {
              "^block[0-9]$": { "type": "boolean" }
            },
            "additionalProperties": false
          },
          "params": {
            "type": "object",
            "description": "blockKey -> {param: value} held for this snapshot.",
            "patternProperties": {
              "^block[0-9]$": {
                "type": "object",
                "additionalProperties": { "type": ["number", "boolean", "integer"] }
              }
            },
            "additionalProperties": false
          }
        }
      }
    }
  }
}
```

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

Then: `podgo build doom.json --out doom.pgp && podgo validate doom.pgp`, and import
`doom.pgp` into POD Go Edit.

## CLI vocabulary
- `podgo inspect <file>` — print the chain + params (add `--json` for structured output)
- `podgo set <file> block2.Drive=0.62 output.gain=8 [--out <file>]` — edit params (validates first)
- `podgo add <file> block1=HD2_DistScream808Mono [--out <file>]` — add/replace a block
- `podgo build <spec.json> [--out <file>]` — build a full preset from a tone spec (validates first)
- `podgo new [--template metal-4snapshot] [--out <file>]` — start from blank/template
- `podgo validate <file>` — confirm it will import (run this before importing)
- `podgo models [--category amp]` — list available model ids
