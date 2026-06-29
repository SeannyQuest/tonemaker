#!/usr/bin/env python3
"""POD Go tone CLI.  Thin wrapper over pgp_tool for quick inspect/edit.

  python3 podgo.py inspect "presets/Loathe Fangs.pgp"
  python3 podgo.py set "presets/Loathe Fangs.pgp" block2.Drive=0.62 output.gain=8
  python3 podgo.py set "presets/x.pgp" block6.Mix=0.3 --out "presets/y.pgp"
  python3 podgo.py models                       # list verified model IDs

`set` addresses: blockN.Param, output.gain, output.pan, input.threshold, input.decay,
input.noiseGate.  Values parse as int/float/bool (true/false) automatically.
Edits write in place unless --out is given.  Booleans for chorus etc: use true/false.
"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pgp_tool

ROOT = os.path.dirname(os.path.abspath(__file__))

def parse_val(s):
    if s.lower() in ('true', 'false'):
        return s.lower() == 'true'
    try:
        return int(s)
    except ValueError:
        pass
    try:
        return float(s)
    except ValueError:
        return s

def cmd_inspect(path):
    d, fmt = pgp_tool.load(path)
    print(f"name={pgp_tool.name(d, fmt)!r}  format={fmt}")
    g = pgp_tool.dsp0(d, fmt)
    print("input gate:", g.get('input'))
    print("output    :", g.get('output'))
    for pos, k, model, en, params in pgp_tool.chain(d, fmt):
        if model == '(empty)':
            continue
        print(f"[{pos}] {k:8} {model:34} en={en}")
        if params:
            print("       ", params)

def cmd_set(args):
    out = None
    if '--out' in args:
        i = args.index('--out'); out = args[i + 1]; args = args[:i] + args[i + 2:]
    path = args[0]; edits = args[1:]
    d, fmt = pgp_tool.load(path)
    for e in edits:
        addr, _, val = e.partition('=')
        pgp_tool.set_param(d, fmt, addr.strip(), parse_val(val.strip()))
        print(f"  set {addr.strip()} = {parse_val(val.strip())}")
    dest = out or path
    pgp_tool.save(d, fmt, dest)
    json.load(open(dest))  # validate
    print("wrote", dest, "(valid JSON)")

def cmd_models():
    db = json.load(open(os.path.join(ROOT, 'models.json')))
    for cat, entries in db.items():
        if cat.startswith('_'):
            continue
        print(f"\n# {cat}")
        for mid, info in entries.items():
            print(f"  {mid:34} {info.get('name','')}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(0)
    c = sys.argv[1]
    if c == 'inspect':
        cmd_inspect(sys.argv[2])
    elif c == 'set':
        cmd_set(sys.argv[2:])
    elif c == 'models':
        cmd_models()
    else:
        print(__doc__)
