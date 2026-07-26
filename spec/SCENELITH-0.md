# SceneLith-0 — Normative Draft

Codec/bitstream family and project: SceneLith
Architecture: MOSAIC
Version: 0.0.4
Status: **NORMATIVE-DRAFT**
Date: 2026-07-26
Canonical standalone filename extension: `.scenelith`

This document currently captures the semantic contract, not the final
bit layout.

## 1. Scope

SceneLith-0 defines a self-contained visual-state bitstream and a
deterministic decoding process for bounded continuous-time MOSAIC Cells and
objective Innovation.

The stable public filename extension is `.scenelith`. A synchronized `.orka`
package belongs to the separate Orkela/SceneLith AV Bridge mapping and does
not change standalone SceneLith decoding semantics.

A frame is not a unit of state mutation, motion, or reference memory. A
`Presentation Query` is a read-only sample of the current state. The accepted
implementation architecture is the **CBF — Causal Basis Field visual ISA**.
The first reference implementation is limited to static and linear
translation. The syntax MAY allow bounded, profile-gated affine and projective
laws. Depth, 3D primitives, and unrestricted learned decoding are not part of
Main-0.

## 2. Terms

- **WorldState** — bounded normative scene state.
- **Truth Core** — reconstruction path eligible for state and reference use.
- **Truth Innovation** — transmitted objective correction to the structural
  render.
- **Perceptual Detail** — optional synthetic display-only correction.
- **Mutation EventBlock** — validated block containing State Events.
- **Read-only EventBlock** — block that does not mutate `WorldState`.
- **Memory Access Point (MAP)** — independent recovery point containing a
  complete valid `WorldState`.
- **Scene Epoch** — bounded lifetime of a namespace and its state.
- **MOSAIC Cell** — bounded state record that synthesizes a scalar Gate \(g\)
  and color Contribution \(c\) from immutable Basis content.
- **CBF** — Causal Basis Field visual ISA in which a Cell is a bounded
  spacetime Basis atom.
- **State Event** — atomic change to one or more Cells at a given timestamp.
- **Presentation Query** — read and composition of state at a timestamp
  without mutation.
- **Content Bank** — bounded coordinate-independent storage containing only
  confirmed Truth samples or inline objective payload.
- **Support** — conservative bounded union of allowed dyadic microtiles for
  storage, scheduling and culling; its border is not a visible shape.
- **Gate** — bounded fixed-point scalar field \(g(p,t)\) that determines the
  fraction of the previous Canvas retained when a Cell is applied.
- **Contribution** — bounded fixed-point color field \(c(p,t)\).
- **Affine composition** — the only composition operation inside a bounded
  layer: \(Canvas'=g\,Canvas+c\). Clipping occurs at the normative layer
  boundary.
- **MotionLaw** — absolute fixed-point mapping from local Content coordinates
  to output coordinates over a specified time interval.
- **CELL_SET** — creates, updates, or terminates a Cell.
- **STATE_RESET** — clears state and begins a self-contained Scene Epoch.
- **PRESENT** — compatibility Presentation Query with optional objective Truth
  payload.
- **DPM** — separate experimental baseline from
  `../docs/13_MINIMAL_PATCH_CORE.md`, not time/state architecture Main-0.

## 3. Conformity language

The key words MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY are to be
interpreted as described by RFC 2119 and RFC 8174.

## 4. Basic requirements

1. A decoder MUST reconstruct the Truth Core deterministically.
2. Perceptual Detail MUST NOT participate in reference prediction.
3. Perceptual Detail MUST NOT change WorldState.
4. A damaged or unverified State Event MUST NOT be used.
5. MAP MUST allow decoding without packets preceding MAP.
6. A bitstream MUST be self-contained with respect to every parameter required
   for normative decoding.
7. A decoder MUST reject streams that exceed profile or level limits.
8. Every transmitted adapter, dictionary, and weight MUST be counted in the
   bitrate.
9. Main profile MUST NOT require an arbitrary executable graph.
10. Main Truth reconstruction MUST NOT depend on device floating-point
    behavior.
11. PRESENT MUST NOT change WorldState.
12. The absence of a State Event MUST preserve the previous valid Cell state;
    per-presentation `HOLD` syntax MUST NOT be required.
13. Main-0 MotionLaw MUST belong to the profile-defined bounded set:
    `STATIC`, absolute fixed-point `LINEAR_TRANSLATION`, `AFFINE` or
    `PROJECTIVE`; first reference implementation MUST implement at least
    `STATIC` and `LINEAR_TRANSLATION`.
14. MotionLaw MUST be evaluated relative to immutable Cell Content and MUST NOT
    recursively warp a previous Presentation output.
15. Main-0 Support MUST be a bounded union of profile-defined dyadic
    microtiles, used only as conservative storage and culling bounds.
16. Main-0 MUST NOT define separate circle, polygon, or arbitrary rasterizer
    primitives.
17. Visible footprint MUST be determined by the Gate, not the Support boundary.
18. Any unresolved output region MUST use a state-independent objective
    `REPLACE` fallback.
19. `CAPTURE_TRUTH` MUST read only completed, verified post-filter
    Truth output.
20. Concealment and Perceptual Detail MUST NOT be stored in the Content Bank.
21. State Events MUST be applied atomically only after integrity and bounds checks.
22. Main-0 MUST NOT require depth, a separate semantic alpha object, a mesh,
    2.5D or 3D primitives, scene semantics, or a learned decoder. The scalar
    Gate in requirement 26 is not a separate object type.
23. An output sample at a timestamp not present in the source ground truth
    MUST be marked as interpolated unless a separate Truth payload validates
    its fidelity.
24. Outside a Cell's Support, a decoder MUST use the identity Cell value
    \(g=1,c=0\).
25. Cell application inside a composition layer MUST use only the affine pair
    \(Canvas'=g\,Canvas+c\), followed by profile-defined clipping at the layer
    boundary.
26. Gate MUST allow binary and fractional coverage with profile-defined
    precision; rectangular storage boundary MUST NOT appear in output.
27. Every interpolation footprint MUST be fully defined by guard or apron
    samples, or be completed by objective fallback.
28. Lossless profile MUST allow pixel-exact full-output fallback.
29. Cell evaluation MUST use immutable Basis and absolute parameter
    laws; recursive reference to a previous presentation is prohibited.
30. A profile or level MUST define an absolute maximum number of non-identity
    Cell contributions per output pixel and a fixed composition-layer count.
31. **TARGET:** the general Main level uses no more than 4 contributions, 4
    layers, 8 texture samples, and approximately 128 simple integer operations
    per output pixel. Final normative limits follow conformance experiments.
32. If a candidate representation exceeds these limits, the encoder MUST use
    objective Innovation fallback. A decoder MUST reject a stream that exceeds
    its declared limits.
33. Inside the composition layer affine pairs MAY merge:
    \[
    (g_2,c_2)\circ(g_1,c_1)=
    (g_2g_1,\ g_2c_1+c_2).
    \]
    Reduction MUST preserve coded order and use a profile-defined wide
    accumulator.
34. Clipping MUST occur at a profile-defined layer boundary. An implementation
    MUST produce output independent of the chosen parallel reduction tree.

## 5. Abstract decoding process

A decoder processes records strictly in coded order:

1. Validate EventBlock syntax, bounds, resource limits, and integrity.
2. On `STATE_RESET(t)`, clear all Cells, the Content Bank, and the namespace.
3. For `CELL_SET(t)`:
   1. expire Cells with `death_time <= t`;
   2. build changed Content, Support, and MotionLaw fields in staging;
   3. allow `CAPTURE_TRUTH` only from an existing confirmed
      Truth output;
   4. atomically commit the new state version.
4. For `PRESENT(t)`:
   1. expire Cells with `death_time <= t`;
   2. evaluate the absolute MotionLaw of each active Cell;
   3. synthesize Gate \(g_i\) and Contribution \(c_i\) for each Cell;
   4. combine pairs \((g_i,c_i)\), preserving coded order, inside fixed
      layers; apply \(Canvas'=gCanvas+c\) and normative clipping at each
      layer boundary;
   5. use state-independent objective fallback to define all unresolved
      pixels;
   6. apply normative in-loop and output filters;
   7. save verified Truth output as the only valid future
      capture source;
   8. independently apply or skip Optional Perceptual Detail;
   9. produce display output without mutating `WorldState`.

A host MAY request an additional timestamp in a continuous-output profile.
Such a query only uses the already active state and does not create a reference.

## 6. WorldState limits

Each profile or level MUST define:

- maximum volume of state;
- maximum number of cells;
- maximum Content Bank size;
- allowed microtile sizes and maximum number of support entries;
- maximum number of active/moving cells per output tile;
- maximum number of State Events and motion knots per time interval;
- maximum number of recent references;
- maximum Scene Epoch duration;
- maximum compute class;
- maximum number of changed/dirty output tiles on compatibility PRESENT.

## 7. Reference graph

- A Mutation EventBlock MAY depend only on confirmed Truth state.
- Read-only EventBlock MAY depend on state and explicitly listed Truth
  outputs.
- Perceptual output MUST NOT appear in the dependency graph.
- The dependency graph MUST be acyclic inside an independently decodable
  interval.
- `PRESENT` MUST read the state snapshot after every earlier State Event at the
  same timestamp and before every later record in coded order.
- CELL_SET MUST NOT read partially committed state.
- Recursive reference to a previous interpolated presentation is prohibited.

## 8. Random access

MAP MUST:

- execute `STATE_RESET`;
- contain self-contained Cells or a full-screen objective fallback;
- fully define the first `PRESENT`;
- not use `KEEP` or `CAPTURE_TRUTH` before the corresponding source is defined;
- not refer to a previous Scene Epoch.

Main-0 does not define partial state repair. The Content Bank is rebuilt after
a MAP.

## 9. Error behavior

After an integrity failure, a decoder:

- MUST NOT commit State Events;
- MAY display concealment presentation;
- MUST mark the state and output as degraded;
- MUST resume state-dependent decoding no earlier than the next MAP.

## 10. Main operator set - NORMATIVE-DRAFT

- fixed-width add/multiply/accumulate;
- lifting/wavelet;
- exact microtile copy;
- bounded Support-list traversal;
- bounded absolute fixed-point translation, affine, or projective coordinate
  law;
- deterministic affine-pair composition and order-preserving tree reduction;
- residual add/replacement, clamp and normative in-loop filter;
- rANS decode;
- STATE_RESET, CELL_SET and PRESENT.

The final microtile sizes, precision, saturation and rounding will be
determined after the first conformance experiments.

## 11. Security requirements

A decoder MUST:

- check all sizes before allocation;
- enforce profile-defined cycle and memory limits;
- never execute code from the bitstream;
- protect against integer overflow and malformed entropy state;
- check offsets and tile directories;
- fail deterministically instead of invoking undefined behavior.

## 12. Unsolved sections

- final binary syntax;
- profile/level table;
- chroma/HDR processing;
- reference color conversion;
- conformance vectors;
- exact entropy tables;
- container mapping;
- decoder capability signaling;
- exact Cell-count, Content Bank, and microtile limits;
- binary syntax STATE_RESET/CELL_SET/PRESENT;
- fixed-point timebase and maximum motion interval;
- clipping/coverage rule on output bounds;
- exact dirty-tile derivation;
- exact order of in-loop filters relative to CAPTURE_TRUTH;
- continuous-output API and interpolated timestamps marking;
- relationship between compatibility `PRESENT` and container sample tables.

Deferred beyond Main v0 to measured marginal gain:

- pixel-exact persistent masks;
- partial slot update;
- depth/2.5D/3D;
- exposure integration;
- learned/generative decoder;
- state snapshots and partial repair.
