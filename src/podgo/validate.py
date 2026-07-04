"""Pre-import validation — the Principle III safety net.

POD Go rejects an entire preset if any one block's @model is unrecognized, so we
catch the known failure modes *before* the user tries to import:

  ERROR  - unknown @model (not in the verified library)
  ERROR  - missing a model's required @-field (@bypassvolume / @mic / @trails)
  ERROR  - @position not contiguous from 0, or block-key index != @position
  WARN   - a parameter key not among the model's known params (tolerates firmware additions)
  WARN   - a block enabled in dsp0 but bypassed in the active snapshot (the "silently off" trap)

`errors` non-empty => the preset should not be imported/written as final.
"""
from . import engine
from ._resources import load_models


def build_index(models=None):
    """Map @model id -> library entry, for every HD2_ model in models.json."""
    models = models or load_models()
    idx = {}
    for cat, entries in models.items():
        if cat.startswith("_") or not isinstance(entries, dict):
            continue
        for mid, info in entries.items():
            if isinstance(mid, str) and mid.startswith("HD2_") and isinstance(info, dict):
                idx[mid] = info
    return idx


def validate_doc(d, fmt, models=None):
    """Validate an already-loaded preset. Returns (errors, warnings) lists of strings."""
    idx = build_index(models)
    g = engine.dsp0(d, fmt)
    tone = engine.tone(d, fmt)
    errors, warnings = [], []

    blocks = {k: v for k, v in g.items()
              if isinstance(k, str) and k.startswith("block") and isinstance(v, dict)}

    for k, v in sorted(blocks.items()):
        try:
            key_index = int(k[5:])
        except ValueError:
            errors.append(f"{k}: malformed block key")
            continue
        pos = v.get("@position")
        if pos != key_index:
            errors.append(f"{k}: @position {pos} != block-key index {key_index}")

        model = v.get("@model")
        if model is None:
            continue  # empty slot {"@position": N} is legal
        info = idx.get(model)
        if info is None:
            errors.append(f"{k}: unknown @model {model!r} (not in verified library) "
                          "— POD Go will reject the whole preset")
            continue
        for ef in info.get("extra_fields", []):
            if ef not in v:
                errors.append(f"{k}: model {model} is missing required field {ef}")
        known = set(info.get("params", []))
        if known:
            for pk in v:
                if not pk.startswith("@") and pk not in known:
                    warnings.append(f"{k}: param {pk!r} not among known params for {model}")

    present = sorted(int(k[5:]) for k in blocks if k[5:].isdigit())
    if present and present != list(range(len(present))):
        errors.append(f"block positions not contiguous from 0: {present}")

    cur = tone.get("global", {}).get("@current_snapshot", 0)
    snap = tone.get(f"snapshot{cur}")
    if isinstance(snap, dict):
        snap_bypass = snap.get("blocks", {}).get("dsp0", {})
        for k, v in blocks.items():
            if v.get("@model") is None:
                continue
            en, sb = v.get("@enabled"), snap_bypass.get(k)
            if en is True and sb is False:
                warnings.append(f"{k}: enabled in dsp0 but OFF in active snapshot{cur} "
                                "— it will sound bypassed on the device")
    return errors, warnings


def validate(path, models=None):
    """Load a .pgp (raises on hxmp DRM) and validate it. Returns (errors, warnings)."""
    d, fmt = engine.load(path)
    return validate_doc(d, fmt, models)


def is_valid(path, models=None):
    errors, _ = validate(path, models)
    return not errors


def format_report(errors, warnings):
    lines = []
    for e in errors:
        lines.append(f"  ERROR  {e}")
    for w in warnings:
        lines.append(f"  WARN   {w}")
    if not lines:
        return "  OK — no issues"
    return "\n".join(lines)
