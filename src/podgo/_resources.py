"""Access bundled package data (models library, templates, knowledge pack).

Uses importlib.resources so paths resolve identically from a source checkout and
an installed wheel/zip. Python 3.9+ (importlib.resources.files).
"""
import json
from importlib.resources import files

_DATA = files("podgo.data")


def data_path(*parts):
    """Return a traversable path object under podgo/data (e.g. data_path('models.json'))."""
    p = _DATA
    for part in parts:
        p = p / part
    return p


def load_models():
    """Return the verified model library (models.json) as a dict."""
    return json.loads(data_path("models.json").read_text(encoding="utf-8"))


def read_text(*parts):
    return data_path(*parts).read_text(encoding="utf-8")
