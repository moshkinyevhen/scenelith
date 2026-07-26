# Paper kill-test and justification for architectural freezing

Date: 2026-07-26
Status: paper model - **HYPOTHESIS**; semantic spine - **ACCEPTED** solution
D-025; payload and numbers - **NORMATIVE-DRAFT / TARGET**.
Related solutions: D-017, D-020, D-021, D-022, D-023, D-025, D-026

## 1. What exactly needs to be surpassed

SceneLith is not compared to the abstract "modern codec" and not to one
united baseline.

The main baselines are measured **separately**:

1. **AV2 v1.0 / AVM v1.0.0** published by AOMedia on May 28, 2026;
2. **VVC / H.266 (2026 edition) / VTM**.

For AV2, all applicable tools must be enabled, including BRU,
long-term references, Show Existing Frame and Atlas. For VVC must be enabled
all applicable inter, merge, affine and long-term-reference tools.

A comparison is considered fair only if the following are the same:

- source, bit depth and chroma format;
- objective or explicitly declared perceptual quality criterion;
- latency and lookahead class;
- random-access interval;
- decoder/reference memory limit;
- encoder effort class;
- taking into account all dictionaries, adapters, weights, checkpoints and container overhead.

Comparison with AV1, HEVC, AVC or fast hardware preset can be published
additionally, but does not prove victory over frontier baseline.

## 2. Why a thought experiment is useful, but not a benchmark

He can:

- display the upper limit of a syntax-only idea;
- show what share of residual/innovation must be eliminated;
- reject an architecture that, even under favorable assumptions, does not
  reaches the goal;
- check universality and bounded decoder complexity.

The paper model cannot determine:

- real distribution of AVM/VTM bits on an unknown corpus;
- how good the encoder is at finding spacetime decomposition;
- real residual entropy after such decomposition;
- BD-rate for a specific quality metric.

Therefore, the paper model is used for architecture selection rather than
public claim about achieved gains.

## 3. Normalized rate model

For each baseline, the following is taken separately:

\[
R_B=C_B+M_B+I_B=1,
\]

where:

- \(C_B\) - partition, mode, reference and control syntax;
- \(M_B\) — motion signaling;
- \(I_B\) - sample innovation: coefficients, new texture, refresh and others
  information that cannot be obtained from the current predictor state.

Hypothetical net gain SceneLith:

\[
G =
C_Bs_C + M_Bs_M + I_Bs_I - O_Q,
\]

where \(s_C,s_M,s_I\) are the eliminated shares of the corresponding
components, and \(O_Q\) is the cost of new Support, lifecycle, event,
checkpoint, and content-state bits. `framebuffer work` is not included in this
formula; it is an energy and memory-traffic advantage, not a bitrate saving.

Main consequence:

> If \(s_I\) is close to zero, lifetime and trajectory can only save
> small control/motion components. Radical compression requires reduction
> namely innovation bits.

## 4. Deterministic sensitivity simulation

Canonical script:
[`../experiments/paper_kill_test.py`](../experiments/paper_kill_test.py).

It runs 200,000 deterministic Monte-Carlo samples per scenario. Intervals
are explicit engineering assumptions rather than measured statistics.

### 4.1 Result against AV2 v1.0 / AVM v1.0.0

| Scenario | p10 | median | p90 |
|---|---:|---:|---:|
| Mixed: lifetime + linear law only | -0.3% | 1.0% | 2.3% |
| Mixed: compact persistent Cell | -0.4% | 1.3% | 3.1% |
| Mixed: persistent TruthInnovation only | 0.6% | 4.1% | 7.6% |
| Mixed: low-rank basis target envelope | 6.2% | 14.1% | 22.0% |
| Coherent pan/occlusion: compact Cell | 1.8% | 5.2% | 8.6% |
| Screen/UI/scroll: compact Cell | 5.7% | 11.0% | 16.0% |
| Stable arbitrary/soft silhouette | 1.9% | 5.5% | 9.0% |
| Hair/smoke/chaotic boundary: forced Cell | -7.7% | -4.3% | -0.9% |
| Hostile dynamics: forced Cell | -1.8% | -0.6% | 0.7% |

### 4.2 Result vs VVC/H.266/VTM

| Scenario | p10 | median | p90 |
|---|---:|---:|---:|
| Mixed: lifetime + linear law only | 1.5% | 3.2% | 5.0% |
| Mixed: compact persistent Cell | 1.7% | 3.8% | 6.1% |
| Mixed: persistent TruthInnovation only | 4.2% | 8.4% | 12.5% ​​|
| Mixed: low-rank basis target envelope | 10.6% | 19.6% | 28.5% |
| Coherent pan/occlusion: compact Cell | 4.7% | 8.4% | 12.1% |
| Screen/UI/scroll: compact Cell | 11.2% | 17.7% | 23.8% |
| Stable arbitrary/soft silhouette | 6.0% | 10.4% | 14.7% |
| Hair/smoke/chaotic boundary: forced Cell | -6.8% | -3.2% | 0.4% |
| Hostile dynamics: forced Cell | -1.2% | 0.2% | 1.6% |

Negative forced result in a real encoder should be limited almost
zero via exact fallback. Fallback prevents loss, but does not create
win.

`Low-rank basis target envelope` is not the expected result. His prior is intentional
suggests that the new model already eliminates 10–32% of the remaining innovation bits
AV2 or 12–38% VVC. The line answers the question “what will happen if the main
the hypothesis will work,” rather than proving that it will work.

### 4.3 Revolutionary result threshold against AV2

For representative mixed-natural ledger:

- control: 7.5%;
- motion: 5.75%;
- elimination of control: 37.5%;
- motion elimination: 45%;
- new SceneLith overhead: 8%.

Then you need to eliminate the following share of **remaining AV2 innovation bits**:| The goal is total bitrate reduction | From all AV2 innovation | At coverage 50% | With coverage 80% |
|---:|---:|---:|---:|
| 10% | 14.5% | 29.0% covered residual | 18.2% |
| 25% | 31.8% | 63.6% covered residual | 39.8% |
| 40% | 49.1% | 98.2% covered residual | 61.4% |

With coverage of 30%, the target of 25% is already mathematically impossible in this ledger: even
Complete elimination of residual on the covered areas is not enough.

This is the main result of the paper kill-test:

> Cells that only live longer and transmit trajectory less frequently cannot be
> revolutionary Main. For 25% against AV2, the new model should remove approximately
> a third of all innovation bits that are already left after AV2 prediction; at
> 50% coverage is almost two-thirds residual in the covered areas.

## 5. Rejected options Main

### 5.1 `HOLD` or different region refresh rates

Useful for power and screen content, but modern codecs are already almost free
code unchanged blocks. This is a component, not an architectural core.

### 5.2 Object/mesh/depth/world reconstruction

Can give gains on individual scenes, but introduces segmentation, topology,
occlusion repair and branch-heavy decoder. This defeats the purpose of the minimum
normative core and overlaps with MPEG-4 object coding and AV2 Atlas.

### 5.3 Unlimited neural graph or shader VM

Simplifies the publication of new models, but eliminates bounded complexity,
determinism, security audit and a chance for a cheap ASIC.

### 5.4 Generative completion inside Truth state

Can dramatically improve perceptual bitrate, but does not preserve objective truth and
pollutes future prediction. Allowed only as Optional Perceptual Detail.

### 5.5 Conventional residual per output sample

If each display/source timestamp again receives almost a full residual
AV2/VVC, frame-free state becomes a beautiful wrapper with little gain.

## 6. Recommended candidate: one Spacetime Basis Cell

Cell is not a semantic object. This is only found by the encoder
rate-distortion atom.

For output coordinate \(p=(x,y)\) Cell synthesizes scalar gate \(g_i\) and
premultiplied or signed color contribution \(c_i\):

\[
\left(g_i(p,t),c_i(p,t)\right)=
\sum_{k=0}^{K_i-1}
a_{i,k}(t)\,
B_{i,k}\!\left(W_i(p,t)\right),
\qquad p\in S_i.
\]

where:

- \(B_{i,k}\) — immutable decoded integer basis fields;
- \(S_i\) - conservative bounded union dyadic microtiles for storage only,
  scheduling and culling;
- \(W_i(p,t)\) — absolute fixed-point coordinate law;
- \(a_{i,k}(t)\) — bounded fixed-point temporal coefficient laws;
- `(order_key, cell_id)` specifies deterministic order.

Outside \(S_i\) Cell is identical no-op: \(g_i=1,c_i=0\).
The only runtime composition operation:

\[
Y_0(p,t)=0,\qquad
Y_{j+1}(p,t)=
Clip\left(g_j(p,t)Y_j(p,t)+c_j(p,t)\right).
\]This is one machine, not a zoo of tools:

- static opaque texture: \(g=0\), \(K=1\), constant \(W\), constant \(a\);
- moving texture: \(g=0\), \(K=1\), time-varying \(W\);
- fade or illumination change: several bases and changing \(a_k(t)\);
- soft arbitrary shape: \(g=1-\alpha,\ c=\alpha F\);
- persistent additive correction: \(g=1,\ c=E\);
- hard replace: \(g=0,\ c=F\);
- arbitrary raster fallback: full-output Cell for one source interval.

Thus, `TruthInnovation` does not have to be a separate frame residual codec.
It appears to be the same affine-composition Cell primitive.

### 6.1 Freeform without rectangular artifacts

Dyadic tiles and rectangular texture allocation **are not visible forms**.
They only limit the area where Cell can differ from identity.

The visible footprint specifies the sampled gate \(g(p,t)\):

- binary opaque silhouette;
- subpixel antialiased edge;
- hair/fur coverage;
- transparency;
- motion-blur edge;
- smoke or shadow contribution.

Gate is encoded using the same basis/payload mechanism, not polygon/circle/spline zoo.
At the border the following are required:

- conservative support padding;
- profile-defined texture apron for all interpolation taps;
- identity \(g=1,c=0\) to the outer border support;
- objective innovation where compact gate predictor is insufficient.

Therefore coarse tiles cannot appear as squares. For mathematically
lossless profile last short-lived Cell can deliver \(g=0\) and accurate
\(c=Truth\) on any erroneous pixels.

We cannot promise the absence of any distortion artifacts at an arbitrarily low
lossy bitrate: this would violate the rate-distortion limit. Normative goal:

- no artifacts caused by the shape of storage tiles;
- lossless exact mode;
- visually transparent mode with a separate strict boundary metric;
- RDO fallback, if coding gate is more expensive than regular innovation.

The Sensitivity model shows why fallback is mandatory:

- a stable arbitrary/soft boundary has a positive hypothetical
  median: 5.5% vs. AV2 and 10.4% vs. VVC;
- forced Cell on hair/smoke/chaotic border has a negative median:
  - 4.3% against AV2 and -3.2% against VVC.

Corollary: arbitrary shape is always supported without visible rectangle, but
a separate persistent shape is used only when RDO wins. B
otherwise Truth is encoded by the short-lived universal Cell without
architectural switching.

### 6.2 Why is it stronger than the previous Cell

The previous Cell dampened control and motion, but usually left almost
same residual.Spacetime Basis Cell tries to reduce the residual in three ways:

1. motion-aligned texture is paid once;
2. changes in appearance over time are described by several coefficient laws;
3. recurring residual becomes persistent/low-rank basis, not new
   table of coefficients for each sample.

This is warped low-rank plus sparse decomposition, but the decoder does not perform
segmentation, neural reasoning or world completion. All the heavy optimization
makes an asymmetric encoder.

## 7. Minimum decoder contract

The state grammar candidate has only:

```text
RESET(epoch_time)
SET(event_time, cell_id, alive, changed_fields, payload_or_reference)
```

- `alive=0` removes Cell;
- the absence of `SET` means infinite preservation of the current state;
- checkpoint is `RESET + SET*`, not a new primitive;
- presentation schedule is in container/API track;
- `PresentationQuery(t)` reads state, but is not mutation opcode.

Standard render loop:

1. entropy-decode changed payload/state fields;
2. evaluate fixed-point \(W_i(p,t)\);
3. sample no more than profile-bounded \(K\) basis textures;
4. execute fixed-point multiply-accumulate;
5. perform one affine-composition FMA \(gY+c\);
6. clip and output.

### 7.1 Main targets, not yet accepted limits

- \(K\le4\) or other small profile-bound value;
- dyadic support is used only for culling/storage, not as a visible shape;
- an arbitrary visible form is set by bounded gate field;
- piecewise-linear coefficient laws;
- static/translation/affine fixed-point coordinate law;
- one affine-composition operation \(gY+c\);
- no depth, mesh, semantics or arbitrary graph;
- no more than eight types of fused GPU/ASIC kernels;
- auditable normative decoder core target: no more than 15 kLOC without platform,
  container and test code.

`kLOC` and kernel count - TARGET, not a measured result and not a replacement for complexity
model.

## 8. The only major open choice

Basis textures still need to be compressed a lot. Using AV2/VVC intra
would preserve their code complexity and would defeat the purpose of the project.

We need one bounded payload synthesizer instead of mode zoo. Candidates:

1. integer multiscale lifting transform + entropy coder;
2. fixed integer nonlinear synthesis transform with a small number of regular
   convolution/GEMM operations;
3. fixed dictionary/residual vector quantization.

The choice cannot be made based on aesthetics. It should separately show:

- objective RD against AV2/VVC intra;
- deterministic cross-device output;
- small code and ASIC area;
- low memory traffic;
- lack of content-specific weights outside of full bitrate accounting.Per-shot adapters MAY be examined, but all their bits are counted; arbitrary
transmitted graph is prohibited.

### 8.1 Leading candidate: cached integer basis synthesizer

The most powerful path to simultaneous compression and code simplicity:

\[
B=D_{\mathrm{int}}\!\left(z;\theta_0+UV^\mathsf{T}\right)+e.
\]

Where:

- \(D_{\mathrm{int}}\) — one fixed bounded synthesis graph;
- \(\theta_0\) — profile-defined immutable integer weights;
- \(z\) — transferred quantized latents;
- \(UV^\mathsf{T}\) — optional bounded low-rank per-shot adapter;
- \(e\) — sparse exact correction for objective/lossless profile.

Critical solution: synthesizer runs **only with `SET` new Basis
Content**, and the result is cached as immutable \(B_k\). Presentation loop is not
launches neural renderer; it only does texture sample, temporal MAC and
\(gY+c\).

This gives:

- one regular int8/int16 convolution/GEMM pipeline instead of hundreds
  block-level tool combinations;
- deterministic CPU/GPU/ASIC output;
- adaptive content model without transmitted arbitrary graph;
- a heavy encoder can search for \(z,U,V\) without complicating the normative renderer;
- exact correction does not allow learned synthesis to contaminate Truth.

It's still **HYPOTHESIS** and not the chosen technology. Primary results
show only the practical possibility of direction:

- [integer-only variable-rate image compression](https://doi.org/10.1016/j.jvcir.2025.104634)
  reports 19.2% bitrate reduction versus VTM-17.2 intra under the same operating conditions;
- [PNVC](https://doi.org/10.1609/aaai.v39i3.32315) reports approximately 5% gain
  vs VTM-20.0 LD and 20+ FPS for 1080p;
- [LotteryCodec](https://proceedings.mlr.press/v267/wu25e.html) demonstrates
  per-instance subnetwork search for image compression.

These numbers cannot be transferred to the SceneLith, AV2 or mixed-video benchmark. They are only
refute the claim that deterministic/instance-adaptive synthesis
fundamentally unrealizable.

Leading payload candidate is rejected if:

- its full bit accounting does not exceed individual AV2/VVC intra anchors;
- update-time energy/latency above profile limit;
- weights/adapters take up more saved bitrate;
- exact correction systematically returns almost the entire residual;
- software reference and silicon model do not provide bit-exact output.

## 9. What to freeze before selling

You can freeze now:

- frame is not a unit of state;
- Cell is not an object, but bounded spacetime basis atom;
- one formula for static, motion, appearance and innovation;
- `RESET/SET`, implicit persistence and read-only presentation;
- immutable Truth content and prohibition of perceptual contamination;
- fixed-point bounded evaluation;
- exact arbitrary-video fallback;- separate reports against AV2 and VVC.

You can't honestly freeze without a short oracle:

- \(K\), tile sizes and transform sizes;
- translation vs affine in a mandatory profile;
- linear lifting vs integer nonlinear payload synthesizer;
- entropy contexts;
- exact memory/profile limits.

This is not architectural throwing. These are the parameters of the same machine. Stable
semantic spine allows you to change them without rewriting the event/state model.

### 9.1 Semantic Closure Rule

After candidate is accepted, new idea doesn't add opcode or renderer tool if
it can be compiled into existing fields:

| Research Idea | Compilation into one Cell |
|---|---|
| Multi-observation canonical memory | new/refined immutable \(B_k\) |
| Trajectory-aligned innovation tube | set \(B_k\) and temporal laws \(a_k(t)\) |
| Low-rank illumination/appearance | additional \(B_k,a_k(t)\) |
| Arbitrary/soft shape | Gate component \(g\) |
| Static/motion/affine placement | coordinate law \(W\) |
| Persistent residual dictionary | \(g=1\), signed \(c\) |
| Full raster escape | \(g=0\), full-output \(c\) |

If an idea is not expressed through `B / W / a / g / c / SET`, it:

1. encoder-only analysis remains;
2. deposited in Optional Perceptual Detail;
3. or waits for the next major version.

This rule allows research to continue without changing the normative
architecture in the process of implementation.

## 10. Architecture acceptance criterion

A candidate becomes implementation architecture only if all conditions
are executed simultaneously:

1. The paper model does not have a syntax-only ceiling;
2. arbitrary input let's imagine exact fallback without the second codec;
3. decoder remains bounded, integer and data-parallel;
4. AV2-specific model allows a path to 25% only through a measurable reduction
   innovation, and not through a dishonest baseline;
5. payload engine has a realistic path to small decoder code;
6. all strong extensions are expressed by the same Cell equation, not new ones
   normative object types.

Before the actual benchmark, the correct wording is:

> SceneLith has an architectural path to victory over AV2/VVC, but victory has not been proven.
> Lifetime-only path has already been rejected on paper; decisive hypothesis - warped
> low-rank spacetime innovation with one bounded decoder kernel.
