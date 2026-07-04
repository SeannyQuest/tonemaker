#!/usr/bin/env python3
"""Harvest verified POD Go model IDs + params from any .pgp files into models.json.

Point it at folders of exported presets (factory setlist, packs, your own) and it
adds every unique model it finds — with exact @model id, @type, and param keys — to
models.json, skipping DRM-encrypted files and preserving existing hand-written entries.

  python3 harvest_models.py                       # scans reference/ and ~/Downloads
  python3 harvest_models.py ~/Downloads/Factory   # scan a specific folder
"""
import json, os, sys, glob

ROOT = os.path.dirname(os.path.abspath(__file__))

def category(mid):
    if mid.startswith(('HD2_Amp', 'HD2_Preamp')): return 'amp'
    if mid.startswith('HD2_Cab'): return 'cab'
    if mid.startswith('HD2_Dist'): return 'distortion'
    if mid.startswith(('HD2_Chorus', 'HD2_Flanger', 'HD2_Phaser', 'HD2_Tremolo',
                       'HD2_Rotary', 'HD2_Vibrato')): return 'modulation'
    if mid.startswith('HD2_Delay'): return 'delay'
    if mid.startswith('HD2_Reverb'): return 'reverb'
    if mid.startswith('HD2_EQ'): return 'eq'
    if mid.startswith(('HD2_Pitch', 'HD2_Synth', 'HD2_Poly', 'HD2_Harmony')): return 'pitch'
    if mid.startswith(('HD2_Gate', 'HD2_Comp', 'HD2_Dynamics')): return 'dynamics'
    if mid.startswith(('HD2_Wah', 'HD2_VolPan', 'HD2_Vol', 'HD2_FXLoop')): return 'utility'
    if mid.startswith('HD2_Filter'): return 'filter'
    return 'other'

def load_preset(path):
    d = json.load(open(path))
    if 'encoded_data' in d:
        import base64, zlib
        enc = d.get('encryption')
        if isinstance(enc, dict) and enc.get('type') not in (None, 'none'):
            return None  # DRM
        d = json.loads(zlib.decompress(base64.b64decode(d['encoded_data'])))
    return d

def harvest(paths):
    db = json.load(open(os.path.join(ROOT, 'models.json')))
    known = {mid for cat, ents in db.items() if not cat.startswith('_')
             for mid in (ents if isinstance(ents, dict) else {})}
    files, added = [], 0
    for p in paths:
        files += glob.glob(os.path.join(p, '**', '*.pgp'), recursive=True) if os.path.isdir(p) else [p]
    for f in sorted(set(files)):
        try:
            d = load_preset(f)
        except Exception as e:
            print('  skip', os.path.basename(f), '-', e); continue
        if d is None:
            print('  skip (DRM)', os.path.basename(f)); continue
        for tone in d.get('data', {}).get('tone', {}).values():
            if not isinstance(tone, dict): continue
        dsp0 = d['data']['tone'].get('dsp0', {})
        for v in dsp0.values():
            if not isinstance(v, dict): continue
            mid = v.get('@model')
            if not mid or mid.startswith('P34_') or mid in known: continue
            params = sorted(pk for pk in v if not pk.startswith('@'))
            cat = category(mid)
            db.setdefault(cat, {})[mid] = {'name': '(auto-harvested)',
                                           'type': v.get('@type'), 'params': params}
            known.add(mid); added += 1
            print(f'  + [{cat}] {mid}')
    json.dump(db, open(os.path.join(ROOT, 'models.json'), 'w'), indent=2)
    total = sum(len(e) for c, e in db.items() if not c.startswith('_') and isinstance(e, dict))
    print(f'\nAdded {added} new models. Library now has {total} total. Scanned {len(set(files))} files.')

if __name__ == '__main__':
    paths = sys.argv[1:] or [os.path.join(ROOT, 'reference'), os.path.expanduser('~/Downloads')]
    harvest(paths)
