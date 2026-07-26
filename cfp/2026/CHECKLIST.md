# SceneLith-CfP-2026: executable checklist

Status: **TARGET**. No item without the mark `[x]` is considered completed.

Official basis:
[ITU-T SG21 TD 348/PLEN - JVET-AQ2021-v1](https://www.itu.int/md/T25-SG21-260706-TD-PLEN-0348/en).
A complete interpretation of the requirements is stored in
[JVET CfP 2026](../../docs/05_JVET_CFP_2026.md).

## 0. Fixed scope

- [ ] **ACCEPTED:** submit one complete `C0` unrestricted improved-compression test case.
- [ ] We do not declare runtime-constrained `C1` `5x`, `C2` `1x`, `C3` `0.2x` without a separate
  solutions and ready-made complete deliverables.
- [ ] Confirmed: `C0` includes all 7 categories, 30 sequences and 5 rates.
- [ ] Confirmed: **150 main `.bit` files** and 150 main reconstructions are required.
- [ ] One person responsible for the final package has been appointed; only it changes the release manifest.
- [ ] Created risk register: registration, organization, fee, compute, Ubuntu portability,
  storage/shipping, hidden set, cross-check, training/IPR.

## 1. After architecture candidate: applicant route, contacts, assets

- [ ] **D-018:** architecture implementation candidate accepted; reminder about
  registration completed.
- [ ] No later than 2026-08-20, internal go/no-go for applicant route has been resolved.
- [ ] The chair has confirmed whether independent individual is allowed as
  proponent and what to indicate in the required field `organization`.
- [ ] A submitting applicant/organization and a payer capable of
  confirm purchase order.
- [ ] A letter was written to Jens-Rainer Ohm - `ohm@ient.rwth-aachen.de`.
- [ ] A letter was written to Mathias Wien - `wien@lfb.rwth-aachen.de`.
- [ ] Requested VTM anchors, all test sequences and official configuration information.
- [ ] Exact SSD delivery address and packaging procedure requested.
- [ ] The order of participation of submitter outside JVET in the January 2027 meeting has been requested.
- [ ] A budget of up to **EUR 20,000** has been reserved for one formal subjective test case.
- [ ] SSD primary, SSD verified duplicate and tracked international shipping are reserved.
- [ ] The possibility of purchase order confirmation no later than 2026-10-26 has been verified.

## 2. Formal registration: 2026-08-01—2026-09-01

- [ ] Annex E is filled in: organization.
- [ ] Annex E is filled in: contact person and email.
- [ ] Marked `Test case on improved compression`.
- [ ] Runtime-constrained test cases are not marked.
- [ ] The number of cases for subjective evaluation is indicated: `1`.
- [ ] Confirmed encoder/decoder executables for Ubuntu 24.04 x86-64.
- [ ] If the platform is different, written approval has been obtained from the coordinator.- [ ] If necessary, a separate Section 6 additional-functionality contribution is marked.
- [ ] Registration sent to both contact persons no later than 2026-09-01.
- [ ] Confirmation of registration and proponent ID `Pyy` received.
- [ ] 2026-09-07 final fee/formal offer received.
- [ ] Formal offer agreed upon by the submitting organization.

## 3. Official test matrix

### SDR RA UHD/4K

- [ ] SRU1 CrowdRun: R1—R5.
- [ ] SRU2 DrivingPOV3: R1—R5.
- [ ] SRU3 FireDance: R1—R5.
- [ ] SRU4 HallwayScene: R1—R5.
- [ ] RAP interval: 32 for 25 fps; 64 for 50/60 fps.

### SDR RA HD

- [ ] SRH1 DucksTakeOff: R1—R5.
- [ ] SRH2 TravelerSwim: R1—R5.
- [ ] SRH3 Seeking: R1—R5.
- [ ] SRH4 Umbrella: R1—R5.
- [ ] RAP interval does not exceed anchor.

### SDR LB HD

- [ ] SLH1 Beatriz: R1—R5.
- [ ] SLH2 GregoryCactus2: R1—R5.
- [ ] SLH3 GregoryScarf2: R1—R5.
- [ ] SLH4 OfficeWalkAtWall: R1—R5.
- [ ] Encoder and preprocessing accept pictures only in display order.
- [ ] Picture look-ahead is missing.
- [ ] Structural delay does not exceed anchor.
- [ ] Output picture reordering missing.

### HDR-PQ RA UHD

- [ ] HPQ1 ChandelierCropBR: R1—R5.
- [ ] HPQ2 FashionLadyCrop1: R1—R5.
- [ ] HPQ3 MeridianHDR2: R1—R5.
- [ ] HPQ4 SparksWelding: R1—R5.
- [ ] HDRTools 0.26 path and PQ metrics tested.

### HDR-HLG RA UHD

- [ ] HLG1 WaterfallForest: R1—R5.
- [ ] HLG2 WomenFootball: R1—R5.
- [ ] HLG3 AMS06: R1—R5.
- [ ] HLG4 SeaWalk: R1—R5.
- [ ] HLG reconstruction and display metadata checked.

### Gaming LB HD/UHD

- [ ] GLH1 DOTA2s360: R1—R5.
- [ ] GLH2 GTAVs090: R1—R5.
- [ ] GLH3 Level1: R1—R5.
- [ ] GLH4 Minecraft: R1—R5.
- [ ] GLU5 Wukong2: R1—R5.
- [ ] GLU6 Carla5: R1—R5.
- [ ] LB no-lookahead and structural-delay constraints checked.

### UGC RA

- [ ] URH1 Camellia: R1—R5.
- [ ] URH2 Hobby-w5xz-backpack: R1—R5.
- [ ] URH3 Sports-76a2-iceball: R1—R5.
- [ ] URH4 VerticalVideo-3709-snow: R1—R5.
- [ ] Portrait and landscape paths go through one decoder binary.

### Matrix completion

- [ ] `30 sequences × 5 rates = 150` rows are present in the release manifest.
- [ ] For each row there is `.bit`, reconstruction, aggregate CSV, per-frame CSV and MD5.
- [ ] No bitstream exceeds target bitrate.
- [ ] All sources are verified with official MD5 from CfP/assets coordinator.

## 4. Anchor and evaluation harness

- [ ] Fixed the exact VTM 23 revision applied by the coordinator.
- [ ] JVET-AP2010 SDR configurations are fixed.
- [ ] JVET-AO2011 HDR/WCG configurations are fixed.
- [ ] Default VTM anchors are decoded locally.- [ ] Anchor metrics are reproduced by HDRTools 0.26 with the required precision.
- [ ] VTM runtime measurement is played on the selected CPU machine.
- [ ] Proposal and anchor are measured using the same method and on the same medium.
- [ ] Aggregate runtime: sum rate points per sequence → geometric mean sequences → anchor ratio.
- [ ] Multithread runtime is calculated as the sum of CPU-time threads, not wall-clock.
- [ ] All preprocessing/multipass operations are included in encoder runtime.
- [ ] All required postprocessing is included in the decoder runtime.
- [ ] Peak encoder and decoder memory are collected.
- [ ] PSNR Y/U/V and MS-SSIM Y/U/V are collected.
- [ ] wPSNR Y/U/V collected for HDR-PQ.

## 5. SceneLith-CfP codec core

- [ ] Self-contained `.bit`: no external model/parameter files.
- [ ] Bounded deterministic WorldState.
- [ ] Full WorldState checkpoint in each random-access point.
- [ ] Decode after RAP does not read any byte/state before RAP.
- [ ] Trajectory/warp syntax has fixed bounds.
- [ ]TruthInnovation always has an objective fallback.
- [ ] Optional Perceptual Detail is not a reference.
- [ ] Optional Perceptual Detail does not change WorldState.
- [ ] One decoder supports SDR/HDR, portrait/landscape, RA/LB, HD/UHD.
- [ ] All normative operations give bit-exact output on repeated decode.
- [ ] Embedded fixed weights included in binary; stream-specific parameters are located in `.bit`.
- [ ] Full bitrate includes state, checkpoints, masks, trajectories, parameters, headers and indexes.

## 6. Encoder strategy

- [ ] Foundry/offline encoder is allowed only in `C0`; the absence of a runtime cap does not hide
  complexity reporting.
- [ ] Each preprocessing stage is listed and measured.
- [ ] Each multipass stage is listed and measured.
- [ ] Representation search/RDO reproducible from config.
- [ ] There is no manual configuration that is not reflected in the config and technical description.
- [ ] Per-sequence optimization is either missing or explicitly documented.
- [ ] Rate control allows only a documented one-time reduction in RD setting.
- [ ] Full-resolution coding is used or the reduced-resolution concept is described.
- [ ] Encoder automatically handles unknown hidden sequences.
- [ ] For each encode job, the command line, config hash, binary hash and logs are saved.

## 7. Training provenance

- [ ] CfP test sequences and their parts are missing from all training sets.
- [ ] Checked duplicates/near-duplicates between training corpus and CfP material.
- [ ] For each learned component, the training corpus is indicated.- [ ] Training scripts, configs, checkpoints and dependency versions saved.
- [ ] Determined what training materials can be provided to JVET.
- [ ] For unavailable materials, a retraining plan has been prepared using permitted data.
- [ ] Model license and dataset license have been verified.
- [ ] Training equations/parameter derivation are ready to be revealed after selection.

## 8. Ubuntu binaries

- [ ] A clean Ubuntu 24.04 x86-64-v3 runner has been created.
- [ ] Encoder starts without network access.
- [ ] Decoder starts without network access.
- [ ] Decoder command line supports `-b input.bit -o output.yuv`.
- [ ] One decoder binary processes all 150 streams.
- [ ] All dynamic libraries are listed; missing dependency test passed.
- [ ] CPU feature detection does not extend beyond x86-64-v3.
- [ ] Output — 10-bit YUV 4:2:0 `.yuv` or `.pyuv`.
- [ ] Double decode of each stream gives the same MD5.
- [ ] Corrupt/truncated input fails with a controlled error.
- [ ] README with command line and configs verified by an independent operator.

## 9. Metrics and naming

- [ ] Filenames correspond to `xxxx_Pyy_Rz_C0.eee`.
- [ ] `Pyy` matches the proponent ID coordinator.
- [ ] `.bit` contains all decoder information.
- [ ] Aggregate CSV uses `;` separator and required decimal precision.
- [ ] Per-frame CSV is present for each stream.
- [ ] Per-frame bit counts are consistent with complete stream size.
- [ ] Recon MD5 in CSV matches actual `.yuv`.
- [ ] MD5 manifest covers all package files.
- [ ] Formal subjective material prepared for R1—R4.
- [ ] R5 is included in objective/runtime evaluation.

## 10. Main package freeze and SSD: official deadline 2026-10-26

- [ ] Internal decoder/syntax freeze: **TARGET 2026-09-15**.
- [ ] Distributed pipeline ready: **TARGET 2026-09-30**.
- [ ] All 150 streams validated: **TARGET 2026-10-09**.
- [ ] Encoder executables and relevant configs are enabled.
- [ ] One decoder executable is enabled.
- [ ] 150 self-contained `.bit` files included.
- [ ] 150 packed 10-bit 4:2:0 reconstructions included.
- [ ] Aggregate and per-frame CSV enabled.
- [ ] Instructions included.
- [ ] MD5 manifest is enabled and verified after copying to SSD.
- [ ] Purchase order confirmation received.
- [ ] SSD tested on an independent Ubuntu machine: **TARGET 2026-10-16**.
- [ ] Verified duplicate SSD is saved separately.
- [ ] Primary SSD sent tracked delivery: **TARGET 2026-10-19**.
- [ ] Test coordinator confirmed receipt until **2026-10-26**.

## 11. Hidden supplemental set: 2026-11-02—2026-12-21- [ ] Frozen binaries and configs are saved with cryptographic hashes.
- [ ] Hidden sequences were received on 2026-11-02 and registered without being placed in the training corpus.
- [ ] A fully automatic encode pipeline has been launched.
- [ ] Each hidden stream falls into 80%—100% target bitrate.
- [ ] The same main encoder/decoder binaries are used.
- [ ] New external parameters/models are not used.
- [ ] Prepared hidden `.bit`, configs, reconstructions, CSV and MD5.
- [ ] Supplemental package frozen: **TARGET 2026-12-14**.
- [ ] Supplemental package received by coordinator until **2026-12-21**.
- [ ] Supplemental package transferred to cross-checkers 2026-12-23.

## 12. Mandatory cross-check

- [ ] The other party's main package assignment has been received.
- [ ] Cross-check is performed in an isolated environment.
- [ ] Encoder configs, decoder output, MD5 and metrics have been checked.
- [ ] Inconsistencies are reported by chair/coordinator without publishing the identity proponent.
- [ ] Main cross-check report sent until 2027-01-06.
- [ ] Received supplemental package assignment.
- [ ] Supplemental cross-check completed until 2027-01-13.
- [ ] Our package was successfully reproduced by the assigned cross-checker.

## 13. Technical document: official deadline 2027-01-06

- [ ] Conceptual overview explains all data paths.
- [ ] Bitstream and decoder architecture are described sufficiently for equivalent implementation.
- [ ] Languages, libraries, platforms and build process are listed.
- [ ] Training material and provenance revealed.
- [ ] Preprocessing, postprocessing, perceptual optimization and multipass are described.
- [ ] Random-access structure and maximum pictures-to-access are described.
- [ ] LB structural delay, buffering and reordering are described.
- [ ] Runtime relative to VTM measured on the same environment.
- [ ] Complexity reporting template is complete.
- [ ] Peak memory and parallel-processing capability are described.
- [ ] Error resilience, scalability and other functions are described without unproven claims.
- [ ] TARGET/HYPOTHESIS are not represented as measured result.
- [ ] JVET input document is registered and submitted before 2027-01-06.
- [ ] Presenter registered for the meeting 2027-01-13—22.

## 14. Source and IPR readiness

- [ ] The relevant source is highlighted, which reproduces the submitted output.
- [ ] Reference source does not contain secrets, credentials and prohibited dependencies.
- [ ] Training scripts/equations prepared for core experiments.
- [ ] License inventory is ready.
- [ ] Patent landscape review completed.
- [ ] Common Patent Policy obligations reviewed by counsel/authorized representative.
- [ ] The position for licensing essential claims has been determined.- [ ] Post-submission corrections do not change results without JVET approval.

## 15. Subjective test and January evaluation

- [ ] Fee paid/issued under a formal offer.
- [ ] R1—R4 subjective reconstructions checked.
- [ ] Tested native-resolution playback 24/25/30/50/60 fps.
- [ ] Internal DCR/DSIS dry run completed.
- [ ] Internal MOS are not issued as official JVET result.
- [ ] Received JVET MOS/CI summary 2027-01-13.
- [ ] Objective results and runtime table are verified.
- [ ] Presentation separates measured facts from targets/hypotheses.
- [ ] The team is ready to answer on complexity, training, RAP, LB delay, source and IPR.

## 16. Section 6 fallback

- [ ] An additional-functionality document about persistent WorldState has been prepared separately.
- [ ] Scalability and compute-bounded decoding are described.
- [ ] The separation of Truth Core and non-reference Perceptual Detail is described.
- [ ] Checkpoint, repair and error-resilience semantics are described.
- [ ] The material is not called formal compression response without the full `C0`.
- [ ] Document submitted by the deadline of the 45th JVET meeting, if the main `C0` is disrupted.

## 17. Final go/no-go

- [ ] **GO:** registration confirmed.
- [ ] **GO:** fee and physical delivery provided.
- [ ] **GO:** all 150 main streams are valid.
- [ ] **GO:** one frozen Ubuntu decoder plays all MD5.
- [ ] **GO:** RAP/LB constraints are proven by tests.
- [ ] **GO:** training/IPR provenance ready.
- [ ] **GO:** hidden-set pipeline does not require code changes.
- [ ] **GO:** independent package rehearsal completed.

If any required GO clause is not satisfied by internal freeze, the package is not declared
full JVET CfP submission; Section 6 fallback is launched and the reason is recorded.