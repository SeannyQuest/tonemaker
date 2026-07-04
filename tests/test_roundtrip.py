"""Principle I — load -> save -> reload is lossless across all reference exports."""
import glob
import os

import pytest

from podgo import engine

REF = glob.glob(os.path.join(os.path.dirname(__file__), "..", "reference", "*.pgp"))
REF += glob.glob(os.path.join(os.path.dirname(__file__), "..", "examples", "*.pgp"))


@pytest.mark.parametrize("path", REF, ids=[os.path.basename(p) for p in REF])
def test_roundtrip_chain_identical(path, tmp_path):
    d, fmt = engine.load(path)
    before = engine.chain(d, fmt)
    out = tmp_path / "rt.pgp"
    engine.save(d, fmt, str(out))
    d2, fmt2 = engine.load(str(out))
    after = engine.chain(d2, fmt2)
    assert before == after
    assert engine.name(d, fmt) == engine.name(d2, fmt2)


def test_reference_files_exist():
    assert REF, "no reference/example .pgp files found"
