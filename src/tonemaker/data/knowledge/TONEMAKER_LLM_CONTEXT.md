# POD Go Tone Builder — LLM Knowledge Pack

> Generated from the verified model library. Do not hand-edit. Paste this whole
> document into your LLM, then describe the guitar tone you want.

You are helping design a tone for the **Line 6 POD Go** by producing data the
`tonemaker` command-line tool can turn into an importable `.pgp` preset. Respond with
**either** of these, and nothing that can't be run:

1. **A tone spec** — a JSON object conforming to the schema below — which the user
   saves as `tone.json` and builds with: `tonemaker build tone.json --out tone.pgp`
2. **A sequence of `tonemaker set` / `tonemaker add` commands** against a named `.pgp` file.

Either way, finish by telling the user to run `tonemaker validate tone.pgp` — this
catches any wrong model id before they try to import it.

## The `.pgp` model (what you're editing)

- A preset is a signal chain of **10 blocks** (`block0`..`block9`) plus an input
  noise gate and a master output. Chain order = each block's `position`.
- Six blocks are dedicated and always present (Volume, Wah, Amp, Cab, EQ, FX Loop);
  up to four are user-assignable effects (distortion, modulation, delay, reverb, ...).
- **Model ids are exact.** Use only the ids listed below (they carry `Mono`/`Stereo`
  suffixes). If ANY block's model id is unrecognized, POD Go rejects the WHOLE preset.
- **Parameter ranges**: amp/drive/fuzz/mix knobs are normalized `0.0`–`1.0`; EQ/cab
  frequencies and cuts are in Hz; gains and levels are in dB; the noise-gate threshold
  is in dB (e.g. `-56`).
- **Snapshots**: a preset can hold up to 4 snapshots (e.g. Clean / Rhythm / Lead /
  Breakdown). Each snapshot overrides which blocks are on (`bypass`) and the values of
  designated parameters (`params`). Keep the active snapshot consistent with which
  blocks you leave enabled.

## Model library (verified — use these ids exactly)

### amp

- **`HD2_AmpCali400Ch1`** — Cali 400 Ch1
  - params: Drive, Bass, Mid, HighMid, Treble, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpCali400Ch2`** — Cali 400 Ch2
  - params: Drive, Bass, Mid, HighMid, Treble, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpCaliBass`** — Cali Bass
  - params: Drive, Bass, Mid, HighMid, Treble, ChVol, Master, Sag, Voice
  - required fields: @bypassvolume
- **`HD2_AmpGCougar800`** — G Cougar 800
  - params: Drive, Bass, LowMid, HighMid, Treble, ChVol, Master, Boost, Contour
  - required fields: @bypassvolume
- **`HD2_AmpSVBeastBrt`** — Ampeg SVT Brt
  - params: Drive, Bass, Mid, MidFreq, Treble, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpSVBeastNrm`** — Ampeg SVT Nrm
  - params: Drive, Bass, Mid, MidFreq, Treble, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpTucknGo`** — Ampeg B-15NF
  - params: Drive, Bass, LowMid, HighMid, Treble, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpA30FawnBrt`** — A30 Fawn Brt
  - params: Drive, Bass, Cut, Treble, Presence, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpA30FawnNrm`** — A30 Fawn Nrm
  - params: Drive, Bass, Cut, Treble, Presence, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpANGLMeteor`** — ANGL Meteor
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX, MidBoost
  - required fields: @bypassvolume
- **`HD2_AmpBrit2204`** — Brit 2204
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpBritJ45Brt`** — Brit J45 Brt
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpBritJ45Nrm`** — Brit J45 Nrm
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpBritP75Brt`** — Brit P75 Brt
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpBritP75Nrm`** — Brit P75 Nrm
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpBritPlexiBrt`** — Brit Plexi Brt
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpBritPlexiJump`** — Brit Plexi Jump
  - params: BrtDrive, NrmDrive, Bass, Mid, Treble, ChVol, Presence, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpBritPlexiNrm`** — Brit Plexi Nrm
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpCaliRectifire`** — Cali Rectifire
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpDividedDuo`** — Divided Duo
  - params: Drive 1, Drive 2, Tone, Cut, Presence, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpEssexA15`** — Essex A15
  - params: Drive, Bass, Mid, Treble, Cut, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpEssexA30`** — Essex A30
  - params: Drive, Bass, Cut, Treble, Presence, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpGermanMahadeva`** — German Mahadeva
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpGermanUbersonic`** — German Ubersonic
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpInterstateZed`** — Interstate Zed
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpJazzRivet120`** — Jazz Rivet 120
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Bright
  - required fields: @bypassvolume
- **`HD2_AmpLine6Doom`** — Line 6 Doom
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpLine6Elektrik`** — Line 6 Elektrik
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpLine6Epic`** — Line 6 Epic
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpMailOrderTwin`** — Mail Order Twin
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpMandarin80`** — Mandarin 80
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX, FAC
  - required fields: @bypassvolume
- **`HD2_AmpPVPanama`** — PV Panama
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX, Resonance
  - required fields: @bypassvolume
- **`HD2_AmpSoloLeadClean`** — Solo Lead Clean
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpSoloLeadCrunch`** — Solo Lead Crunch
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpSoloLeadOD`** — Solo Lead OD
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpSoupPro`** — Soup Pro
  - params: Drive, Bass, Tone, Treble, Presence, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpStoneAge185`** — Stone Age 185
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpTweedBluesBrt`** — Tweed Blues Brt
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpTweedBluesNrm`** — Tweed Blues Nrm
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpUSDeluxeNrm`** — US Deluxe Nrm
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpUSDeluxeVib`** — US Deluxe Vib
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpUSDoubleNrm`** — US Double Nrm
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpUSDoubleVib`** — US Double Vib
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpUSSmallTweed`** — US Small Tweed
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpWhoWatt100`** — WhoWatt 100
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpMatchstickCh1`** — Matchstick Ch1
  - params: Ch1Drive, Bass, Cut, Treble, Presence, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpMatchstickCh2`** — Matchstick Ch2
  - params: Ch2Drive, Tone, Cut, Presence, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpMatchstickJump`** — Matchstick Jump
  - params: Ch1Drive, Bass, Treble, Ch2Drive, Tone, Presence, ChVol, Cut, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpCaliIVLead`** — Cali IV Lead
  - params: LeadGain, LeadDrive, Bass, Mid, Treble, ChVol, Presence, Master, Sag, Ripple, Bias, BiasX, 80Hz, 240Hz, 750Hz, 2200Hz, 6600Hz
  - required fields: @bypassvolume
- **`HD2_AmpCaliIVR1`** — Cali IV Rhythm 1
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Ripple, Bias, BiasX, 80Hz, 240Hz, 750Hz, 2200Hz, 6600Hz
  - required fields: @bypassvolume
- **`HD2_AmpCaliIVR2`** — Cali IV Rhythm 2
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Ripple, Bias, BiasX, 80Hz, 240Hz, 750Hz, 2200Hz, 6600Hz
  - required fields: @bypassvolume
- **`HD2_AmpLine62204Mod`** — Line 6 2204 Mod
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, PreMid, PreMidFc, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpLine6Fatality`** — Line 6 Fatality
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Hum, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpArchetypeClean`** — Archetype Clean
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX, Depth, BrightSW
  - required fields: @bypassvolume
- **`HD2_AmpArchetypeLead`** — Archetype Lead
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX, Depth
  - required fields: @bypassvolume
- **`HD2_AmpLine6Litigator`** — Line 6 Litigator
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpDelSol300`** — Del Sol 300
  - params: Gain, Bright, Contour, Master, ChVol, 62p5Hz, 125Hz, 250Hz, 500Hz, 1kHz, 2kHz, 4kHz
  - required fields: @bypassvolume
- **`HD2_AmpLine6Badonk`** — Line 6 Badonk
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Depth, Sag, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpWoodyBlue`** — Woody Blue
  - params: Drive, Bass, Variamp, Effect, Treble, ChVol, Master, Bright, Hum, TuningFork, TFCoarse, TFFine
  - required fields: @bypassvolume
- **`HD2_AmpBusyOneCh1`** — Busy One Ch1
  - params: Ch1 Drive, Ch1 Bass, Ch1 Mid, Ch1 Mid Freq, Ch1 Treble, Ch1 Master, Input Pad, Ch1 Boost, Limiter, Threshold, Ch Vol
  - required fields: @bypassvolume
- **`HD2_AmpBusyOneCh2`** — Busy One Ch2
  - params: Ch2 Drive, Ch2 Bass, Ch2 Mid, Ch2 Mid Freq, Ch2 Treble, Ch2 Master, Input Pad, Ch2 Boost, Limiter, Threshold, Ch Vol
  - required fields: @bypassvolume
- **`HD2_AmpBusyOneJump`** — Busy One Jump
  - params: Ch1 Drive, Ch1 Bass, Ch1 Mid, Ch1 Mid Freq, Ch1 Treble, Ch1 Master, Ch2 Drive, Ch2 Bass, Ch2 Mid, Ch2 Mid Freq, Ch2 Treble, Ch2 Master, Input Pad, Ch1 Boost, Ch2 Boost, Limiter, Threshold, Ch Vol
  - required fields: @bypassvolume
- **`HD2_AmpDerailedIngrid`** — Derailed Ingrid
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX, Bright
  - required fields: @bypassvolume
- **`HD2_AmpVoltageQueen`** — Voltage Queen
  - params: Drive 1, Drive Trem, Tone, Bass, Treble, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpBritTremNrm`** — Brit Trem Nrm
  - params: NrmDrive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpBritTremBrt`** — Brit Trem Brt
  - params: BrtDrive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpBritTremJump`** — Brit Trem Jump
  - params: BrtDrive, NrmDrive, Bass, Mid, Treble, ChVol, Presence, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpCartographer`** — Cartographer
  - params: Drive, Drive2, Bass, Mid, Treble, ChVol, Master, Presence, Depth, Bright1, Bright2, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpAgua51`** — Agua 51
  - params: Drive, Bass, Mid, Treble, Master, Ch Vol, Deep, Bright
  - required fields: @bypassvolume
- **`HD2_AmpPlacaterDirty`** — Placater Dirty
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, HBE, Fat, C45, Saturation, Ripple, Bias, BiasX, SSwitch, Voice
  - required fields: @bypassvolume
- **`HD2_AmpCaliTexasCh2`** — Cali Texas Ch 2
  - params: Drive 1, Drive 2, Bass, Mid, Treble, ChVol, TS Shape, Presence, Master, Sag, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpPlacaterClean`** — Placater Clean
  - params: Drive, Bass, Treble, Presence, Master, ChVol, Bright, Sag, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpCaliTexasCh1`** — Cali Texas Ch 1
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpSVT4Pro`** — SVT-4 Pro
  - params: Drive, Bass, Mid, MidFreq, Treble, ChVol, Master, UltraLo, UltraHi, Bright, EQ, 33Hz, 80Hz, 150Hz, 300Hz, 600Hz, 900Hz, 2kHz, 5kHz, 8kHz, EQLevel
  - required fields: @bypassvolume
- **`HD2_AmpGrammaticoBrt`** — Grammatico Brt
  - params: DriveNorm, DriveBright, Bass, Tone, Treble, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpGrammaticoJump`** — Grammatico Jump
  - params: DriveNorm, DriveBright, Bass, Tone, Treble, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpGrammaticoNrm`** — Grammatico Nrm
  - params: DriveNorm, DriveBright, Bass, Tone, Treble, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpFullertonBrt`** — Fullerton Brt
  - params: DriveNorm, DriveBright, Bass, Tone, Treble, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpFullertonJump`** — Fullerton Jump
  - params: DriveNorm, DriveBright, Bass, Tone, Treble, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpFullertonNrm`** — Fullerton Nrm
  - params: DriveNorm, DriveBright, Bass, Tone, Treble, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpRevvGenRed`** — Revv Gen Red
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Resonance, Aggression, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpRevvGenPurple`** — Revv Gen Purple
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Resonance, Aggression, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpUSPrincess`** — US Princess
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpDasBenzinLead`** — Das Benzin Lead
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Deep, Sag, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpDasBenzinMega`** — Das Benzin Mega
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Deep, Sag, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpMandarinRocker`** — Mandarin Rocker
  - params: Drive, Bass, Mid, Treble, Master, ChVol, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpLine6Ventoux`** — Line 6 Ventoux
  - params: Drive, HPF, Mid, Presence, Depth, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpMoonNrm`** — Moo)))n Nrm
  - params: BrtDrive, NrmDrive, Bass, Mid, Treble, ChVol, Presence, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpMoonBrt`** — Moo)))n Brt
  - params: BrtDrive, NrmDrive, Bass, Mid, Treble, ChVol, Presence, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpMoonJump`** — Moo)))n Jump
  - params: BrtDrive, NrmDrive, Bass, Mid, Treble, ChVol, Presence, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpAguaSledge`** — Aqua Sledge
  - params: Gain, Drive, Bass, Mid, Treble, Ch Vol, Master, Mid Freq
  - required fields: @bypassvolume
- **`HD2_AmpLine6Elmsley`** — Line 6 Elmsley
  - params: Drive, Bass, Mid, Treble, Master, ChVol, Presence, Depth, NFB, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpGSG100`** — Grammatico GSG
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, MidSwitch, JazzRock, ODSwitch, ODDrive, ODLevel, Bright, FETBoost, PAB, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpLine6Oblivion`** — Line 6 Oblivion
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Boost, Sag, HumSwitch, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpLine6Kinetic`** — Line 6 Kinectic
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Boost, Sag, HumSwitch, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpLine6Voltage`** — Line 6 Voltage
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Boost, Sag, HumSwitch, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpLine6Clarity`** — Line 6 Clarity
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Boost, Sag, HumSwitch
  - required fields: @bypassvolume
- **`HD2_AmpLine6Aristocrat`** — Line 6 Aristocrat
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Boost, Sag, HumSwitch, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpLine6Carillon`** — Line 6 Carillon
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Boost, Sag, HumSwitch, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpUSSuperNorm`** — US Super Nrm
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX, Bright
  - required fields: @bypassvolume
- **`HD2_AmpUSSuperVib`** — US Super Vib
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX, Bright
  - required fields: @bypassvolume
- **`HD2_AmpBrit2203`** — Brit 2203
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX, InputType
  - required fields: @bypassvolume
- **`HD2_AmpGermanXtraBlue`** — German Xtra Blue
  - params: Drive, Bass, Mid, Treble, PreEQ_Brt, ChVol, Boost, Structure, Master, Presence, Excursion_Depth, Old_New, Class_AB_A, Sag, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpGermanXtraRed`** — German Xtra Red
  - params: Drive, Bass, Mid, Treble, PreEQ_Brt, ChVol, Boost, Structure, Master, Presence, Excursion_Depth, Old_New, Class_AB_A, Sag, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpUSDripmanNorm`** — US Dripman Norm
  - params: Norm Drive, Bass, Mid, Treble, Bright, ChVol, Master, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_AmpMandarinBass200`** — Mandarin Bass200
  - params: Gain, Bass, Middle, Treble, Master, ChVol, Sag, Hum, Ripple, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_PreampCali400Ch1`** — Cali 400 Ch1
  - params: Drive, Bass, Mid, HighMid, Treble, ChVol, Master, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampCali400Ch2`** — Cali 400 Ch2
  - params: Drive, Bass, Mid, HighMid, Treble, ChVol, Master, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampCaliBass`** — Cali Bass
  - params: Drive, Bass, Mid, HighMid, Treble, ChVol, Master, Sag, Voice
  - required fields: @bypassvolume
- **`HD2_PreampGCougar800`** — G Cougar 800
  - params: Drive, Bass, LowMid, HighMid, Treble, ChVol, Master, Boost, Contour
  - required fields: @bypassvolume
- **`HD2_PreampSVBeastBrt`** — Ampeg SVT Brt
  - params: Drive, Bass, Mid, MidFreq, Treble, ChVol, Master, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampSVBeastNrm`** — Ampeg SVT Nrm
  - params: Drive, Bass, Mid, MidFreq, Treble, ChVol, Master, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampTucknGo`** — Ampeg B-15NF
  - params: Drive, Bass, LowMid, HighMid, Treble, ChVol, Master, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampA30FawnBrt`** — A30 Fawn Brt
  - params: Drive, Bass, Treble, Master, Sag, ChVol, Hum
  - required fields: @bypassvolume
- **`HD2_PreampA30FawnNrm`** — A30 Fawn Nrm
  - params: Drive, Bass, Treble, Master, Sag, ChVol, Hum
  - required fields: @bypassvolume
- **`HD2_PreampANGLMeteor`** — ANGL Meteor
  - params: Drive, Bass, Mid, Treble, MidBoost, ChVol, Master, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampBrit2204`** — Brit 2204
  - params: Drive, Bass, Mid, Treble, Master, ChVol, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampBritJ45Brt`** — Brit J45 Brt
  - params: Drive, Bass, Mid, Treble, Master, ChVol, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampBritJ45Nrm`** — Brit J45 Nrm
  - params: Drive, Bass, Mid, Treble, Master, ChVol, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampBritP75Brt`** — Brit P75 Brt
  - params: Drive, Bass, Mid, Treble, Master, ChVol, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampBritP75Nrm`** — Brit P75 Nrm
  - params: Drive, Bass, Mid, Treble, Master, ChVol, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampBritPlexiBrt`** — Brit Plexi Brt
  - params: Drive, Bass, Mid, Treble, Master, ChVol, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampBritPlexiJump`** — Brit Plexi Jump
  - params: BrtDrive, NrmDrive, Bass, Mid, Treble, ChVol, Master, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampBritPlexiNrm`** — Brit Plexi Nrm
  - params: Drive, Bass, Mid, Treble, Master, ChVol, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampCaliRectifire`** — Cali Rectifire
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampDividedDuo`** — Divided Duo
  - params: Drive1, Drive2, Tone, Master, ChVol, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampEssexA15`** — Essex A15
  - params: Drive, Bass, Mid, Treble, Master, ChVol, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampEssexA30`** — Essex A30
  - params: Drive, Bass, Treble, Master, Sag, ChVol, Hum
  - required fields: @bypassvolume
- **`HD2_PreampGermanMahadeva`** — German Mahadeva
  - params: Drive, Bass, Mid, Treble, Master, ChVol, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampGermanUbersonic`** — German Ubersonic
  - params: Drive, Bass, Mid, Treble, Ch Vol, Master, Sag
  - required fields: @bypassvolume
- **`HD2_PreampInterstateZed`** — Interstate Zed
  - params: Drive, Bass, Mid, Treble, Master, ChVol, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampJazzRivet120`** — Jazz Rivet 120
  - params: Drive, Bass, Mid, Treble, Bright, ChVol, Master
  - required fields: @bypassvolume
- **`HD2_PreampLine6Doom`** — Line 6 Doom
  - params: Drive, Bass, Mid, Treble, Master, ChVol, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampLine6Elektrik`** — Line 6 Elektrik
  - params: Drive, Bass, Mid, Treble, Master, ChVol, Sag
  - required fields: @bypassvolume
- **`HD2_PreampLine6Epic`** — Line 6 Epic
  - params: Drive, Bass, Mid, Treble, Master, ChVol, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampMailOrderTwin`** — Mail Order Twin
  - params: Drive, Bass, Mid, Treble, Master, ChVol, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampMandarin80`** — Mandarin 80
  - params: Drive, Bass, Mid, Treble, FAC, ChVol, Master, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampPVPanama`** — PV Panama
  - params: Drive, Bass, Mid, Treble, Master, ChVol, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampSoloLeadClean`** — Solo Lead Clean
  - params: Drive, Bass, Mid, Treble, Master, ChVol, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampSoloLeadCrunch`** — Solo Lead Crunch
  - params: Drive, Bass, Mid, Treble, Master, Ch Vol, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampSoloLeadOD`** — Solo Lead OD
  - params: Drive, Bass, Mid, Treble, Master, ChVol, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampSoupPro`** — Soup Pro
  - params: Drive, Bass, Tone, Treble, Master, ChVol, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampStoneAge185`** — Stone Age 185
  - params: Drive, Bass, Mid, Treble, Master, ChVol, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampTweedBluesBrt`** — Tweed Blues Brt
  - params: Drive, Bass, Mid, Treble, Master, ChVol, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampTweedBluesNrm`** — Tweed Blues Nrm
  - params: Drive, Bass, Mid, Treble, Master, ChVol, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampUSDeluxeNrm`** — US Deluxe Nrm
  - params: Drive, Bass, Mid, Treble, Master, ChVol, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampUSDeluxeVib`** — US Deluxe Vib
  - params: Drive, Bass, Mid, Treble, Master, ChVol, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampUSDoubleNrm`** — US Double Nrm
  - params: Drive, Bass, Mid, Treble, Master, ChVol, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampUSDoubleVib`** — US Double Vib
  - params: Drive, Bass, Mid, Treble, Master, ChVol, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampUSSmallTweed`** — US Small Tweed
  - params: Drive, Bass, Mid, Treble, Master, ChVol, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampWhoWatt100`** — WhoWatt 100
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampVintagePre`** — Studio Tube Pre
  - params: Input, Polarity, Hi Pass, Low Pass, Output, MicLine
  - required fields: @bypassvolume
- **`HD2_PreampMatchstickCh1`** — Matchstick Ch1
  - params: Ch1Drive, Bass, Treble, Master, Sag, ChVol, Hum
  - required fields: @bypassvolume
- **`HD2_PreampMatchstickCh2`** — Matchstick Ch2
  - params: Ch2Drive, Tone, ChVol, Master, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampMatchstickJump`** — Matchstick Jump
  - params: Ch1Drive, Bass, Treble, Ch2Drive, Tone, ChVol, Master, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampCaliIVLead`** — Cali IV Lead
  - params: LeadGain, LeadDrive, Bass, Mid, Treble, ChVol, Presence, Master, Sag, 80Hz, 240Hz, 750Hz, 2200Hz, 6600Hz
  - required fields: @bypassvolume
- **`HD2_PreampCaliIVR1`** — Cali IV Rhythm 1
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, 80Hz, 240Hz, 750Hz, 2200Hz, 6600Hz
  - required fields: @bypassvolume
- **`HD2_PreampCaliIVR2`** — Cali IV Rhythm 2
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, 80Hz, 240Hz, 750Hz, 2200Hz, 6600Hz
  - required fields: @bypassvolume
- **`HD2_PreampLine62204Mod`** — Line 6 2204 Mod
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, PreMid, PreMidFc, Bias, BiasX
  - required fields: @bypassvolume
- **`HD2_PreampLine6Fatality`** — Line 6 Fatality
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampLine62204ModV2`** — Line 6 2204 Mod
  - params: Drive, Bass, Mid, Treble, ChVol, Master, Sag, PreMid, PreMidFc
  - required fields: @bypassvolume
- **`HD2_PreampArchetypeClean`** — Archetype Clean
  - params: Drive, Bass, Mid, Treble, Master, ChVol, Sag, Hum, BrightSW
  - required fields: @bypassvolume
- **`HD2_PreampArchetypeLead`** — Archetype Lead
  - params: Drive, Bass, Mid, Treble, Master, ChVol, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampLine6Litigator`** — Line 6 Litigator
  - params: Drive, Bass, Mid, Treble, Master, ChVol, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampDelSol300`** — Del Sol 300
  - params: Gain, 62p5Hz, 125Hz, 250Hz, 500Hz, ChVol, Master, 1kHz, 2kHz, 4kHz, Brite, Contour
  - required fields: @bypassvolume
- **`HD2_PreampWoodyBlue`** — Woody Blue
  - params: Drive, Bass, Variamp, Effect, Treble, ChVol, Master, Bright, Hum, TuningFork, TFCoarse, TFFine
  - required fields: @bypassvolume
- **`HD2_PreampLine6Badonk`** — Line 6 Badonk
  - params: Drive, Bass, Mid, Treble, Master, ChVol, Sag
  - required fields: @bypassvolume
- **`HD2_PreampBusyOneCh1`** — Busy One Ch1
  - params: Ch1 Drive, Ch1 Bass, Ch1 Mid, Ch1 Mid Freq, Ch1 Treble, Ch1 Master, Input Pad, Ch1 Boost, Limiter, Threshold, Ch Vol
  - required fields: @bypassvolume
- **`HD2_PreampBusyOneCh2`** — Busy One Ch2
  - params: Ch2 Drive, Ch2 Bass, Ch2 Mid, Ch2 Mid Freq, Ch2 Treble, Ch2 Master, Input Pad, Ch2 Boost, Limiter, Threshold, Ch Vol
  - required fields: @bypassvolume
- **`HD2_PreampBusyOneJump`** — Busy One Jump
  - params: Ch1 Drive, Ch1 Bass, Ch1 Mid, Ch1 Mid Freq, Ch1 Treble, Ch1 Master, Ch2 Drive, Ch2 Bass, Ch2 Mid, Ch2 Mid Freq, Ch2 Treble, Ch2 Master, Input Pad, Ch1 Boost, Ch2 Boost, Limiter, Threshold, Ch Vol
  - required fields: @bypassvolume
- **`HD2_PreampDerailedIngrid`** — Derailed Ingrid
  - params: Drive, Bass, Mid, Treble, Master, ChVol, Sag, Hum, Bright
  - required fields: @bypassvolume
- **`HD2_PreampVoltageQueen`** — Voltage Queen
  - params: Drive 1, Drive 2, Tone, Bass, Treble, ChVol, Master, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampBritTremNrm`** — Brit Trem Nrm
  - params: NrmDrive, Bass, Mid, Treble, Master, ChVol, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampBritTremBrt`** — Brit Trem Brt
  - params: BrtDrive, Bass, Mid, Treble, Master, ChVol, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampBritTremJump`** — Brit Trem Jump
  - params: BrtDrive, NrmDrive, Bass, Mid, Treble, ChVol, Master, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampCartographer`** — Cartographer
  - params: Drive, Drive2, Bass, Mid, Treble, ChVol, Master, Bright1, Bright2, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampAgua51`** — Agua 51
  - params: Drive, Bass, Mid, Treble, Master, Ch Vol, Deep, Bright
  - required fields: @bypassvolume
- **`HD2_PreampPlacaterDirty`** — Placater Dirty
  - params: Drive, Bass, Mid, Treble, Master, ChVol, Sag, HBE, Fat, C45, Saturation, SSwitch, Voice
  - required fields: @bypassvolume
- **`HD2_PreampCaliTexasCh2`** — Cali Texas Ch 2
  - params: Drive 1, Drive 2, Bass, Mid, Treble, ChVol, TS Shape, Presence, Master
  - required fields: @bypassvolume
- **`HD2_PreampPlacaterClean`** — Placater Clean
  - params: Drive, Bass, Treble, Bright, Master, ChVol, Sag
  - required fields: @bypassvolume
- **`HD2_PreampCaliTexasCh1`** — Cali Texas Ch 1
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Master
  - required fields: @bypassvolume
- **`HD2_PreampSVT4Pro`** — SVT-4 Pro
  - params: Drive, Bass, Mid, MidFreq, Treble, ChVol, Master, UltraLo, UltraHi, Bright, EQ, 33Hz, 80Hz, 150Hz, 300Hz, 600Hz, 900Hz, 2kHz, 5kHz, 8kHz, EQLevel
  - required fields: @bypassvolume
- **`HD2_PreampGrammaticoBrt`** — Grammatico Brt
  - params: DriveNorm, DriveBright, Bass, Tone, Treble, ChVol, Master, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampGrammaticoJump`** — Grammatico Jump
  - params: DriveNorm, DriveBright, Bass, Tone, Treble, ChVol, Master, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampGrammaticoNrm`** — Grammatico Nrm
  - params: DriveNorm, DriveBright, Bass, Tone, Treble, ChVol, Master, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampFullertonBrt`** — Fullerton Brt
  - params: DriveNorm, DriveBright, Bass, Tone, Treble, ChVol, Master, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampFullertonJump`** — Fullerton Jump
  - params: DriveNorm, DriveBright, Bass, Tone, Treble, ChVol, Master, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampFullertonNrm`** — Fullerton Nrm
  - params: DriveNorm, DriveBright, Bass, Tone, Treble, ChVol, Master, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampRevvGenRed`** — Revv Gen Red
  - params: Drive, Bass, Mid, Treble, Master, ChVol, Aggression, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampRevvGenPurple`** — Revv Gen Purple
  - params: Drive, Bass, Mid, Treble, Master, ChVol, Aggression, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampUSPrincess`** — US Princess
  - params: Drive, Bass, Mid, Treble, Master, ChVol, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampDasBenzinLead`** — Das Benzin Lead
  - params: Drive, Bass, Mid, Treble, Master, ChVol, Sag
  - required fields: @bypassvolume
- **`HD2_PreampDasBenzinMega`** — Das Benzin Mega
  - params: Drive, Bass, Mid, Treble, Master, ChVol, Sag
  - required fields: @bypassvolume
- **`HD2_PreampMandarinRocker`** — Mandarin Rocker
  - params: Drive, Bass, Mid, Treble, Master, ChVol, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampLine6Ventoux`** — Line 6 Ventoux
  - params: Drive, HPF, Mid, Presence, Depth, ChVol, Master, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampMoonNrm`** — Moo)))n Nrm
  - params: BrtDrive, NrmDrive, Bass, Mid, Treble, ChVol, Presence, Master, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampMoonBrt`** — Moo)))n Brt
  - params: BrtDrive, NrmDrive, Bass, Mid, Treble, ChVol, Presence, Master, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampMoonJump`** — Moo)))n Jump
  - params: BrtDrive, NrmDrive, Bass, Mid, Treble, ChVol, Presence, Master, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampAguaSledge`** — Aqua Sledge
  - params: Gain, Drive, Bass, Mid, Treble, Ch Vol, Master, Mid Freq
  - required fields: @bypassvolume
- **`HD2_PreampLine6Elmsley`** — Line 6 Elmsley
  - params: Drive, Bass, Mid, Treble, Master, ChVol, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampGSG100`** — Grammatico GSG
  - params: Drive, Bass, Mid, Treble, Master, ChVol, MidSwitch, JazzRock, ODSwitch, ODDrive, ODLevel, Bright, FETBoost, PAB, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampLine6Oblivion`** — Line 6 Oblivion
  - params: Drive, Bass, Mid, Treble, ChVol, Boost, Sag, HumSwitch
  - required fields: @bypassvolume
- **`HD2_PreampLine6Kinetic`** — Line 6 Kinetic
  - params: Drive, Bass, Mid, Treble, ChVol, Boost, Sag, HumSwitch
  - required fields: @bypassvolume
- **`HD2_PreampLine6Voltage`** — Line 6 Voltage
  - params: Drive, Bass, Mid, Treble, ChVol, Boost, Sag, HumSwitch
  - required fields: @bypassvolume
- **`HD2_PreampLine6Clarity`** — Line 6 Clarity
  - params: Drive, Bass, Mid, Treble, Presence, ChVol, Boost, Sag, HumSwitch
  - required fields: @bypassvolume
- **`HD2_PreampLine6Aristocrat`** — Line6 Aristocrat
  - params: Drive, Bass, Mid, Treble, ChVol, Boost, Sag, HumSwitch
  - required fields: @bypassvolume
- **`HD2_PreampLine6Carillon`** — Line 6 Carillon
  - params: Drive, Bass, Mid, Treble, ChVol, Boost, Sag, HumSwitch
  - required fields: @bypassvolume
- **`HD2_PreampUSSuperNorm`** — US Super Nrm
  - params: Drive, Bass, Mid, Treble, Master, ChVol, Sag, Hum, Bright
  - required fields: @bypassvolume
- **`HD2_PreampUSSuperVib`** — US Super Vib
  - params: Drive, Bass, Mid, Treble, Master, ChVol, Sag, Hum, Bright
  - required fields: @bypassvolume
- **`HD2_PreampGermanXtraBlue`** — German Xtra Blue
  - params: Drive, Bass, Mid, Treble, PreEQ_Brt, ChVol, Boost, Structure, Master
  - required fields: @bypassvolume
- **`HD2_PreampGermanXtraRed`** — German Xtra Red
  - params: Drive, Bass, Mid, Treble, PreEQ_Brt, ChVol, Boost, Structure, Master
  - required fields: @bypassvolume
- **`HD2_PreampUSDripmanNorm`** — US Dripman Norm
  - params: Norm Drive, Bass, Mid, Treble, Bright, ChVol, Master, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampMandarinBass200`** — Mandarin Bass200
  - params: Gain, Bass, Middle, Treble, Master, ChVol, Sag, Hum
  - required fields: @bypassvolume
- **`HD2_PreampBrit2203`** — Brit 2203
  - params: Drive, Bass, Mid, Treble, Master, ChVol, Sag, Hum, InputType
  - required fields: @bypassvolume

### cab

- **`HD2_Cab1x12BlueBell`** — 1x12 Blue Bell
  - params: Distance, LowCut, HighCut, EarlyReflections, Level
  - required fields: @mic
- **`HD2_Cab1x12Celest12H`** — 1x12 Celest 12H
  - params: Distance, LowCut, HighCut, EarlyReflections, Level
  - required fields: @mic
- **`HD2_Cab1x12FieldCoil`** — 1x12 Field Coil
  - params: Distance, LowCut, HighCut, EarlyReflections, Level
  - required fields: @mic
- **`HD2_Cab1x12Lead80`** — 1x12 Lead 80
  - params: Distance, LowCut, HighCut, EarlyReflections, Level
  - required fields: @mic
- **`HD2_Cab1x12USDeluxe`** — 1x12 US Deluxe
  - params: Distance, LowCut, HighCut, EarlyReflections, Level
  - required fields: @mic
- **`HD2_Cab1x15TucknGo`** — 1x15 Ampeg B-15
  - params: Distance, LowCut, HighCut, EarlyReflections, Level
  - required fields: @mic
- **`HD2_Cab1x6x9SoupProEllipse`** — Soup Pro Ellipse
  - params: Distance, LowCut, High Cut, EarlyReflections, Level
  - required fields: @mic
- **`HD2_Cab1x8SmallTweed`** — 1x8 Small Tweed
  - params: Distance, LowCut, HighCut, Early Reflections, Level
  - required fields: @mic
- **`HD2_Cab2x12BlueBell`** — 2x12 Blue Bell
  - params: Distance, LowCut, High Cut, EarlyReflections, Level
  - required fields: @mic
- **`HD2_Cab2x12DoubleC12N`** — 2x12 Double C12N
  - params: Distance, LowCut, HighCut, EarlyReflections, Level
  - required fields: @mic
- **`HD2_Cab2x12Interstate`** — 2x12 Interstate
  - params: Distance, Low Cut, HighCut, EarlyReflections, Level
  - required fields: @mic
- **`HD2_Cab2x12JazzRivet`** — 2x12 Jazz Rivet
  - params: Distance, LowCut, HighCut, EarlyReflections, Level
  - required fields: @mic
- **`HD2_Cab2x12MailC12Q`** — 2x12 Mail C12Q
  - params: Distance, LowCut, HighCut, EarlyReflections, Level
  - required fields: @mic
- **`HD2_Cab2x12SilverBell`** — 2x12 Silver Bell
  - params: Distance, LowCut, HighCut, EarlyReflections, Level
  - required fields: @mic
- **`HD2_Cab2x15Brute`** — 2x15 Brute
  - params: Distance, LowCut, HighCut, EarlyReflections, Level
  - required fields: @mic
- **`HD2_Cab4x10Rhino`** — 4x10 Ampeg HLF
  - params: Distance, LowCut, HighCut, EarlyReflections, Level
  - required fields: @mic
- **`HD2_Cab4x10TweedP10R`** — 4x10 Tweed P10R
  - params: Distance, LowCut, HighCut, EarlyReflections, Level
  - required fields: @mic
- **`HD2_Cab4x121960T75`** — 4x12 1960 T75
  - params: Distance, LowCut, HighCut, EarlyReflections, Level
  - required fields: @mic
- **`HD2_Cab4x12Blackback30`** — 4x12 Blackback 30
  - params: Distance, LowCut, HighCut, EarlyReflections, Level
  - required fields: @mic
- **`HD2_Cab4X12CaliV30`** — 4x12 Cali V30
  - params: Distance, LowCut, HighCut, EarlyReflections, Level
  - required fields: @mic
- **`HD2_Cab4x12Greenback20`** — 4x12 Greenback 20
  - params: Distance, LowCut, HighCut, EarlyReflections, Level
  - required fields: @mic
- **`HD2_Cab4x12Greenback25`** — 4x12 Greenback 25
  - params: Distance, LowCut, HighCut, EarlyReflections, Level
  - required fields: @mic
- **`HD2_Cab4x12MandarinEM`** — 4x12 Mandarin EM
  - params: Distance, LowCut, HighCut, EarlyReflections, Level
  - required fields: @mic
- **`HD2_Cab4x12SoloLeadEM`** — 4x12 SoloLead EM
  - params: Distance, LowCut, HighCut, EarlyReflections, Level
  - required fields: @mic
- **`HD2_Cab4x12UberT75`** — 4x12 Uber T75
  - params: Distance, LowCut, HighCut, EarlyReflections, Level
  - required fields: @mic
- **`HD2_Cab4x12UberV30`** — 4x12 Uber V30
  - params: Distance, LowCut, HighCut, EarlyReflections, Level
  - required fields: @mic
- **`HD2_Cab4x12WhoWatt100`** — 4x12 WhoWatt 100
  - params: Distance, LowCut, HighCut, EarlyReflections, Level
  - required fields: @mic
- **`HD2_Cab4x12XXLV30`** — 4x12 XXL V30
  - params: Distance, LowCut, HighCut, EarlyReflections, Level
  - required fields: @mic
- **`HD2_Cab6x10CaliPower`** — 6x10 Cali Power
  - params: Distance, LowCut, HighCut, EarlyReflections, Level
  - required fields: @mic
- **`HD2_Cab8x10SVBeast`** — 8x10 Ampeg SVT-E
  - params: Distance, LowCut, High Cut, EarlyReflections, Level
  - required fields: @mic
- **`HD2_Cab1x12CaliExt`** — 1x12 Cali EXT
  - params: Distance, LowCut, HighCut, EarlyReflections, Level
  - required fields: @mic
- **`HD2_Cab1x12CaliIV`** — 1x12 Cali IV
  - params: Distance, LowCut, HighCut, EarlyReflections, Level
  - required fields: @mic
- **`HD2_Cab1x12DelSol`** — 1x12 Del Sol
  - params: Distance, LowCut, HighCut, EarlyReflections, Level
  - required fields: @mic
- **`HD2_Cab1x12MatchG25`** — 2x12 Match G25
  - params: Distance, LowCut, HighCut, EarlyReflections, Level
  - required fields: @mic
- **`HD2_Cab1x12MatchH30`** — 2x12 Match H30
  - params: Distance, LowCut, HighCut, EarlyReflections, Level
  - required fields: @mic
- **`HD2_Cab1x18DelSol`** — 1x18 Del Sol
  - params: Distance, LowCut, HighCut, EarlyReflections, Level
  - required fields: @mic
- **`HD2_Cab1x18WoodyBlue`** — 1x18 Woody Blue
  - params: Distance, LowCut, HighCut, EarlyReflections, Level
  - required fields: @mic
- **`HD2_Cab1x12Fullerton5C3`** — 1x12 Fullerton
  - params: Distance, LowCut, HighCut, EarlyReflections, Level
  - required fields: @mic
- **`HD2_Cab1x12Grammatico5E3`** — 1x12 Grammatico
  - params: Distance, LowCut, HighCut, EarlyReflections, Level
  - required fields: @mic
- **`HD2_Cab1x10PrincessCopperhead`** — 1x10 US Princess
  - params: Distance, LowCut, HighCut, EarlyReflections, Level
  - required fields: @mic
- **`HD2_Cab1x12PrincessBlue`** — 1x12 US Princess
  - params: Distance, LowCut, HighCut, EarlyReflections, Level
  - required fields: @mic
- **`HD2_CabMicIr_2x12JazzRivet`** — 2x12 Jazz Rivet
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level
- **`HD2_CabMicIr_2x12MailC12Q`** — 2x12 Mail C12Q
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level
- **`HD2_CabMicIr_2x12Mandarin`** — 2x12 Mandarin 30
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level
- **`HD2_CabMicIr_4x121960AT75`** — 4x12 1960A T75
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level
- **`HD2_CabMicIr_4x12BlackbackH30`** — 4x12 Blackback30
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level
- **`HD2_CabMicIr_4x12BritV30`** — 4x12 Brit V30
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level
- **`HD2_CabMicIr_4x12CaliV30`** — 4x12 Cali V30
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level
- **`HD2_CabMicIr_4x12Mandarin`** — 4x12 Mandarin EM
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level
- **`HD2_CabMicIr_4x12MOONT75`** — 4x12 MOO)))N T75
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level
- **`HD2_CabMicIr_4x12UberT75`** — 4x12 Uber T75
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level
- **`HD2_CabMicIr_4x12UberV30`** — 4x12 Uber V30
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level
- **`HD2_CabMicIr_4x12XXLV30`** — 4x12 XXL V30
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level
- **`HD2_CabMicIr_1x12Grammatico`** — 1x12 Grammatico
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level
- **`HD2_CabMicIr_2x12BlueBell`** — 2x12 Blue Bell
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level
- **`HD2_CabMicIr_1x12USDeluxe`** — 1x12 US Deluxe
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level
- **`HD2_CabMicIr_2x12DoubleC12N`** — 2x12 Double C12N
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level
- **`HD2_CabMicIr_4x10TweedP10R`** — 4x10 Tweed P10R
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level
- **`HD2_CabMicIr_4x12Greenback25`** — 4x12 Greenback 25
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level
- **`HD2_CabMicIr_2x15Brute`** — 2x15 Brute
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level
- **`HD2_CabMicIr_8x10SVTAV`** — 8x10 SVT AV
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level
- **`HD2_CabMicIr_1x10USPrincess`** — 1x10 US Princess
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level
- **`HD2_CabMicIr_1x15AmpegB15`** — 1x15 Ampeg B-15
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level
- **`HD2_CabMicIr_4x10Garden`** — 4x10 Garden
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level
- **`HD2_CabMicIr_1x12CaliEXT`** — 1x12 Cali EXT
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level, Pan
- **`HD2_CabMicIr_1x12BlueBell`** — 1x12 Blue Bell
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level
- **`HD2_CabMicIr_4x10AmpegPro`** — 4x10 Ampeg Pro
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level
- **`HD2_CabMicIr_4x12Greenback20`** — 4x12 Greenback20
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level
- **`HD2_CabMicIr_1x12Epicenter`** — 1x12 Epicenter
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level
- **`HD2_CabMicIr_2x12SilverBell`** — 2x12 Silver Bell
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level
- **`HD2_CabMicIr_2x12MatchH30`** — 2x12 Match H30
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level
- **`HD2_CabMicIr_2x12MatchG25`** — 2x12 Match H30
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level
- **`HD2_CabMicIr_1x12OpenCast`** — 1x12 Open Cast
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level
- **`HD2_CabMicIr_1x12OpenCream`** — 1x12 Open Cream
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level
- **`HD2_CabMicIr_4x12Greenback30`** — 4x12 Greenback30
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level
- **`HD2_CabMicIr_2x12Interstate`** — 2x12 Interstate
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level
- **`HD2_CabMicIr_SoupProEllipse`** — Soup Pro Ellipse
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level
- **`HD2_CabMicIr_1x12Fullerton`** — 1x12 Fullerton
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level
- **`HD2_CabMicIr_1x8SmallTweed`** — 1x8 Small Tweed
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level
- **`HD2_CabMicIr_1x12CaliIV`** — 1x12 Cali IV
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level
- **`HD2_CabMicIr_2x15USDripman`** — 2x15 US Dripman
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level
- **`HD2_CabMicIr_6x10CaliPower`** — 6x10 Cali Power
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level
- **`HD2_CabMicIr_4x12WhoWatt100`** — 4x12 WhoWatt 100
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level
- **`HD2_CabMicIr_4x10USSuper`** — 4x10 US Super
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level
- **`HD2_CabMicIr_4x12SoloLeadEM`** — 4x12 SoloLead EM
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level
- **`HD2_CabMicIr_4x12CartogGuv`** — 4x12 Cartog Guv
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level
- **`HD2_CabMicIr_4x12CartogC90`** — 4x12 Cartog C90
  - params: Mic, Position, Distance, Angle, LowCut, HighCut, Level

### distortion

- **`HD2_DistArbitratorFuzzMono`** — Arbitrator Fuzz
  - params: Fuzz, Level
- **`HD2_DistCompulsiveDriveMono`** — Compulsive Drive
  - params: Gain, Tone, LPHP, Version, Level
- **`HD2_DistHedgehogD9Mono`** — Hedgehog D9
  - params: Gain, Tone, Level
- **`HD2_DistIndustrialFuzzMono`** — Industrial Fuzz
  - params: Compress, Gate, Drive, Stability, Oscillator, Level
- **`HD2_DistMegaphoneMono`** — Megaphone
  - params: Grit, Tone, Focus, Space, Mix, Level
- **`HD2_DistMinotaurMono`** — Minotaur
  - params: Gain, Tone, Level
- **`HD2_DistScream808Mono`** — Scream 808
  - params: Gain, Tone, Level
- **`HD2_DistTopSecretODMono`** — Top Secret OD
  - params: Gain, Level
- **`HD2_DistTriangleFuzzMono`** — Triangle Fuzz
  - params: Sustain, Tone, Level
- **`HD2_DistTycoctaviaFuzzMono`** — Tycoctavia Fuzz
  - params: Fuzz, Level
- **`HD2_DistValveDriverMono`** — Valve Driver
  - params: Gain, Bass, Treble, Level
- **`HD2_DistVerminDistMono`** — Vermin Dist
  - params: Gain, Filter, Level
- **`HD2_DistKWBMono`** — KWB
  - params: Gain, PushDiode, PullDiode, Bass, Treble, Level, Asym
- **`HD2_DistBitcrusherMono`** — Bitcrusher
  - params: Gain, BitDepth, SampleRate, LowCut, HighCut, Level, Mix, OpenThreshold, CloseThreshold, HoldTime, Decay
- **`HD2_DistTeemahMono`** — Teemah!
  - params: Gain, Bass, Treble, Clipping, Level
- **`HD2_DistWringerFuzzMono`** — Wringer Fuzz
  - params: Gain, Treble, Bass, Level, FuzzType
- **`HD2_DistStuporODMono`** — Stupor OD
  - params: Drive, Tone, Level
- **`HD2_DistObsidian7000Mono`** — Obsidian 7000
  - params: Drive, Level, Blend, Grunt, Attack, Master, Bass, LoMidFreq, LoMid, HiMidFreq, HiMid, Treble, Distortion
- **`HD2_DistThrifterFuzzMono`** — Thrifter Fuzz
  - params: Drive, Attack, Notch Freq, Notch Gain, Thick, Level
- **`HD2_DistKinkyBoostMono`** — Kinky Boost
  - params: Drive, Boost, Bright
- **`HD2_DM4BuzzSaw`** — Buzz Saw
  - params: Drive, Bass, Mid, Treble, Output
- **`HD2_DM4ClassicDistortion`** — Classic Dist
  - params: Drive, Bass, Filter, Treble, Output
- **`HD2_DM4ColorDrive`** — Colordrive
  - params: Drive, Bass, Mid, Treble, Output
- **`HD2_DM4FacialFuzz`** — Facial Fuzz
  - params: Drive, Bass, Mid, Treble, Output
- **`HD2_DM4FuzzPi`** — Fuzz Pi
  - params: Drive, Bass, Mid, Treble, Output
- **`HD2_DM4HeavyDistortion`** — Heavy Dist
  - params: Drive, Bass, Mid, Treble, Output
- **`HD2_DM4JetFuzz`** — Jet Fuzz
  - params: Drive, Feedback, Tone, Rate, Output
- **`HD2_DM4JumboFuzz`** — Jumbo Fuzz
  - params: Drive, Bass, Mid, Treble, Output
- **`HD2_DM4Line6Distortion`** — L6 Distortion
  - params: Drive, Bass, Mid, Treble, Output
- **`HD2_DM4Line6Drive`** — L6 Drive
  - params: Drive, Bass, Mid, Treble, Output
- **`HD2_DM4OctaveFuzz`** — Octave Fuzz
  - params: Drive, Bass, Mid, Treble, Output
- **`HD2_DM4Overdrive`** — Overdrive
  - params: Drive, Bass, Mid, Treble, Output
- **`HD2_DM4Screamer`** — Screamer
  - params: Drive, Bass, Tone, Treble, Output
- **`HD2_DM4SubOctFuzz`** — Sub Oct Fuzz
  - params: Drive, Bass, Sub, Treble, Output
- **`HD2_DM4TubeDrive`** — Tube Drive
  - params: Drive, Bass, Mid, Treble, Output
- **`HD2_DistDeezOneModMono`** — Deez One Mod
  - params: Drive, Tone, Level, Clipping
- **`HD2_DistDeezOneVintageMono`** — Deez One Vintage
  - params: Drive, Tone, Level
- **`HD2_DistDerangedMasterMono`** — Deranged Master
  - params: Drive, Bass, Treble, Level
- **`HD2_DistAmpegScramblerODMono`** — Ampeg Scrambler
  - params: Drive, Blend, Treble, Level
- **`HD2_DistZeroAmpBassDIMono`** — ZeroAmp Bass DI
  - params: Drive, Bass, Treble, Presence, Blend, Level
- **`HD2_DistDhyanaDriveMono`** — Dyhana Drive
  - params: Gain, Voice, Tone, Level
- **`HD2_DistHeirApparentMono`** — Heir Apparent
  - params: Gain, Tone, Presence, Clipping, GainMod, Level, Voltage
- **`HD2_DistAlpacaRougeMono`** — Alpaca Rouge
  - params: Drive, HiCut, Volume
- **`HD2_DistXenomorphFuzzMono`** — Xenomorph Fuzz
  - params: Gain, Tone, Level, Clipping, OscLevel, OscTone, MinFreq, MaxFreq, WaveShape, Sensitivity
- **`HD2_DistRamsHeadMono`** — Bighorn Fuzz
  - params: Sustain, Tone, Level
- **`HD2_DistSwedishChainsawMono`** — Swedish Chainsaw
  - params: Drive, Bass, Treble, Level
- **`HD2_DistPocketFuzzMono`** — Pocket Fuzz
  - params: Drive, Level
- **`HD2_DistHorizonDriveMono`** — Horizon Drive
  - params: Drive, Attack, Bright, Gate, Gate_Range, Level
- **`HD2_DistBallisticFuzzMono`** — Ballistic Fuzz
  - params: Sustain, Tone, Level
- **`HD2_DistRatatouilleDistMono`** — Ratatouille Dist
  - params: Gain, Filter, Level
- **`HD2_DistPillarsMono`** — Pillars
  - params: Gain, Tone, Level, Mode
- **`HD2_DistDarkDoveFuzzMono`** — Dark Dove Fuzz
  - params: Sustain, Tone, Level
- **`HD2_DistRegalBassDIMono`** — Regal Bass DI
  - params: Bass, Treble, Low Cut, Volume

### modulation

- **`HD2_Chorus70sChorusStereo`** — 70s Chorus
  - params: ChorusIntensity, Mode, VibratoRate, VibratoDepth, Spread, Stereo, Mix, Level, Headroom, SyncSelect1, TempoSync1, SyncSelect2, TempoSync2
- **`HD2_ChorusStereo`** — Chorus
  - params: Speed, Depth, Predelay, WaveShape, Tone, Spread, Mix, Level, SyncSelect1, TempoSync1
- **`HD2_ChorusTrinityChorusStereo`** — Trinity Chorus
  - params: Rate, Left, Center, Right, Preset, Manual, LeftBoost, CenterBoost, RightBoost, Mode, Mix, Level, SyncSelect1, TempoSync1
- **`HD2_FlangerCourtesanFlangeStereo`** — Courtesan Flange
  - params: Rate, Range, Color, FilterMatrix, Spread, Mix, Level, Headroom, SyncSelect1, TempoSync1
- **`HD2_FlangerGrayFlangerStereo`** — Gray Flanger
  - params: Rate, Width, Manual, Regen, Spread, Mix, Level, Headroom, SyncSelect1, TempoSync1
- **`HD2_FlangerHarmonicFlangerStereo`** — Harmonic Flanger
  - params: Rate, Width, Manual, Enhance, Harmonic, Spread, Mix, Level, Headroom, SyncSelect1, TempoSync1
- **`HD2_PhaserScriptModPhaseStereo`** — Script Mod Phase
  - params: Rate, Spread, Mix, Level, SyncSelect1, TempoSync1
- **`HD2_PhaserUbiquitousVibeStereo`** — Ubiquitous Vibe
  - params: Rate, Intensity, Mode, LampBias, Spread, Mix, Level, SyncSelect1, TempoSync1
- **`HD2_RingModulatorAMRingModStereo`** — AM Ring Mod
  - params: Frequency, AM, AMFreq, LFO, LFORate, LFOShape, Mix, Level, SyncSelect1, TempoSync1
- **`HD2_RingModulatorPitchRingModStereo`** — Pitch Ring Mod
  - params: Shape, DutyCycle, Octave, Pitch, LowCut, HighCut, FMAmount, FMShape, FMDuty, FMOctave, FMPitch, Mix, Level
- **`HD2_Rotary122RotaryStereo`** — 122 Rotary
  - params: Speed, SlowSpeed, FastSpeed, RampTime, Drive, Blend, Mix, Level, Headroom, SyncSelect1, TempoSync1, SyncSelect2, TempoSync2
- **`HD2_Rotary145RotaryStereo`** — 145 Rotary
  - params: Speed, SlowSpeed, FastSpeed, RampTime, Drive, Blend, Mix, Level, Headroom, SyncSelect1, TempoSync1, SyncSelect2, TempoSync2
- **`HD2_RotaryVibeRotaryStereo`** — Vibe Rotary
  - params: Speed, SlowSpeed, FastSpeed, RampTime, Drive, Blend, Mix, Level, Headroom, SyncSelect1, TempoSync1, SyncSelect2, TempoSync2
- **`HD2_Tremolo60sBiasTremStereo`** — 60s Bias Trem
  - params: Speed, Intensity, Mode, Spread, Level, SyncSelect1, TempoSync1
- **`HD2_TremoloOpticalTremStereo`** — Optical Trem
  - params: Speed, Intensity, Spread, Level, SyncSelect1, TempoSync1
- **`HD2_VibratoBubbleVibratoStereo`** — Bubble Vibrato
  - params: Speed, Depth, RiseTime, Mix, Level, Spread, Headroom, RiseTimeSwitch, SyncSelect1, TempoSync1
- **`HD2_TremoloTremoloStereo`** — Tremolo/Autopan
  - params: Speed, Intensity, WaveShape, DutyCycle, Spread, Level, SyncSelect1, TempoSync1
- **`HD2_PhaserDeluxePhaserStereo`** — Deluxe Phaser
  - params: Rate, Depth, Offset, Feedback, WaveShape, Mix, Stages, Spread, Level, SyncSelect1, TempoSync1
- **`HD2_FlangerDynamixFlangerStereo`** — Dynamix Flanger
  - params: Speed, Control Select, Depth, Manual, Mix, Phasing, Recycle, CV Dynamics, Max Delay, CV Tracking, Env Lag, Env Input, CV Decay, SyncSelect1, TempoSync1
- **`HD2_TremoloHarmonicStereo`** — Harmonic Tremolo
  - params: Speed, Intensity, WaveShape, DutyCycle, BassFreq, TrebFreq, Level, Mix, Spread, SyncSelect1, TempoSync1
- **`HD2_ChorusPlastiChorusStereo`** — PlastiChorus
  - params: Rate, Depth, Mode, Tone, Mix, Level, Headroom, Spread, TempoSync1, SyncSelect1
- **`HD2_TremoloPatternStereo`** — Bleat Chop Trem
  - params: Speed, WaveShape, Step1, Step2, Step3, Step4, Spread, Depth, Level, TempoSync1, SyncSelect1
- **`HD2_DelayDoubleDoubleStereo`** — Double Take
  - params: Doubles, Slop, Sensitivity, Source, Dry Level, Wet Level
- **`HD2_M1380AFlanger`** — 80A Flanger
  - params: Speed, Range, Enhance, Manual, Harmonic, Level, SyncSelect1, TempoSync1
- **`HD2_M13ACFlanger`** — AC Flanger
  - params: Speed, Width, Regen, Manual, Level, SyncSelect1, TempoSync1
- **`HD2_MM4AnalogChorus`** — Analog Chorus
  - params: Speed, Depth, CH Vib, Tone, Mix, Level, SyncSelect1, TempoSync1
- **`HD2_MM4AnalogFlanger`** — Analog Flanger
  - params: Speed, Depth, Feedback, Manual, Mix, Level, SyncSelect1, TempoSync1
- **`HD2_MM4BarberpolePhaser`** — Barberpole Phaser
  - params: Speed, Feedback, Mode, Mix, Level, SyncSelect1, TempoSync1
- **`HD2_MM4BiasTremolo`** — Bias Tremolo
  - params: Speed, Depth, Shape, Volsens, Mix, Level, SyncSelect1, TempoSync1
- **`HD2_MM4Dimension`** — Dimension
  - params: SW1, SW2, SW3, SW4, Mix, Level
- **`HD2_MM4DualPhaser`** — Dual Phaser
  - params: Speed, Depth, Feedback, LFOShape, Mix, Level, SyncSelect1, TempoSync1
- **`HD2_MM4FrequencyShifter`** — Freq Shift
  - params: Speed, Mode, Mix, Level
- **`HD2_MM4JetFlanger`** — Jet Flanger
  - params: Speed, Depth, Feedback, Manual, Mix, Level, SyncSelect1, TempoSync1
- **`HD2_MM4OptoTremolo`** — Opto Tremolo
  - params: Speed, Depth, Shape, VolSens, Mix, Level, SyncSelect1, TempoSync1
- **`HD2_MM4PannedPhaser`** — Panned Phaser
  - params: Speed, Depth, Pan, Pan Speed, Mix, Level, SyncSelect1, TempoSync1
- **`HD2_MM4Panner`** — Panner
  - params: Speed, Depth, Shape, VolSen, Mix, Level, SyncSelect1, TempoSync1
- **`HD2_MM4PatternTrem`** — Pattern Trem
  - params: Speed, Step1, Step2, Step3, Step4, Level, SyncSelect1, TempoSync1
- **`HD2_MM4Phaser`** — Phaser
  - params: Speed, Depth, Feedback, Stage, Mix, Level, SyncSelect1, TempoSync1
- **`HD2_MM4PitchVibrato`** — Pitch Vibrato
  - params: Speed, Depth, Rise, Volsens, Mix, Level, RiseTimeSwitch, SyncSelect1, TempoSync1
- **`HD2_MM4RingModulator`** — Ring Modulator
  - params: Speed, Depth, Shape, AM/FM, Mix, Level, SyncSelect1, TempoSync1
- **`HD2_MM4RotaryDrum`** — Rotary Drum
  - params: Speed, Depth, Tone, Drive, Mix, Level
- **`HD2_MM4RotaryDrumHorn`** — Rotary Drum/Horn
  - params: Speed, Depth, Horn Depth, Drive, Mix, Level
- **`HD2_MM4ScriptPhase`** — Script Phase
  - params: Speed, Level, SyncSelect1, TempoSync1
- **`HD2_MM4TriChorus`** — Tri Chorus
  - params: Speed, Depth1, Depth2, Depth3, Mix, Level, SyncSelect1, TempoSync1
- **`HD2_MM4UVibe`** — U-Vibe
  - params: Speed, Depth, Feedback, VolSens, Mix, Level, SyncSelect1, TempoSync1
- **`HD2_PhaserPebblePhaserStereo`** — Pebble Phaser
  - params: Rate, Color, Spread, Level, SyncSelect1, TempoSync1
- **`HD2_RetroReelStereo`** — Retro Reel
  - params: WowFluttr, Saturation, LowCut, HighCut, TapeSpeed, Level, Texture
- **`HD2_ChorusAmpegLiquifierStereo`** — Ampeg Liquifier
  - params: Rate, Depth, Mix, Level, Headroom, Mode, Spread, TempoSync1, SyncSelect1
- **`HD2_Chorus4VoiceStereo`** — 4-Voice Chorus
  - params: Speed, Depth, NumVoices, HPFFrq, HighShelf, Mix, Level, SyncSelect1, TempoSync1
- **`HD2_Rotary3RotorStereo`** — Triple Rotary
  - params: Speed, SlowSpeed, FastSpeed, RampTime, Mix, Level, Drive, Headroom, LowCut, HighCut, Wobble, Separation, RotorFcDrift, Rotor2Level, Rotor3Level, TempoSync1, SyncSelect1, TempoSync2, SyncSelect2

### delay

- **`HD2_DelayAdriaticDelayStereo`** — Adriatic Delay
  - params: Time, Scale, Feedback, Noise, BBD Size, Mix, Level, Rate, Depth, Spread, Headroom, SyncSelect1, TempoSync1
  - required fields: @trails
- **`HD2_DelayBucketBrigadeStereo`** — Bucket Brigade
  - params: Time, Feedback, Scale, Noise, Mix, Level, Headroom, SyncSelect1, TempoSync1
  - required fields: @trails
- **`HD2_DelayDuckedDelayStereo`** — Ducked Delay
  - params: Time, Feedback, LowCut, HighCut, Mix, Level, Scale, Threshold, Ducking, DynAttack, DynRel, DynType, TempoSync1, SyncSelect1
  - required fields: @trails
- **`HD2_DelayElephantManStereo`** — Elephant Man
  - params: Time, Feedback, Mode, Depth, Mix, Level, Scale, Spread, Noise, Headroom, SyncSelect1, TempoSync1
  - required fields: @trails
- **`HD2_DelayHarmonyDelayStereo`** — Harmony Delay
  - params: Time, Feedback, Key, Scale, Mix, Level, IntervalVoice1, LevelVoice1, PanVoice1, IntervalVoice2, LevelVoice2, PanVoice2, DelayVoice1, DelayVoice2, LevelRootVoice, PanRootVoice, LowCut, HighCut, SyncSelect1, TempoSync1
  - required fields: @trails
- **`HD2_DelayModChorusEchoStereo`** — Mod/Chorus Echo
  - params: Time, Feedback, LowCut, HighCut, Mix, Level, Scale, ModulationMode, Speed, Depth, Spread, SyncSelect1, TempoSync1
  - required fields: @trails
- **`HD2_DelayMultitap4Stereo`** — Multitap 4
  - params: Time, Feedback, Diffusion, LowCut, HighCut, Mix, Tap1Delay, Tap1Pan, Tap1Level, Tap2Delay, Tap2Pan, Tap2Level, Tap3Delay, Tap3Pan, Tap3Level, Tap4Delay, Tap4Pan, Tap4Level, ModulationMode, Speed, Depth, Spread, Level, SyncSelect1, TempoSync1
  - required fields: @trails
- **`HD2_DelayMultitap6Stereo`** — Multitap 6
  - params: Time, Feedback, LowCut, HighCut, Mix, Level, Tap1Delay, Tap1Pan, Tap1Level, Tap2Delay, Tap2Pan, Tap2Level, Tap3Delay, Tap3Pan, Tap3Level, Tap4Delay, Tap4Pan, Tap4Level, Tap5Delay, Tap5Pan, Tap5Level, Tap6Delay, Tap6Pan, Tap6Level, SyncSelect1, TempoSync1
  - required fields: @trails
- **`HD2_DelayPingPongStereo`** — Ping Pong
  - params: Time, Feedback, Scale, Spread, Mix, Level, LowCut, HighCut, TempoSync1, SyncSelect1
  - required fields: @trails
- **`HD2_DelaySimpleDelayStereo`** — Simple Delay
  - params: Time, Feedback, Mix, Level, Scale, SyncSelect1, TempoSync1
  - required fields: @trails
- **`HD2_DelaySweepEchoStereo`** — Sweep Echo
  - params: Time, Feedback, LowCut, HighCut, Mix, Level, FilterType, SweepShape, SweepSpeed, SweepStart, SweepDepth, SweepResonance, SweepSymmetry, Scale, SweepSpread, Headroom, TempoSync1, SyncSelect1
  - required fields: @trails
- **`HD2_DelayTransistorTapeStereo`** — Transistor Tape
  - params: Time, Feedback, WowFlutter, Scale, Spread, Mix, Level, Headroom, SyncSelect1, TempoSync1
  - required fields: @trails
- **`HD2_DelayReverseDelayStereo`** — Reverse Delay
  - params: Time, Feedback, LowCut, HighCut, Mix, Level, Speed, Depth, ModulationMode, Spread, SyncSelect1, TempoSync1
  - required fields: @trails
- **`HD2_DelayDualDelayStereo`** — Dual Delay
  - params: Left Time, Right Time, LeftFeedback, RightFeedback, MixL, MixR, Level, LowCut, HighCut, Speed, Depth, ModulationMode, Spread, SyncSelect1, TempoSync1, SyncSelect2, TempoSync2
  - required fields: @trails
- **`HD2_DelayVintageDigitalStereoV2`** — Vintage Digital
  - params: Time, Feedback, BitDepth, SampleRate, Mix, Level, Rate, Depth, Scale, Headroom, SyncSelect1, TempoSync1
  - required fields: @trails
- **`HD2_DelayPitchStereo`** — Pitch Echo
  - params: Time, Feedback, Interval1, Cents1, Mix, Level, LowCut, HighCut, Scale, SyncSelect1, TempoSync1
  - required fields: @trails
- **`HD2_DelaySwellAdriaticStereo`** — Adriatic Swell
  - params: Time, Scale, Feedback, Noise, BBD Size, Mix, Rate, Depth, Spread, Level, Headroom, Threshold, Attack, SyncSelect1, TempoSync1
  - required fields: @trails
- **`HD2_DelaySwellVintageDigitalStereo`** — Vintage Swell
  - params: Time, Feedback, BitDepth, SampleRate, Mix, Level, Rate, Depth, Scale, Headroom, Threshold, Attack, SyncSelect1, TempoSync1
  - required fields: @trails
- **`HD2_DL4AnalogDelayStereo`** — Analog Echo
  - params: Time, Feedback, Bass, Treble, Mix, Level, SyncSelect1, TempoSync1
  - required fields: @trails
- **`HD2_DL4AnalogDelayStereoMod`** — Analog w/Mod
  - params: Time, Feedback, ModSpeed, Depth, Mix, Level, SyncSelect1, TempoSync1
  - required fields: @trails
- **`HD2_DL4AutoVolStereo`** — Auto-Vol Echo
  - params: Time, Feedback, Depth, Swell, Mix, Level, SyncSelect1, TempoSync1
  - required fields: @trails
- **`HD2_DL4DigDelay`** — Digital
  - params: Time, Feedback, Bass, Treble, Mix, Level, SyncSelect1, TempoSync1
  - required fields: @trails
- **`HD2_DL4DigDelayWithMod`** — Digital w/Mod
  - params: Time, Feedback, ModSpeed, Depth, Mix, Level, SyncSelect1, TempoSync1
  - required fields: @trails
- **`HD2_DL4DynamicDelayStereo`** — Dynamic
  - params: Time, Feedback, Threshold, Ducking, Mix, Level, SyncSelect1, TempoSync1
  - required fields: @trails
- **`HD2_DL4EchoPlatterStereo`** — Echo Platter
  - params: Time, Feedback, Wow Flt, Drive, Mix, Level, DryThru, SyncSelect1, TempoSync1
  - required fields: @trails
- **`HD2_DL4LowResDelay`** — Lo Res
  - params: Time, Feedback, Tone, Res, Mix, Level, SyncSelect1, TempoSync1
  - required fields: @trails
- **`HD2_DL4MultiheadStereo`** — Multi-Head
  - params: Time, Feedback, Heads 1-2, Heads 3-4, Mix, Level, SyncSelect1, TempoSync1
  - required fields: @trails
- **`HD2_DL4PingPong`** — Ping Pong
  - params: Time, Feedback, Offset, Spread, Mix, Level, SyncSelect1, TempoSync1
  - required fields: @trails
- **`HD2_DL4Reverse`** — Reverse
  - params: Time, Feedback, ModSpeed, Depth, Mix, Level, SyncSelect1, TempoSync1
  - required fields: @trails
- **`HD2_DL4StereoDelay`** — Stereo
  - params: LTime, LFeedback, RTime, RFeedback, Mix, Level, SyncSelect1, TempoSync1, SyncSelect2, TempoSync2
  - required fields: @trails
- **`HD2_DL4SweepEchoStereo`** — Sweep Echo
  - params: Time, Feedback, Speed, Depth, Mix, Level, DryThru, SyncSelect1, TempoSync1
  - required fields: @trails
- **`HD2_DL4TapeEchoStereo`** — Tape Echo
  - params: Time, Feedback, Bass, Treble, Mix, Level, DryThru, SyncSelect1, TempoSync1
  - required fields: @trails
- **`HD2_DL4TubeEchoStereo`** — Tube Echo
  - params: Time, Feedback, Wow Flt, Drive, Mix, Level, DryThru, SyncSelect1, TempoSync1
  - required fields: @trails
- **`HD2_DelayMultiPassStereo`** — Multi Pass
  - params: Time, Feedback, Pattern, Mode, Mix, Level, Tap1Pan, Tap2Pan, Tap3Pan, Tap4Pan, Tap5Pan, Tap6Pan, SyncSelect1, TempoSync1
  - required fields: @trails
- **`HD2_DelayADTStereo`** — ADT
  - params: DelayDeck1, DelayDeck2, WowFlutter1, WowFlutter2, DistDeck1, DistDeck2, Deck1Vol, Deck2Vol, Deck2Pol, ModRate, ModDepth, Level, TapeSpeed, Texture, LowCut, HighCut, Deck1Pan, Deck2Pan, Threshold
  - required fields: @trails
- **`HD2_DelayCrissCrossStereo`** — Crisscross
  - params: TimeA, TimeB, FeedbackA, FeedbackB, PanA, PanB, Mix, Level, Crossfeed, Headroom, ModRate, ModDepth, Shape, Phase, BitDepth, SampleRate, LowCut, HighCut, TempoSync1, SyncSelect1, TempoSync2, SyncSelect2
  - required fields: @trails

### reverb

- **`HD2_Reverb63SpringStereo`** — '63 Spring
  - params: Decay, Predelay, LowCut, HighCut, Mix, Level
  - required fields: @trails
- **`HD2_ReverbCaveStereo`** — Cave
  - params: Decay, Predelay, LowCut, HighCut, Mix, Level
  - required fields: @trails
- **`HD2_ReverbChamberStereo`** — Chamber
  - params: Decay, Predelay, LowCut, HighCut, Mix, Level
  - required fields: @trails
- **`HD2_ReverbDuckingStereo`** — Ducking
  - params: Decay, Predelay, LowCut, HighCut, Mix, Level
  - required fields: @trails
- **`HD2_ReverbEchoStereo`** — Echo
  - params: Decay, Predelay, LowCut, HighCut, Mix, Level
  - required fields: @trails
- **`HD2_ReverbHallStereo`** — Hall
  - params: Decay, Predelay, LowCut, HighCut, Mix, Level
  - required fields: @trails
- **`HD2_ReverbOctoStereo`** — Octo
  - params: Decay, Intensity, LowCut, HighCut, Mix, Level
  - required fields: @trails
- **`HD2_ReverbParticleStereo`** — Particle Verb
  - params: Dwell, Condition, Mix, Level
  - required fields: @trails
- **`HD2_ReverbPlateStereo`** — Plate
  - params: Decay, Predelay, LowCut, HighCut, Mix, Level
  - required fields: @trails
- **`HD2_ReverbRoomStereo`** — Room
  - params: Decay, Predelay, LowCut, HighCut, Mix, Level
  - required fields: @trails
- **`HD2_ReverbSpringStereo`** — Spring
  - params: Decay, Predelay, LowCut, HighCut, Mix, Level
  - required fields: @trails
- **`HD2_ReverbTileStereo`** — Tile
  - params: Decay, Predelay, LowCut, HighCut, Mix, Level
  - required fields: @trails
- **`HD2_ReverbGlitzStereo`** — Glitz
  - params: Decay, Predelay, LowCut, HighCut, Mix, Level, Delay, Rate, Depth, Xover, Mod Mix, SyncSelect1, TempoSync1
  - required fields: @trails
- **`HD2_ReverbGanymedeStereo`** — Ganymede
  - params: Decay, Predelay, Tone, Modulation, Mix, Level
  - required fields: @trails
- **`HD2_ReverbSearchlightsStereo`** — Searchlights
  - params: Decay, Predelay, LowCut, HighCut, Mix, Level, Modulation, Speed, Intensity, Spread
  - required fields: @trails
- **`HD2_ReverbDoubleTankStereo`** — Double Tank
  - params: Decay, Predelay, Rate, Modulation, Mix, Level, LowCut, HighCut
  - required fields: @trails
- **`HD2_ReverbPlateauxStereo`** — Plateaux
  - params: Decay, Predelay, Tone, Modulation, Mix, Level, Pitch1, Cents1, Pitch2, Cents2, PitchMix
  - required fields: @trails
- **`HD2_ReverbHxSpringStereo`** — Hot Springs
  - params: Dwell, Spring Count, Drip, LowCut, HighCut, Mix, Level
  - required fields: @trails

### eq

- **`HD2_EQGraphic10BandStereo`** — 10 Band Graphic
  - params: 31p25Hz, 62p5Hz, 125Hz, 250Hz, 500Hz, 1kHz, 2kHz, 4kHz, 8kHz, 16kHz, Level
- **`HD2_EQLowCutHighCutStereo`** — Low and High Cut
  - params: LowCut, HighCut, Level
- **`HD2_EQParametricStereo`** — Parametric
  - params: LowFreq, LowQ, LowGain, MidFreq, MidQ, MidGain, HighFreq, HighQ, HighGain, LowCut, HighCut, Level
- **`HD2_EQSimple3BandStereo`** — Simple EQ
  - params: LowGain, MidFreq, MidGain, HighGain, Level
- **`HD2_CaliQStereo`** — Cali Q Graphic
  - params: 80Hz, 240Hz, 750Hz, 2200Hz, 6600Hz, Level
- **`HD2_EQLowShelfHighShelfStereo`** — Low/High Shelf
  - params: LowGain, LowFreq, HighGain, HighFreq, Level
- **`HD2_EQSimpleTiltStereo`** — Simple Tilt
  - params: Tilt, CenterFreq, Level
- **`HD2_EQ_STATIC_Graphic10BandStereo`** — 10 Band Graphic
  - params: 31p25Hz, 62p5Hz, 125Hz, 250Hz, 500Hz, 1kHz, 2kHz, 4kHz, 8kHz, 16kHz, Level
- **`HD2_EQ_STATIC_LowCutHighCutStereo`** — Low and High Cut
  - params: LowCut, HighCut, Level
- **`HD2_EQ_STATIC_ParametricStereo`** — Parametric
  - params: LowFreq, LowQ, LowGain, MidFreq, MidQ, MidGain, HighFreq, HighQ, HighGain, LowCut, HighCut, Level
- **`HD2_EQ_STATIC_Simple3BandStereo`** — Simple EQ
  - params: LowGain, MidFreq, MidGain, HighGain, Level
- **`HD2_EQ_STATIC_CaliQStereo`** — Cali Q Graphic
  - params: 80Hz, 240Hz, 750Hz, 2200Hz, 6600Hz, Level
- **`HD2_EQ_STATIC_LowShelfHighShelfStereo`** — Low/High Shelf
  - params: LowGain, LowFreq, HighGain, HighFreq, Level
- **`HD2_EQ_STATIC_SimpleTiltStereo`** — Simple Tilt
  - params: Tilt, CenterFreq, Level

### pitch

- **`HD2_PitchPitchWhamMono`** — Pitch Wham
  - params: Pedal, Heel, Toe, Mix, Level
- **`HD2_PitchTwinHarmonyMono`** — Twin Harmony
  - params: KeyVoice1, ScaleVoice1, IntervalVoice1, LevelVoice1, Mix, Level, KeyVoice2, ScaleVoice2, IntervalVoice2, LevelVoice2
- **`HD2_PitchSimplePitchMono`** — Simple Pitch
  - params: Interval1, Cents1, Time1, LevelVoice1, Mix, Level
- **`HD2_PitchDualPitchMono`** — Dual Pitch
  - params: Interval1, Cents1, Time1, LevelVoice1, Interval2, Cents2, Time2, LevelVoice2, Mix, Level
- **`HD2_Synth4OSCGeneratorMono`** — 4 OSC Generator
  - params: Osc1Shape, Osc1Freq, Osc1Level, Osc2Shape, Osc2Freq, Osc2Level, Osc3Shape, Osc3Freq, Osc3Level, Osc4Shape, Osc4Freq, Osc4Level, Attack, Decay, DryLevel, Level, RiseTimeSwitch
- **`HD2_Synth3NoteGeneratorMono`** — 3 Note Generator
  - params: Osc1Shape, Osc1Octave, Osc1Note, Osc1Level, Osc1Glide, Osc2Shape, Osc2Octave, Osc2Note, Osc2Level, Osc2Glide, Osc3Shape, Osc3Octave, Osc3Note, Osc3Level, Osc3Glide, Attack, Decay, DryLevel, Level, RiseTimeSwitch
- **`HD2_DM4BassOctaver`** — Bass Octaver
  - params: Tone, Normal, Octave, Level
- **`HD2_FM4AttackSynth`** — Attack Synth
  - params: Freq, Wave, Attack, Pitch, Mix, Level
- **`HD2_FM4Growler`** — Growler
  - params: Speed, Freq, Q, Pitch, Mix, Level, SyncSelect1, TempoSync1
- **`HD2_FM4OctiSynth`** — Octi Synth
  - params: Speed, Freq, Q, Depth, Mix, Level, SyncSelect1, TempoSync1
- **`HD2_FM4SynthOMatic`** — Synth O Matic
  - params: Frequency, Q, Wave, Pitch, Mix, Level
- **`HD2_FM4SynthString`** — Synth String
  - params: Speed, Freq, Attack, Pitch, Mix, Level, SyncSelect1, TempoSync1
- **`HD2_M13TwoVoiceHarmony`** — Smart Harmony
  - params: Key, Shift, Scale, Mix, Level

### dynamics

- **`HD2_CompressorDeluxeCompMono`** — Deluxe Comp
  - params: Threshold, Ratio, Attack, Release, Mix, Level, Knee
- **`HD2_CompressorLAStudioCompMono`** — LA Studio Comp
  - params: PeakReduction, Gain, Type, Emphasis, Mix, Level
- **`HD2_CompressorRedSqueezeMono`** — Red Squeeze
  - params: Sensitivity, Mix, Level
- **`HD2_CompressorAutoSwellMono`** — Autoswell
  - params: Threshold, Rel Offset, Attack, Decay, Taper, Level
- **`HD2_Compressor3BandCompMono`** — 3-Band Comp
  - params: Ratio, Attack, Release, Lo X Freq, Hi X Freq, Level, Lo Thresh, Lo Gain, Mid Thresh, Mid Gain, Hi Thresh, Hi Gain
- **`HD2_DM4BlueComp`** — Blue Comp
  - params: Sustain, Level
- **`HD2_DM4BlueCompTreb`** — Blue Comp Treb
  - params: Sustain, Level
- **`HD2_DM4BoostComp`** — Boost Comp
  - params: Drive, Bass, Comp, Treble, Output, Level
- **`HD2_DM4RedComp`** — Red Comp
  - params: Sustain, Level
- **`HD2_DM4TubeComp`** — Tube Comp
  - params: Thresh, Level
- **`HD2_DM4VettaComp`** — Vetta Comp
  - params: Sens, Level
- **`HD2_DM4VettaJuice`** — Vetta Juice
  - params: Amount, Level
- **`HD2_CompressorKinkyCompMono`** — Kinky Comp
  - params: Sensitivity, Mix, Attack, Release, Level
- **`HD2_CompressorRochesterCompMono`** — Rochester Comp
  - params: Gain, Threshold, Ratio, Attack, Release, Level, Knee, Mix
- **`HD2_GateHorizonGateMono`** — Horizon Gate
  - params: Mode, Sensitivity, Gate Range, Level
- **`HD2_CompressorOptoCompMono`** — Ampeg Opto Comp
  - params: Compression, Release, Blend, Level
- **`HD2_GateHardGateMono`** — Hard Gate
  - params: OpenThreshold, CloseThreshold, HoldTime, Decay, Level
- **`HD2_GateNoiseGateMono`** — Noise Gate
  - params: Threshold, Decay, Level

### filter

- **`HD2_FilterMutantFilterStereo`** — Mutant Filter
  - params: Mode, Peak, Gain, Range, Drive, Mix, Level
- **`HD2_FilterMysterFilterStereo`** — Mystery Filter
  - params: Sensitivity, Frequency, Resonance, Attack, Release, Mix, Level
- **`HD2_FilterAutoFilterStereo`** — Auto Filter
  - params: Mode, FilterGain, FilterQ, Sens, Attack, Decay, Frequency, FreqDepth, Direction, Mix, Level
- **`HD2_FM4CometTrails`** — Comet Trails
  - params: Speed, Freq, Q, Gain, Mix, Level, SyncSelect1, TempoSync1
- **`HD2_FM4ObiWah`** — Obi Wah
  - params: Speed, Freq, Q, Type, Mix, Level, SyncSelect1, TempoSync1
- **`HD2_FM4QFilter`** — Q Filter
  - params: Freq, Q, Gain, Type, Mix, Level
- **`HD2_FM4Seeker`** — Seeker
  - params: Speed, Freq, Q, Steps, Mix, Level, SyncSelect1, TempoSync1
- **`HD2_FM4SlowFilter`** — Slow Filter
  - params: Freq, Q, Speed, Mode, Mix, Level
- **`HD2_FM4SpinCycle`** — Spin Cycle
  - params: Speed, Freq, Q, Vol Sens, Mix, Level, SyncSelect1, TempoSync1
- **`HD2_FM4Throbber`** — Throbber
  - params: Speed, Freq, Q, Wave, Mix, Level, SyncSelect1, TempoSync1
- **`HD2_FM4TronDown`** — Tron Down
  - params: Freq, Q, Range, Type, Mix, Level
- **`HD2_FM4TronUp`** — Tron Up
  - params: Freq, Q, Range, Type, Mix, Level
- **`HD2_FM4VoiceBox`** — Voice Box
  - params: Speed, Start, End, Auto, Mix, Level, SyncSelect1, TempoSync1
- **`HD2_FM4VTron`** — V Tron
  - params: Speed, Start, End, Mode, Mix, Level
- **`HD2_FilterAshevillePattrnStereo`** — Asheville Pattrn
  - params: Rate, Pattern, Envelope, Voice, Mix, Output, Drive, Direction, LFO, Spread, Level1, Level2, Level3, Level4, Level5, Level6, Level7, Level8, SyncSelect1, TempoSync1, SyncSelect2, TempoSync2

### utility

- **`HD2_WahChromeCustomStereo`** — Chrome Custom
  - params: Pedal, FcLow, FcHigh, Mix, Level
- **`HD2_WahChromeStereo`** — Chrome
  - params: Pedal, FcLow, FcHigh, Mix, Level
- **`HD2_WahColorfulStereo`** — Colorful
  - params: Pedal, FcLow, FcHigh, Mix, Level
- **`HD2_WahConductorStereo`** — Conductor
  - params: Pedal, FcLow, FcHigh, Mix, Level
- **`HD2_WahFasselStereo`** — Fassel
  - params: Pedal, FcLow, FcHigh, Mix, Level
- **`HD2_WahTeardrop310Stereo`** — Teardrop 310
  - params: Pedal, Mix, Level
- **`HD2_WahThroatyStereo`** — Throaty
  - params: Pedal, FcLow, FcHigh, Mix, Level
- **`HD2_WahUKWah846Stereo`** — UK Wah 846
  - params: Pedal, Mix, Level
- **`HD2_WahVettaWahStereo`** — Vetta Wah
  - params: Pedal, FcLow, FcHigh, Mix, Level
- **`HD2_WahWeeperStereo`** — Weeper
  - params: Pedal, FcLow, FcHigh, Mix, Level
- **`HD2_WahTeardropBassQStereo`** — Teardrop Bass Q
  - params: Pedal, Q Trim, Volume Trim, Mix, Level
- **`HD2_VolPanGainStereo`** — Gain
  - params: Gain
- **`HD2_VolPanVolStereo`** — Volume
  - params: Pedal, VolumeTaper
- **`HD2_VolPanPanStereo`** — Pan
  - params: Pedal
- **`HD2_VolPanStereoWidthStereo`** — Stereo Width
  - params: Width, LR In Swap, Balance, Level, R Polarity
- **`HD2_FXLoopMono1`** — FX Loop 1
  - params: Send, Return, Mix
  - required fields: @trails
- **`HD2_FXLoopStereo1_2`** — FX Loop 1/2
  - params: Send, Return, Mix
  - required fields: @trails

## Tone spec schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://github.com/SeannyQuest/tonemaker/tone-spec.schema.json",
  "title": "POD Go Tone Spec",
  "description": "Declarative description of a POD Go preset that `tonemaker build` turns into an importable .pgp. Emitted by an LLM from the knowledge pack.",
  "type": "object",
  "required": ["name", "blocks"],
  "additionalProperties": false,
  "properties": {
    "name": {
      "type": "string",
      "description": "Preset display name.",
      "minLength": 1,
      "maxLength": 32
    },
    "blocks": {
      "type": "array",
      "description": "Signal chain. Up to 10 blocks; positions must be contiguous from 0.",
      "minItems": 1,
      "maxItems": 10,
      "items": {
        "type": "object",
        "required": ["model", "position"],
        "additionalProperties": false,
        "properties": {
          "model": {
            "type": "string",
            "description": "Exact POD Go @model id from the library (e.g. HD2_AmpCaliRectifire). Validated against models.json.",
            "pattern": "^HD2_[A-Za-z0-9_]+$"
          },
          "position": {
            "type": "integer",
            "description": "Chain order 0..9; block-key index equals position.",
            "minimum": 0,
            "maximum": 9
          },
          "enabled": {
            "type": "boolean",
            "description": "On/off in dsp0. Default true.",
            "default": true
          },
          "params": {
            "type": "object",
            "description": "Parameter values for this model. Keys must be among the model's known params; amp/drive/mix knobs are 0.0-1.0, freq/cut in Hz, gain/level in dB.",
            "additionalProperties": {
              "type": ["number", "boolean", "integer"]
            }
          }
        }
      }
    },
    "input": {
      "type": "object",
      "description": "Noise gate overrides (dsp0.input).",
      "additionalProperties": false,
      "properties": {
        "noiseGate": { "type": "boolean" },
        "threshold": { "type": "number", "description": "dB, e.g. -56" },
        "decay": { "type": "number", "minimum": 0, "maximum": 1 }
      }
    },
    "output": {
      "type": "object",
      "description": "Master output overrides (dsp0.output).",
      "additionalProperties": false,
      "properties": {
        "pan": { "type": "number", "minimum": 0, "maximum": 1, "description": "0.5 = center" },
        "gain": { "type": "number", "description": "dB" }
      }
    },
    "snapshots": {
      "type": "array",
      "description": "Up to 4 snapshots. Each overrides per-block bypass and snapshot-controlled params (wired via controller 11).",
      "maxItems": 4,
      "items": {
        "type": "object",
        "required": ["name"],
        "additionalProperties": false,
        "properties": {
          "name": { "type": "string", "maxLength": 16 },
          "bypass": {
            "type": "object",
            "description": "blockKey -> on/off for this snapshot.",
            "patternProperties": {
              "^block[0-9]$": { "type": "boolean" }
            },
            "additionalProperties": false
          },
          "params": {
            "type": "object",
            "description": "blockKey -> {param: value} held for this snapshot.",
            "patternProperties": {
              "^block[0-9]$": {
                "type": "object",
                "additionalProperties": { "type": ["number", "boolean", "integer"] }
              }
            },
            "additionalProperties": false
          }
        }
      }
    }
  }
}
```

## Worked example

Request: *"A doomy, downtuned tone — heavy fuzz into a mid-scooped Recto, big cave reverb."*

A valid tone spec:

```json
{
  "name": "Doom Cave",
  "blocks": [
    {"model": "HD2_VolPanVolStereo", "position": 0},
    {"model": "HD2_DistTriangleFuzzMono", "position": 1, "params": {"Sustain": 0.6, "Tone": 0.45, "Level": 0.7}},
    {"model": "HD2_AmpCaliRectifire", "position": 2, "params": {"Drive": 0.55, "Bass": 0.6, "Mid": 0.3, "Treble": 0.55, "Presence": 0.4, "Master": 0.5, "ChVol": 0.85}},
    {"model": "HD2_CabMicIr_4x12CaliV30", "position": 3, "params": {"LowCut": 85, "HighCut": 7000, "Level": 0}},
    {"model": "HD2_EQ_STATIC_ParametricStereo", "position": 4, "params": {"MidFreq": 500, "MidGain": -3, "Level": 0}},
    {"model": "HD2_ReverbGanymedeStereo", "position": 7, "params": {"Mix": 0.4, "Decay": 0.8, "Level": 0}}
  ],
  "input": {"noiseGate": true, "threshold": -58, "decay": 0.3},
  "output": {"gain": 6},
  "snapshots": [
    {"name": "Rhythm", "bypass": {"block1": false}, "params": {"block2": {"Drive": 0.55}, "block7": {"Mix": 0.2}}},
    {"name": "Lead",   "bypass": {"block1": true},  "params": {"block2": {"Drive": 0.7},  "block7": {"Mix": 0.5}}}
  ]
}
```

Then: `tonemaker build doom.json --out doom.pgp && tonemaker validate doom.pgp`, and import
`doom.pgp` into POD Go Edit.

## CLI vocabulary
- `tonemaker inspect <file>` — print the chain + params (add `--json` for structured output)
- `tonemaker set <file> block2.Drive=0.62 output.gain=8 [--out <file>]` — edit params (validates first)
- `tonemaker add <file> block1=HD2_DistScream808Mono [--out <file>]` — add/replace a block
- `tonemaker build <spec.json> [--out <file>]` — build a full preset from a tone spec (validates first)
- `tonemaker new [--template metal-4snapshot] [--out <file>]` — start from blank/template
- `tonemaker validate <file>` — confirm it will import (run this before importing)
- `tonemaker models [--category amp]` — list available model ids
