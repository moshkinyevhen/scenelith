# Frame-free core: Continuous-Time MOSAIC Cells

Status: frame-free time/state principles — **ACCEPTED** by decision D-025;
hard dyadic visible support and `REPLACE/ADD` formula - **SUPERSEDED** solutions
D-021/D-022; physical limitations and prior art card - **FACT**; numerical
thresholds - **TARGET**.
Date: 2026-07-26
Solution: D-017.

Adopted one-equation CBF architecture and separate AV2/VVC kill-test:
[`15_PAPER_KILL_TEST_AND_FREEZE.md`](15_PAPER_KILL_TEST_AND_FREEZE.md).

Working terms:

- **MOSAIC Cell** - a single long-lived visual-state primitive;
- **State Event** — asynchronous change of cell fields;
- **Presentation Query** - reading the scene at the moment \(t\), without changing the state;
- **Continuous-Time Retained Video (CTRV)** is a descriptive name of the model, not
  accepted product name.

Product hierarchy:

> **SceneLith — a SceneLith codec, powered by MOSAIC.**

## 1. Major coup

The frame should not be:

- reference memory unit;
- unit of state change;
- unit of movement description;
- obligatory bitstream clock;
- cause of repeated decoding or recording of static pixels.

The frame can only remain a compatible result:

> `PresentationQuery(t)` asks what the confirmed scene looks like at the moment
> \(t\), but the request itself does not change anything in it.

The normative flow should describe **what has changed and for how long it is valid
description**, and display selects moments of observation.

## 2. Physical limit: “no frames” does not mean “no time”

You can't show movement without changing the light emitted from the screen at all. Any
real display:

- updates pixels discretely;
- scans lines;
- or supports analog/event changing with end band.

Therefore, SceneLith's honest goal is:

> Remove frame clock from transport, reference state, motion syntax and main
> decoder work. The latter display sampling remains a physical necessity.

On a normal 60/120/240 Hz display, the controller calculates the scene in its timestamps.
In the future event-driven panel it will only be able to apply
changed regions. The same SceneLith stream is not required to have
soldered FPS.

For a source film shot with a regular camera with discrete frames, the values are between
The moments of filming are not uniquely defined mathematically. Result in new
timestamp is an interpolation/synthesis if it is not confirmed:

- more frequent shooting;
- event sensor;
- to others ground truth;
- or explicitly transmitted `TruthInnovation`.

This limitation cannot be hidden by marketing.

## 3. One primitive, eliminating three repeated fees

Each active cell has:

\[
Cell_i=
\left(
Content_i,\ Support_i,\ MotionLaw_i(t),\
[birth_i,death_i),\ Order_i,\ Mode_i
\right).
\]

Where:- `Content` — texture or signed objective correction, transmitted once
  or captured from the already decoded Truth output;
- `Support` — a set of local microtiles for which content is defined;
- `MotionLaw(t)` - absolute fixed-point display of local coordinates in
  output space;
- `Lifetime` — action interval, including open-ended;
- `Order` — deterministic order of opaque composition;
- `Mode` - `REPLACE` or `ADD_TRUTH`.

The same mechanism removes:

| Re-cost frame codec | MOSAIC Cell Field | Why pay once |
|---|---|---|
| `unchanged/skip` on each frame | `Lifetime` | Without an event, the state persists indefinitely |
| ref/MV/mode on each frame | `MotionLaw(t)` | One segment affects many display queries |
| frame-sized reference buffers | `Content + Support` | Only useful coordinate-independent samples are stored |

Important boundary: if cell does not reduce the total
`content + support + motion + event + checkpoint + innovation` rate, encoder it
does not use.

Comparison of one coherent interval:

\[
R_{\mathrm{frame}} \approx
\sum_{t}
\left(
R_{\mathrm{partition}}+
R_{\mathrm{ref/mode/MV}}+
R_{\mathrm{residual}}
\right),
\]

\[
R_{\mathrm{cell}} \approx
R_{\mathrm{content}}+
R_{\mathrm{support}}+
R_{\mathrm{motion\ law}}+
R_{\mathrm{events/checkpoints}}+
\sum_t R_{\mathrm{innovation}}.
\]

SceneLith only benefits if one-time cell costs are amortized and
`TruthInnovation` does not return almost the entire residual anchor. Otherwise new state
contract is just another packaging of the same bits.

## 4. Four independent clocks

Modern frame codec usually reduces different processes to one picture cadence.
MOSAIC shares:

1. **State clock** — content/support/order/lifetime changes only based on events.
2. **Motion clock** - a new knot comes when the previous law of motion has ceased
   be accurate enough.
3. **Innovation clock** — objective correction appears where and when
   structural render is not enough.
4. **Presentation clock** — display or compatibility container asks
   result in arbitrary timestamps.

A static wall can have zero state and motion events after appearing.
A smoothly moving logo can have one motion segment per second and 240
presentation queries. The speaker's mouth can receive frequent innovation events,
and his clothes are rare. These are different clocks within the same scene, not separate ones
full video streams.

## 5. State and output equations

\[
WorldState(t^+)=ApplyEvents(WorldState(t^-),E_t).
\]

\[
\hat V(p,t)=
Compose_{i:\ birth_i\le t<death_i}
Sample(Content_i,Support_i,MotionLaw_i(t),p).
\]

\[
V(p,t)=
\hat V(p,t)+TruthInnovation(p,t)+OptionalPerceptualDetail(p,t).
\]

This is a specification of the accepted formula:

\[
Video(t)=Render(WorldState_t,\ Trajectories_t)
       + TruthInnovation_t
       + OptionalPerceptualDetail_t.
\]

`PresentationQuery(t)` reads \(WorldState(t)\) but does not execute
`ApplyEvents`.

## 6. How to show static without redrawing

### 6.1 In bitstream

Static cell:

```text
MotionLaw = IDENTITY
death_time = INFINITE
```

After `CELL_SET`, `HOLD`, skip flags or empty per-frame records are not transmitted.Silence means maintaining the state.

### 6.2 In decoder/compositor

Each cell and each output microtile has a generation/version. Implementation
caches an already composed tile and recalculates it only if:

- contributing cell has changed;
- a moving cell passed through the tile;
- Truth Innovation has arrived;
- color/display parameters have changed.

Dirty set:

\[
D(t)=ChangedFootprints(t)\cup SweptMovingFootprints(t)
     \cup InnovationFootprints(t).
\]

The incremental compositor's operation should scale with \(|D(t)|\), not with
\(Width\times Height\).

On a legacy display, the full scanout can be saved, but the decoder/GPU is not required
again decode and rewrite static framebuffer tiles. When panel
self-refresh static part may not be sent via display link. This
separate energy/memory-traffic metric, not a replacement for bitrate.

## 7. How to show movement without encoded FPS

### 7.1 Absolute motion law

First minimum law:

\[
x(t)=x_0+v_x(t-t_0), \qquad
y(t)=y_0+v_y(t-t_0).
\]

Possible next extension - linear interpolation bounded integer affine
matrix between two knots.

Motion is always calculated relative to the unchanged stored `Content`, and not
by warp of the previous output. Therefore, the number of presentation queries does not create
recursive blur or numerical drift.

### 7.2 Event instead of vectors

```text
CELL_SET {
    event_time
    cell_id
    changed_fields = MOTION | LIFETIME
    motion_model = LINEAR_TRANSLATION
    x0, y0, vx, vy
    motion_end_time
}
```

Until `motion_end_time`, no new motion syntax is needed. If movement
has changed, a new knot comes. If the model has become unprofitable, short-lived
Truth cell or raster fallback corrects the output.

### 7.3 Display execution

The display controller receives active content, trajectory and layer order. For
each own presentation time he:

1. calculates absolute transform;
2. determines old/new/swept dirty footprint;
3. reads only affected source tiles;
4. Updates only the pixels whose light should change.

A moving object physically requires updating pixels in its old and new
footprint. It is impossible to eliminate this work; eliminate full-screen decode,
full-frame write and per-frame CPU/GPU command - possible.

### 7.4 Exposure

Natural motion blur depends not on the instantaneous \(t\), but on the integral over
exposure interval. Possible future tool:

\[
V_\Delta(p,t)=\frac{1}{\Delta}
\int_{t-\Delta/2}^{t+\Delta/2}V(p,\tau)\,d\tau.
\]

Main-0 does not standardize expensive arbitrary integration. It uses sample at
\(t\), and blur of the original samples preserves Truth Innovation. Fixed integer
shutter integration is considered only after a separate RD/compute gate.

## 8. Why not rectangles, circles or arbitrary polygon zoo

Rectangle was chosen by DPM as the cheapest falsification test:

- contiguous storage;
- one descriptor;
- coalesced GPU copy;
- existing blit hardware;
- simple bounds.Circle is not a more general answer:

- most real boundaries are not circular;
- you need a separate rasterizer/coverage rule;
- rotation, aliasing and chroma boundary still require definition;
- the next object will require another primitive.

Full polygon/mask is accurate, but may eat up topology/mask bits and
irregular execution.

Candidate solution:

> Shape is not a type. `Support` - only bounded set of identical
>dyadic microtiles.

- the internal area is encoded with large tile runs;
- the border is refined with smaller tiles only with positive RDO;
- a circle, a person or a letter are a union of the same cells;
- the first profile starts with one coarse grid;
- pixel mask is allowed only as a separate extension after measured gain;
- boundary error is closed by objective innovation, and not by a new shape engine.

On GPU `Support` is deployed once during a state event in the dense owner map or
compact active-tile list. Presentation does not bypass pointer-rich tree.

## 9. Minimal semantics of bitstream

The number of opcodes in itself is not a criterion for simplicity. One opcode with
dozens of hidden modes are worse than three clear operations. Minimal semantic set:

```text
STATE_RESET(t)
CELL_SET(t, cell_id, changed_fields, ...)
PRESENT(t, optional_truth_payload)
```

### `STATE_RESET`

- starts self-contained epoch;
- clears all cells;
- prohibits references to the past epoch.

### `CELL_SET`

Creates a cell or atomically changes the listed fields:

```text
CELL_SET {
    event_time
    cell_id
    alive
    changed_fields

    if CONTENT:
        source = INLINE | CAPTURE_TRUTH | KEEP
        payload_or_capture_address

    if SUPPORT:
        bounded_microtile_set

    if MOTION:
        STATIC | LINEAR_TRANSLATION
        parameters
        motion_end_time

    if LIFETIME:
        death_time_or_infinite

    if COMPOSITION:
        REPLACE | ADD_TRUTH
        order_key
}
```

- `alive=0` completes cell;
- `death_time` makes a separate DROP optional;
- `KEEP` changes movement without repeating texture;
- `CAPTURE_TRUTH` saves only verified post-filter Truth samples;
- Optional Perceptual Detail and concealment cannot be source;
- the new version is committed only after an integrity check.

### `PRESENT`

- sets compatibility output timestamp or source sample to be checked;
- does not change state;
- may contain short-lived objective innovation;
- in continuous-output profile host MAY make a query in a different timestamp, but
  such an output is considered interpolated if there is no ground truth for it.

## 10. Versatility and fallback

Let's imagine any raster video:

- full-screen opaque `REPLACE` cell;
- lifetime until next source timestamp;
- new cell before each `PRESENT`.

This is an expensive but correct fallback. Well simulated video instead
has long lifetimes, compact content and rare motion/innovation events.

Chaotic water, fire, foliage, hair, reflections, grain and cuts should not
forcibly transform into thousands of tiny persistent cells. Encoder selectsshort-lived raster/innovation representation.

## 11. Occlusion without full 3D

The first profile uses only deterministic opaque order:

```text
(order_key, cell_id)
```

When the foreground cell goes away, the underlying background cell is visible again without
retransmission. The never observed background region is not created:
if it becomes visible for the first time, Truth Innovation restores it, after
which encoder MAY execute `CAPTURE_TRUTH`.

Depth, alpha, mesh and semantic object identity are not needed for the first gate.
The encoder prediction error is always corrected by Truth path.

## 12. Hardware contract

Main-0 candidate uses:

- bounded cell table;
- bounded compact content bank;
- fixed microtile size;
- fixed-point absolute translation;
- exact copy or one existing interpolation filter;
- deterministic opaque composition;
- residual/replacement path;
- multi-lane entropy;
- tile generation map and dirty list;
- atomic state event commit.

No:

- arbitrary shaders;
- unbounded scene graph;
- device floating point;
- segmentation/SLAM in decoder;
- per-pixel linked lists;
- recursive output warp;
- mandatory neural model;
- generation of the invisible world.

Future ASIC can connect the decoder state bank to the display/overlay controller.
Then the trajectory is set once, static tiles remain in local memory, and
controller only performs dirty/swept composition.

## 13. What has already happened and what cannot be declared new

**FACT:**

- conditional replenishment transferred only significantly changed parts
  picture is already in [ITU-T H.120](https://www.itu.int/rec/T-REC-H.120/en);
- [MPEG-4 Visual](https://mpeg.chiariglione.org/standards/mpeg-4/video.html)
  supported arbitrary-shaped Video Object Planes and sprites;
- [MPEG-4 BIFS](https://mpeg.chiariglione.org/standards/mpeg-4/scene-description-and-application-engine.html)
  passed insert/delete/replace commands for dynamic scene graph;
- different temporal rates of objects were studied in
  [Asynchronous Rate Control for Multi-Object Videos](https://doi.org/10.1109/TCSVT.2005.852415);
- event cameras and
  [time-encoding video](https://arxiv.org/abs/2206.04341) are already in use
  asynchronous per-pixel events;
- [ADΔER](https://arxiv.org/abs/2408.06248) transcodes framed video into
  sparse asynchronous intensity representation;
- motion-aligned spatiotemporal tubes were researched in
  [Tube-based video coding](https://doi.org/10.1016/S0923-5965(96)00034-3);
- final [AV2 v1.0](https://av2.aomedia.org/v1.0.0/index.html) already has
  partial Backwards Reference Update, long-term references, output existing
  reference frames, multistream layers and Atlas composition.

Therefore, they are not an independent revolution:

- dirty rectangles;
- region-specific FPS;
- object layers;
- arbitrary masks;
- sprites;
- partial reference update;
- scene graph;- continuous affine animation;
- event stream itself.

SceneLith's potential difference requires prior-art/FTO review. It is formulated as
single bounded natural-video contract:

1. frame-free state events;
2. motion-lifetime cell, simultaneously shock-absorbing state, motion and compact
   content reference;
3. objective innovation at the same time domain;
4. observed-only capture with reference provenance;
5. independent presentation clock;
6. incremental GPU/display execution;
7. bitrate, random access, loss and hardware limits in one RDO.

The novelty of the combination is still **HYPOTHESIS**, not a patent conclusion.

## 14. Why HOLD alone is not enough

Modern codec already transfers static block via very cheap skip/merge without
residual. If SceneLith only removes skip flags, the ceiling is small.

Illustration **not as measured result**: 4K contains about 510 blocks
`128×128`. Even one conventional bit per block at 60 Hz is about 30.6 kbit/s.
On multi-megabit natural video this is less than a few percent.

Therefore cell is obliged to amortize simultaneously:

- partition/support;
- reference choice;
- motion law;
- lifecycle;
- texture after occlusion/reappearance;
- decoder writes.

Otherwise, the mechanism remains useful power optimization for screen content, but not
compression revolution.

## 15. Honest working hypotheses

These are the ranges of the first minimum `STATIC + LINEAR_TRANSLATION` Main-0,
not claims SceneLith. Baselines cannot be combined:

| Class | Vs AV2 v1.0 | VS VVC/H.266 |
|---|---:|---:|
| Full replay output | 0–1% | 0–2% |
| Ideal rigid/screen | 5–15% | 8–18% |
| Puzzle-friendly natural | 2–8% | 3–10% |
| Mixed natural | 0–3% | 0–4% |
| Hostile dynamic with fallback | about 0% | about 0% |

This is not the ceiling of full MOSAIC. Compact observed content, occlusion reuse,
multi-frame innovation and new transforms can provide additional benefits,
but percentages cannot be added without end-to-end measurement.

The main potentially big result could be two-dimensional:

- bitrate reduction;
- decoder/DRAM/display work reduction.

They are measured and published separately.

### 15.1 Working score for “average video”

Until oracle the result is unknown. Current engineering hypothesis:

- only lifetime/HOLD syntax: about `0–1%` broad mixed natural;
- compact persistent Cell on mixed: `0–3%` against AV2 and `0–4%` against VVC;
- persistent TruthInnovation without real low-rank residual reduction:
  `2–6%` against AV2 and `3–8%` against VVC;
- double-digit gains are most likely for screen/UI content, scrolling, 2D
  animation, static-camera scenes, and long-gap reappearance;
- more than 10% on truly mixed natural cannot be promised before measurement.

For SceneLith to produce the revolutionary `25%+` on average, Cells must be combined with
significantly better Truth Innovation/transform/entropy path and indeed
reduce residual, and not just service syntax.

Separate sensitivity model, coverage thresholds and new Spacetime Basis Cell
candidates are in
[`15_PAPER_KILL_TEST_AND_FREEZE.md`](15_PAPER_KILL_TEST_AND_FREEZE.md).

### 15.2 Changing encoder difficulty

`STATIC/LINEAR` runs can reuse conventional motion candidates.
Additional task - temporal dynamic programming: how long is profitable
save law and when to break run.

Workers **HYPOTHESIS/TARGET**:

- Gate A: `+5–15%` analysis;
- Gate B Live: `+10–30%` encode time;
- Gate C Live with compact content: `1.5–3×`;
- full-shot Studio: `3–10×`;
- Foundry global oracle: `10–100×+`, but this is a non-standard regulated budget.

Live doesn't have to know the future: it opens a cell without an expiration date and sends
event when the objective-error/RDO threshold is exceeded. Studio/Foundry wins
due to knowledge of the future lifetime.

### 15.3 Changing decoder power

It is necessary to distinguish between peak capability and average consumption.

- **Peak compute does not disappear:** universal fallback must decode
  full-screen hostile 4K/8K content. The mass chip cannot be reduced only by
  based on calm scenes.
- **Initial software decoder MAY be slower** on `0–20%` while cell
  scheduling and composition are not merged into GPU kernels.
- **ASIC target:** cell control state no more than tens of KB, without additional
  DPB for Gate B, worst-case control/compute overhead no more than `2–5%`.
- **Mixed natural target:** `0–15%` less than average decoder/DRAM work; it might
  be zero if almost the entire screen is constantly dirty.
- **Sparse screen/UI target:** `20–60%` less decoder/compositor energy.
- When the dirty area is less than 10%, the ideal incremental path can remove
  `50–90%+` output-buffer writes, but this does not equal the same reduction in total
  wall power: scanout, source reads, panel and OS remain.

For a completely unchanged frame, AV2/VVC is already very cheap. Additional
SceneLith's savings appear primarily in the absence of repeated composition/
framebuffer writes also with panel self-refresh, and not in miraculous elimination
residual, which is not there anyway.

### 15.4 Regular Monitors and Transition Period

A new monitor is **not needed** to decode and display SceneLith:

1. The player stores Cell state.
2. At every VSync of a conventional 60/120/144/240 Hz monitor, it evaluates
   `PresentationQuery(t)`.
3. Updates dirty tiles of a regular GPU framebuffer.
4. Transmits standard raster output via HDMI/DisplayPort.

At 60 Hz the motion will be physically shown at 60 samples/s; at 240 Hz the same
MotionLaw can be sampled 240 times without 4× motion syntax. New timestamps all
are equally marked interpolated if the source Truth was only 60 Hz.

Already existing interfaces partially support the desired path:

- [Vulkan `VK_KHR_incremental_present`](https://registry.khronos.org/vulkan/specs/latest/man/html/VK_KHR_incremental_present.html)
  passes the presentation engine a list of changed rectangles;
- [DXGI dirty rectangles/scroll metadata](https://learn.microsoft.com/en-us/windows/win32/direct3ddxgi/dxgi-1-2-presentation-improvements)
  reduce memory bandwidth and related power;
- [Windows multiplane overlay/direct scanout](https://learn.microsoft.com/en-us/windows/win32/comp_swapchain/comp-swapchain)
  can avoid unnecessary desktop composition;
- [VESA eDP Panel Self Refresh](https://vesa.org/featured-articles/vesa-publishes-embedded-displayport-standard-version-1-5/)
  already allows panel to store a static image and receive partial updates.

On a regular external monitor, scanout will often continue to run at full refresh rate,
so the main early gain will be in transport/decode/GPU writes, not in
the entire panel.

The new display/controller is needed only for the maximum version:

- accept Cells/trajectories directly;
- store texture locally;
- sample MotionLaw yourself;
- update only changed pixels.

This is a promising hardware profile, not a codec launch condition.

## 16. Implementation ladder: simplicity to complexity

### Gate A - Temporal syntax oracle

- fixed `128×128` screen grid;
- persistent `HOLD`;
- ideal temporal RLE of existing partition/ref/mode solutions;
- no compact textures, masks or object semantics.

Goal: measure the absolute ceiling of per-frame unchanged syntax removal.

### Gate B - Persistent motion runs

- `STATIC` and `LINEAR_TRANSLATION`;
- fixed decoded reference;
- maximum run 256 ticks;
- conventional Truth override;
- up to approximately 16 KB control state for 4K candidate profile.

Goal: test motion/ref/partition syntax damping without a new renderer.

### Gate C - Compact content cells

- `CAPTURE_TRUTH`;
- coordinate-independent microtile content bank;
- equal memory versus AV2 BRU/LTR/Atlas and decoded patch cache;
- opaque order and disocclusion.

Goal: remove frame-sized reference waste and repeated texture after the long gap.

### Gate D - Frame-free decoder API

- arbitrary `PresentationQuery(t)`;
- incremental dirty-tile compositor;
- one stream is output at 60/120/240 Hz;
- original timestamps are checked by objective Truth;
- interpolated timestamps are marked separately.

Goal: to prove new functionality and energy scaling, not just rate.### Only after success

One at a time, with separate ablation:

- subpixel translation;
- bounded affine;
- finer boundary support;
- exposure integration;
- partial checkpoint/repair;
- illumination trajectory;
- learned innovation transform.

Depth, mesh, 3D, semantics and generative core are not added to save
Gates A-C failure.

## 17. Experiments and baselines

Required baselines:

1. final AV2/AVM with BRU, skip/merge, global/affine motion, long-term
   references, SEF/implicit output and Atlas/multistream where applicable;
2. VVC/VTM with strong inter/merge/affine/LTR;
3. equal-memory decoded patch cache;
4. ideal temporal RLE existing mode maps;
5. native multi-layer screen stream, if source layers are available;
6. flattened raster separately, without mixing the results.

Dataset axes:

- changed area: `0.1/1/5/20/50/100%`;
- lifetime: `2/4/8/16/32/64/256` ticks;
- static/constant velocity/acceleration/nonlinear motion;
- stable and churning boundaries;
- occlusion/reappearance;
- sensor noise, exposure change and motion blur;
- packet loss and random access;
- slides, cursor, IDE, terminal, scrolling, 2D game/animation, surveillance;
- broad natural and hostile water/foliage/crowd/cuts.

Count:

- full bitstream;
- state/event/motion/support/checkpoint bits;
- residual/innovation;
- state bytes;
- DRAM reads/writes;
- pixels recomposited per presentation;
- energy estimate;
- latency;
- random-access penalty;
- loss freeze/repair time.

## 18. Kill gates

### Gate A

- `HOLD/RLE` gives at least 5% on sparse screen suite and 0.5% on mixed natural;
- otherwise leave it as implementation-only power optimization.

### Gate B

`STATIC + LINEAR_TRANSLATION` vs tool-complete baseline:

- at least 12% on scroll/sprite;
- at least 7% on broad screen suite;
- at least 3% for mixed natural;
- at least 5% above the ideal temporal RLE on the target subset;
- event/checkpoint syntax no more than 20% gross saving;
- hostile mean regression no more than 0.2%, any clip no more than +1%.

### Gate C

Compact cells vs equal-memory AV2 BRU/LTR/Atlas and decoded patch cache:

- at least 15% on puzzle/reappearance subset;
- at least 5% for mixed corpus;
- median admitted content pays for insertion/support/checkpoint no later than three
  uses;
- practical encoder retains at least 80% oracle net gain.

### Architecture gate

The new standard is justified if, after combining the winning tools, although
just one thing:

- at least 25% universal gain against contemporaneous anchor;
- new continuous-output class with materially lower bitrate/latency/energy,
  which cannot be obtained with an equivalent AV2/VVC configuration;- at least 25–30% decoder/DRAM energy reduction on a large declared profile
  in the absence of significant rate regression.

A negative gate cannot be saved by adding depth, masks and neural decoder.

## 19. Aggressive but verifiable timeline

During parallel round-the-clock operation:

| From the start of implementation | TARGET |
|---|---|
| 1–3 days | Event/state simulator, `SET/PRESENT`, synthetic static/motion demo |
| 4–7 days | Dirty-tile renderer and bit-exact fixed-point translation |
| 1–2 weeks | Gate A and the first perfect-lookahead Gate B oracle |
| 2–4 weeks | Fair AV2/VVC temporal-run comparison and negative classes |
| 3–6 weeks | Gate C compact `CAPTURE_TRUTH` memory experiment |
| 4–8 weeks | GPU incremental compositor and multi-refresh demo |
| 8–16 weeks | Broad RD/power corpus, random access, loss and architecture verdict |

Demonstration of frame-free state is possible in days. Proof of the universal
compression claim stays longer due to strong baselines, corpus runs,
bit-accounting and conformance, and not because of the volume of opcodes.

## 20. Revision of tasks

Immediately:

1. implement tiny event/state simulator;
2. build ideal temporal RLE control;
3. check `HOLD + LINEAR_TRANSLATION`;
4. compare with AV2 BRU/SEF/LTR/Atlas and VVC;
5. measure dirty pixels/DRAM separately from bitrate;
6. Only then turn on the compact `CAPTURE_TRUTH` cells.

Don't do it now:

- full 3D world;
- semantic object decoder;
- arbitrary circle/polygon zoo;
- per-pixel asynchronous event stream;
- neural renderer;
- diffusion;
- alpha/depth/mesh;
- complex scene graph;
- new transform to state/motion thesis proof.

The main paradox of simplicity:

> Don't update image faster. Give each piece one
> space-time contract and remain silent as long as the contract is true.
