# Feature Specification: POD Go Tone Builder

**Feature Branch**: `001-podgo-tone-builder`

**Created**: 2026-07-04

**Status**: Draft

**Input**: User description: "LLM-drivable POD Go .pgp preset editor and tone builder distributed as a
pip package with a comprehensive verified model library and a machine-readable knowledge pack"

## Overview

POD Go Edit (Line 6's official editor) has no scripting interface, but its preset files (`.pgp`) are
editable data. This feature packages a tool that lets anyone read, edit, build, and validate POD Go
presets from the command line — and, crucially, lets them design tones by describing them in plain
language to **their own** LLM (Claude, ChatGPT, a local model — the user's choice). The tool ships a
machine-readable knowledge pack the user hands to their LLM; the LLM emits editing commands or a tone
spec; the tool applies them and guarantees the result will import into POD Go without error.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Design a tone with any LLM (Priority: P1)

A guitarist wants a specific sound ("doomy, downtuned, fuzzy, big reverb") but doesn't know POD Go's
internal model names or parameter ranges. They obtain the tool's knowledge pack, paste it into
whatever LLM they already use, and describe the tone. The LLM replies with a ready-to-run set of tool
commands (or a tone spec). The guitarist runs them, gets a `.pgp` file, and imports it into POD Go
Edit — and it loads correctly on the first try.

**Why this priority**: This is the headline capability and the reason the project exists. It turns an
opaque, expert-only editor into something anyone can drive in natural language, without the project
having to build or pay for any AI itself.

**Independent Test**: Take the knowledge pack, give it plus a plain-language tone request to an LLM,
run the commands it returns, and confirm the produced preset passes validation and imports into POD
Go Edit with no "unrecognized models" error.

**Acceptance Scenarios**:

1. **Given** the knowledge pack and a plain-language tone description, **When** an LLM produces tool
   commands from them, **Then** running those commands yields a preset that passes validation.
2. **Given** an LLM that invents a plausible-but-wrong model name, **When** the resulting preset is
   validated, **Then** validation fails with a clear message naming the offending block — before the
   user ever tries to import it.
3. **Given** a produced preset, **When** it is imported into POD Go Edit, **Then** it loads with the
   intended signal chain and no error.

### User Story 2 - Inspect and edit an existing preset (Priority: P1)

A user has a `.pgp` (their own export or a built tone) and wants to see its full signal chain and
tweak parameters — raise the amp gain, lower a reverb mix, change the EQ — without opening the editor.

**Why this priority**: Inspection and parameter editing are the atomic operations everything else is
built on, and they deliver standalone value (fast, scriptable tweaks). Without this there is no tool.

**Independent Test**: Inspect a real export and confirm the reported chain matches POD Go Edit; change
a parameter, save, re-inspect, and confirm only that value changed and the file still imports.

**Acceptance Scenarios**:

1. **Given** a preset file, **When** the user inspects it, **Then** the tool lists every block in
   signal order with its model, on/off state, and parameters.
2. **Given** a preset file, **When** the user sets a parameter to a new value and saves, **Then** the
   file round-trips losslessly (nothing else changes) and still imports into POD Go.
3. **Given** a commercial DRM-protected preset, **When** the user tries to open it, **Then** the tool
   refuses with a clear message and makes no attempt to decrypt it.

### User Story 3 - Build a full preset from a tone spec (Priority: P2)

A user (or their LLM) wants a complete preset built from scratch — a chosen chain of blocks, with
several snapshots (e.g. Clean / Rhythm / Lead / Breakdown) that swap gain and effects — described as
a single structured spec rather than assembled by hand block-by-block.

**Why this priority**: This is what makes "describe a tone" produce a *finished, giggable* preset
instead of a bare chain. It depends on the editing core (US2) and is the natural target of US1's LLM
output. Higher effort, so P2.

**Independent Test**: Feed a tone spec describing blocks, parameters, and snapshots; build it; inspect
the result and confirm the chain, parameters, and per-snapshot behavior match the spec and it imports.

**Acceptance Scenarios**:

1. **Given** a tone spec, **When** the user builds it, **Then** the produced preset has the specified
   blocks in the specified order with the specified parameters.
2. **Given** a tone spec that defines multiple snapshots, **When** the preset is built and imported,
   **Then** switching snapshots on the device changes the sound as the spec described.
3. **Given** any build, **When** it completes, **Then** the output has passed validation before being
   written.

### User Story 4 - Start with a comprehensive model library, no calibration (Priority: P2)

A user wants to use any of POD Go's stock amps, cabs, and effects by name and trust that the tool
knows their exact internal identifier and parameters — without first having to export presets to
"teach" the tool each model.

**Why this priority**: The single biggest usability wall is that guessed model identifiers fail to
import. Shipping a comprehensive, verified library removes that wall for everyone. It's foundational
to US1 and US3 succeeding for real users, but is a data-gathering effort, so P2.

**Independent Test**: Ask the tool to list its known models and confirm the stock POD Go models are
present with correct identifiers and parameter keys; build a preset using several of them and confirm
it imports.

**Acceptance Scenarios**:

1. **Given** the installed tool, **When** the user lists available models, **Then** the stock POD Go
   models are available with verified identifiers and parameter keys.
2. **Given** a model in the library, **When** it is used in a built preset, **Then** the preset
   imports into POD Go with that block recognized.
3. **Given** a new model not yet in the library, **When** the user exports a preset containing it and
   runs the harvest step, **Then** the model is added to the library from that real export.

### User Story 5 - Install and get started in one step (Priority: P3)

A user wants to install the tool with a single standard command and immediately produce the knowledge
pack to hand to their LLM, without cloning a repo or configuring anything.

**Why this priority**: Frictionless install and a one-command "give me the knowledge pack" are what
make the tool shareable with strangers, but they layer on top of working functionality, so P3.

**Independent Test**: Install the published package in a clean environment, run the command that emits
the knowledge pack, and confirm a complete, self-contained knowledge pack is produced.

**Acceptance Scenarios**:

1. **Given** a clean environment, **When** the user installs the published package, **Then** a single
   command runs the tool.
2. **Given** the installed tool, **When** the user requests the knowledge pack, **Then** a complete,
   copy-pasteable knowledge pack is emitted (schema + full model library + rules + a worked example).

### Edge Cases

- A preset references a model the library does not know → validation fails and names the block; the
  tool never silently emits an unimportable file.
- A DRM/commercial preset (`hxmp` encryption) is opened → refused, no decryption attempted.
- A block is enabled in the chain but not in the active snapshot → validation flags the inconsistency
  (enabling a block requires enabling it in the snapshot too).
- Blocks are reordered → positions and per-snapshot bypass are rebuilt and stale control references
  cleared, so the reordered preset still imports.
- The knowledge pack and the model library disagree → must be impossible: the pack is generated from
  the library, so a stale pack is a build error, not a runtime surprise.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The tool MUST read a `.pgp` preset in both on-disk forms (uncompressed export and
  compressed/wrapped) and report its full signal chain in order with each block's model, on/off state,
  and parameters.
- **FR-002**: The tool MUST edit a parameter of any block (and of the input gate and master output)
  and save the preset without altering any data the edit did not intend to change (lossless round-trip).
- **FR-003**: The tool MUST detect DRM-protected presets and refuse to decode or edit them, making no
  attempt to bypass the protection.
- **FR-004**: The tool MUST validate a preset before treating it as final — confirming every model is
  known, required per-model fields are present, block order is consistent, and snapshot on/off state
  is consistent — and MUST report failures clearly, naming the offending block.
- **FR-005**: The tool MUST build a complete preset (including multiple snapshots) from a structured
  tone spec, handling block order, per-snapshot on/off, and snapshot-controlled parameters.
- **FR-006**: The tool MUST support adding, removing, reordering, and bypassing blocks such that the
  resulting preset still imports (positions and snapshot state kept consistent).
- **FR-007**: The tool MUST ship a comprehensive library of POD Go's stock models with verified
  identifiers and parameter keys, sourced only from real exports or authoritative device data.
- **FR-008**: The tool MUST let a user extend the library by harvesting model identifiers and
  parameters from their own exported presets.
- **FR-009**: The tool MUST emit a self-contained, machine-readable knowledge pack — the preset
  schema, the full model library, the editing rules and gotchas, the exact command vocabulary, and a
  worked example — suitable for pasting into any LLM.
- **FR-010**: The knowledge pack MUST be generated from the model library (single source of truth), so
  it can never describe models the tool does not actually support.
- **FR-011**: The tool MUST NOT require or embed any specific LLM provider, API key, or network call
  to an AI service.
- **FR-012**: The tool MUST be installable as a standard package and expose a single command-line
  entry point.

### Key Entities *(include if feature involves data)*

- **Preset**: a POD Go tone as data — metadata (name), a signal path of up to ten blocks, an input
  gate, a master output, and up to four snapshots.
- **Block**: one position in the signal chain — a model identifier, an on/off state, a type (amp, cab,
  effect, etc.), and a set of typed parameters. Six blocks are dedicated (Volume, Wah, Amp, Cab, EQ,
  FX Loop); up to four are user-assignable effects.
- **Snapshot**: a saved variation within a preset that overrides which blocks are on and the values of
  designated parameters, letting one preset hold several sounds.
- **Model library**: the verified catalog of POD Go models — each with its exact identifier, type, and
  parameter keys (and units/ranges where known).
- **Tone spec**: a structured description of a desired preset (blocks, parameters, snapshots) that the
  tool turns into a finished preset.
- **Knowledge pack**: the generated, self-contained reference a user gives their LLM so it can produce
  valid tone specs or commands.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A new user can go from installing the tool to a POD Go-importable preset produced with
  their own LLM in under 15 minutes, without prior knowledge of POD Go's internal model names.
- **SC-002**: 100% of presets the tool reports as valid import into POD Go Edit without an
  "unrecognized models" error.
- **SC-003**: Inspecting and editing a preset never corrupts it: a load-edit-save cycle changes only
  the intended values, verified across all reference exports.
- **SC-004**: The shipped library covers the stock POD Go models a typical user reaches for, such that
  common tone requests can be built entirely from library models with no manual calibration.
- **SC-005**: The knowledge pack and the model library never disagree — every model the pack describes
  is one the tool supports (guaranteed by generation).
- **SC-006**: A user can extend the library from one of their own exports in a single step and then
  build a preset using the newly added model.

## Assumptions

- Users operate on their own unencrypted POD Go exports; editing commercial/DRM packs is explicitly
  out of scope (and refused).
- Users have access to some LLM of their choosing; the project provides no AI and pays for none.
- The primary interface is a command-line tool (standard for this kind of developer/power-user
  utility); a graphical interface is out of scope for the first release.
- Building a truly exhaustive model library depends on obtaining source exports (factory setlist
  and/or authoritative device data); the library grows toward completeness and supports user
  contribution to fill gaps.
- POD Go's preset format and model identifiers are treated as an observed contract (from real
  exports), not a published spec, and may evolve with firmware.
