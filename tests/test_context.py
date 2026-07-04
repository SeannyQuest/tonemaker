"""Principle IV — the generated knowledge pack never names a model outside the library."""
from podgo import context
from podgo._resources import load_models


def _library_ids():
    ids = set()
    for cat, entries in load_models().items():
        if cat.startswith("_") or not isinstance(entries, dict):
            continue
        ids.update(m for m in entries if isinstance(m, str) and m.startswith("HD2_"))
    return ids


def test_pack_only_references_library_models():
    pack = context.generate()
    referenced = context.model_ids_in_pack(pack)
    library = _library_ids()
    stray = referenced - library
    assert not stray, f"knowledge pack references models not in the library: {sorted(stray)}"


def test_pack_has_core_sections():
    pack = context.generate()
    for marker in ("Model library", "Tone spec schema", "Worked example", "CLI vocabulary"):
        assert marker in pack, f"knowledge pack missing section: {marker}"


def test_pack_lists_every_library_model():
    pack = context.generate()
    referenced = context.model_ids_in_pack(pack)
    for mid in _library_ids():
        assert mid in referenced, f"library model missing from pack: {mid}"
