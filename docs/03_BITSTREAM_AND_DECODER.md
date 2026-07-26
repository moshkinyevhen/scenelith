# Draft bitstream and decoder structure

Status: **NORMATIVE-DRAFT**
Bit-level syntax is not frozen yet.

## 1. Hierarchy

Suggested structure:

1.`SequenceHeader`
2. `MemoryAccessPoint`
3.`SceneEpoch`
4.`EventBlock`
5. `PayloadTile`
6. optional `ModelSet` extension
7. `EndOfSequence`

## 2.SequenceHeader

Minimum fields:

- magic and bitstream version;
- profile/level;
- coded/display dimensions;
- chroma format, bit depth and nominal color space;
- integer timebase and scene duration;
- optional compatibility presentation schedule;
- color primaries, transfer and matrix;
- maximum state bytes;
- maximum cells, content bytes and support entries;
- maximum State Events and moving cells;
- maximum model bytes, if extension is enabled;
- maximum MAC/output-pixel class;
- enabled tool flags;
- integrity mode;
- model-set identifier/hash.

All data needed for decoding is in stream or in
a normatively defined baseline decoder. External parameter files are prohibited.

## 3. ModelSet - optional extension

Main-0 does not require a learned ModelSet. If extension is enabled:

- fixed normative operator graph;
- baseline weights or transmitted self-contained quantized weights within
  profile;
- cryptographic/content hash;
- explicit compatible version identifier.

Arbitrary executable code or dynamic graph is prohibited.

## 4. MemoryAccessPoint

`MemoryAccessPoint` provides random access:

- clears or completely replaces the previous state;
- contains self-contained active MOSAIC Cells/Content or full-screen
  objective fallback;
- does not refer to packets to the access point;
- ends with checking the restored state hash.

The CfP branch must comply with the RAP cadence of the corresponding anchor.

## 5. SceneEpoch

Epoch limits the lifetime state and contains:

- epoch identifier;
- cell/content namespace;
- memory budget;
- deterministic eviction policy;
- optional scene-level adapter;
- initial state hash.

Any adapter is fully taken into account in the bitrate.

## 6. EventBlock

`EventBlock` has:

- timestamp interval;
- exact record count and offsets independent entropy lanes;
- ordered `STATE_RESET`, `CELL_SET` and `PRESENT` records;
- inline/captured content directories;
- `TRUTH_INNOVATION`;
- optional `PERCEPTUAL_DETAIL`;
- integrity check and post-state hash, if the block changes state.

`PERCEPTUAL_DETAIL` is always optional and is not included in the reference path.

State events inside the checked block are applied in coded order. PRESENT
reads all earlier events with the same timestamp and does not see later ones.

## 7. PayloadTile

Payload tile has:- fixed geometry, pre-128×128 or 256×256;
- halo policy;
- content/innovation mode;
- offsets of independent entropy lanes;
- integrity check;
- cell/support ownership metadata;
- optional ROI priority.

Support is a bounded union of allowed dyadic microtiles. Recursive
unlimited quadtree partitioning is not a basic MOSAIC model.

## 8. Decoder state machine

High level order:

1. Parse and check `SequenceHeader`.
2. Initialize profile limits.
3. Load/check optional `ModelSet`, if it is allowed by profile.
4. On `MemoryAccessPoint`, clean and self-contained restore `WorldState`.
5. For each EventBlock:
   1. check directory/integrity and resource bounds;
   2. get entropy parameters and decode lanes;
   3. apply `STATE_RESET/CELL_SET` atomically in coded order;
   4. on `PRESENT(t)` calculate absolute MotionLaw active cells;
   5. perform deterministic composition;
   6. add Truth Innovation and objective fallback;
   7. generate post-filter Truth output;
   8. save it only as a valid future `CAPTURE_TRUTH` source;
   9. separately apply the optional Perceptual Detail;
   10. issue output without changing the state of PRESENT itself.
6. In case of an error, do not use unconfirmed State Events.

## 9. Bit-exact arithmetic

It is necessary to define:

- signed/unsigned widths;
- rounding direction;
- saturation;
- overflow behavior;
- accumulator width;
- interpolation coefficients;
- LUT values;
- rANS normalization;
- PRNG and seed for optional stochastic tools.

Floating point should not participate in Main reference reconstruction.

## 10. Parallelism

- Several independent rANS lanes.
- Tile directory is known before payload decode.
- Read-only presentation tiles can be executed in parallel.
- Only ordered State Event commit requires serialization.
- Cross-tile dependencies are limited by the normative halo.

## 11. Profiles

Preliminary:

- `Main-Fidelity` - event-retained state and universal deterministic
  reconstruction;
- `Live` — causal/low-delay, bounded state, loss repair;
- `Perceptual` — Main-Fidelity plus non-reference shell;
- `VOD-Adaptive` — scene adapters/dictionaries with full regard to bits;
- `Screen` — text/vector/sprite and optional exact refinement.
- `Continuous-Output` — host queries arbitrary timestamps; unconfirmed
  source timestamps are explicitly marked interpolated.

CfP-2026 uses a separate minimum subset described in
`05_JVET_CFP_2026.md`.

## 12. Open questions

- Standard tile size.
- Maximum duration/events per EventBlock.- Separation of State, Motion, Innovation and Presentation clocks.
- Binary syntax `STATE_RESET/CELL_SET/PRESENT`.
- Microtile Support coding.
- Continuous-output API and container presentation mapping.
- Baseline weights in binary or bitstream.
- Model-set update model after hardware release.
- Accurate lattice/FSQ circuit.
- Depth/visibility format after Main-0 gate.
- Acceptable types of splat.
- Lossless enhancement structure.
- Conformance tolerance: strictly bit-exact or separate bounded-error profile.