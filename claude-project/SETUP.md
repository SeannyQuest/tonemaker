# Set up the "POD Go Tone Designer" Claude Project

This turns tonemaker into something anyone can use with **no terminal, no install** — just chat.
A guitarist describes a tone, Claude hands back a `.pgp` file they drag into POD Go Edit.

## One-time setup (about 3 minutes)

1. Go to **claude.ai → Projects → Create project**. Name it something like
   **"POD Go Tone Designer"**.
2. Open the project's **Custom instructions** and paste in the entire contents of
   [`project-instructions.md`](./project-instructions.md).
3. Add these files to the project's **knowledge** (drag them into the project files area):
   - `knowledge/blocks.json`  ← the exact building blocks (source of truth)
   - `knowledge/models.json`  ← all models, by name
   - `knowledge/example-simple.json`  ← a complete single-sound preset (structural template)
   - `knowledge/example-4snapshot.json`  ← a complete 4-snapshot preset (advanced template)
   - `knowledge/tone-guide.md`  ← genre-by-genre starting points
4. That's it. Start a chat in the project and try: *"Give me a warm blues lead with a bit of
   delay,"* or *"an ambient clean with shimmer for headphones."*

## How someone uses it (end-user flow)

1. Open the project, describe the tone they want.
2. Claude replies with a preset as a code block.
3. Copy it, paste into a plain-text editor, save as `MyTone.pgp`.
4. In POD Go Edit: right-click a slot → Import (or drag the file on). Done.

## How reliable is this?

The Project builds the preset by copying real, correct block bodies out of `blocks.json` (the same
data the tonemaker tool uses) and mimicking a known-good example file, so it's quite reliable. But
an LLM is doing the final assembly, so it isn't 100% guaranteed the way the command-line builder is.

If you want to spot-check outputs while dialing in the project: save any preset Claude gives you and
run it through the real validator —

```bash
tonemaker validate MyTone.pgp
```

Anything wrong will be named. The eventual browser version will do this build+validate step
deterministically for a 100%-reliable, no-terminal experience; this Claude Project is the fast first
step to get it into people's hands.

## Keeping it in sync

If the model library is regenerated (`scripts/generate_library.py`), re-copy `models.json` and
`blocks.json` from `src/tonemaker/data/` into `claude-project/knowledge/` and re-upload them so the
project always matches the tool. (Run `python scripts/refresh_claude_project.py` if present.)
