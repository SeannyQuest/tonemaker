#!/usr/bin/env python3
"""Harvest verified POD Go models from real .pgp exports into the packaged library.

Point it at exported presets (factory setlist, your own, editable packs) and it adds
every unique model it finds to two bundled files, skipping DRM and P34_ I/O blocks:

  - models.json : @model id -> {name, type, params}   (the verified catalog)
  - blocks.json : @model id -> full default block body (used by `build` as a template)
                  plus `_input` / `_output` skeletons from the first export seen.

Only real exports feed the library (Principle V: no guessed ids).
"""
import base64
import glob
import json
import os
import zlib

from ._resources import data_path

MODELS_PATH = str(data_path("models.json"))
BLOCKS_PATH = str(data_path("blocks.json"))


def category(mid):
    if mid.startswith(("HD2_Amp", "HD2_Preamp")): return "amp"
    if mid.startswith("HD2_Cab"): return "cab"
    if mid.startswith("HD2_Dist"): return "distortion"
    if mid.startswith(("HD2_Chorus", "HD2_Flanger", "HD2_Phaser", "HD2_Tremolo",
                       "HD2_Rotary", "HD2_Vibrato")): return "modulation"
    if mid.startswith("HD2_Delay"): return "delay"
    if mid.startswith("HD2_Reverb"): return "reverb"
    if mid.startswith("HD2_EQ"): return "eq"
    if mid.startswith(("HD2_Pitch", "HD2_Synth", "HD2_Poly", "HD2_Harmony")): return "pitch"
    if mid.startswith(("HD2_Gate", "HD2_Comp", "HD2_Dynamics")): return "dynamics"
    if mid.startswith(("HD2_Wah", "HD2_VolPan", "HD2_Vol", "HD2_FXLoop")): return "utility"
    if mid.startswith("HD2_Filter"): return "filter"
    return "other"


def load_preset(path):
    """Return the inner preset dict, or None for DRM. Raises on unreadable files."""
    d = json.load(open(path))
    if "encoded_data" in d:
        enc = d.get("encryption")
        if isinstance(enc, dict) and enc.get("type") not in (None, "none"):
            return None  # DRM — never decode
        d = json.loads(zlib.decompress(base64.b64decode(d["encoded_data"])))
    return d


def _extra_fields(block):
    return [k for k in ("@bypassvolume", "@mic", "@trails", "@no_snapshot_bypass") if k in block]


def harvest(paths):
    """Scan paths (files or folders) and extend models.json + blocks.json. Returns (added, total)."""
    db = json.load(open(MODELS_PATH))
    blocks = json.load(open(BLOCKS_PATH)) if os.path.exists(BLOCKS_PATH) else {}
    known = {mid for cat, ents in db.items() if not cat.startswith("_")
             for mid in (ents if isinstance(ents, dict) else {})}

    files = []
    for p in paths:
        files += (glob.glob(os.path.join(p, "**", "*.pgp"), recursive=True)
                  if os.path.isdir(p) else [p])

    added = 0
    for f in sorted(set(files)):
        try:
            d = load_preset(f)
        except Exception as e:
            print(f"  skip {os.path.basename(f)} - {e}")
            continue
        if d is None:
            print(f"  skip (DRM) {os.path.basename(f)}")
            continue
        dsp0 = d.get("data", {}).get("tone", {}).get("dsp0", {})
        if "_input" not in blocks and isinstance(dsp0.get("input"), dict):
            blocks["_input"] = dsp0["input"]
        if "_output" not in blocks and isinstance(dsp0.get("output"), dict):
            blocks["_output"] = dsp0["output"]
        if "_shell" not in blocks and "data" in d and "tone" in d.get("data", {}):
            import copy as _copy
            shell = _copy.deepcopy(d)
            # keep only the container; build replaces tone wholesale
            shell["data"]["tone"] = {}
            blocks["_shell"] = shell
        for v in dsp0.values():
            if not isinstance(v, dict):
                continue
            mid = v.get("@model")
            if not mid or mid.startswith("P34_"):
                continue
            if mid not in blocks:
                body = {k: val for k, val in v.items() if k not in ("@position", "@enabled")}
                blocks[mid] = body
            if mid in known:
                continue
            params = sorted(pk for pk in v if not pk.startswith("@"))
            entry = {"name": "(auto-harvested)", "type": v.get("@type"), "params": params}
            ef = _extra_fields(v)
            if ef:
                entry["extra_fields"] = ef
            db.setdefault(category(mid), {})[mid] = entry
            known.add(mid)
            added += 1
            print(f"  + [{category(mid)}] {mid}")

    json.dump(db, open(MODELS_PATH, "w"), indent=2)
    json.dump(blocks, open(BLOCKS_PATH, "w"), indent=2)
    total = sum(len(e) for c, e in db.items() if not c.startswith("_") and isinstance(e, dict))
    print(f"\nAdded {added} new models. Library now has {total} total. "
          f"Scanned {len(set(files))} files.")
    return added, total


def default_paths():
    repo = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    return [os.path.join(repo, "reference"), os.path.expanduser("~/Downloads")]


if __name__ == "__main__":
    import sys
    harvest(sys.argv[1:] or default_paths())
