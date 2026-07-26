# North Star and architectural invariants

Status: **ACCEPTED**

## Main idea

SceneLith encodes not a sequence
independent images, and a program for changing a limited visual scene:

\[
\hat{V}_t=Render(S_t,\tau_t)+\Delta^{truth}_t+\Delta^{perceptual}_t
\]

where:

- \(S_t\) - `WorldState`;
- \(\tau_t\) — `Trajectories`;
- \(\Delta^{truth}_t\) - `TruthInnovation`;
- \(\Delta^{perceptual}_t\) — `OptionalPerceptualDetail`.

## Normative invariants

### N1. Limited condition

`WorldState` has normative memory limits, lifetime, page IDs,
eviction rules, hash checkpoints and full/delta checkpoints.

No unlimited accumulation of history.

### N2. Determinacy of truth

`Render(WorldState, Trajectories) + TruthInnovation` must be bit-exact for
all conforming decoder of one profile version.

### N3. The generative layer is not a reference

`OptionalPerceptualDetail`:

- does not change `WorldState`;
- not used for temporal prediction;
- does not affect the entropy context of the underlying thread;
- can be discarded without disrupting subsequent decoding;
- must have provenance/uncertainty marking.

### N4. Random access restores state

Each random-access point must contain everything necessary for
restoring a valid `WorldState` without access to previous packages.

### N5. Universal fallback

If atlas, geometry, latent memory or trajectory are ineffective, the encoder can
switch to independent objective innovation/residual mode. No class
content should not be required to use scene representation.

### N6. Decoder is limited, encoder is free

The standard defines bitstream and decoding process. Encoder can apply
arbitrarily heavy models and search, if it creates a conforming stream.

### N7. One stream - different encoder budgets

Live, Studio and Foundry use the same prescriptive syntax. Foundry does not have
the right to transmit an arbitrary decoder graph that is not in the Main profile.

### N8. GPU/ASIC-first

Main profile is built from fixed integer tensor/render operations,
parallel chunks/tiles and independent entropy lanes. Full screen
autoregression and arbitrary dynamic graphs are prohibited.

### N9. Presentation is not state mutation

**NORMATIVE-DRAFT:** the output request at time \(t\) reads `WorldState`, but itself
in itself does not change it. State, motion knots, Truth Innovation and presentation
sampling have independent clocks.

The static area remains valid without per-frame `HOLD`. Smooth
the movement is specified by absolute fixed-point law for the interval and is not calculated
recursive warp of previous output. Details:
[14_CONTINUOUS_TIME_CELLS.md](14_CONTINUOUS_TIME_CELLS.md).## Fundamental hypotheses

### H1. Bitrate follows new information

**HYPOTHESIS:** on a coherent scene the flow cost should be mostly
determined by scene changes and not by the work `width × height × FPS`.

### H2. Long-term reuse

**HYPOTHESIS:** reappearance of a surface after occlusion or camera exit
can be encoded with a reference to a saved state, cheaper than repeating
pixel-domain intra/inter coding.

### H3. Temporal continuity

**HYPOTHESIS:** spline/trajectory description allows you to increase the frequency
frames are significantly cheaper than the linear increase in bitrate for smooth movement.

Clarification D-017: the frequency of presentation samples does not have to be the frequency
bitstream events. For a source with discrete ground truth, new timestamps
are considered interpolated/synthetic until confirmed by additional
observation or Truth Innovation.

### H4. Asymmetry is useful

**HYPOTHESIS:** Expensive encoder can compile complex video into small
limited decoder ISA without transferring much of the complexity to the client.

## Rules of Honesty

1. Fidelity and perceptual results are published separately.
2. Synthesized parts are not called remanufactured original parts.
3. All side information, weights, adapters, checkpoints and metadata are included in
   final bitrate.
4. Encoder preprocessing and multipass are taken into account at runtime.
5. Comparisons are performed with comparable latency, GOP, random-access,
   resolution, chroma format and bit depth.
