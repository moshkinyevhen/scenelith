# MOSAIC architecture

Status: mixture of **ACCEPTED**, **NORMATIVE-DRAFT** and **HYPOTHESIS**.
Regulatory language is specified in `../spec/SCENELITH-0.md`.

## 1. General model

MOSAIC is a limited visual scene machine. Encoder compiles video to:

1. snapshots and deltas `WorldState`;
2. continuous or piecewise continuous `Trajectories`;
3. checked `TruthInnovation`;
4. optional `PerceptualDetail`.

The decoder performs a small fixed set of integer render/tensor
operations. Complex depth, segmentation, tracking, re-identification and global
optimizations are encoder-only.

**ACCEPTED - D-025:** MOSAIC uses
**CBF - Causal Basis Field visual ISA**. Long term formula does not mean
heavy world model. One unified primitive - long-lived `MOSAIC Cell` -
combines immutable Basis, invisible tiled Support, arbitrary soft Gate,
absolute coordinate/appearance laws, Lifetime and Truth contribution. Frame
is a read-only presentation sample. 2.5D, tensor renderer and
semantic scene graph are not included in Main.

## 2. WorldState

### 2.1 State composition

Main v0:

- bounded table `MOSAIC Cells`;
- bounded coordinate-independent `Content Bank`;
- fixed microtile Support;
- bounded absolute `STATIC`, `LINEAR_TRANSLATION` and profile-gated
  affine/projective coordinate laws;
- arbitrary-lifetime state events;
- compatibility PRESENT and objective fallback;
- integrity metadata;
- full state reset in RAP.

Research after positive cell gate:

- fine persistent masks and partial content updates;
- canonical surface atlas;
- 2.5D/depth/visibility;
- feature planes/latent tokens;
- surfels/Gaussian splats;
- semantic object/surface identifiers;
- state snapshots and partial repair.

**NORMATIVE-DRAFT:** An unobserved fragment does not receive Content at all.
Main-0 does not represent the "unknown part of the object"; Support only lists
certain microtiles. Undefined output must receive an objective fallback.

### 2.2 Limitations

**TARGET:**

- persistent state: no more than 64 MB for 4K profile;
- strictly limited number of recent frames;
- no external state/model files;
- full state reset at random-access point.

The limits must be set level/profile so that the hardware decoder can advance
allocate SRAM/DRAM.

### 2.3 State change

Only verified mutation `EventBlock` can use State Events.
Read-only presentation/quality blocks use already confirmed state
and can be decoded in parallel or discarded.

Order of mutation:

1. Check EventBlock/payload integrity.
2. Restore Truth Core.
3. Check the state hash.
4. Apply the confirmed `MemoryDelta`.
5. Calculate the new state hash.
6. Only after this allow dependent EventBlocks/Presentation Queries.

Damaged or concealment-generated material is not applied to state.

## 3. Representation primitives

Encoder selects one or a combination of modes per tile/region/chunk.

### 3.1 Structural modes

Main v0:

- active MOSAIC Cell with static/linear absolute mapping;
- compact Content capture from confirmed Truth;
- recent-frame fallback, if it was left by the experimental profile;
- state-independent replacement.

Research extensions:

- mask;
- mesh/deformation;
- depth/visibility;
- surfel/Gaussian splat;
- screen/vector/text primitive.

### 3.2 Innovation modes

- integer 5/3 wavelet base;
- transform/residual fallback;
- optional exact/lossless residual.

Research after core gate:

- shallow learned latent transform;
- progressive objective refinement.

### 3.3 Continuous-Time MOSAIC Cells

Main-0 has three semantic records:

- `STATE_RESET`;
- `CELL_SET`: atomically create/modify/end cell;
- `PRESENT`: read-only sample state in timestamp.

`CELL_SET` combines Content, Support, MotionLaw, Lifetime, Order and Mode.
The absence of an event means implicit persistence; separate per-frame HOLD not
encoded. `CAPTURE_TRUTH` saves already restored objective samples without
re-texture. Full semantics:
[14_CONTINUOUS_TIME_CELLS.md](14_CONTINUOUS_TIME_CELLS.md).

DPM remains a separate spatial-memory baseline:
[13_MINIMAL_PATCH_CORE.md](13_MINIMAL_PATCH_CORE.md).

### 3.4 Representation routing

The encoder solution is evaluated based on its full functionality:

\[
J=R+\lambda D+\mu C_{decode}+\nu B_{memory}
  + \rho L_{seek}+\sigma Risk_{loss}
\]

where all address, mask, model, adapter, checkpoint and side-information are taken into account
bits.

### 3.5 Bounded affine-pair composition

CBF Cell synthesizes the pair \((g,c)\). Pair composition is associative:

\[
(g_2,c_2)\circ(g_1,c_1)=(g_2g_1,\ g_2c_1+c_2).
\]

Decoder MAY perform order-preserving tree reduction in wide integer
accumulator and clip only on fixed layer boundary. Main target limits
entire active overlap by four non-identity contributions/output pixel, four
composition layers, eight texture samples and approximately 128 simple integers
operations/pixel. The exact values ​​are determined by level.

Full fixation:
[16_CBF_ACCEPTANCE_AND_FINAL_RED_TEAM.md](16_CBF_ACCEPTANCE_AND_FINAL_RED_TEAM.md).

## 4. Chunk-native temporal model - after cell gates

**RESEARCH:** Main-0 already has bounded static/linear MotionLaw, but does not require
multi-frame latent, deformable trajectories or temporal tensor graph.
The following subsections describe a possible next step.

### 4.1 Chunk**NORMATIVE-DRAFT:** main multi-frame chunk contains 8–16 display frames
in the Main RA profile. The specific range is not frozen yet.

Chunk uses:

- general spatiotemporal latent;
- fully computable to entropy decoding hyperprior;
- parallel recovery of read-only frames;
- separately designated spine output/state update.

### 4.2 Low-delay

For Live/LB the causal variant is used:

- frames arrive in display order;
- lookahead is missing where configuration is prohibited;
- state update is limited to frames already received;
- decoder output reordering is not required.

### 4.3 Time-continuous trajectories

For coherent motion, Main-0 transmits rare absolute linear knots instead
per-frame vectors. Possible extensions:

- camera/global motion;
- rigid object motion;
- deformable mesh/surface motion;
- lighting/exposure trajectory.

Decoder interpolates them with a normative integer function. For areas where
trajectory representation is more expensive than residual, encoder chooses fallback.

## 5. Two quality contracts

### 5.1 Fidelity/Truth Core

**ACCEPTED:**

- deterministic and bit-exact;
- the only source reference/state;
- preserves structure, text, faces and measurable details as much as possible
  this provides the selected rate;
- supports objective enhancement;
- decoded without Perceptual Shell.

### 5.2 Optional Perceptual Detail

**RESEARCH / NORMATIVE-DRAFT:**

- one-step distilled diffusion or rectified-flow renderer;
- display-only;
- seeded deterministically within a specific model-set;
- does not affect base entropy contexts;
- accompanied by a provenance/uncertainty mask;
- disabled in evidence, medical, scientific and archive profiles.

Perceptual gain is measured by blind MOS and specialized identity/OCR/
flicker gates, separate from PSNR/MS-SSIM fidelity.

## 6. Decoder ISA

Main v0:

- exact microtile copy;
- bounded support-list traversal;
- absolute fixed-point linear translation;
- deterministic opaque composition;
- fixed-width residual add/clamp;
- integer transform/lifting fallback;
- normative in-loop filter;
- multi-lane rANS;
- STATE_RESET, CELL_SET and PRESENT.

Research after cell gate:

- INT8/INT4 tensor operators;
- integer bilinear/affine warp;
- mesh deformation;
- splat/blend;
- pixel shuffle;
- finite scalar/lattice/vector quantization.

Prohibited in Main:

- arbitrary downloadable graph;
- device-dependent floating-point reference loop;
- full-resolution attention;
- softmax-dependent normative reconstruction;
- dynamic unlimited cycles;
- mandatory multi-step diffusion decoder;- full-resolution autoregressive entropy.

## 7. Entropy and quantization

### Main v0

- scalar quantization;
- independent/interleaved rANS lanes;
- chunk/tile directory with exact offsets;
- CDFs available before the start of the corresponding entropy decode.

### Research only

- lattice/progressive VQ;
- non-autoregressive learned hyperprior;
- relative-entropy coding;
- bits-back;
- reverse-channel coding;
- shared-prior sample indices.

These methods are only allowed for restartable low-KL microblocks/adapters,
limited worst-case complexity has not yet been proven.

## 8. Loss-native resilience

- Independent tile/chunk entropy streams.
- CRC or stronger integrity check for state/base.
- Unequal FEC: state and Truth Base are protected more strongly than enhancement.
- complete Cell/Content state reset in each Main v0 RAP.
- Concealment never becomes reference.

Research:

- State snapshot/delta checkpoints.
- Erasure-trained concealment.
- Partial repair access unit.

**TARGET:** recovery from state desynchronization no more than 250 ms per
Live profile.

## 9. Hardware mapping

Suggested hardware blocks:

- multi-lane RANS engine;
- exact-copy/translation compositor;
- bounded SRAM cell table and DRAM Content Bank;
- support/dirty-tile scheduler;
- optional display/overlay trajectory handoff;
- wavelet/lifting block;
- residual compositor;
- integrity/reset engine.

Research extensions MAY reuse texture/warp, tensor and splat hardware only
after the measured marginal gain.

The main restrictions are designed on MAC/pixel, state memory and off-chip
traffic, and not just by the number of syntactic tools.

## 10. Scalability

One stream should eventually allow:

- temporal scalability;
- spatial scalability;
- quality scalability;
- compute scalability;
- ROI/tile decode;
- disabling Perceptual Shell;
- discardable enhancement;
- different resolution/FPS outputs from the same truth state without declaration
  synthesized novel view with a reliable source.
