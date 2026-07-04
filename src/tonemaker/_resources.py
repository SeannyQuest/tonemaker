"""Access bundled package data (models library, templates, knowledge pack).

Uses importlib.resources so paths resolve identically from a source checkout and
an installed wheel/zip. Python 3.9+ (importlib.resources.files).
"""
import json
from importlib.resources import files

# Anchor on the tonemaker package (which has __init__.py) and descend into data/.
# Using files("tonemaker.data") directly fails on Python 3.9 when data/ is a
# namespace package (spec.origin is None); this form resolves the same everywhere.
_DATA = files("tonemaker") / "data"


def data_path(*parts):
    """Return a traversable path object under tonemaker/data (e.g. data_path('models.json'))."""
    p = _DATA
    for part in parts:
        p = p / part
    return p


def load_models():
    """Return the verified model library (models.json) as a dict."""
    return json.loads(data_path("models.json").read_text(encoding="utf-8"))


def read_text(*parts):
    return data_path(*parts).read_text(encoding="utf-8")
