# Observed Surface Memory: Evidence Atlas

Status: **RESEARCH / SUPERSEDED FOR MAIN-0** by decisions D-015 and D-017.
Semantics `Domain/Known`, 2.5D and full OSM are not included in the first implementation
gate. DPM baseline is in
[13_MINIMAL_PATCH_CORE.md](13_MINIMAL_PATCH_CORE.md), current time/state
candidate - in
[14_CONTINUOUS_TIME_CELLS.md](14_CONTINUOUS_TIME_CELLS.md). All indicators
**HYPOTHESIS/TARGET** remain here.
Date: 2026-07-26

Working titles:

- **Observed Surface Memory (OSM)** — normative `WorldState` subsystem;
- **Evidence Atlas** or **Witness Atlas** - colloquial/internal name;
- **Minimal Sufficient Scene** — encoder-only representation construction principle.

The term `Atlas` is already used by AV2 and immersive standards for others
designs. In public syntax, **Observed Surface Memory** is preferred,
terminological and IP review has not yet been completed.

## 1. What is changing

SceneLith should not restore complete physically correct or
a believably completed world. To play a given video, it is enough
a minimum set of surface fragments that actually participate in
target frames.

**NORMATIVE-DRAFT:**

- never observed and never inferred region requires no bits;
- obscurity is a clear state, not black, transparent or
  synthesized texel;
- `Truth` renderer does not have the right to read an unknown sample;
- visible fragments can be saved in
  long-lived memory and reusability;
- any place that cannot be predicted from a certain state,
  coded `REPLACE/TruthInnovation`;
- generative display-only layer never renders unknown texel
  normatively known.

This transfers the main complexity from decoder-side world generation to
encoder-only correspondence, segmentation, geometry estimation and RDO.

## 2. Fragment model

For surface \(i\):

\[
F_i=(T_i,\Omega_i,W_i(t),V_i(t),Z_i(t),P_i),
\]

where:

- \(T_i\) — reconstructed canonical texture;
- \(\Omega_i\) - sparse area of ​​certain samples;
- \(W_i(t)\) — integer warp, mesh or trajectory;
- \(V_i(t)\) — visibility;
- \(Z_i(t)\) — depth/order;
- \(P_i\) — provenance class.

For each atlas texel, `DomainMask D` and `KnownMask K` are used:

| D | K | Meaning |
|---|---|---|
| 0 | 0 | texel is not declared as part of the surface |
| 1 | 0 | surface exists, sample unknown |
| 1 | 1 | sample has been restored and is available |
| 0 | 1 | prohibited state |

`UNKNOWN` does not equal transparency. If the front surface is unknownoccludes the background, the decoder should not show the back layer through it. Such
output region receives `REPLACE` or secure frame-based fallback.

For filtered sampling, all taps footprint must be known. In the first
profile integer bilinear sample is valid only with `K=1` for all four taps.

## 3. Key operation: CAPTURE_PROMOTE

Main practical primitive:

```text
CAPTURE_PROMOTE {
    source_truth_slot
    source_instance_id
    destination_surface
    destination_page
    destination_mask
    destination_to_source_integer_map
    capture_mask_mode          // DERIVED_VISIBLE | EXPLICIT | BOTH
    capture_filter_id
    write_mode                  // NEW_ONLY | REFRESH
}
```

After complete restoration and verification, Truth frame decoder copies the selected
reconstructed pixels in atlas. Texture payload has already been paid by the current frame;
Only mask, mapping and lifecycle metadata are retransmitted.

For destination texel \(d\) mapped to frame coordinate \(F(d)\):

\[
CaptureValid(d)=M(d)\land
\bigwedge_{q\in Footprint(F(d))}
Owner(q)=source\_instance.
\]

No tap should belong to a foreground object or another surface.
Decoder does not check the semantic statement "this is a house"; it only checks
normative ownership/mask consistency. Encoder error degrades future
rate, but does not change bit-exact output.

Encoder SHOULD capture guard ring one source texel wide for bilinear
reuse. Decoder MUST NOT do dilation, edge replication or
clamp-to-known. A missing guard makes a future selection `UNRESOLVED`.

Order:

1. Decoder reads the immutable pre-access-unit state.
2. Structural render creates prediction and `ResolvedMask`.
3. Truth Innovation restores objective output.
4. Integrity and bounds are checked.
5. `CAPTURE_PROMOTE` builds a new page in staging memory.
6. Post-state hash is checked.
7. Memory Delta is committed atomically and becomes available to the next Spine Unit.

Damaged, concealment-generated or perceptual output cannot be
source `CAPTURE_PROMOTE`.
All target writes of one transaction must be disjoint; sources
read only from immutable pre-state or completed Truth outputs.

## 4. Example: a person walks along the house

1. Encoder associates visible parts of the wall in different frames with one surface.
2. The silhouette of a person is excluded by the capture-mask.
3. As a person moves, the newly opened parts of the wall are preserved through
   `CAPTURE_PROMOTE`.
4. Parts of the wall that are never shown remain `UNKNOWN` and do not occupy the texture
   payload.
5. The wall is rendered from atlas using homography or bounded mesh warp.
6. A person is encoded with a separate patch/deformable layer or regular motion
   fallback
7. Shadows, reflections, hair, motion blur and lighting changes are corrected
   ephemeral layer and Truth Innovation.
8. If the fragment is not repeated again, RDO may not save it at all.No semantic “house model” decoder is needed. Sufficient compression
a geometry that cheaply reproduces the original camera path.

## 5. GPU/ASIC-friendly freeform

An arbitrary fragment should not mean pointer-rich pixel list.

**NORMATIVE-DRAFT candidates:**

- logical atlas pages of fixed size;
- sparse microtiles;
- rectangular texture resource and compact `Domain/Known` bitmasks;
- bounded per-output-tile draw list;
- affine/projective or piecewise-affine inverse mapping;
- integer depth or compact explicit owner map;
- deterministic fill, tie-break, interpolation, rounding and saturation;
- generation counters to protect against use-after-free old page.

**CANDIDATE:** page `128×128`, microtile `8×8`, one 64-bit word each
`DomainMask` and `KnownMask` on microtile. These sizes are not frozen.

Decoder does not perform segmentation, SLAM, depth inference, object recognition
or generative completion.

## 6. Hierarchy of modes

Encoder selects the cheapest mode for each region/chunk:

1. recent-frame motion compensation;
2. equal-memory long-term decoded reference;
3. decoded patch cache;
4. 2D Evidence Atlas;
5. layered 2.5D atlas with depth/alpha/mesh;
6. sparse 3D surfels/splats for suitable scenes;
7. intra/innovation replacement.

Main v0 starts with 2D and limited to 2.5D. Full 3D and INR are not
mandatory regimes.

## 7. Encoder and a million frames

A million frames cannot be compared in pairs: these are on the order of \(10^{12}\) pairs.
The practical Foundry pipeline is hierarchical:

1. scene-cut and shot segmentation;
2. low-resolution features for all frames;
3.keyframe selection;
4. local tracks via flow/masks;
5. loop-closure retrieval by compact index;
6. full-resolution registration only for a small list of candidates;
7. observation graph and global hardware-aware RDO.

Live builds a causal atlas based on the observations already obtained. Studio analyzes the shot.
Foundry can analyze the entire title and select the best observations, but the decoder
and their bitstreams are the same.

Foundry-router is not replaced:

- OSM determines **what can be stored and rendered**;
- router suggests **when to create/expand/use/delete fragment**;
- accurate RDO checks that the full rate is indeed below the fallback.

## 8. Full rate model

For surface reuse:

\[
\begin{aligned}
R_{\mathrm{OSM}}={}&R_{\mathrm{capture}}+R_{\mathrm{domain}}
+ R_{\mathrm{geometry}}+R_{\mathrm{visibility}}\\
&+R_{\mathrm{updates}}+R_{\mathrm{checkpoints}}
+ R_{\mathrm{residual,OSM}},\\
R_{\mathrm{baseline}}={}&R_{\mathrm{motion}}+R_{\mathrm{ref\_management}}
+ R_{\mathrm{residual,baseline}}.
\end{aligned}
\]

OSM is selected only if reuse is on the horizon:

\[
G=R_{\mathrm{baseline}}-R_{\mathrm{OSM}}>0.
\]

Comparison must be performed with **equal-memory long-term reference** and
decoded patch cache. Otherwise, the gain may turn out to be a consequence of greater memory, andnot a new scene representation.

## 9. Why the compression ceiling changes

For a stable surface used \(q\) times:

\[
R_{\mathrm{OSM}}(q)
\approx R_{\mathrm{texture\ once}}
+ q(R_{\mathrm{pose}}+R_{\mathrm{visibility}}+R_{\mathrm{small\ residual}}).
\]

For frame-based baseline, repeated texture mismatch usually continues to create
residual. If the scene is perfectly repeatable and innovation tends to zero, texture
cost SceneLith is depreciated once. Therefore, the maximum gain does not have
single percent: on artificial periodic content the ratio can grow
with the duration of the video.

This does not mean universal infinite compression. First unique sample
should be:

- once transferred;
- either received by normative predictor and objective correction;
- or already exist in a confirmed Truth state.

## 10. Ranges for experimentation

All numbers below are **HYPOTHESIS/TARGET**, not results. `Net saving` means
full delta bitrate after geometry, masks, state updates, checkpoints and
residual with the same objective quality.

| Content | Working TARGET net saving | HYPOTHESIS ceiling |
|---|---:|---:|
| Static/planar, everything is already placed in equal-memory LTR | 0–8% | 10–15% |
| Rigid/screen with long-gap revisit, sprite reuse or working set more frame-reference coverage | 20–45% | 45–65% |
| Puzzle-friendly natural: long shot, repeated surfaces, moderate parallax/light | 10–25% | 25–40% |
| Mixed uncurated natural corpus | 4–12% | 12–20% |
| Fire/water/foliage/crowds/grain/reflections/cuts | 0–1% with fallback | 1–3% on rare periodic regions |

With self-contained random access about 1 second the lower/middle part of these
ranges are more likely: state snapshot re-charges texture and metadata.

On an artificial infinite-GOP video, where almost the entire inter payload is
by reintroducing the displaced surfaces, it is theoretically possible to remove 70–95%
this inter payload, and the limit at \(T\to\infty\) approaches 100%. This is not
means 70–95% of the full bitrate for natural video and is not a product claim.
If the desired texture is already available equal-memory LTR with exact warp, OSM wins
may be almost zero.

Full SceneLith can combine OSM with multi-frame innovation, quantization and
entropy tools. The percentages of individual modules cannot be added mechanically.

## 11. Updated engineering timeline

The assessment assumes 3–4 parallel workstreams, 24/7 continuation
works, ready-made flow/depth/segmentation components and a narrow first profile:
opaque patches, affine/bounded mesh, bilinear filter, no diffusion decoder.

| Result | Optimistic | Realistic |
|---|---:|---:|
| Executable synthetic skeleton with known masks/warps | 48–72 hours | 4–7 days || Oracle experiment with full bit accounting on selected real shots | 2–3 weeks | 4–6 weeks |
| First end-to-end stream: encoder → syntax → CPU Truth output | 4–6 weeks | 8–12 weeks |
| GPU decode, `CAPTURE/PROMOTE`, basic MAP and conformance | 6–9 weeks | 10–16 weeks |
| Sustainable research platform with practical Studio encoder | 8–12 weeks | 14–22 weeks |
| Proposal-grade evidence on a wide corpus | 12–20 weeks | 24–40 weeks |

Previous **6-12 weeks** remain plausible for first vertical
versions, not to a proven standard. The new formulation does not destroy
timeline; she:

- gives an executable skeleton in days;
- allows you to kill an incorrect hypothesis with an oracle test before heavy ML development;
- excludes from Main v0 universal 3D reconstruction, generation of invisible and
  neural world decoder;
- makes the 6–12 week version significantly more meaningful and
  standardized.

Version with honest general BD-rate, GPU path, masks, checkpoints and several
content classes are more realistically estimated at **10–16 weeks**. Full standard and
silicon-ready profile does not turn into a weekly task due to datasets,
interoperability, corpus runs and serial bit-exact/RD gates.

The main time saving is relative to the complete world model - no need to first
solve universal monocular 3D reconstruction, generation of invisible regions
and a heavy neural decoder. The complexity remains in practical encoder and
proof of benefit, but it can now be introduced in stages.

### 11.1 Changing difficulty

| Property | Frame codec | OSM SceneLith | Full generative world model |
|---|---|---|---|
| Persistent state | DPB frames | Sparse pages, masks, lifecycle | 3D/neural latent world |
| Decoder analysis | No | No | Often model inference/rendering |
| Decoder operations | MC, filters, transforms | Integer warp, mask, depth/owner, capture, residual | Large tensor graph/neural renderer |
| Bit-exactness | Completed | Reachable fixed integer ISA | Significantly more difficult |
| Encoder analysis | Motion/RDO | Global tracking, stitching, observation graph, state RDO | World reconstruction, inference/training and RDO |
| ASIC path | Proven | Realistic via texture/cache/mask blocks | High risk before freezing models |

**HYPOTHESIS for planning, not measured result:**

- OSM reference decoder - approximately `1.3–2×` of minimum engineering complexity
  conventional research decoder; this is not a silicon area or runtime forecast;
- early Live encoder pipeline - about `2–5×` conventional Live in number
  analysis stages;- early Studio pipeline - about `5–20×` conventional Studio;
- Foundry can be orders of magnitude heavier without changing the standard decoder;
- full generative world decoder is expected to be significantly heavier and worse than OSM
  suitable for the first bit-exact ASIC profile.

OSM is not required to be added on top of all VVC tools. The goal is to replace a complex part
frame-based prediction by more regular GPU-native operations, so
The complexity of the final decoder is determined after removing the losing tools.

## 12. Kill gates

1. Oracle with perfect camera/depth/visibility should give after all side bits:
   - at least 30% for ideal long-gap revisit;
   - at least 15% on puzzle subset;
   - at least 5% for mixed set against equal-memory AVM/VTM-class LTR.
2. Against equal-memory deduplicating decoded patch cache OSM should not give
   less than 10% for puzzle subset and 3–5% for mixed set. Otherwise leave it simple
   patch cache and remove unnecessary world geometry.
3. Practical estimator must retain at least 65–70% oracle **net** delta.
4. Geometry, masks and updates on active puzzle regions should not be
   more than 8% baseline rate; all non-residual OSM side information - no more
   12%.
5. Checkpoint overhead should remain no more than 8% with 1 s random access and
   4–5% at 2 s.
6. Average hostile class regression after fallback - no more than 0.5%, p95 clip -
   no more than +3%, no clip - no more than +5%.
7. OSM syntax overhead with mode disabled - no more than 0.3%.
8. Uncorrected never-observed pixels in Truth Core: exactly 0.
9. If full 3D gives less than 7–10% over 2.5D after geometry/checkpoint bits,
   it is excluded from Main.
10. Median admitted page must pay for insertion, mapping, masks, updates and
    checkpoint allocation no later than 2–3 uses.

## 13. Prior art and potential novelty

Themselves background mosaic, arbitrary-shape object, progressive sprite
reveal, layered atlas, occupancy map and 3D splat are not new.

Potentially distinctive SceneLith combination:

- uncertainty as a normative state of reference memory;
- evidence-bounded fragment instead of the required full object;
- `CAPTURE_PROMOTE` without repeated texture payload;
- explicit visibility/filter-footprint contract;
- transactional sparse GPU memory with bounded lifetime/checkpoints;
- global RDO, taking into account the entire cost of state;
- one universal fallback codec path;
- strict Truth boundary and generative display shell.

The novelty of this combination must be confirmed by a separate patent/prior-art
search to syntax freeze.

Additional terminology risk: AV2 already uses `Atlas` as virtual2D image for decoded layers/multistream composition. Therefore the working
the standard name of the module is `Observed Surface Memory`, not just `Atlas`.
