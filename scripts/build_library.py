#!/usr/bin/env python3
"""Build the curated tone library shipped in the web app.

A broad, inclusive spread of ready-made tones across many playing styles, authored
as specs and built + validated through the real engine. Every param is filtered
against the model's real template body, so nothing unknown is ever injected.

  python3 scripts/build_library.py
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "src"))
from tonemaker import build, validate  # noqa: E402
from tonemaker._resources import data_path  # noqa: E402

BLK = json.loads(data_path("blocks.json").read_text())
_M = json.loads(data_path("models.json").read_text())
AMPS = {mid for cat in ("amp", "preamp") for mid in _M.get(cat, {})}


def set_levels(doc, genre):
    """Central loudness policy. ChVol is the real level control on POD Go amps
    (Master is power-amp breakup, not volume), so max ChVol and use a healthy
    global output makeup. Reference patches that sound normal run Drive ~0.45 +
    ChVol ~0.85 + Master ~1.0; clean library tones use low Drive, so they need
    the makeup here. Metal is already hot from gain, so it gets less."""
    g = doc["data"]["tone"]["dsp0"]
    metal = genre == "Metal"
    g["output"]["gain"] = 5 if metal else 9
    for v in g.values():
        if isinstance(v, dict) and v.get("@model") in AMPS:
            v["ChVol"] = 1.0                    # channel volume = main level → full
            v["Master"] = 0.5 if metal else 0.6  # power-amp breakup only; keep moderate
        # open up cabs that default very dark so clean tones aren't muffled/quiet
        if isinstance(v, dict) and str(v.get("@model", "")).startswith(("HD2_Cab", "HD2_CabMicIr")):
            if isinstance(v.get("HighCut"), (int, float)) and v["HighCut"] <= 5000 and not metal:
                v["HighCut"] = 9000.0


def b(model, pos, params=None, enabled=True):
    """A spec block with params filtered to those the model actually has."""
    body = BLK.get(model, {})
    kept = {k: v for k, v in (params or {}).items() if k in body}
    d = {"model": model, "position": pos, "enabled": enabled}
    if kept:
        d["params"] = kept
    return d


VOL = {"model": "HD2_VolPanVolStereo", "position": 0}
GATE = {"noiseGate": True, "threshold": -58, "decay": 0.3}
OPEN = {"noiseGate": False, "threshold": -70, "decay": 0.3}


# (genre, name, blurb, spec)
TONES = [
    ("Clean", "Sparkle Clean", "An everyday Fender-style clean with a touch of spring. Pedal-platform "
     "ready, sits great in a mix.", {
        "name": "Sparkle Clean", "input": {"noiseGate": True, "threshold": -64, "decay": 0.3}, "output": {"gain": 4},
        "blocks": [VOL,
            b("HD2_AmpUSDeluxeNrm", 2, {"Drive": 0.22, "Bass": 0.45, "Mid": 0.5, "Treble": 0.6, "Master": 0.9, "ChVol": 0.85}),
            b("HD2_CabMicIr_1x12USDeluxe", 3, {"Level": 0}),
            b("HD2_Reverb63SpringStereo", 7, {"Mix": 0.18, "Level": 0})]}),

    ("Clean", "Pop Sparkle", "Compressed, chorused, polished clean for pop and worship rhythm. Big open "
     "chords ring out.", {
        "name": "Pop Sparkle", "input": {"noiseGate": True, "threshold": -64, "decay": 0.3}, "output": {"gain": 4},
        "blocks": [VOL,
            b("HD2_CompressorRedSqueezeMono", 1),
            b("HD2_AmpUSDeluxeNrm", 2, {"Drive": 0.18, "Bass": 0.45, "Mid": 0.5, "Treble": 0.62, "Master": 0.9, "ChVol": 0.85}),
            b("HD2_CabMicIr_2x12SilverBell", 3, {"Level": 0}),
            b("HD2_ChorusTrinityChorusStereo", 5, {"Mix": 0.25, "Level": 0}),
            b("HD2_ReverbPlateStereo", 7, {"Mix": 0.2, "Level": 0})]}),

    ("Funk", "Funk Rhythm", "Bright, tight and compressed for snappy funk chords. A hint of chorus for "
     "shimmer on the muted stabs.", {
        "name": "Funk Rhythm", "input": {"noiseGate": True, "threshold": -60, "decay": 0.25}, "output": {"gain": 4},
        "blocks": [VOL,
            b("HD2_CompressorRedSqueezeMono", 1),
            b("HD2_AmpUSDoubleNrm", 2, {"Drive": 0.2, "Bass": 0.4, "Mid": 0.5, "Treble": 0.65, "Master": 0.9, "ChVol": 0.85}),
            b("HD2_CabMicIr_2x12SilverBell", 3, {"Level": 0}),
            b("HD2_MM4AnalogChorus", 5, {"Mix": 0.18, "Level": 0}),
            b("HD2_ReverbRoomStereo", 7, {"Mix": 0.12, "Level": 0})]}),

    ("Jazz", "Jazz Box", "Warm, round hollowbody clean. Highs rolled off, a small room around it. Comping "
     "and single-note lines.", {
        "name": "Jazz Box", "input": {"noiseGate": True, "threshold": -62, "decay": 0.3}, "output": {"gain": 4},
        "blocks": [VOL,
            b("HD2_AmpJazzRivet120", 2, {"Drive": 0.15, "Bass": 0.55, "Mid": 0.55, "Treble": 0.4, "Master": 0.9, "ChVol": 0.85}),
            b("HD2_CabMicIr_2x12JazzRivet", 3, {"HighCut": 6000, "Level": 0}),
            b("HD2_ReverbRoomStereo", 7, {"Mix": 0.14, "Level": 0})]}),

    ("Country", "Country Twang", "Bright, compressed twang with a slapback echo and spring. Chicken pickin' "
     "and clean rhythm both covered.", {
        "name": "Country Twang", "input": {"noiseGate": True, "threshold": -60, "decay": 0.25}, "output": {"gain": 4},
        "blocks": [VOL,
            b("HD2_CompressorRedSqueezeMono", 1),
            b("HD2_AmpTweedBluesBrt", 2, {"Drive": 0.3, "Bass": 0.45, "Mid": 0.5, "Treble": 0.65, "Master": 0.9, "ChVol": 0.85}),
            b("HD2_CabMicIr_1x12USDeluxe", 3, {"Level": 0}),
            b("HD2_DelayVintageDigitalStereoV2", 6, {"Time": 0.12, "Feedback": 0.15, "Mix": 0.18, "Level": 0}),
            b("HD2_Reverb63SpringStereo", 7, {"Mix": 0.16, "Level": 0})]}),

    ("Surf", "Surf Dream", "Drippy vibrato-channel clean drenched in spring reverb, with a slow tremolo "
     "sway. Reverb-tank surf.", {
        "name": "Surf Dream", "input": {"noiseGate": False, "threshold": -70, "decay": 0.3}, "output": {"gain": 4},
        "blocks": [VOL,
            b("HD2_AmpUSDoubleVib", 2, {"Drive": 0.22, "Bass": 0.5, "Mid": 0.5, "Treble": 0.6, "Master": 0.9, "ChVol": 0.85}),
            b("HD2_CabMicIr_2x12SilverBell", 3, {"Level": 0}),
            b("HD2_TremoloOpticalTremStereo", 5),
            b("HD2_ReverbSpringStereo", 7, {"Mix": 0.38, "Level": 0})]}),

    ("Blues", "Blues Breakup", "Edge-of-breakup tweed with a spring tank. Clean when you play soft, growls "
     "when you dig in. Lead kicks in a boost.", {
        "name": "Blues Breakup", "input": {"noiseGate": True, "threshold": -62, "decay": 0.3}, "output": {"gain": 5},
        "blocks": [VOL,
            b("HD2_DistMinotaurMono", 1, {"Gain": 0.4, "Tone": 0.55, "Level": 0.7}, enabled=False),
            b("HD2_AmpTweedBluesNrm", 2, {"Drive": 0.5, "Bass": 0.5, "Mid": 0.6, "Treble": 0.55, "Master": 0.8, "ChVol": 0.9}),
            b("HD2_CabMicIr_4x10TweedP10R", 3, {"Level": 0}),
            b("HD2_Reverb63SpringStereo", 7, {"Mix": 0.2, "Level": 0})],
        "snapshots": [
            {"name": "Rhythm", "bypass": {"block1": False}},
            {"name": "Lead", "bypass": {"block1": True}, "params": {"block7": {"Mix": 0.25}}}]}),

    ("Blues", "Blues Lead", "A singing mid-gain lead voice with a touch of delay and a warm room. Vocal, "
     "sustaining, expressive.", {
        "name": "Blues Lead", "input": {"noiseGate": True, "threshold": -60, "decay": 0.3}, "output": {"gain": 5},
        "blocks": [VOL,
            b("HD2_DistMinotaurMono", 1, {"Gain": 0.5, "Tone": 0.6, "Level": 0.75}),
            b("HD2_AmpUSDeluxeNrm", 2, {"Drive": 0.45, "Bass": 0.5, "Mid": 0.6, "Treble": 0.58, "Master": 0.9, "ChVol": 0.85}),
            b("HD2_CabMicIr_1x12USDeluxe", 3, {"Level": 0}),
            b("HD2_DelayTransistorTapeStereo", 6, {"Time": 0.35, "Feedback": 0.25, "Mix": 0.2, "Level": 0}),
            b("HD2_ReverbRoomStereo", 7, {"Mix": 0.2, "Level": 0})]}),

    ("Rock", "Classic Crunch", "Plexi crunch through a Greenback-style 4x12. Riffs, power chords, and a "
     "little room. The bread and butter.", {
        "name": "Classic Crunch", "input": {"noiseGate": True, "threshold": -60, "decay": 0.3}, "output": {"gain": 5},
        "blocks": [VOL,
            b("HD2_AmpBritPlexiNrm", 2, {"Drive": 0.6, "Bass": 0.5, "Mid": 0.6, "Treble": 0.6, "Master": 0.8, "ChVol": 0.9}),
            b("HD2_CabMicIr_4x12BritV30", 3, {"Level": 0}),
            b("HD2_ReverbRoomStereo", 7, {"Mix": 0.12, "Level": 0})]}),

    ("Rock", "Arena Lead", "JCM800-style rock lead with delay and a hall behind it. Rhythm and Lead "
     "snapshots so you can switch on the fly.", {
        "name": "Arena Lead", "input": {"noiseGate": True, "threshold": -58, "decay": 0.3}, "output": {"gain": 5},
        "blocks": [VOL,
            b("HD2_AmpBrit2204", 2, {"Drive": 0.62, "Bass": 0.5, "Mid": 0.6, "Treble": 0.6, "Master": 0.8, "ChVol": 0.9}),
            b("HD2_CabMicIr_4x12BritV30", 3, {"Level": 0}),
            b("HD2_DelayTransistorTapeStereo", 6, {"Time": 0.4, "Feedback": 0.3, "Mix": 0.22, "Level": 0}),
            b("HD2_ReverbHallStereo", 7, {"Mix": 0.2, "Level": 0})],
        "snapshots": [
            {"name": "Rhythm", "bypass": {"block6": False}, "params": {"block7": {"Mix": 0.12}}},
            {"name": "Lead", "bypass": {"block6": True}, "params": {"block7": {"Mix": 0.3}}}]}),

    ("Rock", "Indie Jangle", "Chimey Vox-style clean-to-edge with analog chorus and a light spring. Jangly "
     "arpeggios and driving eighths.", {
        "name": "Indie Jangle", "input": {"noiseGate": True, "threshold": -62, "decay": 0.3}, "output": {"gain": 4},
        "blocks": [VOL,
            b("HD2_AmpEssexA30", 2, {"Drive": 0.32, "Bass": 0.45, "Mid": 0.5, "Treble": 0.62, "Master": 0.9, "ChVol": 0.85}),
            b("HD2_CabMicIr_2x12BlueBell", 3, {"Level": 0}),
            b("HD2_MM4AnalogChorus", 5, {"Mix": 0.2, "Level": 0}),
            b("HD2_Reverb63SpringStereo", 7, {"Mix": 0.16, "Level": 0})]}),

    ("Ambient", "Ambient Shimmer", "Glassy clean, a digital delay and a shimmer reverb. Swells and big open "
     "chords turn into a pad.", {
        "name": "Ambient Shimmer", "input": {"noiseGate": True, "threshold": -64, "decay": 0.3}, "output": {"gain": 4},
        "blocks": [VOL,
            b("HD2_AmpUSDoubleNrm", 2, {"Drive": 0.18, "Bass": 0.45, "Mid": 0.5, "Treble": 0.6, "Master": 0.9, "ChVol": 0.85}),
            b("HD2_CabMicIr_2x12SilverBell", 3, {"Level": 0}),
            b("HD2_DelayVintageDigitalStereoV2", 6, {"Mix": 0.3, "Level": 0}),
            b("HD2_ReverbGanymedeStereo", 7, {"Mix": 0.45, "Decay": 0.8, "Level": 0})]}),

    ("Ambient", "Post-Rock Swell", "Clean into a cavernous reverb with a trailing delay. Build it up and "
     "let it ring out forever.", {
        "name": "Post-Rock Swell", "input": OPEN, "output": {"gain": 4},
        "blocks": [VOL,
            b("HD2_AmpUSDoubleNrm", 2, {"Drive": 0.2, "Bass": 0.5, "Mid": 0.5, "Treble": 0.55, "Master": 0.9, "ChVol": 0.85}),
            b("HD2_CabMicIr_2x12SilverBell", 3, {"Level": 0}),
            b("HD2_DelayTransistorTapeStereo", 6, {"Time": 0.5, "Feedback": 0.45, "Mix": 0.35, "Level": 0}),
            b("HD2_ReverbCaveStereo", 7, {"Mix": 0.55, "Decay": 0.9, "Level": 0})]}),

    ("Ambient", "Shoegaze Wash", "Clean amp buried under fuzz, chorus, tape delay and a huge reverb. Chords "
     "become weather. Gaze at those shoes.", {
        "name": "Shoegaze Wash", "input": OPEN, "output": {"gain": 4},
        "blocks": [VOL,
            b("HD2_DistTriangleFuzzMono", 1, {"Sustain": 0.5, "Tone": 0.45, "Level": 0.6}),
            b("HD2_AmpUSDoubleNrm", 2, {"Drive": 0.25, "Bass": 0.5, "Mid": 0.5, "Treble": 0.55, "Master": 0.9, "ChVol": 0.85}),
            b("HD2_CabMicIr_4x12CaliV30", 3, {"Level": 0}),
            b("HD2_Chorus70sChorusStereo", 5, {"Mix": 0.4, "Level": 0}),
            b("HD2_DelayTransistorTapeStereo", 6, {"Time": 0.45, "Feedback": 0.4, "Mix": 0.3, "Level": 0}),
            b("HD2_ReverbGanymedeStereo", 7, {"Mix": 0.5, "Decay": 0.85, "Level": 0})]}),

    ("Metal", "Modern High Gain", "Tight, percussive high-gain. Screamer boost into an Uberschall, scooped "
     "but present. Rhythm and Lead snapshots.", {
        "name": "Modern High Gain", "input": {"noiseGate": True, "threshold": -54, "decay": 0.2}, "output": {"gain": 5},
        "blocks": [VOL,
            b("HD2_DistScream808Mono", 1, {"Gain": 0.15, "Tone": 0.6, "Level": 0.85}),
            b("HD2_AmpGermanUbersonic", 2, {"Drive": 0.6, "Bass": 0.45, "Mid": 0.4, "Treble": 0.6, "Master": 0.65, "ChVol": 0.85}),
            b("HD2_Cab4x12Greenback20", 3, {"Level": 0}),
            b("HD2_EQ_STATIC_ParametricStereo", 4, {"MidFreq": 700, "MidGain": -2, "Level": 0}),
            b("HD2_ReverbGanymedeStereo", 7, {"Mix": 0.15, "Decay": 0.4, "Level": 0})],
        "snapshots": [
            {"name": "Rhythm", "bypass": {"block1": True}, "params": {"block7": {"Mix": 0.1}}},
            {"name": "Lead", "bypass": {"block1": True}, "params": {"block2": {"Drive": 0.72}, "block7": {"Mix": 0.35}}}]}),

    ("Metal", "Metalcore", "Aggressive Revv-style gain with a Screamer tightening the low end. Mid-forward "
     "so it cuts. Rhythm and Lead.", {
        "name": "Metalcore", "input": {"noiseGate": True, "threshold": -54, "decay": 0.2}, "output": {"gain": 5},
        "blocks": [VOL,
            b("HD2_DistScream808Mono", 1, {"Gain": 0.2, "Tone": 0.55, "Level": 0.8}),
            b("HD2_AmpRevvGenRed", 2, {"Drive": 0.62, "Bass": 0.5, "Mid": 0.55, "Treble": 0.6, "Master": 0.65, "ChVol": 0.85}),
            b("HD2_CabMicIr_4x12CaliV30", 3, {"Level": 0}),
            b("HD2_EQ_STATIC_ParametricStereo", 4, {"Level": 0}),
            b("HD2_ReverbGanymedeStereo", 7, {"Mix": 0.15, "Decay": 0.4, "Level": 0})],
        "snapshots": [
            {"name": "Rhythm", "bypass": {"block1": True}, "params": {"block7": {"Mix": 0.1}}},
            {"name": "Lead", "bypass": {"block1": True}, "params": {"block2": {"Drive": 0.75}, "block7": {"Mix": 0.35}}}]}),
]

# order of the genre filter chips (lighter styles first, heavy last)
GENRE_ORDER = ["Clean", "Blues", "Rock", "Country", "Jazz", "Funk", "Surf", "Ambient", "Metal"]


def main():
    missing = [blk["model"] for _, _, _, spec in TONES for blk in spec["blocks"] if blk["model"] not in BLK]
    if missing:
        sys.exit(f"models with no template: {sorted(set(missing))}")

    lib = []
    for genre, name, blurb, spec in TONES:
        doc = build.build_from_spec(spec)
        set_levels(doc, genre)
        errors, warnings = validate.validate_doc(doc, "raw")
        if errors:
            sys.exit(f"TONE {name} INVALID: {errors}")
        lib.append({"id": name.lower().replace(" ", "-"), "name": name, "genre": genre,
                    "blurb": blurb, "doc": doc})
        print(f"  built [{genre}] {name}{'  (warnings)' if warnings else ''}")

    # stable order: by GENRE_ORDER, then as authored
    lib.sort(key=lambda t: GENRE_ORDER.index(t["genre"]))
    out = os.path.join(ROOT, "web", "library.json")
    json.dump(lib, open(out, "w"), separators=(",", ":"))
    counts = {}
    for t in lib:
        counts[t["genre"]] = counts.get(t["genre"], 0) + 1
    print(f"\nWrote {out} — {len(lib)} tones across {len(counts)} genres: "
          + ", ".join(f"{g} {counts[g]}" for g in GENRE_ORDER if g in counts))


if __name__ == "__main__":
    main()
