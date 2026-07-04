#!/usr/bin/env python3
"""POD Go .pgp engine: load / save / inspect preset files losslessly.

Two on-disk formats are handled:
  A) raw     : {data, meta, schema, version}  -- what POD Go Edit exports (uncompressed)
  B) wrapped : {encoded_data, compression, encryption, ...}
               encoded_data = base64( zlib( preset_json ) )
               If encryption.type is "hxmp" (commercial/DRM packs) it CANNOT be edited.

POD Go architecture: a preset has 10 blocks (block0..block9) on path "dsp0".
Six are dedicated + movable + bypassable but always present (Volume, Wah, Amp,
Cab, EQ, FX Loop); up to four are user-assignable effects. Chain order == each
block's @position (the editor keeps block-key index == @position). dsp0 also has
`input` (noise gate) and `output` (master pan/gain).
"""
import json, base64, zlib, copy

# ---------------------------------------------------------------- load / save
def load(path):
    """Return (preset_dict, fmt). For wrapped files the decoded preset is under d['_inner']."""
    d = json.load(open(path))
    if 'encoded_data' not in d:
        return d, 'raw'
    enc = d.get('encryption')
    if isinstance(enc, dict) and enc.get('type') not in (None, 'none'):
        raise SystemExit(f"Encrypted ({enc.get('type')}) -- DRM, cannot edit.")
    d['_inner'] = json.loads(zlib.decompress(base64.b64decode(d['encoded_data'])))
    return d, 'wrapped'

def save(d, fmt, path):
    if fmt == 'raw':
        json.dump(d, open(path, 'w'), separators=(',', ':'))
    else:
        inner = json.dumps(d['_inner'], separators=(',', ':')).encode()
        d['encoded_data'] = base64.b64encode(zlib.compress(inner)).decode()
        d.pop('_inner', None)
        json.dump(d, open(path, 'w'))

# ---------------------------------------------------------------- accessors
def _preset(d, fmt):
    return d if fmt == 'raw' else d['_inner']

def tone(d, fmt):
    return _preset(d, fmt)['data']['tone']

def dsp0(d, fmt):
    return tone(d, fmt)['dsp0']

def name(d, fmt):
    return _preset(d, fmt)['data']['meta'].get('name')

def set_name(d, fmt, n):
    _preset(d, fmt)['data']['meta']['name'] = n

def chain(d, fmt):
    """List of (position, block_key, model, enabled, params_dict) sorted by position."""
    rows = []
    for k, v in dsp0(d, fmt).items():
        if isinstance(v, dict):
            rows.append((v.get('@position', 99), k, v.get('@model', '(empty)'),
                         v.get('@enabled', '-'),
                         {pk: pv for pk, pv in v.items() if not pk.startswith('@')}))
    rows.sort()
    return rows

# ---------------------------------------------------------------- editing
def set_param(d, fmt, addr, value):
    """Set a parameter. addr = 'blockN.Param' | 'output.gain' | 'input.threshold'."""
    blk_key, _, param = addr.partition('.')
    blk = dsp0(d, fmt)[blk_key]
    blk[param] = value

def set_enabled(d, fmt, block_key, on):
    """Enable/bypass a block in dsp0 AND in all snapshots (snapshots gate bypass)."""
    dsp0(d, fmt)[block_key]['@enabled'] = on
    t = tone(d, fmt)
    for sn in ('snapshot0', 'snapshot1', 'snapshot2', 'snapshot3'):
        if sn in t:
            t[sn].setdefault('blocks', {}).setdefault('dsp0', {})[block_key] = on

if __name__ == '__main__':
    import sys
    d, fmt = load(sys.argv[1])
    print(f"name={name(d, fmt)!r}  format={fmt}")
    for pos, k, model, en, params in chain(d, fmt):
        print(f"[{pos}] {k:8} {model:34} en={en}")
        if params:
            print('       ', params)
