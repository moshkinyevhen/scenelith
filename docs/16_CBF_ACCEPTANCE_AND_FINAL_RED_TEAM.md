# CBF acceptance and final architectural red-team

Status: semantic spine - **ACCEPTED**; numerical limits - **NORMATIVE-DRAFT**;
compression estimates - **HYPOTHESIS**.

## 1. Accepted kernel

**CBF - Causal Basis Field** is a visual ISA SceneLith inside MOSAIC.

\[
(g_i,c_i)(p,t)=\sum_k a_{i,k}(t)B_{i,k}(W_i(p,t)),
\qquad
Y_{i+1}=g_iY_i+c_i.
\]

Cell does not mean an object, rectangle, face or 3D surface. It's bounded
rate-distortion atom:

- `B` — immutable reusable local Truth basis;
- `W` — absolute coordinate law;
- `a` — absolute temporal coefficient law;
- `g` — arbitrary binary/soft coverage;
- `c` — color contribution;
- `Lifetime` — action interval;
- `SET` - an event only when the law changes.

Any area of ​​arbitrary shape is specified by Gate. Rectangle/tile is only
invisible storage/culling bound. Full objective raster replacement is
exact fallback of the same affine formula.

## 2. The missing piece: algebra before clip

The strongest compute engine found does not require a new visual tool.
Affine pairs are associative:

\[
(g_2,c_2)\circ(g_1,c_1)=
(g_2g_1,\ g_2c_1+c_2).
\]

This allows you to:

- parallel prefix/tree reduction;
- one wide accumulation path;
- clip only on 2–4 fixed layer boundaries;
- reduction of serial dependency;
- less framebuffer read/write traffic;
- deterministic GPU/DSP/ASIC scheduling.

The order does not become arbitrary: reduction must preserve the coded order.
Profile specifies bit widths and range proof.

## 3. What compression does without changing the decoder

### Conditional novelty

Encoder does not update “everything that has changed”, but only information that
reduces the total conditional description length:

\[
J=R+\lambda D+\mu C+\nu M+\rho L+\kappa P.
\]

One Atom is accepted only when Basis, gate, trajectory, lifetime, indexes and
checkpoint together is cheaper objective fallback.

### Whole-shot time symmetry

Studio/Foundry MAY analyze the past and future, collect the surface from
all observations and search for globally consistent tracks. Decoder anyway
gets causal absolute laws and doesn't get complicated.

### Basis dedup

Immutable Basis gets content identity and is reused by all Cells
asset Repeated texture, recurring graphics, resurfacing region and
persistent innovation is paid once. External dictionary is not
required.

### Independent update clocks

Gate, coordinate law, appearance coefficients and Innovation are updated only
when their own parameters contain Innovation. Presentation refresh rate is not
their clock.

## 4. What else can give you a big win?

Only three directions retain a chance for large additional gain without a new
opcode zoo:

1. **Cached integer Basis synthesis** — the encoder transmits a compact latent;
   decoder once builds immutable `B`; per-pixel neural rendering
   prohibited.
2. **Deterministic stochastic field** — grain/water/foliage predictor with seed
   and sparse Truth correction; Perceptual variant is never reference.
3. **Predictive-only hidden observer state** - invisible state for
   future residual, not for display; accepted only with net gain no less
   8% on hostile natural class and bounded random access.

All three are **RESEARCH**. They should compile to `B/W/a/g/c/SET` or
wait for the next major version.

## 5. What is consciously rejected

- mandatory semantic scene graph;
- an attempt to complete the invisible world for Truth;
- depth/mesh/Gaussian primitive zoo in Main;
- unrestricted neural decoder;
- generative detail as reference;
- external model, without which the stream is not self-sufficient;
- recursive warp of the previous presentation;
- separate codec for fallback.

These mechanisms may be encoder-side hypotheses or Perceptual enhancement,
but do not complicate CBF Core.

## 6. Bounded software decode target

Main general target:

- no more than 4 non-identity contributions/output pixel;
- no more than 4 fixed composition layers;
- no more than 8 texture samples/output pixel;
- about 128 simple integer operations/output pixel;
- bounded Basis/Cell working set;
- translation/affine/projective laws only in profile limits;
- excess complexity is translated into objective Innovation.

This should allow software GPU decode prior to hardware adoption. Exact values
will be frozen by conformance experiment; device-specific performance is not
is a normative guarantee.

## 7. Consumer encoder target

The first reference encoder must have tiled mode for an 8 GB-class GPU. RTX
2080 Super is a development target, not a bitstream dependency.

For 1080p30 minute:

| Encoder | **HYPOTHESIS** |
|---|---:|
| First prototype | 1–6 h |
| Consumer Fast | 3–10 min |
| Balanced | 20–90 min |
| Local Foundry | 3–12 h |

1080p60 is expected to take approximately 2 times longer, 4K30 - 4-6 times.

## 8. Honest compression hypothesis

The report is kept separately against full AV2 and full VVC:

| Content | vs AV2 | vs VVC |
|---|---:|---:|
| Screen/UI/2D animation | 20–60% | 25–65% |
| stable/pan/reuse | 15–40% | 20–45% |
| Mixed natural, first mature generation | 5–15% | 8–20% |
| Hostile stochastic | 0–5% | 0–8% |
| Foundry mixed-natural upper hypothesis | 15–30% | 20–35% |

This is **HYPOTHESIS**, not a measured result. The revolutionary bar remainsat least 25% separately against both anchors on broad mixed corpus with more
lightweight bounded decoder.

## 9. Freeze rule

The architecture is no longer revised due to each new encoder idea.
Frozen:

```text
immutable Basis
absolute laws
arbitrary soft Gate
affine-pair composition
RESET / SET
implicit persistence
read-only presentation
objective Innovation fallback
non-reference Perceptual Detail
```

Only basis payload, entropy, precisions, transforms, profile limits are open
and encoder search. These are the parameters of one machine, not a new architecture.
