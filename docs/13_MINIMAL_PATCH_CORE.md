# Baseline A: Minimal Decoded Patch Memory

Status: DPM experiment **ACCEPTED**, role of the main SceneLith core
**SUPERSEDED** by solution D-017, exact syntax **RESEARCH**, compression claims
**HYPOTHESIS/TARGET**.
Date: 2026-07-26

DPM remains mandatory falsification baseline and possible compact-content
component `MOSAIC Cell`, but no longer defines time/state architecture.
Current Candidate:
[14_CONTINUOUS_TIME_CELLS.md](14_CONTINUOUS_TIME_CELLS.md).

Working titles:

- **Decoded Patch Memory (DPM)** — normative mechanism;
- **PROMOTE memory** is the key difference;
- **geometric visual dictionary** — encoder-side interpretation.

## 1. Hard revision

Background mosaic, progressive sprite, arbitrary-shape object, atlas packing,
long-term reference and layered 2D representation have already been attempted.

Therefore, SceneLith should not be declared a revolution:

- collecting a wall from different frames;
- saving sprite/patch;
- warp old texture;
- progressive reveal;
- regular atlas or scene graph.

Full Observed Surface Memory from `12_OBSERVED_SURFACE_MEMORY.md` too early
introduced `Domain/Known`, depth, 2.5D, lifecycle and other unproven mechanisms.
For DPM-0 experiment it is replaced by a more strict question:

> Can a compact reference memory of already decoded patches at the same time
> in number of bytes significantly outperform the storage of entire long-term frames?

If the answer is negative even for oracle, there is no further scene complexity
justified.

## 2. The paradox of simplicity

DPM-0 changes only the reference memory unit:

- conventional codec stores entire reconstructed frames;
- DPM stores only selected reconstructed rectangles;
- patch is no longer tied to the coordinates and lifetime of the original frame;
- one slot can be placed in the prediction canvas as many times as desired;
- new pixels are encoded by the usual Truth Innovation;
- the never shown area does not exist at all in the state.

This can be understood as a two-dimensional Lempel–Ziv with geometric placement:

```text
NEW INFORMATION -> restore once
PROMOTE -> save useful decoded rectangle
PLACE -> refer to it multiple times
INNOVATION -> correct mismatch
```

The decoder doesn't know whether the patch is a house, a face, a background, or text.

## 3. Single state

```text
PatchSlot {
    valid
    size_id
    pixels[size_id]
}
```

**DPM-0:**

- fixed bounded bank;
- candidate sizes: `16×16`, `32×32`, `64×64`;
- maximum slots and bytes are set by profile;
- pixels are post-filter reconstructed Truth samples;
- no persistent mask, depth, alpha, object ID, world coordinates or
  confidence.The first fair comparison uses exactly the same physical state-memory budget,
same as anchor DPB/LTR.

## 4. Four opcodes

```text
PM_RESET
PM_PROMOTE
PM_PLACE
PM_DROP
```

### 4.1 PM_RESET

```text
PM_RESET {}
```

- required in every RAP;
- resets all slot validity;
- after reset the old state is not available;
- DPM-0 does not transmit atlas snapshot and does not do partial repair.

### 4.2 PM_PROMOTE

```text
PM_PROMOTE {
    dst_slot
    size_id
    source_x
    source_y
}
```

After completion and verification of Truth reconstruction, the command copies exactly
integer-aligned rectangle from current post-filter Truth frame in `dst_slot`.

- no repeat texture payload;
- partial slot update missing;
- new PROMOTE completely replaces slot;
- source must lie entirely inside frame;
- perceptual or concealment output is prohibited.

It is coordinate-free compaction post-filter decoded pixels that is
the only potentially distinctive primitive is DPM-0.

### 4.3 PM_PLACE

```text
PM_PLACE {
    src_slot
    destination_x
    destination_y
}
```

- only integer translation;
- slot is copied to the prediction canvas without resampling;
- commands are executed in bitstream order;
- the last command overwrites the previous prediction;
- output pixels not covered by PLACE remain unresolved;
- prediction is always corrected by Truth residual/replacement.

No affine, homography, mesh or bilinear filtering in the first oracle.
The encoder approximates a complex form with several rectangles or does not use it
DPM.

### 4.4 PM_DROP

```text
PM_DROP {
    slot_list
}
```

- invalidates slots after the current output has completed;
- current unit reads immutable pre-unit bank;
- DROP/PROMOTE are committed atomically for the next unit.

Technically, DROP can be replaced by rewriting slot. It's left as trivial
operation for explicit liveness and testing; after measuring the syntax cost it
can be deleted.

## 5. Full decoder loop

```text
for each AccessUnit:
    1. Parse and validate syntax, counts, offsets, integrity.
    2. For RAP, perform PM_RESET; PLACE count MUST be 0.
    3. Freeze the current PatchBank as read-only.
    4. Prediction = 0; ResolvedMask = 0.
    5. Execute PM_PLACE in bitstream order:
           exact-copy pixels;
           set ResolvedMask on destination rectangle.
    6. Decode Truth payload.
    7. For each pixel:
           resolved -> Prediction + objective residual;
           unresolved -> objective replacement/intra.
    8. Run normative in-loop filters.
    9. Issue Truth output.
   10. In staging, apply PM_DROP and PM_PROMOTE only from post-filter Truth.
   11. Check bounds, duplicate writers and memory limit.
   12. Atomically commit state for the next AccessUnit.
   13. Optional Perceptual Detail applied only to display.
```If damaged, the state-dependent unit decoder does not update PatchBank and
resumes the experimental DPM path only after the next RAP. DPM-0 is not
contains partial repair.

## 6. How the house example is preserved

1. In the first frame, the encoder finds the blank rectangles of the wall around the person.
2. After reconstruction they end up in slots via `PM_PROMOTE`.
3. In the following frames, `PM_PLACE` assembles a prediction from already known pieces.
4. The person and the yet unknown parts are restored by the usual Truth Innovation.
5. When a new piece of wall becomes visible for the first time, it can be PROMOTE for
   future reuse.
6. A piece that has never been opened is not stored or generated.

The Arbitrary shape in v0 is the union of rectangles. It's less bit-efficient,
than an ideal mask, but leaves the decoder extremely simple and gives an honest answer,
Is there a big win at all?

## 7. How is this different from previous approaches?

| Approach | What can you already do | Narrow Possible DPM Difference |
|---|---|---|
| MPEG-4 sprite | Panorama, warp, arbitrary-shape foreground, progressive/online sprite | Not a special background object, but a common compact bank of independent decoded rectangles |
| VVC/AV2 LTR | Long life reconstructed frames, block/affine prediction | Don't pay for memory for useless pixels of the whole frame |
| AV2 BRU/composite reference | Partial update reference picture | Coordinate-free dense packing patches from many frames with the same byte budget |
| MPEG Immersive Video | Patches, atlases, geometry, inverse placement | Only original 2D playback; no multiview/depth/novel view |
| Layered Neural Atlases | Persistent texture, alpha, learned frame↔atlas mapping | No MLP, semantic layer or per-video neural decoder |

**Honest status:** these differences may not be sufficient for a patent
novelty. `PM_PROMOTE/PLACE` - first a compression experiment, not a claim
inventions.

## 8. Why the previous versions did not become a universal frame codec

- MPEG-4 sprite was specialized background/object mode and depended on
  high-quality segmentation/authoring.
- Whole-frame LTR is simple, but wastes memory on pixels that are no longer needed.
- MIV solves the more difficult 6DoF problem and pays depth/patch metadata.
- Neural atlases have been optimized for editing/view synthesis, requiring heavy
  per-video fitting and do not specify a massive bit-exact decoder.
- Composite reference approaches already show that simple memory gain can
  be only a few percent on average.

DPM is potentially better not because it is more intelligent, but because it doescompact patch memory is the only new inter-memory primitive and has
cheap per-block fallback.

## 9. Revision of tasks

### Immediately implement

1. Strong anchor:
   - AV2 v1 with long-term references and Backwards Reference Update;
   - VVC/VTM LTR;
   - equal-byte composite/deduplicating patch-cache baseline.
2. DPM oracle:
   - rectangles `16/32/64`;
   - integer PROMOTE/PLACE;
   - exact full-rate accounting;
   - identical residual/transform/entropy tools with anchor.
3.Dataset:
   - long-gap camera return;
   - moving occluder/background reveal;
   - UI/game/animation sprites;
   - repeated logos/text;
   - negative water/foliage/crowd/grain/cuts.
4. Metrics:
   - BD-rate and per-class result;
   - bytes patch bank and DPB;
   - cache hit/useful-hit;
   - PROMOTE/PLACE bits;
   - DRAM read/write per output pixel;
   - RAP penalty.

### Do not add to DPM-0

- `DomainMask/KnownMask`;
- arbitrary-shape persistent masks;
- canonical surface atlas;
- depth, z-buffer and owner map;
- affine/homography/mesh;
- trajectories;
- 2.5D and 3D;
- surfels/Gaussians;
- semantic objects;
- scene/world reconstruction;
- generative completion;
- learned decoder;
- atlas snapshots and partial repair;
- Foundry-router distillation.

These mechanisms remain in Research Radar and are not implemented until
a four-team core will not pass the gate.

## 10. Go/no-go

Continue DPM as a core coding tool only if oracle is the same:

- decoder memory bytes;
- random-access interval;
- latency/lookahead;
- objective quality;
- residual/transform/entropy path;
- encoder search effort for reported anchor

gives:

- more than 15% net bitrate reduction on several different long-gap categories;
- at least 10–15% for puzzle-friendly natural subset;
- at least 5% for mixed corpus;
- average hostile regression no more than 0.5%;
- memory traffic within the future hardware profile.

If DPM fails gate:

- do not add masks/depth/3D in an attempt to save the idea;
- leave it niche screen/sprite tool or close it;
- return to multi-frame innovation as the main research path.

## 11. Complexity tax for any extension

After the success of DPM-0, a new tool is added only separately and one at a time:

1. binary `8×8` mask;
2. subpixel translation;
3. affine;
4. partial slot update;
5. trajectory parameterization.

Each extension must:

- give at least 3% net gain on mixed corpus or at least 7% on large corpus
  declared subset above the previous level;
- do not increase disabled-stream syntax by more than 0.2%;
- have bounded integer implementation;- do not require semantic inference in the decoder;
- undergo separate ablation.

No measured marginal gain - no syntax.

## 12. Simplified timeline

During parallel round-the-clock operation:

| Deadline | Result |
|---|---|
| 2–4 days | DPM state machine, synthetic bitstream and bit-exact CPU copy path |
| 1–2 weeks | Oracle on selected long-gap sequences |
| 2–4 weeks | Fair comparison with equal-memory LTR/BRU/composite cache |
| 4–6 weeks | Solution: core, niche or kill |
| 6–10 weeks | GPU/conformance work only if the decision is positive |

This is significantly faster and cheaper than the full OSM/2.5D branch. The most important:
SceneLith gets verifiable answer before unproven complexity
will turn into architectural debt.
