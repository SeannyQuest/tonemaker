"""User Story 3 — build from a tone spec; result matches the spec and validates."""
from tonemaker import build, engine, validate


SPEC = {
    "name": "Test Build",
    "blocks": [
        {"model": "HD2_VolPanVolStereo", "position": 0},
        {"model": "HD2_AmpCaliRectifire", "position": 2, "params": {"Drive": 0.62, "Bass": 0.5}},
        {"model": "HD2_CabMicIr_4x12CaliV30", "position": 3, "params": {"Level": 0}},
    ],
    "output": {"gain": 8},
    "snapshots": [
        {"name": "Rhythm", "params": {"block2": {"Drive": 0.6}}},
        {"name": "Lead", "params": {"block2": {"Drive": 0.8}}},
    ],
}


def test_build_matches_spec_and_validates(tmp_path):
    out = tmp_path / "test.pgp"
    doc, warnings = build.build(SPEC, str(out))
    d, fmt = engine.load(str(out))

    assert engine.name(d, fmt) == "Test Build"
    dsp0 = engine.dsp0(d, fmt)
    assert dsp0["block2"]["@model"] == "HD2_AmpCaliRectifire"
    # active snapshot (0) base value applied
    assert dsp0["block2"]["Drive"] == 0.6
    assert dsp0["output"]["gain"] == 8

    # snapshots present and named
    tone = engine.tone(d, fmt)
    assert tone["snapshot0"]["@name"] == "Rhythm"
    assert tone["snapshot1"]["@name"] == "Lead"
    # controller-11 wiring for the snapshot-controlled param
    assert tone["controller"]["dsp0"]["block2"]["Drive"]["@controller"] == 11

    errors, _ = validate.validate_doc(d, fmt)
    assert errors == []


def test_build_rejects_unknown_model(tmp_path):
    bad = {"name": "Bad", "blocks": [{"model": "HD2_DoesNotExistMono", "position": 0}]}
    out = tmp_path / "bad.pgp"
    try:
        build.build(bad, str(out))
    except ValueError:
        return
    assert False, "expected build to reject an unknown/untemplated model"
