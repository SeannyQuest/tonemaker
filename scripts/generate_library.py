#!/usr/bin/env python3
"""Generate models.json + blocks.json from POD Go Edit's authoritative model data.

Maintainer tool (not shipped, not run at install time). It reads the .models files
inside an installed POD Go Edit.app and DERIVES our library from them — factual model
data (ids, param names, defaults, ranges, required @-fields) for interoperability. It
does NOT copy Line 6's files verbatim; only the derived facts land in the package.
Constitution Principle V permits "authoritative POD Go application data" as a source.

Usage:
  python3 scripts/generate_library.py ["/Applications/Line6/POD Go Edit.app"]

Real device exports remain the ground truth for the models we already verified: where
a model already has a body in blocks.json (harvested from a real export), that body is
kept; app-derived bodies fill in the rest.
"""
import copy
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "src", "tonemaker", "data")
DEFAULT_APP = "/Applications/Line6/POD Go Edit.app"

# .models filename -> (our category, export @type integer). Cross-checked against the
# 21 models verified from real device exports.
CATEGORY_MAP = {
    "amp.models":         ("amp", 1),
    "preamp.models":      ("amp", 1),
    "cab.models":         ("cab", 2),
    "cabmicirs.models":   ("cab", 0),
    "distortion.models":  ("distortion", 0),
    "modulation.models":  ("modulation", 0),
    "delay.models":       ("delay", 5),
    "reverb.models":      ("reverb", 5),
    "eq.models":          ("eq", 0),
    "pitch-synth.models": ("pitch", 0),
    "compressor.models":  ("dynamics", 0),
    "gate.models":        ("dynamics", 0),
    "filter.models":      ("filter", 0),
    "wah.models":         ("utility", 0),
    "volumepan.models":   ("utility", 0),
    "sendreturn.models":  ("utility", 5),
}

# @-fields that appear as real top-level fields in export blocks (keep with defaults);
# @enabled/@position are set by the builder, not stored as template fields.
KEEP_AT_FIELDS = {"@bypassvolume", "@mic", "@trails", "@no_snapshot_bypass"}


def load_models_file(app, fname):
    path = os.path.join(app, "Contents", "Resources", fname)
    if not os.path.exists(path):
        return []
    return json.load(open(path))


def main(app):
    if not os.path.isdir(app):
        sys.exit(f"POD Go Edit.app not found at {app!r} — install it or pass the path")

    models = {"_note": ("VERIFIED POD Go model library, DERIVED from authoritative POD Go "
                        "Edit application data (per-category .models files) plus real device "
                        "exports. Facts only (ids/params/defaults/ranges), not Line 6 files "
                        "verbatim. Param values: valueType 1 = normalized 0-1; freq/cut in Hz; "
                        "gain/level in dB. Regenerate with scripts/generate_library.py.")}
    blocks = {}
    if os.path.exists(os.path.join(DATA, "blocks.json")):
        blocks = json.load(open(os.path.join(DATA, "blocks.json")))  # keep _shell/_input/_output + real bodies

    n_models = n_blocks = 0
    for fname, (cat, atype) in CATEGORY_MAP.items():
        for m in load_models_file(app, fname):
            mid = m.get("symbolicID", "")
            if not mid.startswith("HD2_"):
                continue
            params = [p["symbolicID"] for p in m.get("params", [])
                      if not str(p.get("symbolicID", "")).startswith("@")]
            extra = [p["symbolicID"] for p in m.get("params", [])
                     if p.get("symbolicID") in KEEP_AT_FIELDS]

            entry = {"name": m.get("name", "") or mid, "type": atype, "params": params}
            if extra:
                entry["extra_fields"] = extra
            # ranges for the knowledge pack (compact: only non-default 0..1)
            ranges = {p["symbolicID"]: [p["min"], p["max"]]
                      for p in m.get("params", [])
                      if not str(p.get("symbolicID", "")).startswith("@")
                      and (p.get("min"), p.get("max")) not in ((0.0, 1.0), (0, 1))
                      and "min" in p and "max" in p}
            if ranges:
                entry["ranges"] = ranges
            models.setdefault(cat, {})[mid] = entry
            n_models += 1

            # block template body (skip if we already have a real-export body)
            if mid not in blocks:
                body = {"@model": mid, "@type": atype}
                for p in m.get("params", []):
                    sid = p.get("symbolicID", "")
                    if sid in ("@enabled", "@position") or "default" not in p:
                        continue
                    if sid.startswith("@") and sid not in KEEP_AT_FIELDS:
                        continue
                    body[sid] = p["default"]
                blocks[mid] = body
                n_blocks += 1

    json.dump(models, open(os.path.join(DATA, "models.json"), "w"), indent=2)
    json.dump(blocks, open(os.path.join(DATA, "blocks.json"), "w"), indent=2)
    total = sum(len(e) for c, e in models.items() if not c.startswith("_") and isinstance(e, dict))
    print(f"Wrote models.json ({total} models) and blocks.json "
          f"({sum(1 for k in blocks if k.startswith('HD2_'))} bodies). "
          f"Added {n_blocks} new app-derived bodies this run.")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else DEFAULT_APP)
