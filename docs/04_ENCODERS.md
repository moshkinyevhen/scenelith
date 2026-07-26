# SceneLith Encoders: Live, Studio and Foundry

Document status: **NORMATIVE-DRAFT** for bitstream/decoder boundary and
**TARGET** for all numerical budgets and performance indicators.

The numbers below are design goals. They are not measured
SceneLith results and must be supported by reproducible experiments.

## 1. One bitstream and one decoder

**ACCEPTED:** SceneLith defines one normative bitstream and one
deterministic decoder for three non-normative encoder classes:

1. **Live** - strictly causal real-time coding on a consumer GPU;
2. **Studio** - multi-pass encoding on a workstation;
3. **Foundry** - distributed offline scene compiler with almost
   unlimited search budget.

All three encoders use the same set of MOSAIC primitives, the same restrictions
decoder ISA and the same WorldState semantics. The encoder class does not change
reconstruction of an already created stream and is not a condition for its decodability.
The only differences are the quality of the analysis, the depth of the search, and the encoder solutions chosen.

Foundry cannot pass an arbitrary executable graph or hidden model.
Any transmitted scene adapter must use a bounded normative
decoder operations, sizes and number formats; the full cost of the adapter is included
bitrate. Live can use a legal subset of syntax without adapter.

Optional Perceptual Detail for any encoder class remains non-reference,
never modifies WorldState or participates in Fidelity/Truth Core predictions.

## 2. Encoder classes

| Characteristics | Live | Studio | Foundry |
|---|---|---|---|
| Main Application | broadcasts, calls, local recording, UGC | master files, creator/VOD, archive | films, catalogues, reference encode, research |
| Future Analysis | **ACCEPTED:** 0 frames in strict Live; optional near-live preset up to 8 frames | **TARGET:** 8–32 frames; quality preset up to 1–4 s or full shot | full title and connections between shots |
| RDO Candidates | **TARGET:** top-K 2–8 on tile/chunk | **TARGET:** top-K 8–64 and multiple passes | distributed beam/A*/DP search and multiple λ-runs |
| Encoder compute | **TARGET:** 10–30 kMAC per output pixel | **TARGET:** 30–300 kMAC per output pixel | **TARGET:** 10-500 GPU-s per second source |
| Extreme Mode | **TARGET:** 1× real-time and preset 2–10× slower | **TARGET:** 2–100 GPU-s per source second | **TARGET:** 10³–10⁴ GPU-s per second for hero/research encode || Equipment | **TARGET:** 1080p60 on 8 GB VRAM; 4K60 on 12–16 GB | **TARGET:** 1–4 GPU, 16–96 GB total VRAM | distributed GPU cluster |
| Adaptation | without compulsory training; short online statistics | shot/title dictionary and limited adapter | **TARGET:** 10–500 GPU-hours per-title adaptation, when it pays off in bitrate |

For Live, a budget of 10–30 kMAC/pixel corresponds to approximately 5–15 TMAC/s
at 4K60. This is a **TARGET** and not a statement of speed achieved. Real
bandwidth is also limited by memory, synchronizations, entropy
coding and GPU loading.

### 2.1 Live

Live uses:

- causal MOSAIC Cell state and limited history;
- fixed-grid change detection and flow at 1/4–1/8 resolution;
- open-ended `STATIC/LINEAR_TRANSLATION` runs;
- run break when objective error or full RDO stops passing gate;
- bounded online `CAPTURE_TRUTH`/eviction;
- local verification of candidates based on actually generated bits;
- conventional objective fallback and parallel rANS.

**TARGET:** Interactive delay - 50-250 ms if selected transport
and checkpoint interval allow this.

### 2.2 Studio

Studio extends Live with the following features:

- bidirectional analysis of the full shot;
- multiple allocation/RDO passes;
- more accurate flow, boundary/support and tracking;
- joint optimization of motion knots, cell lifetime and checkpoints;
- small per-shot/per-title dictionaries and adapters;
- re-encode problem areas after checking the metrics.

Studio is the main mass-produced high-quality encoder: its work must be
possible on one powerful workstation without mandatory access to the cluster.

### 2.3 Foundry

Foundry is an encoder-only research oracle and production
scene compiler. It can use:

- analysis of the full movie and loop closure in minutes;
- large encoder-only vision/world models;
- global comparison of fragments and re-appearing surfaces;
- joint search for Cell Content/Support/MotionLaw/Lifetime, representation
  routing and rate;
- many independent encode trials;
- ensemble of objective, perceptual, OCR, identity, geometry and flicker metrics;
- distributed per-title optimization of dictionaries and limited adapters.

Foundry is not required to receive a useful SceneLith stream. His
additional role is to create teacher solutions to speed up Live and Studio.

### 2.4 Continuous-Time Cell pipeline

One encoder task selects for each candidate:

```text
Content + Support + MotionLaw + Lifetime + Order + Mode
```

Pipeline:

1. detector measures spatiotemporal error against the current active cells;
2. existing motion estimator offers `STATIC/LINEAR_TRANSLATION`;
3. temporal DP decides whether to continue run, put a knot, split support or
   go to Truth fallback;
4. compact-memory planner decides whether `CAPTURE_TRUTH` will pay off;
5. exact RDO compares the full event/support/motion/checkpoint/innovation rate
   with AV2/VVC-like raster path;
6. only positive net candidate gets into stream.

Live is not required to know `death_time` in advance: it creates an open-ended cell and
sends a new event when the contract is no longer valid. Studio knows shot and
can optimize duration. Foundry searches for long-gap correspondence by title,
but decoder and bitstream are the same.

Foundry does not compare a million samples pairwise. It performs shot segmentation,
low-resolution indexing, key-sample selection, local tracks and loop-closure
retrieval; full-resolution registration runs only for shortlist.

A never observed region is not generated for Truth playback. Content
becomes reference only through inline objective decode or confirmed
`CAPTURE_TRUTH`. Display-only generation remains Perceptual Detail.

Full model:
[14_CONTINUOUS_TIME_CELLS.md](14_CONTINUOUS_TIME_CELLS.md).

### 2.5 Changing encoder complexity

All multipliers are **HYPOTHESIS/TARGET**, unmeasured results:

| Implementation | Relatively strong conventional encoder |
|---|---:|
| Gate A: ideal temporal RLE/HOLD | `+5–15%` analysis |
| Gate B: fixed-grid linear motion runs | `+10–30%` Live encode time |
| Gate C: causal compact cells | `1.5–3×` Live |
| Full-shot Studio cells | `3–10×` |
| Foundry global oracle | `10–100×+`, budget-controlled |

Gate B reuses conventional motion candidates and adds temporal DP.
Gate C is more difficult due to support, capture/eviction and long-horizon value. These costs
non-normative and do not go to decoder.

If practical Live retains less than 80% oracle net gain, the tool is simplified either
remains Studio/VOD-only.

## 3. Rate-distortion-compute optimization

Basic multi-objective encoder criterion:

\[
J =
R_{\mathrm{total}}
+ \lambda D_{\mathrm{truth}}
+ \alpha D_{\mathrm{perceptual}}
+ \mu C_{\mathrm{decode}}
+ \nu M_{\mathrm{state}}
+ \rho L_{\mathrm{seek}}
+ \kappa P_{\mathrm{loss}}
+ \eta S_{\mathrm{instability}}.
\]

Where:

- \(R_{\mathrm{total}}\) includes payload, headers, memory deltas, adapters,
  checkpoints, indexes and FEC;
- \(D_{\mathrm{truth}}\) measures Fidelity/Truth Core;
- \(D_{\mathrm{perceptual}}\) applies only to allowed non-referential
  perceptual layer;
- \(C_{\mathrm{decode}}\) and \(M_{\mathrm{state}}\) limit decoder compute
  and memory;
- \(L_{\mathrm{seek}}\) penalizes expensive random access;
- \(P_{\mathrm{loss}}\) takes into account error propagation;- \(S_{\mathrm{instability}}\) penalizes flicker, state drift and unstable
  representation switching.

The final mode selection must take into account the actual complete bits. Entropy proxy
allowed for preliminary ranking, but not for final RD report.
Encoder comparison is carried out with the same decoder profile, latency,
random-access and resilience constraints.

Live uses a learned proposal and precise local RDO. Studio increases
horizon and beam. Foundry performs global or approximately global
optimization by chunks, checkpoints and scene state.

## 4. Teacher–student distillation

Foundry stores for each explored site:

- Pareto-set of candidates and their actual rate;
- selected representation primitive;
- Cell Content/Support and capture/reuse decisions;
- cell lifetime, update and eviction solutions;
- MotionLaw knots, order and occlusion decisions;
- Q/bit allocation;
- checkpoint placement;
- the full value of the components \(J\);
- reasons for the discrepancy with Live/Studio.

Non-normative student-router Live/Studio learns:

1. imitation learning using the best Foundry solutions;
2. pairwise ranking of candidates;
3. regression of RDO components;
4. DAgger/hard-negative cycle on cases of discrepancy between student and teacher;
5. quantization-aware training and INT8 pruning.

Student only offers top-K. Bit-exact RDO reserves the right to reject it
proposal. With high uncertainty, the encoder expands K or uses
safe fallback. The encoder weights are non-standard and can be updated without change
bitstream or decoder.

This is how the cost of Foundry search is amortized: once a pattern is found
becomes a fast solution on a consumer GPU.

## 5. Target quality gap

For the same content, quality level and the same restrictions, we denote:

- \(B_A\) — full bitrate of the external anchor;
- \(B_F\) — full Foundry bitrate;
- \(B_L\) — full Live bitrate.

Share of Foundry gains retained by Live:

\[
G_{\mathrm{capture}} =
\frac{B_A - B_L}{B_A - B_F}.
\]

**TARGET:** Live must retain at least 80% of Foundry gains in the early
usable version and 90% in the mature version on the main closed test set.
The rule only applies when Foundry is statistically significantly better than anchor.

Additional goals:

- **TARGET:** mature Live uses no more than 8–15% more bits than
  Foundry, on general video with equal quality and constraints;
- **TARGET:** Studio uses no more than 3-8% more bits than Foundry;
- **TARGET:** against contemporaneous strong anchor Live reaches 25–35%
  bitrate savings, Studio - 30-40%, Foundry - 35-45%;- **TARGET:** a significantly larger Foundry gap is allowed as a separate
  the result is only for predefined specialized classes, for example
  talking-head, UI or long repeating VOD.

Percentage goals are not considered achieved without hidden-set testing, full
accounting of all service bits and verification by an independent decoder.

If Live systematically retains less than 80% of Foundry gains, the problem cannot be solved
mask with mandatory cloud encode. Representation needs to be simplified
search, improve distillation/router or revise syntax. Massive success
SceneLith requires a consumer encoder to already provide the bulk of the structural
gains, while Foundry improves the ceiling, trains the fast encoder, and maintains
expensive offline VOD.
