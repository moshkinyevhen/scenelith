# JVET CfP 2026: official SceneLith bid outline

Document status: **NORMATIVE-DRAFT** for branch `SceneLith-CfP-2026`.

Primary source review date: **2026-07-26**.

This document separates the external requirements of JVET from the goals and hypotheses of SceneLith:

- **FACT - JVET**: requirement or fact from an approved Call for Proposals.
- **ACCEPTED - SceneLith**: Accepted project branch constraint.
- **TARGET - SceneLith**: a deadline or result that has not yet been achieved.
- **HYPOTHESIS - SceneLith**: a technical idea that requires measurement.

The main primary source is an approved document
[ITU-T SG21 TD 348/PLEN, JVET-AQ2021-v1](https://www.itu.int/md/T25-SG21-260706-TD-PLEN-0348/en)
([direct DOCX](https://www.itu.int/dms_pub/itu-t/md/25/sg21/td/260706/PLEN/T25-SG21-260706-TD-PLEN-0348%21%21MSW-E.docx)).
Official [JVET page](https://www.itu.int/en/ITU-T/studygroups/2025-2028/21/video/Pages/jvet.aspx)
confirms the release of the joint CfP in July 2026. Concurrent ISO/IEC official record
is on the MPEG page
[Enhanced compression beyond VVC capability](https://www.mpeg.org/standards/Explorations/41/).

## 1. CfP subject

**FACT - JVET.** CfP is looking for a generation of video compression technology that is significantly superior
VVC Main 10 not only for compression efficiency, but also for:

- implementability encoder and decoder;
- diversity of content and applications;
- latency and robustness;
- scalability and additional functionality;
- practical encoding speed.

**FACT - JVET.** Formal evaluation of the proposal is scheduled for the 45th JVET meeting in January
2027. The first prospective test model is expected to begin to be selected in January 2027,
complete the initial selection no later than October 2027 and complete the first version of the standard
in October 2029.

## 2. Official calendar

| Date | FACT - JVET |
|---|---|
| 2026-05-31 | VTM anchors, runtime-constrained VTM encodings, additional VTM encodings with RPR and encoder configurations are available. |
| 2026-07-17 | Call for Proposals released. The approved TD is dated 2026-07-15. |
| 2026-08-01 | Formal registration opens. |
| 2026-09-01 | Formal registration closes. |
| 2026-09-07 | The final testing fee is determined; test coordinator sends a formal offer. |
| 2026-10-26 | Main submission package must be received by test coordinator; confirmation of the purchase order is required by the same date. |
| 2026-11-02 | The formal subjective assessment begins; planned completion - 2026-12-21. |
| 2026-11-02 | Proponents receive an additional hidden set of sequences. |
| 2026-11-30 | Main package is provided by cross-checkers; Participation of proponents in cross-check is mandatory. |
| 2026-12-21 | Supplemental package for the additional set must be received by the test coordinator. || 2026-12-23 | Supplemental package provided by cross-checkers; the review must be completed by 2027-01-13. |
| 2027-01-06 | Deadline for registration and submission of documents with a technical description of the proposal. |
| 2027-01-06 | Deadline for the cross-check main package report. |
| 2027-01-13 | Proponents and JVET receive summary subjective and objective results. |
| 2027-01-13—22 | Evaluation of proposals at the JVET meeting. |

**FACT - JVET.** The critical deadline for the executable codec is not January, but **2026-10-26**:
By this day we need working binaries, all the main bitstreams and reconstructions.

## 3. Registration and participation

**FACT - JVET.** Annex E must be sent no later than **2026-09-01** to both recipients:

- Jens-Rainer Ohm, JVET chair – `ohm@ient.rwth-aachen.de`;
- Mathias Wien, test coordinator - `wien@lfb.rwth-aachen.de`.

The form contains:

- organization;
- contact person and email;
- select unrestricted improved-compression test case;
- selection of runtime-constrained test cases;
- expected runtime targets: `0.2x`, `1x`, `5x`;
- number of test cases requested for subjective test;
- confirmation of encoder/decoder executables for Ubuntu 24.04 x86-64 or another request
  platforms at coordinator;
- a note about the proposal for additional functionality under Section 6;
- remarks.

**FACT - JVET.** CfP invites companies and organizations. JVET provisional membership
not declared as a condition of registration. Chair directly promises to help submitters outside JVET with
participation in the January meeting.

**FACT - ITU.** For continuous participation and submission of contributions through ITU-T, Sector Members are available,
Associate selected by Study Group and Academia. Current participation rights are described at
[ITU official page](https://www.itu.int/hub/membership/become-a-member/participation/),
and fees are on the page
[ITU-T Categories and Fees](https://www.itu.int/en/ITU-T/membership/Pages/Categories-and-Fees.aspx).

**ACCEPTED - SceneLith, D-018.** External registration deferred until selected
architecture implementation candidate. Owner Plan - Enroll As
independent private applicant; legal name is not kept in public
technical repository before registration is required.

**OPEN / UNVERIFIED.** This intent does not mean permissibility: CfP
invites companies/organizations, and Annex E requires the `organization` field.
Immediately after acceptance of the architecture candidate, and well in advance before
2026-09-01, request in writing from chair/test coordinator:

1. is an independent individual allowed as a proponent;
2. what to write in `organization` if there is no legal entity;
3. proponent ID;
4. test sequences, anchors and configuration information;
5. precise delivery logistics;
6. the participation procedure for a submitter outside JVET in January 2027.

**TARGET:** internal go/no-go by registration route - no later than
2026-08-20 so that the possible answer chair does not end up on the critical path to
2026-09-01.

## 4. Test cases

### 4.1 Mandatory completeness

**FACT - JVET.** Four test cases are defined:

1. unrestricted improved compression;
2. improved compression with encoder runtime around `5x` default VTM;
3. improved compression with encoder runtime around `1x` default VTM;
4. improved compression with encoder runtime around `0.2x` default VTM.

It is not necessary to participate in all four. However, each selected test case requires
full results for **all seven categories**. Incomplete proposal may not be considered.

**FACT - JVET.** One complete test case contains:

- 30 test sequences;
- 5 rate points per sequence;
- **150 main bitstreams**;
- corresponding 150 reconstructed sequences;
- aggregate and per-frame results;
- hidden supplemental set of no more than 50% of the main content.

### 4.2 Complete Core Set

All bitrates below are in kbit/s and are listed as `R1 / R2 / R3 / R4 / R5`.

#### SDR RA UHD/4K

Category format: 3840×2160, YCbCr 4:2:0 BT.709, 10 bit, random access.

| SID | Sequence | Frames@fps | Target bitrates |
|---|---|---:|---:|
| SRU1 | CrowdRun | 500 @ 50 | 700 / 1500 / 3200 / 7000 / 14000 |
| SRU2 | DrivingPOV3 | 600 @ 60 | 300 / 600 / 1200 / 2400 / 4800 |
| SRU3 | FireDance | 250 @ 25 | 400 / 800 / 1500 / 2500 / 5000 |
| SRU4 | HallwayScene | 250 @ 25 | 150 / 250 / 500 / 1000 / 2000 |

#### SDR RA HD

Category format: 1920×1080, YCbCr 4:2:0 BT.709, random access.

| SID | Sequence | Bit depth | Frames@fps | Target bitrates |
|---|---|---:|---:|---:|
| SRH1 | DucksTakeOff | 8 | 500 @ 50 | 300 / 900 / 2400 / 4000 / 8000 |
| SRH2 | TravelerSwim | 10 | 500 @ 50 | 150 / 300 / 600 / 1200 / 2400 |
| SRH3 | Seeking | 8 | 500 @ 50 | 200 / 400 / 800 / 1600 / 3200 |
| SRH4 | Umbrella | 8 | 500 @ 50 | 300 / 600 / 1400 / 3500 / 7000 |

#### SDR LB HD

Category format: landscape 1920×1080 or portrait 1080×1920, YCbCr 4:2:0 BT.709,
low-delay B-picture configuration.

| SID | Sequence | Orientation / bit depth | Frames@fps | Target bitrates |
|---|---|---:|---:|---:|
| SLH1 | Beatriz | L/8 | 500 @ 50 | 70 / 140 / 280 / 550 / 1100 |
| SLH2 | GregoryCactus2 | P/10 | 300 @ 30 | 200 / 600 / 1500 / 4000 / 8000 |
| SLH3 | GregoryScarf2 | P/10 | 300 @ 30 | 200 / 600 / 1800 / 5000 / 10000 |
| SLH4 | OfficeWalkAtWall | L/8 | 300 @ 30 | 90 / 200 / 450 / 1000 / 2000 |#### HDR-PQ RA UHD

Category format: YCbCr 4:2:0, 10 bit, BT.2100 PQ, random access. UHD/4K/8K sources
cropped to 3840x2160 for evaluation.

| SID | Sequence | Transfer | Frames@fps | Target bitrates |
|---|---|---|---:|---:|
| HPQ1 | ChandelierCropBR | HDR10 PQ | 360 @ 60 | 300 / 650 / 1300 / 2800 / 5600 |
| HPQ2 | FashionLadyCrop1 | HDR10 PQ | 380 @ 60 | 250 / 650 / 1700 / 4500 / 9000 |
| HPQ3 | MeridianHDR2 | P3 PQ 4000 nits | 600 @ 60 | 150 / 300 / 600 / 1200 / 2400 |
| HPQ4 | SparksWelding | HDR10 PQ 1000 nits | 600 @ 60 | 400 / 1000 / 2500 / 6000 / 12000 |

#### HDR-HLG RA UHD

Category format: YCbCr 4:2:0, 10 bit, BT.2100 HLG, random access. UHD/4K/8K sources
cropped to 3840x2160 for evaluation.

| SID | Sequence | Frames@fps | Target bitrates |
|---|---|---:|---:|
| HLG1 | WaterfallForest | 500 @ 50 | 1000 / 2500 / 6000 / 14000 / 28000 |
| HLG2 | WomenFootball | 500 @ 50 | 300 / 600 / 1100 / 2000 / 4000 |
| HLG3 | AMS06 | 600 @ 60 | 600 / 1300 / 3500 / 8000 / 16000 |
| HLG4 | SeaWalk | 500 @ 50 | 200 / 400 / 800 / 1800 / 3600 |

#### Gaming LB HD/UHD

Category format: YCbCr 4:2:0 BT.709, low-delay B-picture configuration.

| SID | Sequence | Raster/bit depth | Frames@fps | Target bitrates |
|---|---|---:|---:|---:|
| GLH1 | DOTA2s360 | 1920x1080 / 8 | 550 @ 60 | 180 / 300 / 550 / 1000 / 2000 |
| GLH2 | GTAVs090 | 1920x1080 / 8 | 600 @ 60 | 400 / 900 / 2000 / 3600 / 7200 |
| GLH3 | Level1 | 1920x1080 / 10 | 600 @ 60 | 400 / 1000 / 2000 / 4000 / 8000 |
| GLH4 | Minecraft | 1920x1080 / 8 | 600 @ 60 | 300 / 600 / 1200 / 2400 / 4800 |
| GLU5 | Wukong2 | 3840x2160 / 10 | 600 @ 60 | 1000 / 2400 / 6000 / 14000 / 28000 |
| GLU6 | Carla5 | 3840x2160 / 8 | 600 @ 60 | 1100 / 2200 / 4300 / 8500 / 17000 |

#### UGC RA

Category format: landscape 1920×1080 or portrait 1080×1920, YCbCr 4:2:0 BT.709,
8 bit, random access.

| SID | Sequence | Orientation | Frames@fps | Target bitrates |
|---|---|---:|---:|---:|
| URH1 | Camellia | P | 600 @ 60 | 200 / 400 / 800 / 1600 / 3200 |
| URH2 | Hobby-w5xz-backpack | P | 240 @ 24 | 90 / 160 / 280 / 500 / 1000 |
| URH3 | Sports-76a2-iceball | L | 600 @ 60 | 80 / 160 / 250 / 400 / 800 |
| URH4 | VerticalVideo-3709-snow | P | 300 @ 30 | 80 / 160 / 300 / 500 / 1000 |

MD5 source sequences are part of the official CfP tables and must be verified
directly with TD 348 and materials received from the coordinator.

## 5. Anchors and coding configurations

**FACT - JVET.**

- Anchor is described by VVC Test Model 23 and JVET-AO2002.
- SDR common test conditions and software reference configurations are specified by JVET-AP2010.- HDR/WCG conditions are specified by JVET-AO2011.
- Default VTM is the basis for relative compression performance and runtime.
- For runtime curve, high-performance VTM configuration is provided approximately `2x` default
  and three reduced-time variants approximately `0.2x`—`0.75x` default.
- VTM encodings with reference picture resampling are additionally available.
- The official reference implementation is in
  [VVCSoftware_VTM](https://vcgit.hhi.fraunhofer.de/jvet/VVCSoftware_VTM).

**FACT - JVET.** For random-access categories:

- intra refresh period anchor is 32 for 24/25/30 fps;
- intra refresh period anchor is 64 for 50/60 fps;
- the proposal is obliged to provide random access at least less frequently;
- after random-access point decoder is obliged to restore the stream after deleting **all**
  information preceding this point.

**ACCEPTED - SceneLith.** Each CfP random-access point contains a self-sufficient
WorldState checkpoint. No pre-RAP condition is required. Optional Perceptual Detail
does not participate in checkpoint, prediction or WorldState changes.

**FACT - JVET.** For low-delay categories:

- output picture reordering is not applied;
- overall structural delay proposal does not exceed anchor;
- encoder and preprocessing process pictures in display order;
- picture look-ahead is prohibited.

## 6. General encoding rules

**FACT - JVET.**

1. Bitstream should not exceed the target bitrate.
2. All rate points are encoded in full input resolution. If reduced-resolution coding is
   part of the algorithm, it needs to be described.
3. Quantization/RD settings should remain static. One small change allowed
   only towards a lower bitrate for the remaining part of the stream; it needs to be documented.
4. Manual and per-sequence optimization is discouraged and should be exposed.
5. No part of test sequences can be used for training entropy tables, VQ
   codebooks, transforms, predictors, filters, neural models and other parts of codec.
6. Training material for the trained parts of the algorithm must be disclosed.
7. Preprocessing, postprocessing, perceptual optimization and multi-pass encoding, as well as their
   the impact on compression performance must be described.
8. Preprocessing time is included in encoder runtime; required postprocessing is included in
   decoder runtime.
9. If the proposal uses special optimization, it is recommended to provide an anchor with
   equivalent optimization.

### Runtime measurement

**FACT - JVET.**

- With multithreading, runtime is equal to the sum of the time of all threads, and not wall-clock time.- With segment-wise parallelism, it is recommended to summarize runtime segments.
- Anchor and proposal are measured using the same methodology.
- For sequence, the time of all rate points is first summed up; then take the geometric mean by
  sequences; then the ratio to the anchor is calculated.
- For runtime-constrained cases, the goals are `5x`, `1x`, `0.2x` aggregate default VTM runtime.
- An exact match is not required, but the points must cover comparable runtime/compression
  curve.
- Decoder runtime target is missing, but runtime and complexity implementation are required
  reported and taken into account.

**FACT - JVET.** Unrestricted improved-compression case does not introduce a hard encoder limit
runtime. This allows a very heavy offline encoder, but does not exclude runtime from the evaluation:
the full time and degree of optimization is required to be disclosed.

## 7. Main submission package — 2026-10-26

**FACT - JVET.** Materials are delivered to the SSD at the test coordinator address. Receipt must
take place no later than the deadline; The risk of delivery and media failure is borne by proponent.

Required:

1. bitstreams for all sequences, rate points and selected test cases;
2. encoder binaries and corresponding configuration settings;
3. one decoder executable for all selected test cases;
4. instructions for command line and configuration parameters;
5. reconstructed 10-bit YUV 4:2:0 sequences;
6. Annex D CSV with aggregate objective metrics;
7. separate per-frame CSV for each sequence/rate combination;
8. MD5 checksums of all files, preferably in one manifest;
9. Confirmed purchase order for subjective testing.

**FACT - JVET.**

- Executables should be built for **Ubuntu 24.04, x86-64-v3**. For another platform you need
  Agree the order in advance with the coordinator.
- One decoder should accept bitstream and output path, for example
  `decoder -b input.bit -o output.yuv`.
- Decoder produces 10-bit 4:2:0 `.yuv` or `.pyuv`.
- Proposal bitstream has the extension `.bit`.
- Bitstream can be proprietary, but must contain all the information for decoding.
  External parameter/model files are not allowed.

Naming:

```text
xxxx_Pyy_Rz_Cw.eee
```

where `xxxx` — SID, `yy` — proponent ID, `z` — rate 1…5, `w` — test case:

- `C0`: unrestricted improved compression;
- `C1`: runtime `5x`;
- `C2`: runtime `1x`;
- `C3`: runtime `0.2x`.

`P00` is reserved for VVC anchor. Extensions: `bit`, `pyuv`, `csv`.

## 8. Hidden supplemental set

**FACT - JVET.**- Additional sequences are issued **2026-11-02**, after main binaries and bitstreams.
- The volume of material is expected to be no more than 50% of the main test content.
- Resolutions, content types, structural delay and bitrate ranges will be similar to the main set.
- Supplemental bitstreams must fall within the range of 80%—100% of the specified target bitrate.
- The same binaries sent to the main package must encode and decode the hidden set.
- Until **2026-12-21** bitstreams, configs, reconstructions, CSV and MD5 are sent.
- New encoder/decoder executables are not included in the supplemental package list.

**ACCEPTED - SceneLith.** Decoder and bitstream semantics for CfP are frozen before main
submission. You cannot rely on hard-coded test sequence knowledge or manual
per-sequence learning. Hidden-set generalization is a release gate.

## 9. Cross-check

**FACT - JVET.**

- Cross-checking checks binaries, configs, reconstruction reproducibility and correctness
  metrics.
- Packages are distributed between other parties without disclosing the proposing party.
- The participation of each proponent in checking someone else’s package is mandatory.
- Main package is transferred to cross-checkers 2026-11-30.
- Main cross-check report required 2027-01-06.
- Supplemental cross-check must be completed by 2027-01-13.

## 10. Technical proposal document — 2027-01-06

**FACT - JVET.** The document must allow experts to conceptually understand the proposal,
reproduce equivalent performance and evaluate the degree of optimization. Required:

- all data-processing paths and components that form the bitstream;
- implementation languages, external libraries and supported build platforms;
- random-access behavior and maximum pictures-to-access;
- encoding/decoding delay, reordering, buffering, multipass decisions and parallelization;
- encoder/decoder runtime relative to VTM on the same environment;
- completed complexity reporting template;
- degree of parallel processing;
- additional functionality: resilience, scalability, 4:4:4, etc.

## 11. Source code, training and IPR

**FACT - JVET.** Main submission accepts binaries, but if technology is selected for
further research:

- relevant source code becomes a condition for participation in core experiments and possible inclusion
  in reference software;
- source must reproduce the results of the proposal;
- relevant technology may include training scripts or equations for obtaining parameters;
- expected availability of training materials for testing or retraining on an available JVET
  material;
- valid
  [Common Patent Policy for ITU-T/ITU-R/ISO/IEC](https://www.itu.int/ITU-T/dbase/patent/patent-policy.html).## 12. Formal subjective assessment

**FACT - JVET.**

- Formal subjective testing is carried out only for R1-R4 main package.
- R5 is used for objective metrics and runtime.
- All sequences and rates, including hidden set, undergo objective evaluation.
- If there is a large number of proposals, the chair and coordinator can choose a representative subset for
  subjective testing.
- Method - DCR/DSIS: uncompressed reference, then processed sequence.
- An 11-level impairment scale is planned from `0` - severely annoying to `10` - imperceptible.
- Native resolution is required; viewing distance - `1.5H`.
- MOS and confidence interval are published separately for each sequence; different sequences are not
  are combined into one graph.

The technique refers to
[ITU-R BT.500](https://www.itu.int/rec/R-REC-BT.500) and
[ITU-T P.910](https://www.itu.int/rec/T-REC-P.910).

## 13. Testing fee

**FACT - JVET.**

- Fee covers formal subjective assessment.
- Expected maximum - **EUR 20,000 for each test case** included in the subjective test.
- Partial test case is considered complete when determining fee.
- Proponent indicates how many submitted cases it wants to include in the subjective assessment.
- The final set is decided at the 44th JVET meeting for maximum comparability.
- The total amount is reported on 2026-09-07; confirmation of purchase order is required by 2026-10-26.

## 14. Narrow strategy SceneLith-CfP-2026

### 14.1 Scope

**ACCEPTED - SceneLith.** One complete `C0` unrestricted is being prepared for the current CfP
improved-compression test case. Runtime-constrained `C1`—`C3` are not included in the initial response.
This reduces deliverables from a potential 600 to 150 main bitstreams without weakening
formal completeness of the selected case.

**ACCEPTED - SceneLith.** The CfP branch does not attempt to implement the entire future MOSAIC. She must
save canonical model:

\[
Video(t)=Render(WorldState_t,\ Trajectories_t)
       + TruthInnovation_t
       + OptionalPerceptualDetail_t
\]

but is limited to the minimum checked set:

1. bounded deterministic WorldState;
2. self-sufficient checkpoint on each RAP;
3. bounded `MOSAIC Cell` with Support, Lifetime and
   `STATIC/LINEAR_TRANSLATION` MotionLaw;
4. objective TruthInnovation residual;
5. self-contained bitstream;
6. one reproducible decoder;
7. Optional Perceptual Detail only if it does not threaten objective reconstruction,
   term and hidden-set generalization.

### 14.2 Fastest implementation path

**HYPOTHESIS - SceneLith.** The fastest way to a complete application is to use
tested VTM-compatible residual backend as transport/fallback and add
small SceneLith subset: asynchronous `CELL_SET`, persistent linear motion runs,compact `CAPTURE_TRUTH` content and read-only `PRESENT`. This measures the effect
frame-free state without simultaneously reinventing each codec layer.

**HYPOTHESIS - SceneLith.** Foundry encoder may receive additional
gain through multi-pass analysis of the entire RA epoch, flow, support/lifetime
search, compact-content reuse and RDO. Depth/3D/semantic decoder are not included
fastest path.

**TARGET — SceneLith.** Any gain must be calculated based on the full bitstream, including:

- WorldState checkpoint;
- Cell Content/Support/Lifetime events;
- MotionLaw knots and presentation metadata;
- embedded parameters/weights;
- TruthInnovation;
- headers, indexes and checksums.

### 14.3 CfP release gates

**TARGET - SceneLith.**

1. All 150 main bitstreams are decoded by one Ubuntu binary.
2. Repeated decode gives byte-identical output and MD5.
3. Each RA stream starts without data before RAP.
4. Low-delay categories do not use look-ahead.
5. Each bitstream fits into a target; hidden streams - 80%—100%.
6. Training provenance is fully documented; CfP material is not included in training.
7. Full runtime includes preprocessing, multipass and postprocessing.
8. Package is played by an independent cross-check runner.
9. Hidden set goes through the same frozen binaries.
10. Offline encoder complexity is revealed honestly and is not masked by wall-clock parallelism.

## 15. Project buffer dates

These are internal goals, not JVET dates.

| TARGET - SceneLith | Result |
|---|---|
| 2026-08-01 | formal registration sent; proponent ID and assets received/requested. |
| 2026-08-07 | Anchor pipeline and Annex D metrics are played locally. |
| 2026-08-21 | First self-contained `.bit` round trip on Ubuntu 24.04. |
| 2026-09-01 | Registration confirmed; Exactly one `C0` case is selected. |
| 2026-09-15 | ISA decoder, syntax and WorldState checkpoint semantics are frozen. |
| 2026-09-30 | The full 30-sequence distributed encoding pipeline is running. |
| 2026-10-09 | All 150 candidate streams passed decode/MD5/rate validation. |
| 2026-10-16 | Main package frozen, SSD assembled and tested on an independent Ubuntu machine. |
| 2026-10-19 | SSD shipped with tracked delivery; verified duplicate saved. |
| 2026-10-26 | Official main deadline without using an internal buffer. |
| 2026-11-02 | Hidden-set encoding is launched automatically by the frozen toolchain. |
| 2026-12-14 | Supplemental package frozen one week before the official deadline. |

## 16. Section 6 fallback, not equal to formal proposal

**FACT - JVET.** Additional functionality can be provided as a separate contribution todocument deadline for the 45th meeting. This material:

- not included in the main submission package;
- does not participate in formal subjective test;
- does not require mandatory pre-meeting cross-check;
- may receive expert viewing or informal demonstration.

**TARGET - SceneLith.** Even if the complete failure `C0` prepare Section 6 contribution about:

- persistent scene state;
- compute/scalability dimensions;
- truth-preserving base and non-reference perceptual detail;
- state checkpointing and error recovery.

This is insurance for SceneLith's presence in the discussion, but **not** a replacement for a full-fledged formal
compression response.
