# POD Go Tone Guide — 7-string Drop G#, Headphones

Research-backed (deep-research workflow, 24/25 claims adversarially verified). Knob
values are **0–10 starting points** to tune by ear; sources strongest on architecture,
amp/pedal mapping, and real rigs; weakest on exact parameter numbers. Internally POD Go
params are 0.0–1.0 (the build tool converts).

## Universal foundation (all heavy presets)
- **Signal order**: Noise Gate (input) → [Scream 808 boost] → Amp → Cab → Preset EQ → [mod] → [delay] → [reverb]
- **Noise gate** (input block): threshold ~ −58 dB, decay ~0.3. Essential for Drop G# high-gain.
- **Scream 808** (TS808) in FRONT for tight bands: Drive **2**, Tone **5.5**, Level **8**. Low drive + high level = tighten low end + push amp, not add fuzz.
- **Cab 4x12 Cali V30**: **Low Cut ~90 Hz** (tightens flub, preserves G#1≈52 Hz fundamental), **High Cut ~7.5 kHz** (kills headphone fizz).
- **Preset EQ** (parametric): surgical only — cut ~2.8–3.5 kHz by −2 dB (harsh fizz), small low-mid bump ~220–250 Hz +1.5 dB if thin. Don't just roll amp treble.
- **Headphones**: if still harsh, drop cab High Cut to 7 kHz before touching the amp.

## Snapshots (4 per preset)
Snapshots recall block bypass + controller-assigned param values. With one amp, "clean"
= same amp with **Drive rolled down** (snapshot-controlled) + boost/fuzz off + time-fx up.
Standard layout used below: **1 Clean/Ambient · 2 Rhythm · 3 Lead · 4 Breakdown/Wash**.

---

## 1. Loathe — JCM800 + Big Muff wall + ambience
Erik Bickerstaffe: modded JCM800 (via Axe-Fx) + stacked fuzz + ambient textures.
- **Amp**: Brit 2204 — Drive 7, Bass 5, Mid 6, Treble 6, Presence 5, Master 5
- **User blocks**: Triangle Fuzz (Sustain 4, Tone 5, Level 6) · 70s Chorus · Transistor Tape delay · Ganymede reverb
- No TS — the fuzz is the dirt.

| Snap | Amp Drive | Fuzz | Chorus | Delay | Reverb Mix |
|---|---|---|---|---|---|
| 1 Clean/Ambient | 2 | off | on | on | 0.55 |
| 2 Rhythm | 7 | off | off | off | 0.20 |
| 3 Fuzz Wall | 7 | **on** | off | on | 0.40 |
| 4 Lead/Wash | 7 | on | on | on | 0.50 |

## 2. Deftones — Recto crush ↔ ethereal cleans
Stephen Carpenter: Bogner Uberschall → closest POD Go = Recto into V30. Chorus on cleans.
- **Amp**: Cali Rectifire — Drive 7.5, Bass 5, Mid 4.5, Treble 6, Presence 5, Master 4.5
- **User blocks**: Scream 808 · 70s Chorus · Transistor Tape delay · Ganymede reverb

| Snap | Amp Drive | TS808 | Chorus | Delay | Reverb Mix |
|---|---|---|---|---|---|
| 1 Clean (ethereal) | 1.5 | off | **on** | on | 0.50 |
| 2 Rhythm (crush) | 7.5 | **on** | off | off | 0.15 |
| 3 Lead | 7.5 | on | off | **on** | 0.30 |
| 4 Heavy+Ambient | 7.5 | on | off | on | 0.45 |

## 3. Architects — tight 5150 + soaring leads
Kemper-profiled 5150-style + Maxon OD boost; Strymon delay/verb on leads.
- **Amp**: PV Panama — Drive 7, Bass 5, Mid 5, Treble 6.5, Presence 6, Master 5 (mids up = tight/percussive)
- **User blocks**: Scream 808 (key!) · Transistor Tape delay · Ganymede reverb · 70s Chorus (spare)

| Snap | Amp Drive | TS808 | Delay | Reverb Mix | Notes |
|---|---|---|---|---|---|
| 1 Clean | 1.5 | off | on | 0.40 | — |
| 2 Rhythm (chug) | 7 | **on** | off | 0.10 | tightest gate |
| 3 Lead (soaring) | 7 | on | **on** (dotted-8, Mix 0.35) | 0.30 | ChVol +1 |
| 4 Breakdown | 7.5 | on | off | 0.0 | low-cut up to ~100 |

## 4. Bring Me The Horizon — JCM800 heritage + big choruses
Lee Malia: modded JCM800s historically; ambient/electronic layers, anthemic choruses.
- **Amp**: Brit 2204 + Scream 808 ON for modern heavy — Drive 7.5, Bass 5.5, Mid 4.5, Treble 6, Presence 5.5, Master 5
- **User blocks**: Scream 808 · 70s Chorus · Transistor Tape delay · Ganymede reverb

| Snap | Amp Drive | TS808 | Chorus | Delay | Reverb Mix |
|---|---|---|---|---|---|
| 1 Clean/Ambient | 1.5 | off | **on** | on | 0.50 |
| 2 Rhythm | 7.5 | **on** | off | off | 0.15 |
| 3 Big Chorus | 7.5 | on | **on** | on | 0.35 |
| 4 Breakdown | 7.5 | on | off | off | 0.10 |

## 5. Sleep Token — pristine ambient ↔ djent  *(less-sourced; design by ear)*
Guitarist III: huge ambient cleans (reverb/delay/mod) contrasted with crushing djent.
Single amp compromise: Cali Rectifire cleans at low drive, pushes for heavy.
- **Amp**: Cali Rectifire — heavy: Drive 6.5, Bass 5, Mid 5, Treble 6, Presence 5
- **User blocks**: Scream 808 · 70s Chorus · Transistor Tape delay · Ganymede reverb (shimmer)

| Snap | Amp Drive | TS808 | Chorus | Delay Mix | Reverb Mix |
|---|---|---|---|---|---|
| 1 Ambient Pad | 1.0 | off | **on** | 0.40 | **0.60** |
| 2 Clean Build | 2.5 | off | on | 0.35 | 0.45 |
| 3 Heavy Djent | 6.5 | **on** | off | 0.0 | 0.15 |
| 4 Breakdown/Wash | 6.5 | on | off | 0.20 | 0.40 |

---

## Amps/models used (and what to calibrate)
Verified in library: Cali Rectifire, 4x12 Cali V30, Triangle Fuzz, 70s Chorus, Ganymede, EQ, gate.
**Need verified IDs** (one-time export): **PV Panama** (5150), **Brit 2204** (JCM800),
**Scream 808** (TS808), **Transistor Tape** (delay), plus optional **Searchlights** reverb.

## Sources
Line 6 POD Go Owner's Manual; line6.com/podgo-models; Premier Guitar Rig Rundowns
(Loathe, Deftones, Architects, BMTH); Guitar World; Guitar Chalk; foobazaar tone guide.
Caveats: parameter values are starting points; Sleep Token rig unverified; Deftones'
Bogner has no exact POD Go model; rigs change over time.
