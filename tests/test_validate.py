"""Principle III — validation catches the failure modes that make POD Go reject a preset."""
import copy
import os

from tonemaker import engine, validate

REF = os.path.join(os.path.dirname(__file__), "..", "reference", "logic.pgp")


def test_clean_reference_passes():
    errors, _ = validate.validate(REF)
    assert errors == []


def test_unknown_model_fails_naming_block():
    d, fmt = engine.load(REF)
    d = copy.deepcopy(d)
    # break one block's model id
    dsp0 = engine.dsp0(d, fmt)
    block_key = next(k for k, v in dsp0.items()
                     if isinstance(v, dict) and v.get("@model", "").startswith("HD2_"))
    dsp0[block_key]["@model"] = "HD2_TotallyMadeUpMono"
    errors, _ = validate.validate_doc(d, fmt)
    assert any("unknown @model" in e and block_key in e for e in errors)


def test_position_mismatch_fails():
    d, fmt = engine.load(REF)
    d = copy.deepcopy(d)
    dsp0 = engine.dsp0(d, fmt)
    block_key = next(k for k, v in dsp0.items()
                     if isinstance(v, dict) and "@position" in v)
    dsp0[block_key]["@position"] = 99
    errors, _ = validate.validate_doc(d, fmt)
    assert any("position" in e.lower() for e in errors)
