#!/usr/bin/env python3
"""Build a complete POD Go preset from a declarative tone spec.

The spec (see contracts/tone-spec.schema.json) lists blocks + params + snapshots;
this fills each block from a verified template in blocks.json, wires snapshot-
controlled params via controller 11, keeps dsp0 @enabled consistent with the active
snapshot, and validates before returning. Reuses the proven structure from the
original artist-preset builder, generalized over any library model.
"""
import copy
import json

from . import engine, validate
from ._resources import data_path


def _blocks():
    return json.loads(data_path("blocks.json").read_text(encoding="utf-8"))


def _control_range(values):
    lo, hi = min(values), max(values)
    return min(0.0, lo), max(1.0, hi)


def build_from_spec(spec, blocks=None):
    """Turn a tone spec (dict) into a preset doc. Raises ValueError on unknown/untemplated models."""
    blocks = blocks or _blocks()
    if "_shell" not in blocks:
        raise ValueError("blocks.json has no _shell template — run `tonemaker harvest` on a real export")

    doc = copy.deepcopy(blocks["_shell"])
    doc["data"]["meta"]["name"] = spec["name"]

    dsp0 = {"input": copy.deepcopy(blocks.get("_input", {})),
            "output": copy.deepcopy(blocks.get("_output", {}))}
    for k, v in (spec.get("input") or {}).items():
        dsp0["input"][k] = v
    for k, v in (spec.get("output") or {}).items():
        dsp0["output"][k] = v

    for blk in spec["blocks"]:
        pos, model = blk["position"], blk["model"]
        if model not in blocks:
            raise ValueError(f"model {model!r} has no template in blocks.json — "
                             "harvest it from a real POD Go export first")
        body = copy.deepcopy(blocks[model])
        body["@position"] = pos
        body["@enabled"] = bool(blk.get("enabled", True))
        for pk, pv in (blk.get("params") or {}).items():
            body[pk] = pv
        dsp0[f"block{pos}"] = body

    for i in range(10):  # POD Go presets carry exactly block0..block9; empty = {"@position": N}
        dsp0.setdefault(f"block{i}", {"@position": i})

    tone = {"dsp0": dsp0,
            "global": {"@model": "@global_params", "@cursor_group": "block0",
                       "@pedalstate": 2, "@current_snapshot": 0, "@tempo": 120},
            "footswitch": {"dsp0": {}}}

    snaps = spec.get("snapshots") or []
    controlled = {}  # (blockKey, param) -> list of values across snapshots
    for s in snaps:
        for bk, params in (s.get("params") or {}).items():
            for pk, pv in params.items():
                controlled.setdefault((bk, pk), []).append(pv)

    # base value of each controlled param = its value in the active snapshot (snapshot0)
    if snaps:
        for bk, params in (snaps[0].get("params") or {}).items():
            if bk in dsp0 and isinstance(dsp0[bk], dict):
                for pk, pv in params.items():
                    dsp0[bk][pk] = pv
        for bk, bv in (snaps[0].get("bypass") or {}).items():
            if bk in dsp0 and isinstance(dsp0[bk], dict) and "@model" in dsp0[bk]:
                dsp0[bk]["@enabled"] = bool(bv)

    controller = {"dsp0": {}}
    for (bk, pk), values in controlled.items():
        base = dsp0.get(bk, {}).get(pk)
        nums = [v for v in values + [base] if isinstance(v, (int, float))]
        lo, hi = _control_range(nums or [0.0, 1.0])
        controller["dsp0"].setdefault(bk, {})[pk] = {"@min": lo, "@max": hi, "@controller": 11}
    tone["controller"] = controller

    def block_bypass_map(bypass_overrides):
        m = {}
        for key, v in dsp0.items():
            if key.startswith("block") and isinstance(v, dict):
                m[key] = bool(v.get("@enabled", False)) if "@model" in v else False
        for bk, bv in (bypass_overrides or {}).items():
            m[bk] = bool(bv)
        return m

    for i in range(4):
        sn = f"snapshot{i}"
        if i < len(snaps):
            s = snaps[i]
            ctrls = {"dsp0": {}}
            for bk, params in (s.get("params") or {}).items():
                for pk, pv in params.items():
                    ctrls["dsp0"].setdefault(bk, {})[pk] = {"@fs_enabled": False, "@value": pv}
            tone[sn] = {"@name": s.get("name", f"Snapshot {i + 1}"), "@tempo": 120,
                        "@valid": True, "blocks": {"dsp0": block_bypass_map(s.get("bypass"))},
                        "controllers": ctrls}
        else:
            # unused snapshot: mirror the active one so all four are valid on the device
            tone[sn] = {"@name": f"Snapshot {i + 1}", "@tempo": 120, "@valid": True,
                        "blocks": {"dsp0": block_bypass_map(snaps[0].get("bypass") if snaps else None)},
                        "controllers": copy.deepcopy(tone["snapshot0"]["controllers"]) if snaps else {"dsp0": {}}}

    doc["data"]["tone"] = tone
    return doc


def build(spec, out_path):
    """Build from spec, validate, and write to out_path. Raises on validation errors."""
    doc = build_from_spec(spec)
    errors, warnings = validate.validate_doc(doc, "raw")
    if errors:
        raise ValueError("built preset failed validation:\n" + validate.format_report(errors, warnings))
    engine.save(doc, "raw", out_path)
    return doc, warnings


def new(template=None):
    """Return a starter preset doc — from a bundled template, or a blank single-amp chain."""
    if template:
        spec = json.loads(data_path("templates", f"{template}.json").read_text(encoding="utf-8"))
        return build_from_spec(spec)
    blocks = _blocks()
    amp = next((m for m in blocks if m.startswith(("HD2_Amp", "HD2_Preamp"))), None)
    cab = next((m for m in blocks if m.startswith("HD2_Cab")), None)
    chain = []
    if amp:
        chain.append({"model": amp, "position": 0})
    if cab:
        chain.append({"model": cab, "position": 1})
    if not chain:
        chain = [{"model": next(m for m in blocks if m.startswith("HD2_")), "position": 0}]
    return build_from_spec({"name": "New Tone", "blocks": chain})
