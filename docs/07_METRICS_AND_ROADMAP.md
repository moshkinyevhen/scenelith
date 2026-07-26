# Metrics and roadmap

Status: deadlines - **TARGET**, control thresholds - **ACCEPTED**.

## 1. Two parallel tracks

### Track A - SceneLith-CfP-2026

Goal: formally complete unrestricted improved-compression proposal to
October 26, 2026.

### Track B — SceneLith Main

Goal: mainstream GPU/ASIC-friendly format with Live, Studio and Foundry encoder.

The CfP branch should not freeze false trade-offs in the future
format. Useful tools are transferred to Main only after experimentation.

## 2. Aggressive implementation calendar

Countdown: 2026-07-26.

| Deadline | TARGET deliverable |
|---|---|
| 48–72 hours | Repository, charter, spec skeleton, CI and benchmark harness |
| 2–3 weeks | Self-contained bitstream skeleton, CPU decoder, wavelet/residual, multi-lane rANS |
| 6–8 weeks | SceneLith-0: bounded Cells, MotionLaw, MAP/checkpoints, GPU path |
| 12-13 weeks | Full CfP main package and honest RD results |
| 4 months | Multi-frame learned innovation prototype |
| 6 months | 1080p60 Alpha, bit-exact CPU/GPU |
| 9 months | Loss repair, HDR/screen modes, experimental Perceptual Shell |
| 12 months | Main v1 Candidate |
| 18 months | 4K60, independent tests, conformance suite, FPGA preparation |
| 24–36 months | Standard-grade specification/implementation |

A formal standard and mass silicon remain a long-standing external challenge.

### 2.1 Critical path Continuous-Time Cells

| Result | TARGET from the start of implementation |
|---|---:|
| Event/state simulator and synthetic demo | 1–3 days |
| Dirty-tile renderer, bit-exact linear translation | 4–7 days |
| Gate A and first Gate B oracle | 1–2 weeks |
| Fair AV2/VVC run comparison | 2–4 weeks |
| Compact `CAPTURE_TRUTH` Gate C | 3–6 weeks |
| GPU multi-refresh demo | 4–8 weeks |
| Broad RD/power corpus and architecture verdict | 8–16 weeks |

Demonstration of new time semantics is possible in days; strong overall compression
claim requires tool-complete AV2/VVC baselines, full bit accounting and
multiple corpus runs. Details:
[14_CONTINUOUS_TIME_CELLS.md](14_CONTINUOUS_TIME_CELLS.md).

## 3. Fidelity metrics

Required:

- bitrate, including all side information;
- PSNR-Y, PSNR-YUV;
- MS-SSIM;
- VMAF with fixed version;
- BD-rate;
- per-frame rate and quality;
- HDR-compatible objective metrics;
- random-access penalty;
- decoder runtime, MAC/pixel, peak memory and traffic.

No single metric is sufficient.

## 4. Perceptual/truth metrics

- blind MOS/DCR/DSIS;
- LPIPS/DISTS only as additional perceptual indicators;
- OCR accuracy and character error rate;
- face/identity consistency;- geometry/edge displacement;
- temporal flicker;
- color/HDR consistency;
- provenance coverage;
- synthetic-region false-negative rate.

Perceptual results are published separately from Fidelity.

## 5. Twelve-month goals

**TARGET:**

- bit-exact 1080p60 GPU decoder;
- no less than −25% BD-rate separately for AVM AV2 v1.0 and VTM VVC/H.266 on closed
  broad validation set; stretch −40% to stronger anchor;
- compact cells give at least 10% total-rate improvement on reappearance
  subset;
- innovation bits are reduced by at least 20% on the same subset;
- checkpoint/address overhead is less than 8%;
- no main content class is degraded by more than 10%.

## 6. Twenty-four month goals

**TARGET:**

- 4K60 desktop GPU;
- −35% to VTM-RA;
- minimum −10% to the strongest reproducible learned anchor of the same class
  latency/random access;
- Perceptual Shell: ≥2× bitrate reduction with equal blind MOS;
- mandatory OCR, identity, geometry and flicker gates.

## 7. Thirty-six month stretch

**TARGET:**

- −40…−45% to VTM-RA;
- minimum −15% to the modern reproducible learned codec;
- not a single large content class is worse than anchor by more than 5%;
- 2–3× perceptual reduction with equal blind MOS;
- 4–10× only for specialized VOD/UI/talking-head modes;
- Main High ≤5 kMAC/output-pixel;
- Low Compute ≤1.5 kMAC/output-pixel;
- weights ≤32 MB;
- persistent state ≤64 MB;
- random access 0.25–0.5 seconds;
- state repair ≤250 ms.

## 8. Consumer encoder requirements

**ACCEPTED:**

- a mature Studio encoder should extract 80–90% of the full Foundry savings;
- Main profile is rejected as mass if a high-quality stream is possible
  obtained only by astronomical search;
- real-time preset is part of the architecture from the first prototype, not
  late optimization.

Example TARGET:

- anchor: 100 conditional bits;
- Foundry: 55–65;
- Studio: 62–70;
- Live: 70–80.

These are illustrative goals, not measured results.

## 9. Fair-comparison protocol

Each public comparison records:

- exact commit/version anchors;
- test sequences and training leakage ban;
- RA/LB configuration;
- GOP/intra period;
- structural delay/lookahead;
- bit depth/chroma/color;
- encoder and decoder hardware;
- preprocessing/postprocessing;
- model/adaptor/checkpoint bits;
- wall time and total CPU/GPU time;
- command lines and hashes outputs.

## 10. Go/no-go

- After the first complete reappearance experiment:
  - baseline must include AV2 BRU/LTR/Atlas, VVC and equal-memory decoded
    patch cache;- if Gate B gives <12% on scroll/sprite, <7% broad screen or <3% mixed,
    do not enable persistent motion runs in universal core;
  - if compact-cell oracle gives <15% on puzzle subset or <5% mixed,
    redesign/kill compact reference path;
  - if it does not beat the equal-memory patch cache, leave a simple cache;
  - if events/support/checkpoints consume >20% gross saving, change syntax.
- After 12 months:
  - lack of measurable universal gain requires a core change
    representation.
- After 18 months:
  - if there is no ≥25% fair win separately over AV2 and VVC and no
    fundamentally new functionality, a separate new standard does not
    acquitted.

The deadline is not a reason to hide a negative result.