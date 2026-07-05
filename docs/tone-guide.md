# POD Go Tone Guide — genre starting points

Starting points to tune by ear, spanning clean to heavy. Knob values are **0–10**
(internally POD Go is 0.0–1.0; the build tool converts). Every model named here is
verified in the library. Use these as a scaffold, then dial to taste.

## Signal order (general)
Noise Gate (input) → [Comp or Boost] → Amp → Cab → [Preset EQ] → [Mod] → [Delay] → [Reverb]

- **Noise gate** (input block): only needed for higher gain. Clean/low-gain: off or gentle
  (threshold ~ −64). High gain: threshold ~ −54 to −58, decay ~0.3.
- **Cab low/high cut**: a Low Cut ~85–95 Hz tightens the low end; a High Cut ~7–9 kHz tames
  fizz (drop toward 7 kHz on headphones). Cleaner styles can open the High Cut up to ~9.5 kHz.
- **Preset EQ**: surgical cuts only, not a tone stack replacement.

## Snapshots
Snapshots recall block bypass + controller-assigned param values, so one preset can hold
several sounds (e.g. Rhythm vs Lead) you switch between hands-free. A common two-snapshot
layout: **Rhythm** (boost/drive off, reverb low) and **Lead** (boost on, reverb up).

---

## Clean
Sparkle and headroom. Great as a pedal platform.
- **Amp**: US Deluxe Nrm or US Double Nrm — Drive ~2, Bass 4.5, Mid 5, Treble 6, **Master ~9**
  (on POD Go an amp's Master is the main level control — keep it high on cleans or the patch is quiet)
- **Cab**: 1x12 US Deluxe or 2x12 Silver Bell
- **Add**: Red Squeeze comp in front for evenness; '63 Spring or Plate reverb (Mix ~2)
- **Pop/worship variant**: add a Trinity Chorus (Mix ~2.5) and a Plate reverb for polish.

## Blues
Edge-of-breakup warmth that cleans up with your picking.
- **Amp**: Tweed Blues Nrm — Drive ~5, Mid 6, Treble 5.5; or US Deluxe ~4.5 for a smoother lead
- **Cab**: 4x10 Tweed P10R or 1x12 US Deluxe
- **Add**: a Minotaur (Klon-style) boost, off for rhythm and on for lead; '63 Spring or Room
- Snapshots: **Rhythm** boost off · **Lead** boost on, reverb up.

## Rock
Crunch to arena lead.
- **Crunch amp**: Brit Plexi Nrm — Drive ~6, Mid 6; **Cab** 4x12 Brit V30; Room reverb ~1.2
- **Lead amp**: Brit 2204 (JCM800) — Drive ~6; add a Transistor Tape delay (Mix ~2) and a Hall
- **Jangle/indie variant**: Essex A30 (Vox-style) chime — Drive ~3, add Analog Chorus + light spring.

## Country
Bright, compressed twang.
- **Amp**: Tweed Blues Brt — Drive ~3, Treble 6.5; **Cab** 1x12 US Deluxe
- **Add**: Red Squeeze comp in front; a short **slapback** (Vintage Digital delay, Time low,
  Feedback ~1.5, Mix ~2); '63 Spring.

## Jazz
Warm, round hollowbody.
- **Amp**: Jazz Rivet 120 (Roland JC-style) — Drive ~1.5, Bass 5.5, Mid 5.5, Treble 4
- **Cab**: 2x12 Jazz Rivet, High Cut ~6 kHz to roll off the highs
- **Add**: a small Room (Mix ~1.4). Keep it clean and dark.

## Funk
Snappy, tight, percussive.
- **Amp**: US Double Nrm bright — Drive ~2, Treble 6.5; **Cab** 2x12 Silver Bell
- **Add**: Red Squeeze comp (essential for snap); a light Analog Chorus; small Room.

## Surf
Drippy and drenched.
- **Amp**: US Double Vib (vibrato channel) — Drive ~2; **Cab** 2x12 Silver Bell
- **Add**: an Optical Tremolo and a heavy Spring reverb (Mix ~4).

## Ambient
Cleans that turn into weather.
- **Shimmer**: US Double clean → Vintage Digital delay (Mix ~3) → Ganymede shimmer (Mix ~4.5, Decay ~8)
- **Post-rock swell**: US Double → Transistor Tape delay (Feedback ~4.5, Mix ~3.5) → Cave (Mix ~5.5, Decay ~9)
- **Shoegaze**: add a Triangle Fuzz up front and a 70s Chorus before the delay/reverb for a fuzz wash.

## Metal
Tight modern high gain. Keep it to a few, dialed well.
- **Amp**: German Ubersonic or Revv Gen Red — Drive ~6, Mid scooped-but-present (4–5.5)
- **Boost**: Scream 808 (TS808) in FRONT — Drive **2**, Tone 5.5, Level 8. Low drive + high level
  tightens the low end and pushes the amp without adding fuzz.
- **Cab**: 4x12 Greenback or 4x12 Cali V30, Low Cut ~90–95 Hz, High Cut ~7 kHz
- **Preset EQ**: small mid cut around 500–700 Hz if it's muddy.
- **Gate**: threshold ~ −54, decay ~0.2. Snapshots: **Rhythm** boost on · **Lead** more drive, reverb up.

---

## Notes
Knob values are starting points, strongest on architecture and amp/cab/pedal choice, looser
on exact numbers — trust your ears and the room. The build tool validates every preset before
you get it, so a wrong model name can't slip through.
