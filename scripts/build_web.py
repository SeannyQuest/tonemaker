#!/usr/bin/env python3
"""Build the self-contained web app: inline core.js + models.json + blocks.json into
web/template.html and write docs/index.html (served by GitHub Pages).

Run after regenerating the library so the site stays in sync with the tool.

  python3 scripts/build_web.py
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, "src", "tonemaker", "data")


def read(*parts):
    return open(os.path.join(*parts), encoding="utf-8").read()


def main():
    template = read(ROOT, "web", "template.html")
    core = read(ROOT, "web", "core.js")
    models = read(DATA, "models.json").strip()
    blocks = read(DATA, "blocks.json").strip()

    out = (template
           .replace("/*__CORE_JS__*/", core)
           .replace("/*__MODELS__*/ null", models)
           .replace("/*__BLOCKS__*/ null", blocks))

    for marker in ("/*__CORE_JS__*/", "/*__MODELS__*/", "/*__BLOCKS__*/"):
        if marker in out:
            raise SystemExit(f"injection marker not replaced: {marker}")

    os.makedirs(os.path.join(ROOT, "docs"), exist_ok=True)
    dest = os.path.join(ROOT, "docs", "index.html")
    open(dest, "w", encoding="utf-8").write(out)
    print(f"wrote {dest} ({len(out):,} bytes)")


if __name__ == "__main__":
    main()
