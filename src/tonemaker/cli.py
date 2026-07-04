#!/usr/bin/env python3
"""tonemaker — command-line tool for editing POD Go .pgp presets, drivable by any LLM.

Subcommands: inspect, set, add, build, new, validate, models, harvest, context.
Run `tonemaker <cmd> --help` for details. Presets must be your own unencrypted exports;
DRM (hxmp) presets are refused.
"""
import argparse
import json
import sys

from . import engine, validate as validate_mod, build as build_mod, context as context_mod
from ._resources import load_models


def _parse_val(s):
    low = s.lower()
    if low in ("true", "false"):
        return low == "true"
    for cast in (int, float):
        try:
            return cast(s)
        except ValueError:
            pass
    return s


def _load(path):
    try:
        return engine.load(path)
    except SystemExit as e:  # engine raises SystemExit on hxmp DRM / bad file
        print(f"error: {e}", file=sys.stderr)
        raise SystemExit(2)


def cmd_inspect(args):
    d, fmt = _load(args.file)
    g = engine.dsp0(d, fmt)
    if args.json:
        rows = [{"position": p, "block": k, "model": m, "enabled": en, "params": params}
                for p, k, m, en, params in engine.chain(d, fmt) if m != "(empty)"]
        print(json.dumps({"name": engine.name(d, fmt), "format": fmt,
                          "input": g.get("input"), "output": g.get("output"),
                          "chain": rows}, indent=2))
        return
    print(f"name={engine.name(d, fmt)!r}  format={fmt}")
    print("input gate:", g.get("input"))
    print("output    :", g.get("output"))
    for pos, k, model, en, params in engine.chain(d, fmt):
        if model == "(empty)":
            continue
        print(f"[{pos}] {k:8} {model:34} en={en}")
        if params:
            print("       ", params)


def _validate_or_die(d, fmt, path):
    errors, warnings = validate_mod.validate_doc(d, fmt)
    if warnings:
        print("validation warnings:", file=sys.stderr)
        print(validate_mod.format_report([], warnings), file=sys.stderr)
    if errors:
        print(f"refusing to write {path}: preset would not import:", file=sys.stderr)
        print(validate_mod.format_report(errors, []), file=sys.stderr)
        raise SystemExit(1)


def cmd_set(args):
    d, fmt = _load(args.file)
    for e in args.edits:
        addr, _, val = e.partition("=")
        engine.set_param(d, fmt, addr.strip(), _parse_val(val.strip()))
        print(f"  set {addr.strip()} = {_parse_val(val.strip())}")
    dest = args.out or args.file
    _validate_or_die(d, fmt, dest)
    engine.save(d, fmt, dest)
    print("wrote", dest)


def cmd_add(args):
    d, fmt = _load(args.file)
    models = load_models()
    idx = validate_mod.build_index(models)
    blocks = build_mod._blocks()
    for spec in args.blocks:
        key, _, model = spec.partition("=")
        key = key.strip()
        model = model.strip()
        if model not in idx:
            print(f"error: unknown model {model!r} (not in library)", file=sys.stderr)
            raise SystemExit(1)
        if model not in blocks:
            print(f"error: no template for {model!r}; harvest it from a real export first",
                  file=sys.stderr)
            raise SystemExit(1)
        pos = int(key[5:])
        import copy
        body = copy.deepcopy(blocks[model])
        body["@position"] = pos
        body["@enabled"] = True
        engine.dsp0(d, fmt)[key] = body
        # keep active-snapshot bypass consistent
        engine.set_enabled(d, fmt, key, True)
        print(f"  add {key} = {model}")
    dest = args.out or args.file
    _validate_or_die(d, fmt, dest)
    engine.save(d, fmt, dest)
    print("wrote", dest)


def cmd_build(args):
    spec = json.loads(open(args.spec).read())
    dest = args.out or (spec.get("name", "tone") + ".pgp")
    try:
        _, warnings = build_mod.build(spec, dest)
    except ValueError as e:
        print(f"error: {e}", file=sys.stderr)
        raise SystemExit(1)
    if warnings:
        print(validate_mod.format_report([], warnings), file=sys.stderr)
    print("built + validated:", dest)


def cmd_new(args):
    try:
        doc = build_mod.new(args.template)
    except (ValueError, FileNotFoundError) as e:
        print(f"error: {e}", file=sys.stderr)
        raise SystemExit(1)
    dest = args.out or "new-tone.pgp"
    _validate_or_die(doc, "raw", dest)
    engine.save(doc, "raw", dest)
    print("wrote", dest)


def cmd_validate(args):
    try:
        errors, warnings = validate_mod.validate(args.file)
    except SystemExit as e:
        print(f"error: {e}", file=sys.stderr)
        raise SystemExit(2)
    print(validate_mod.format_report(errors, warnings))
    raise SystemExit(1 if errors else 0)


def cmd_models(args):
    db = load_models()
    if args.json:
        print(json.dumps(db, indent=2))
        return
    for cat, entries in db.items():
        if cat.startswith("_") or not isinstance(entries, dict):
            continue
        if args.category and cat != args.category:
            continue
        ids = [m for m in entries if isinstance(m, str) and m.startswith("HD2_")]
        if not ids:
            continue
        print(f"\n# {cat}")
        for mid in ids:
            print(f"  {mid:34} {entries[mid].get('name', '')}")


def cmd_harvest(args):
    from . import harvest as harvest_mod
    paths = args.paths or harvest_mod.default_paths()
    harvest_mod.harvest(paths)


def cmd_context(args):
    text = context_mod.generate()
    if args.out:
        open(args.out, "w").write(text)
        print("wrote", args.out, file=sys.stderr)
    else:
        sys.stdout.write(text)


def build_parser():
    p = argparse.ArgumentParser(prog="tonemaker", description=__doc__.splitlines()[0])
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("inspect", help="print a preset's chain + params")
    s.add_argument("file")
    s.add_argument("--json", action="store_true")
    s.set_defaults(func=cmd_inspect)

    s = sub.add_parser("set", help="edit parameters (blockN.Param=val, output.gain=8, ...)")
    s.add_argument("file")
    s.add_argument("edits", nargs="+")
    s.add_argument("--out")
    s.set_defaults(func=cmd_set)

    s = sub.add_parser("add", help="add/replace a block (blockN=HD2_ModelId)")
    s.add_argument("file")
    s.add_argument("blocks", nargs="+")
    s.add_argument("--out")
    s.set_defaults(func=cmd_add)

    s = sub.add_parser("build", help="build a preset from a tone spec JSON")
    s.add_argument("spec")
    s.add_argument("--out")
    s.set_defaults(func=cmd_build)

    s = sub.add_parser("new", help="start a new preset (blank or --template)")
    s.add_argument("--template")
    s.add_argument("--out")
    s.set_defaults(func=cmd_new)

    s = sub.add_parser("validate", help="check a preset will import")
    s.add_argument("file")
    s.set_defaults(func=cmd_validate)

    s = sub.add_parser("models", help="list verified model ids")
    s.add_argument("--json", action="store_true")
    s.add_argument("--category")
    s.set_defaults(func=cmd_models)

    s = sub.add_parser("harvest", help="add models from real exports into the library")
    s.add_argument("paths", nargs="*")
    s.set_defaults(func=cmd_harvest)

    s = sub.add_parser("context", help="emit the LLM knowledge pack")
    s.add_argument("--out")
    s.set_defaults(func=cmd_context)

    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    main()
