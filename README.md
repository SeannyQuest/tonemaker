# POD Go Tones

Edit Line 6 **POD Go** guitar tones as data — and design them by describing what you want to
**any LLM you already use** (Claude, ChatGPT, a local model). POD Go Edit has no scripting
interface, but its preset files (`.pgp`) are editable JSON, so this tool reads, edits, builds, and
**validates** presets from the command line, and ships a knowledge pack you hand to your LLM.

> Unofficial — not affiliated with or endorsed by Line 6 / Yamaha Guitar Group. POD Go and Helix are
> trademarks of their respective owners. Works only on your own unencrypted exports; DRM (`hxmp`)
> commercial packs are detected and refused.

## Install

```bash
pip install podgo-tones
```

## The LLM workflow (the point)

```bash
podgo context | pbcopy          # copy the knowledge pack (macOS; use xclip/clip elsewhere)
```

1. Paste it into your LLM and describe a tone ("doomy, downtuned, big cave reverb").
2. The LLM replies with a tone spec (JSON) or a set of `podgo` commands.
3. Build and check it, then import the `.pgp` into POD Go Edit:

```bash
podgo build doom.json --out doom.pgp    # build from the spec the LLM gave you
podgo validate doom.pgp                 # confirms it will import (no unrecognized models)
```

`validate` is the safety net: if the LLM invents a model id that POD Go wouldn't recognize, you find
out here — not when the device rejects the whole preset.

## Commands

```bash
podgo inspect tone.pgp                              # show the full chain + params
podgo set tone.pgp block2.Drive=0.62 output.gain=8  # edit params (validates before writing)
podgo add tone.pgp block1=HD2_DistScream808Mono     # add/replace a block
podgo build spec.json --out tone.pgp                # build a full preset from a tone spec
podgo new --template metal-4snapshot --out t.pgp    # start from a template
podgo validate tone.pgp                             # check it will import
podgo models --category amp                         # list verified model ids
podgo harvest ~/Downloads/MyExport.pgp              # extend the library from your own export
podgo context                                       # emit the LLM knowledge pack
```

Import a `.pgp` into POD Go Edit by dragging it onto a slot (or right-click → Import).

## How it works

A preset is a signal chain of 10 blocks (`block0`..`block9`) plus an input gate and a master output,
ordered by each block's position. Six blocks are dedicated (Volume, Wah, Amp, Cab, EQ, FX Loop); up
to four are user effects. Snapshots (up to 4) override which blocks are on and the values of chosen
parameters. Model ids are exact and POD Go-specific (they carry `Mono`/`Stereo` suffixes) — a single
wrong id makes POD Go reject the whole preset, which is why the shipped library is verified from real
exports and every write is validated first.

## Extending the model library

The library is built only from real POD Go exports (never guessed). To add a model the tool doesn't
know yet: add the block in POD Go Edit, export the preset, then:

```bash
podgo harvest that-export.pgp     # adds the model's exact id + params (+ a build template)
```

Contributions that widen coverage are welcome via PR.

## Development

```bash
pip install -e ".[dev]"
pytest                 # lossless round-trip, validation, build, knowledge-pack drift
```

Built with spec-driven development (GitHub Spec Kit) — see `.specify/memory/constitution.md` and
`specs/001-podgo-tone-builder/`.
