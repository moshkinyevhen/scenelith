# Risks and stopping criteria

Status: **ACCEPTED**

## 1. Continuous-Time Cells do not pay off

Risks:

- event/support/motion/checkpoint bits eat up savings;
- AV2 skip/merge/BRU/LTR/Atlas already take almost all the available gain;
- MotionLaw runs are too short;
- lighting/deformation makes old Content useless;
- bounded memory forgets the scene too quickly.

Check:

- separate reappearance/occlusion dataset;
- ablation `HOLD`, `HOLD+LINEAR`, compact Content;
- separately tool-complete AV2 v1.0 BRU/LTR/Atlas and VVC/H.266 baseline;
- equal-memory deduplicating decoded patch cache;
- ideal temporal RLE existing mode maps;
- full accounting of metadata.

Kill/pivot:

- Main-0 vs AV2: <10% broad screen, <5% puzzle or <2% mixed;
- Main-0 vs VVC: <12% broad screen, <7% puzzle or <3% mixed;
- persistent TruthInnovation adds <7% screen or <5% puzzle over
  Main-0 after own state/checkpoint bits;
- lack of gain against decoded patch cache means pivot to simple cache;
- practical encoder saves <70% oracle net gain;
- event/support/checkpoint >20% gross saving;
- frequent large false references.

Intransitive cell invariants:

- PRESENT does not change state;
- the absence of event means persistence;
- only verified Truth output can be the source of `CAPTURE_TRUTH`;
- MotionLaw is absolute and does not warp the previous interpolated output;
- uncorrected never-observed pixels in Truth Core: exactly 0.

If rate gain <3%, but decoder/DRAM energy drops >25–30% on a large screen
profile, the mechanism may remain low-power profile, but is not declared
universal compression revolution.

## 2. Chaotic content

Classes:

- water;
- fire/smoke;
- film and sensor grain;
- foliage;
- crowd;
- rapid cuts;
- complex sports motion.

Protection:

- objective residual fallback;
- tile-level representation routing;
- prohibition of forced scene mode;
- no-regression gates.

## 3. State drift

Reasons:

- arithmetic mismatch;
- corrupted delta;
- concealment is included in reference;
- erroneous eviction;
- lost asynchronous event frozen cell;
- model version mismatch.

Protection:

- integer bit-exact path;
- state hashes;
- commit only after integrity;
- MAP/full state reset;
- repair units;
- conformance across CPU/GPU vendors.

## 4. Random access penalty

A full cell/content checkpoint can be expensive.

**TARGET:**

- overhead <8%;
- RA 0.25–0.5 seconds in the main product;
- CfP cadence at least anchor;
- after RAP there is no dependence on the previous state.

If checkpoints systematically destroy the primary gains, the state should be
simplified or divided into independently refreshable Cell groups.

## 5. Decoder is too complicated

Risks:

- DRAM traffic is more important than MAC;
- many small kernels;
- fragmented support and too many moving cells;
- entropy stalls;
- unpredictable peak state.

Protection:

- compute/memory/traffic as standard level axes;
- fixed microtiles;
- fused integer kernels;
- multi-lane entropy;
- baseline fallback graph;
- early GPU profiler and FPGA model.

## 6. Consumer encoder is too weak

If Foundry finds a win that cannot be predicted by the small router,
the mass product will fail.

Criterion:

- a mature Studio should maintain 80–90% Foundry delta;
- early gap >30% requires distillation/redesign;
- a persistent gap >20% after training is a reason to exclude the tool from
  Main profile or leave it VOD-only.

## 7. Generative hallucinations

Risks:

- change of text, person or fact;
- temporal identity drift;
- the user does not know that the part has been synthesized;
- generative error poisons the following frames.

Unbreakable rules:

- Perceptual Shell is not reference;
- provenance mask is required;
- evidence profiles disable shell;
- OCR/identity/geometry gates;
- Truth-only decode is always available.

## 8. Training leakage and generalization

- Official test sequences are not used for training.
- Training corpus is revealed where CfP requires it.
- Hidden set is processed by the same binaries.
- Manual per-sequence tuning is not considered a universal result.
- All adapters are included in bitrate.

## 9. Incorrect comparisons

Dangers:

- compare LD with RA;
- ignore delay;
- exclude model bits;
- compare reference encoder with production preset without explanation;
- pass VMAF/LPIPS as authentic.

Each result passes the fair-comparison checklist of
`07_METRICS_AND_ROADMAP.md`.

## 10. IP and standardization

Risks:

- hidden patent claims;
- incompatible training/code license;
- closed weights interfere with conformance;
- formal CfP logistics have not been completed.

Protection:

- source/license inventory;
- prior-art search to freeze;
- narrow patent claims and RF/FRAND strategy;
- separate submission checklist;
- partner/organization for JVET.

## 11. Deadline risk CfP

The critical result by October 26 is not a scientific presentation, but:

- one decoder;
- encoder/configs;
- 150 main streams for the selected full test case;
- reconstructed sequences;
- metrics/MD5;
- self-contained package on a physical SSD.

When there is a lack of time, the number of experimental tools is reduced, but not
conformance, reproducibility or completeness.

## 12. Visible tile seams and arbitrary bordersRisk:

- storage rectangle or dyadic support becomes visible as square
  contour;
- binary mask gives aliasing;
- bilinear taps read the padding of another surface;
- hair, smoke, transparency and motion blur generate mask churn, which
  destroys bitrate gain;
- spatially acceptable error flickers in time.

Non-negotiable requirements:

- storage/culling Support is not a visible shape;
- outside the Support Cell strictly identity: \(g=1,c=0\);
- the visible shape is set by scalar Gate with fractional coverage;
- each sampling footprint has a canonical apron or objective fallback;
- lossless test is played by pixel-exact;
- changing the internal tile partition with the same decoded fields does not change
  output;
- encoder can abandon persistent shape and use short-lived
  exact Truth Cell.

Adversarial shape suite:

- diagonal/subpixel lines;
- rotating antialiased disc;
- text and subtle glyph strokes;
- hair/fur;
- glass/transparency;
- smoke/shadow;
- motion-blurred silhouette;
- chroma subsampling boundaries;
- slow subpixel movement, revealing temporal shimmer.

Kill gates:

- any seam that correlates with the storage tile boundary is a correctness bug;
- lossless mismatch — immediate stop;
- boundary-weighted distortion or temporal-edge flicker is worse separately
  configured AV2/VVC baseline - Cell mode is disabled for this region;
- forced persistent shape on a chaotic boundary can be expected to lose;
  automatic RDO fallback is required to limit total regression.
