# Research Radar

Status: **RESEARCH**
Purpose: to separate practically implemented technologies from high-risk ones
research and not turn the Main profile into a set of unrelated fancy tools.

## 1. Main / implement now

### Continuous-Time MOSAIC Cells

Why:

- one lifetime removes per-presentation `unchanged`;
- absolute MotionLaw absorbs motion over an interval;
- compact Content eliminates the mandatory frame-sized reference memory;
- Presentation Query is separated from state mutation;
- static output tiles may not be decoded or rewritten;
- minimal decoder uses fixed microtiles and integer translation.

Gates order: temporal RLE/HOLD → linear motion runs → compact
`CAPTURE_TRUTH` cells → incremental GPU/display compositor. Full model:
[14_CONTINUOUS_TIME_CELLS.md](14_CONTINUOUS_TIME_CELLS.md).

### Multi-frame chunk coding

Why:

- removes part of frame-by-frame autoregression;
- parallelizes well on GPU;
- allows general temporal latent;
- compatible with read-only temporal layers.

Practicality signal: DCVC-UF reports real-time/higher real-time results for
1080p and 4K and big wins in low-delay configuration.

### Integer learned transforms

Why:

- bit-exact cross-device;
- direct path to NPU/ASIC;
- managed compute;
- real-time operation of DCVC-RT has already been demonstrated.

### Bounded 2.5D scene memory - only after cell gates

Components:

- atlas pages;
- depth/visibility;
- sparse splats/surfels;
- patch dictionary;
- deterministic lifetime/eviction/checkpoints.

Main experiment: surface reappearance after occlusion or
camera return.

### Lattice/finite scalar quantization

Why:

- better takes into account the multidimensional structure of latent;
- almost scalar complexity is possible;
- no need for a giant learned codebook search.

Explore FSQ, OLVQ and adaptive lattice VQ in groups of 4–32 measurements.

### Parallel entropy

- 16–64 interleaved rANS lanes;
- tile/chunk offsets;
- non-autoregressive hyperprior;
- limited restart points.

## 2. Main after limited prototype

### One-dimensional flexible latent memory

GVC1D shows large perceptual bitrate reduction thanks to 1D tokens and
long-term memory. Main needs rework:

- bounded token count;
- lack of full-resolution attention;
- non-autoregressive decode;
- integer implementation;
- independent restartable chunks.

### Sparse Gaussian/surfel mode

Use as a regional primitive for stable surfaces and
predictable movement. Don't make it the only view: current methodsare not universal, and encoder optimization can be slow.

### Multiple descriptions / erasure training

Base/state are divided into independently decodable parts; loss concealment never
does not update state. Explore NeuralMDC/GRACE-like principles without the heavy lifting
multi-step decoder.

## 3. Optional profile

### Per-scene adaptation

- low-rank adapter;
- limited size, preliminary 32–128 KB/epoch;
- full cost is included in bitrate;
- mainly VOD/long-form/talking-head/UI.

Instance-adaptive work shows significant potential, but requires
slow finetuning and may not generalize well between datasets.

### One-step perceptual renderer

- distilled diffusion/rectified flow;
- display-only;
- fact/identity/OCR/flicker gates;
- synthetic provenance;
- never reference.

### Screen primitives

Text/vector/sprite representation can give a significantly greater effect on the UI,
slides and games, but requires a separate fidelity contract and exact fallback.

## 4. High potential, not Main v1

### Relative-entropy / reverse-channel coding

Theoretically, it encodes sample relative to a common prior approximately according to KL-cost.
A practical limitation is the rapidly increasing computational complexity.

Permitted research area:

- KL-capped microblocks;
- small adapters;
- perceptual texture shell;
- independently restartable units.

### Bits-back recurrent stream

Do not include in the main temporal loop until the solution:

- initial seed cost;
- serial chain;
- catastrophic state corruption;
- random access.

### Full video foundation model as codec

Use as encoder-only oracle, data generator or optional research
profile. Do not include multi-step DiT/world generator in the standard Main decoder
due to compute, model drift, nondeterminism and hallucination.

### Per-video INR

Suitable for specialized VOD and archive. Not Main due to:

- slow optimization;
- instability between sequence classes;
- the need to transfer model/adapters;
- complex random access.

## 5. Forbidden shortcuts

- Treat LPIPS/DISTS gains as proof of fidelity.
- Exclude weights/adapters from bitrate.
- Learn from official test sequences.
- Use generative output as reference.
- Add a custom downloadable graph.
- Make full-resolution autoregressive entropy.
- Declare semantic prompt as a reconstruction of the original video.

## 6. Order of experiments

1. Ideal temporal RLE/HOLD control.
2. `STATIC + LINEAR_TRANSLATION` persistent runs.
3. Compact `CAPTURE_TRUTH` cells versus AV2 BRU/Atlas and patch cache.
4. Incremental GPU/display compositor.
5. Chunk-native learned Innovation.
6. Integerization and bit-exact conformance.
7. Lattice/FSQ.
8. Sparse splat regional mode.
9. Consumer routing/distillation.
10. Perceptual Shell.
11. REC/INR and other optional extensions.

This order first tests the central hypothesis and then adds
research rates.
