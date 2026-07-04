#!/usr/bin/env python3
"""Build the curated tone library shipped in the web app.

Authors genre starter tones as specs (built + validated through the real engine),
plus the 5 artist presets from examples/, and writes web/library.json — an array of
{id, name, genre, blurb, doc}. Every entry is validated; invalid ones abort the build.

  python3 scripts/build_library.py
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "src"))
from tonemaker import build, validate, engine  # noqa: E402

GATE = {"noiseGate": True, "threshold": -58, "decay": 0.3}


def vol():
    return {"model": "HD2_VolPanVolStereo", "position": 0}


# genre starter specs — full, dialed chains (not just "amp with gain up")
STARTERS = [
    ("Metal", "Modern Djent", "Tight, percussive high-gain. Screamer boost into an Uberschall, "
        "scooped-but-present mids. Rhythm and Lead snapshots.", {
        "name": "Modern Djent", "input": GATE, "output": {"gain": 6},
        "blocks": [vol(),
            {"model": "HD2_DistScream808Mono", "position": 1, "params": {"Gain": 0.15, "Tone": 0.6, "Level": 0.85}},
            {"model": "HD2_AmpGermanUbersonic", "position": 2, "params": {"Drive": 0.6, "Bass": 0.45, "Mid": 0.4, "Treble": 0.6, "Master": 0.5, "ChVol": 0.85}},
            {"model": "HD2_Cab4x12Greenback20", "position": 3, "params": {"LowCut": 95, "HighCut": 7000, "Level": 0}},
            {"model": "HD2_EQ_STATIC_ParametricStereo", "position": 4, "params": {"MidFreq": 700, "MidGain": -2, "Level": 0}},
            {"model": "HD2_ReverbGanymedeStereo", "position": 7, "params": {"Mix": 0.15, "Decay": 0.4, "Level": 0}}],
        "snapshots": [
            {"name": "Rhythm", "bypass": {"block1": True}, "params": {"block7": {"Mix": 0.1}}},
            {"name": "Lead", "bypass": {"block1": True}, "params": {"block2": {"Drive": 0.72}, "block7": {"Mix": 0.35}}}]}),

    ("Metal", "Death Metal", "Buzzsaw and chunk. Rectifier with a mid scoop and a fast gate, "
        "just enough room to not sound dry.", {
        "name": "Death Metal", "input": {"noiseGate": True, "threshold": -52, "decay": 0.2}, "output": {"gain": 6},
        "blocks": [vol(),
            {"model": "HD2_AmpCaliRectifire", "position": 2, "params": {"Drive": 0.7, "Bass": 0.6, "Mid": 0.3, "Treble": 0.6, "Presence": 0.5, "Master": 0.5, "ChVol": 0.85}},
            {"model": "HD2_CabMicIr_4x12CaliV30", "position": 3, "params": {"LowCut": 90, "HighCut": 6500, "Level": 0}},
            {"model": "HD2_EQ_STATIC_ParametricStereo", "position": 4, "params": {"MidFreq": 500, "MidGain": -4, "Level": 0}},
            {"model": "HD2_ReverbCaveStereo", "position": 7, "params": {"Mix": 0.12, "Decay": 0.5, "Level": 0}}]}),

    ("Metal", "Metalcore Rhythm", "5150-style aggression with a Screamer tightening the low end. "
        "Mid-forward so it cuts. Rhythm and Lead.", {
        "name": "Metalcore Rhythm", "input": GATE, "output": {"gain": 10},
        "blocks": [vol(),
            {"model": "HD2_DistScream808Mono", "position": 1, "params": {"Gain": 0.2, "Tone": 0.55, "Level": 0.8}},
            {"model": "HD2_PreampPVPanama", "position": 2, "params": {"Drive": 0.65, "Bass": 0.5, "Mid": 0.55, "Treble": 0.6, "Master": 0.7, "ChVol": 0.9}},
            {"model": "HD2_CabMicIr_4x12CaliV30", "position": 3, "params": {"LowCut": 95, "HighCut": 7000, "Level": 0}},
            {"model": "HD2_EQ_STATIC_ParametricStereo", "position": 4, "params": {"Level": 0}},
            {"model": "HD2_ReverbGanymedeStereo", "position": 7, "params": {"Mix": 0.15, "Decay": 0.4, "Level": 0}}],
        "snapshots": [
            {"name": "Rhythm", "bypass": {"block1": True}, "params": {"block7": {"Mix": 0.1}}},
            {"name": "Lead", "bypass": {"block1": True}, "params": {"block2": {"Drive": 0.75}, "block7": {"Mix": 0.35}}}]}),

    ("Ambient", "Shoegaze Wash", "Clean amp buried under fuzz, chorus, tape delay and a huge reverb. "
        "Chords turn into weather.", {
        "name": "Shoegaze Wash", "input": {"noiseGate": False, "threshold": -70, "decay": 0.3}, "output": {"gain": 4},
        "blocks": [vol(),
            {"model": "HD2_DistTriangleFuzzMono", "position": 1, "params": {"Sustain": 0.5, "Tone": 0.45, "Level": 0.6}},
            {"model": "HD2_AmpUSDoubleNrm", "position": 2, "params": {"Drive": 0.25, "Bass": 0.5, "Mid": 0.5, "Treble": 0.55, "Presence": 0.45, "Master": 0.5, "ChVol": 0.85}},
            {"model": "HD2_CabMicIr_4x12CaliV30", "position": 3, "params": {"LowCut": 80, "HighCut": 9000, "Level": 0}},
            {"model": "HD2_Chorus70sChorusStereo", "position": 5, "params": {"Mix": 0.4, "Level": 0}},
            {"model": "HD2_DelayTransistorTapeStereo", "position": 6, "params": {"Time": 0.45, "Feedback": 0.4, "Mix": 0.3, "Level": 0}},
            {"model": "HD2_ReverbGanymedeStereo", "position": 7, "params": {"Mix": 0.5, "Decay": 0.85, "Level": 0}}]}),

    ("Ambient", "Worship Clean + Shimmer", "Glassy clean, a dotted digital delay and a shimmer reverb. "
        "Swells and big open chords.", {
        "name": "Worship Shimmer", "input": {"noiseGate": True, "threshold": -64, "decay": 0.3}, "output": {"gain": 4},
        "blocks": [vol(),
            {"model": "HD2_AmpUSDoubleNrm", "position": 2, "params": {"Drive": 0.18, "Bass": 0.45, "Mid": 0.5, "Treble": 0.6, "Presence": 0.5, "Master": 0.5, "ChVol": 0.85}},
            {"model": "HD2_CabMicIr_4x12CaliV30", "position": 3, "params": {"LowCut": 85, "HighCut": 9500, "Level": 0}},
            {"model": "HD2_DelayVintageDigitalStereoV2", "position": 6, "params": {"Mix": 0.3, "Level": 0}},
            {"model": "HD2_ReverbGanymedeStereo", "position": 7, "params": {"Mix": 0.45, "Modulation": 0.5, "Decay": 0.8, "Level": 0}}]}),

    ("Ambient", "Post-Rock Swell", "Clean into a cavernous reverb with a trailing delay. Build it up, "
        "let it ring out.", {
        "name": "Post-Rock Swell", "input": {"noiseGate": False, "threshold": -70, "decay": 0.3}, "output": {"gain": 4},
        "blocks": [vol(),
            {"model": "HD2_AmpUSDoubleNrm", "position": 2, "params": {"Drive": 0.2, "Bass": 0.5, "Mid": 0.5, "Treble": 0.55, "Presence": 0.45, "Master": 0.5, "ChVol": 0.85}},
            {"model": "HD2_CabMicIr_4x12CaliV30", "position": 3, "params": {"LowCut": 80, "HighCut": 9000, "Level": 0}},
            {"model": "HD2_DelayTransistorTapeStereo", "position": 6, "params": {"Time": 0.5, "Feedback": 0.45, "Mix": 0.35, "Level": 0}},
            {"model": "HD2_ReverbCaveStereo", "position": 7, "params": {"Mix": 0.55, "Decay": 0.9, "Level": 0}}]}),

    ("Classic", "Blues Breakup", "Edge-of-breakup Marshall with a spring reverb. Clean when you play "
        "soft, growls when you dig in. Lead adds a boost.", {
        "name": "Blues Breakup", "input": {"noiseGate": True, "threshold": -62, "decay": 0.3}, "output": {"gain": 10},
        "blocks": [vol(),
            {"model": "HD2_DistMinotaurMono", "position": 1, "enabled": False, "params": {"Gain": 0.4, "Tone": 0.55, "Level": 0.7}},
            {"model": "HD2_PreampBrit2204", "position": 2, "params": {"Drive": 0.4, "Bass": 0.5, "Mid": 0.6, "Treble": 0.6, "Master": 0.7, "ChVol": 0.9}},
            {"model": "HD2_CabMicIr_4x12BritV30", "position": 3, "params": {"LowCut": 90, "HighCut": 7500, "Level": 0}},
            {"model": "HD2_Reverb63SpringStereo", "position": 7, "params": {"Mix": 0.2, "Level": 0}}],
        "snapshots": [
            {"name": "Rhythm", "bypass": {"block1": False}},
            {"name": "Lead", "bypass": {"block1": True}, "params": {"block7": {"Mix": 0.25}}}]}),

    ("Classic", "Classic Rock Crunch", "JCM800 crunch through a Greenback-flavored cab with a touch of "
        "spring. Riffs and power chords.", {
        "name": "Classic Rock Crunch", "input": {"noiseGate": True, "threshold": -60, "decay": 0.3}, "output": {"gain": 10},
        "blocks": [vol(),
            {"model": "HD2_PreampBrit2204", "position": 2, "params": {"Drive": 0.6, "Bass": 0.5, "Mid": 0.6, "Treble": 0.6, "Master": 0.7, "ChVol": 0.9}},
            {"model": "HD2_CabMicIr_4x12BritV30", "position": 3, "params": {"LowCut": 90, "HighCut": 7500, "Level": 0}},
            {"model": "HD2_Reverb63SpringStereo", "position": 7, "params": {"Mix": 0.15, "Level": 0}}]}),

    ("Classic", "Texas Clean", "Fender-style sparkle with a hint of grit and a spring tank. Great for "
        "blues leads and clean rhythm.", {
        "name": "Texas Clean", "input": {"noiseGate": True, "threshold": -64, "decay": 0.3}, "output": {"gain": 4},
        "blocks": [vol(),
            {"model": "HD2_DistMinotaurMono", "position": 1, "enabled": False, "params": {"Gain": 0.3, "Tone": 0.6, "Level": 0.7}},
            {"model": "HD2_AmpUSDoubleNrm", "position": 2, "params": {"Drive": 0.3, "Bass": 0.5, "Mid": 0.55, "Treble": 0.6, "Presence": 0.5, "Master": 0.5, "ChVol": 0.85}},
            {"model": "HD2_CabMicIr_4x12CaliV30", "position": 3, "params": {"LowCut": 85, "HighCut": 9000, "Level": 0}},
            {"model": "HD2_Reverb63SpringStereo", "position": 7, "params": {"Mix": 0.18, "Level": 0}}],
        "snapshots": [
            {"name": "Clean", "bypass": {"block1": False}},
            {"name": "Lead", "bypass": {"block1": True}, "params": {"block7": {"Mix": 0.25}}}]}),
]

ARTISTS = {
    "Loathe": "Downtuned shoegaze-metal — JCM800 preamp + Big Muff, four snapshots from clean to fuzz wall.",
    "Deftones": "Recto grit into a V30, TS boost, ambient washes. Clean / Rhythm / Lead / Heavy+Ambient.",
    "Architects": "5150 preamp, tight and modern, with a Screamer out front. Four gig-ready snapshots.",
    "Bring Me The Horizon": "JCM800 crunch, big choruses and breakdowns across four snapshots.",
    "Sleep Token": "Recto ambient-to-djent dynamics, from pad-clean to heavy. Four snapshots.",
}


def main():
    lib = []
    for genre, name, blurb, spec in STARTERS:
        doc = build.build_from_spec(spec)
        errors, warnings = validate.validate_doc(doc, "raw")
        if errors:
            sys.exit(f"STARTER {name} INVALID: {errors}")
        lib.append({"id": name.lower().replace(" ", "-"), "name": name, "genre": genre,
                    "blurb": blurb, "doc": doc})
        print(f"  built [{genre}] {name}{'  (warnings)' if warnings else ''}")

    for fn, blurb in ARTISTS.items():
        path = os.path.join(ROOT, "examples", f"{fn}.pgp")
        d, fmt = engine.load(path)
        errors, _ = validate.validate_doc(d, fmt)
        status = "OK" if not errors else f"WARN {errors[:1]}"
        lib.append({"id": fn.lower().replace(" ", "-"), "name": fn, "genre": "Artist",
                    "blurb": blurb, "doc": d})
        print(f"  loaded [Artist] {fn}  ({status})")

    out = os.path.join(ROOT, "web", "library.json")
    json.dump(lib, open(out, "w"), separators=(",", ":"))
    print(f"\nWrote {out} — {len(lib)} tones "
          f"({sum(1 for x in lib if x['genre']!='Artist')} starters + {len(ARTISTS)} artist).")


if __name__ == "__main__":
    main()
