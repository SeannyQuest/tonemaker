#!/usr/bin/env python3
"""Build 5 artist presets (4 snapshots each) from verified block templates.

Chain layout (position=block key index):
  0 Vol | 1 pre(fuzz/boost) | 2 Amp | 3 Cab | 4 EQ | 5 Chorus | 6 Delay | 7 Reverb | 8 Wah(off) | 9 FXLoop(off)

Snapshot-controlled params (controller 11 = snapshots): amp Drive & ChVol (block2),
delay Mix (block6), reverb Mix (block7). Bypass per snapshot for blocks 1,5,6,7.
"""
import json, copy, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pgp_tool

ROOT = os.path.dirname(os.path.abspath(__file__))

# ---- gather verified block templates by @model across all reference exports ----
by_model = {}
base_doc = None
for fn in ('reference/logic.pgp', 'reference/cal-pv.pgp', 'reference/cal-brit.pgp'):
    d = json.load(open(os.path.join(ROOT, fn)))
    if base_doc is None:
        base_doc = d
    for k, v in d['data']['tone']['dsp0'].items():
        if isinstance(v, dict) and '@model' in v:
            by_model.setdefault(v['@model'], copy.deepcopy(v))

INPUT_TMPL = copy.deepcopy(base_doc['data']['tone']['dsp0']['input'])
OUTPUT_TMPL = copy.deepcopy(base_doc['data']['tone']['dsp0']['output'])

def blk(model, pos, enabled, params):
    b = copy.deepcopy(by_model[model])
    b['@position'] = pos
    b['@enabled'] = enabled
    for pk, pv in params.items():
        b[pk] = pv
    return b

# ---- shared effect param bases ----
EQ = dict(LowCut=20, HighCut=10000, LowFreq=250, LowGain=1.0, LowQ=0.7,
          MidFreq=3000, MidGain=-2.0, MidQ=1.0, HighFreq=5000, HighGain=-1.0,
          HighQ=0.707, Level=0)
CHORUS = dict(Mix=0.30, ChorusIntensity=0.35, VibratoDepth=0.4, VibratoRate=0.35,
              Spread=0.7, Stereo=True, Mode=False, Level=0)
DELAY = dict(Feedback=0.35, Time=0.42, WowFlutter=0.3, Level=0, Spread=0.3,
             Scale=1, SyncSelect1=6, TempoSync1=False, Headroom=0)      # Mix set per-snap
def reverb(decay=0.6, mod=0.45):
    return dict(Modulation=mod, Tone=0.5, Decay=decay, Predelay=0.05, Level=0)  # Mix per-snap

# ---- preset specs ----  snap = (name, {pre,chorus,delay,reverb bypass}, drive,chvol,revmix,dlymix)
P = {
 'Loathe': dict(
   amp=('HD2_PreampBrit2204', dict(Bass=0.50, Mid=0.60, Treble=0.60, Master=0.50, Sag=0.5, Hum=0.3)),
   cab=('HD2_CabMicIr_4x12BritV30', dict(LowCut=90, HighCut=7500, Position=0.35, Mic=2, Angle=45, Distance=1, Level=0)),
   pre=('HD2_DistTriangleFuzzMono', dict(Sustain=0.40, Tone=0.50, Level=0.60)),
   rv=reverb(0.60, 0.5),
   snaps=[('Clean',    dict(pre=0,chorus=1,delay=1,reverb=1), .18,.85,.55,.35),
          ('Rhythm',   dict(pre=0,chorus=0,delay=0,reverb=1), .70,.80,.20,.00),
          ('Fuzz Wall',dict(pre=1,chorus=0,delay=1,reverb=1), .70,.80,.40,.30),
          ('Lead',     dict(pre=1,chorus=1,delay=1,reverb=1), .70,.82,.50,.35)]),
 'Deftones': dict(
   amp=('HD2_AmpCaliRectifire', dict(Bass=0.50, Mid=0.45, Treble=0.60, Presence=0.50, Master=0.45, Sag=0.5, Hum=0.3)),
   cab=('HD2_CabMicIr_4x12CaliV30', dict(LowCut=90, HighCut=7500, Position=0.40, Mic=1, Angle=45, Distance=2, Level=0)),
   pre=('HD2_DistScream808Mono', dict(Gain=0.20, Tone=0.55, Level=0.80)),
   rv=reverb(0.60, 0.45),
   snaps=[('Clean',       dict(pre=0,chorus=1,delay=1,reverb=1), .15,.80,.50,.30),
          ('Rhythm',      dict(pre=1,chorus=0,delay=0,reverb=1), .75,.80,.15,.00),
          ('Lead',        dict(pre=1,chorus=0,delay=1,reverb=1), .75,.82,.30,.35),
          ('Heavy+Ambient',dict(pre=1,chorus=0,delay=1,reverb=1),.75,.80,.45,.25)]),
 'Architects': dict(
   amp=('HD2_PreampPVPanama', dict(Bass=0.50, Mid=0.50, Treble=0.65, Master=0.50, Sag=0.4, Hum=0.3)),
   cab=('HD2_CabMicIr_4x12CaliV30', dict(LowCut=95, HighCut=7500, Position=0.45, Mic=1, Angle=45, Distance=1, Level=0)),
   pre=('HD2_DistScream808Mono', dict(Gain=0.20, Tone=0.60, Level=0.80)),
   rv=reverb(0.55, 0.4),
   snaps=[('Clean',    dict(pre=0,chorus=1,delay=1,reverb=1), .15,.80,.40,.30),
          ('Rhythm',   dict(pre=1,chorus=0,delay=0,reverb=1), .70,.80,.10,.00),
          ('Lead',     dict(pre=1,chorus=0,delay=1,reverb=1), .70,.85,.30,.35),
          ('Breakdown',dict(pre=1,chorus=0,delay=0,reverb=0), .75,.82,.00,.00)]),
 'Bring Me The Horizon': dict(
   amp=('HD2_PreampBrit2204', dict(Bass=0.55, Mid=0.45, Treble=0.60, Master=0.50, Sag=0.5, Hum=0.3)),
   cab=('HD2_CabMicIr_4x12BritV30', dict(LowCut=90, HighCut=7800, Position=0.30, Mic=2, Angle=45, Distance=1, Level=0)),
   pre=('HD2_DistScream808Mono', dict(Gain=0.25, Tone=0.55, Level=0.80)),
   rv=reverb(0.58, 0.45),
   snaps=[('Clean',     dict(pre=0,chorus=1,delay=1,reverb=1), .15,.80,.50,.30),
          ('Rhythm',    dict(pre=1,chorus=0,delay=0,reverb=1), .75,.80,.15,.00),
          ('Big Chorus',dict(pre=1,chorus=1,delay=1,reverb=1), .75,.82,.35,.30),
          ('Breakdown', dict(pre=1,chorus=0,delay=0,reverb=1), .78,.82,.10,.00)]),
 'Sleep Token': dict(
   amp=('HD2_AmpCaliRectifire', dict(Bass=0.50, Mid=0.50, Treble=0.60, Presence=0.50, Master=0.45, Sag=0.5, Hum=0.3)),
   cab=('HD2_CabMicIr_4x12CaliV30', dict(LowCut=90, HighCut=7500, Position=0.45, Mic=1, Angle=45, Distance=2, Level=0)),
   pre=('HD2_DistScream808Mono', dict(Gain=0.20, Tone=0.55, Level=0.80)),
   rv=reverb(0.72, 0.5),
   snaps=[('Ambient Pad', dict(pre=0,chorus=1,delay=1,reverb=1), .10,.85,.60,.40),
          ('Clean Build', dict(pre=0,chorus=1,delay=1,reverb=1), .25,.82,.45,.35),
          ('Heavy Djent', dict(pre=1,chorus=0,delay=0,reverb=1), .65,.80,.15,.00),
          ('Breakdown/Wash',dict(pre=1,chorus=0,delay=1,reverb=1),.65,.80,.40,.20)]),
}

TEMPLATE = json.load(open(os.path.join(ROOT, 'reference/logic.pgp')))  # for meta/schema shell

def build(name, spec):
    doc = copy.deepcopy(TEMPLATE)
    tone = doc['data']['tone']
    s0 = spec['snaps'][0]
    ampM, ampP = spec['amp']; cabM, cabP = spec['cab']; preM, preP = spec['pre']
    # Preamp models are much quieter than full Amp models (no power-amp stage):
    # compensate with more Master, channel volume, and output gain.
    is_preamp = ampM.startswith('HD2_Preamp')
    cbst = 0.15 if is_preamp else 0.0
    if is_preamp:
        ampP = dict(ampP, Master=0.70)
    outgain = 12.0 if is_preamp else 6.0
    # precompute per-snapshot control values. Clean snaps (low drive): pristine the
    # amp gain, max channel volume, and add post-amp EQ makeup gain (block4 Level) so
    # they're LOUDER without adding dirt (louder+cleaner at once).
    adj = []
    for (snapname, byp, drive, chvol, revmix, dlymix) in spec['snaps']:
        is_clean = drive < 0.30
        drv = 0.05 if drive < 0.20 else drive         # pristine the main clean snap
        chv = 1.0 if is_clean else min(1.0, chvol + cbst)
        eql = 8.0 if is_clean else 0.0                # dB makeup gain, clean only
        adj.append(dict(name=snapname, byp=byp, drive=drv, chvol=chv,
                        revmix=revmix, dlymix=dlymix, eql=eql))
    a0 = adj[0]
    ampP = dict(ampP, Drive=a0['drive'], ChVol=a0['chvol'])
    dsp0 = {
        'input': copy.deepcopy(INPUT_TMPL), 'output': copy.deepcopy(OUTPUT_TMPL),
        'block0': blk('HD2_VolPanVolStereo', 0, True, {}),
        'block1': blk(preM, 1, bool(a0['byp']['pre']), preP),
        'block2': blk(ampM, 2, True, ampP),
        'block3': blk(cabM, 3, True, cabP),
        'block4': blk('HD2_EQ_STATIC_ParametricStereo', 4, True, dict(EQ, Level=a0['eql'])),
        'block5': blk('HD2_Chorus70sChorusStereo', 5, bool(a0['byp']['chorus']), CHORUS),
        'block6': blk('HD2_DelayTransistorTapeStereo', 6, bool(a0['byp']['delay']), dict(DELAY, Mix=a0['dlymix'])),
        'block7': blk('HD2_ReverbGanymedeStereo', 7, bool(a0['byp']['reverb']), dict(spec['rv'], Mix=a0['revmix'])),
        'block8': blk('HD2_WahThroatyStereo', 8, False, {}),
        'block9': blk('HD2_FXLoopStereo1_2', 9, False, {}),
    }
    dsp0['input'].update(noiseGate=True, threshold=-58, decay=0.3)
    dsp0['output']['gain'] = outgain
    tone['dsp0'] = dsp0
    # controller wiring: these params vary by snapshot (controller 11)
    tone['controller'] = {'dsp0': {
        'block2': {'Drive': {'@min': 0, '@max': 1, '@controller': 11},
                   'ChVol': {'@min': 0, '@max': 1, '@controller': 11}},
        'block4': {'Level': {'@min': -12, '@max': 12, '@controller': 11}},
        'block6': {'Mix': {'@min': 0, '@max': 1, '@controller': 11}},
        'block7': {'Mix': {'@min': 0, '@max': 1, '@controller': 11}},
    }}
    tone['footswitch'] = {'dsp0': {}}
    ledcolors = [10, 65280, 16744192, 255]
    for i, a in enumerate(adj):
        sn = f'snapshot{i}'
        byp = a['byp']
        tone[sn] = {
            '@name': a['name'], '@tempo': 120, '@valid': True,
            '@pedalstate': 2, '@ledcolor': ledcolors[i],
            'blocks': {'dsp0': {
                'block0': True, 'block1': bool(byp['pre']), 'block2': True, 'block3': True,
                'block4': True, 'block5': bool(byp['chorus']), 'block6': bool(byp['delay']),
                'block7': bool(byp['reverb']), 'block8': False, 'block9': False}},
            'controllers': {'dsp0': {
                'block2': {'Drive': {'@fs_enabled': False, '@value': a['drive']},
                           'ChVol': {'@fs_enabled': False, '@value': a['chvol']}},
                'block4': {'Level': {'@fs_enabled': False, '@value': a['eql']}},
                'block6': {'Mix': {'@fs_enabled': False, '@value': a['dlymix']}},
                'block7': {'Mix': {'@fs_enabled': False, '@value': a['revmix']}}}},
        }
    tone['global'] = {'@model': '@global_params', '@cursor_group': 'block2',
                      '@pedalstate': 2, '@current_snapshot': 0, '@tempo': 120}
    doc['data']['meta']['name'] = name
    out = os.path.join(ROOT, 'presets', f'{name}.pgp')
    json.dump(doc, open(out, 'w'), separators=(',', ':'))
    json.load(open(out))  # validate
    return out

for name, spec in P.items():
    out = build(name, spec)
    print('built', os.path.basename(out))
print('\nAll 5 presets built + validated.')
