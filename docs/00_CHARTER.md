# SceneLith Project Charter

Status: **ACCEPTED**
Initial approval date: 2026-07-26

## Mission

Create a new open video encoding format in which the main unit
compression is not a rectangular block of a single frame, but a limited
the dynamic state of the visual scene and the flow of new information about it.

SceneLith should:

1. Give a qualitatively new increase in compression, and not a single-digit percentage
   H.266/VVC or AV2 enhancement.
2. Have a deterministic, secure and hardware-implemented decoder.
3. Run efficiently on modern GPUs and have a direct path to ASIC.
4. Support household real-time encoder and do not depend solely on
   cloud supercomputer.
5. Allow extremely heavy offline encoder to extract maximum
   quality from the same standard bitstream.
6. Clearly separate reliable reconstruction from synthesized parts.
7. Have an open decoder/bitstream and a long-term competitive lead in
   non-standard encoder compiler.

## Titles

- Standalone video codec, bitstream family and project: **SceneLith**.
- Architecture:
  **MOSAIC - Memory-Oriented Scalable Asymmetric Integer Codec**.
- First normative draft name: **SceneLith-0**.
- Marketing wording:
  **“SceneLith Video – powered by MOSAIC.”**

FourCC, MIME type and container extension are not yet approved.

## Main formula

\[
Video(t)=Render(WorldState_t,\ Trajectories_t)
       + TruthInnovation_t
       + OptionalPerceptualDetail_t
\]

The meaning of the formula:

- `WorldState` stores limited deterministic knowledge of the decoder about the scene;
- `Trajectories` describes the movement of the camera, objects and deformations;
- `TruthInnovation` transmits new verifiable information and corrects errors
  scene models;
- `OptionalPerceptualDetail` synthesizes only optional visuals
  details and never affects further prediction.

## New time object

**NORMATIVE-DRAFT / HYPOTHESIS:** frame is not a unit of state, reference
or motion. SceneLith describes long-lived `MOSAIC Cells` and asynchronous events,
and the output frame is only compatible with `PresentationQuery(t)`.

The statics are preserved without repeated commands. The movement is set absolute
fixed-point law for the interval. Display sampling has its own clock and is not
causes bitstream to repeat unchanged state. Full model:
[14_CONTINUOUS_TIME_CELLS.md](14_CONTINUOUS_TIME_CELLS.md).

## Criterion of revolutionaryness

**TARGET:** the new standard is justified if independently configured
in tests it shows at least 25% universal advantage **standalone**
against AV2 v1.0/AVM and VVC/H.266/VTM. Stretch North Star - 40% against morethe stronger of the two anchors and 50% on the broad screen/UI corpus, no mixing
Fidelity and Perceptual claims.

An improvement of 5–10% by itself is not enough to create a new standard.

## Strategy of openness and separation

> Open and simple decoder; extremely strong, constantly improving
>encoder.

An open standard cannot be made inaccessible to competitors. The goal is to provide
3–5 year practical lead due to:

- world extraction and representation routing;
- accumulated RDO solutions;
- corpus and subjective data;
- per-title adaptation;
- GPU/ASIC kernels;
- conformance and fuzzing ecosystem;
- narrow and standard-friendly IP strategy.

## Public engineering result

**TARGET:** Regardless of the outcome of standardization, the repository and proposal must
become a verifiable professional portfolio owner and a team assembly point.
This requires not only ambitious claims, but:

- public specification and decision log;
- reproducible benchmark harness;
- bit-exact reference decoder and conformance vectors;
- honest positive/negative RD results;
- architecture paper/demo;
- transparent history of authorship and contributions;
- contribution guide, roadmap and limited first tasks.

Submitting a proposal does not in itself guarantee a career impact or a team.
Value comes from proven system performance, reproducibility and
correct distinction between `submitted`, `evaluated` and `adopted`.

## Current deadline mission

**ACCEPTED:** prepare a full unrestricted improved-compression response for
JVET CfP beyond VVC by October 26, 2026.

For this purpose, a narrow experimental branch `SceneLith-CfP-2026` is being created.
It does not need to contain all future MOSAIC features, but it should be
This is a self-contained codec proposal.

## What is not considered success

- beautiful demonstrations without taking into account the full bitrate;
- comparison only with the outdated AV1;
- perceptual gain, given as fidelity;
- external hidden decoder weights;
- results on training or manually adjusted test scenes;
- codec suitable only for unlimited cloud encoder;
- acceleration due to non-matching GOP, latency, random access or color format.