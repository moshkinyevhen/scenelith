# SceneLith Solution Log

Last update: 2026-07-26

## D-001 - Name and architecture

- Date: 2026-07-26
- Status: **ACCEPTED**
- Solution:
  - the project is called **SceneLith**;
  - architecture is called
    **MOSAIC - Memory-Oriented Scalable Asymmetric Integer Codec**.

## D-002 - Master Formula

- Date: 2026-07-26
- Status: **ACCEPTED**
- Solution:

\[
Video(t)=Render(WorldState_t,\ Trajectories_t)
       + TruthInnovation_t
       + OptionalPerceptualDetail_t
\]

## D-003 - Project Root

- Date: 2026-07-26
- Status: **ACCEPTED**
- Decision: all canonical materials and project code are stored in the
  SceneLith repository.

## D-004 - Reference safety

- Date: 2026-07-26
- Status: **ACCEPTED**
- Solution: Only deterministic Fidelity/Truth Core can change
  `WorldState` and used as a temporal reference. Perceptual Shell
  always non-reference and switchable.

## D-005 - New standardization object

- Date: 2026-07-26
- Status: **ACCEPTED**
- Solution: SceneLith standardizes limited visual scene machine and flow
  innovation, and is not just another extension of the block hybrid codec.

## D-006 — Deadline of the current JVET CfP

- Date: 2026-07-26
- Status: **ACCEPTED**, replaces the previous rating
- Solution: prepare a full formal unrestricted improved-compression
  response by October 26, 2026.
- Supersedes: statement from the original text that the submission is complete
  proposal in this window is “unrealistic”. It is now classified as
  extremely risky, but formally feasible deadline mission.

## D-007 - Separate CfP branch

- Date: 2026-07-26
- Status: **ACCEPTED**
- Solution: create `SceneLith-CfP-2026` with a narrow deterministic kernel:
  bounded state, trajectories, multi-frame innovation, mandatory RAPs
  checkpoints and reliable residual fallback. Don't block the thread with an attempt
  simultaneously implement the entire future MOSAIC.

## D-008 – Three class encoder

- Date: 2026-07-26
- Status: **ACCEPTED**
- Solution: one decoder/bitstream serves:
  - `Live` — causal real-time;
  - `Studio` - consumer GPU with lookahead and limited multipass;
  - `Foundry` - distributed hyperscale/offline scene compiler.

## D-009 — Foundry as teacher

- Date: 2026-07-26
- Status: **ACCEPTED**
- Solution: RDO traces Foundry are used for distillation of small
  consumer-router. A household encoder should extract at least 80–90% of the total
  delta Foundry after maturation.

## D-010 - Documentation is canonical

- Date: 2026-07-26
- Status: **ACCEPTED**
- Solution: all new standards and ideas from the chat are written into the project files.
  Historical sources are saved in `archive/`; changes are reflected throughthis journal, and not through the silent rewriting of history.

## D-011 - QINTRA Re-Evaluation

- Date: 2026-07-26
- Status: **SUPERSEDED** by decision D-016
- Question: should QINTRA be used instead of SceneLith due to the shorter and
  memorable sound.
- Preliminary conclusion:
  - QINTRA is really more striking as a codec name;
  - SceneLith better conveys the central idea and is more unique;
  - QINTRA phonetically conflicts with an existing technology/software name
    Quintra and requires professional trademark verification.
- Historical output D-011: SceneLith remained the project name, and the role of QINTRA
  has not yet been accepted. This pin has been replaced by D-016.

## D-012 - Recommended Codex Sol mode

- Date: 2026-07-26
- Status: **SUPERSEDED** by decision D-013
- Recommendation:
  - for the SceneLith root task use Sol Ultra;
  - for the only mode without delegation, use Sol XHigh;
  - Max reserve for freeze and hardest single-problem reviews;
  - High/XHigh used for the main implementation;
  - Medium/Low is used for mechanically verifiable mass tasks.
- Reason: maximum project throughput requires combining deep reasoning
  on irreversible decisions with rapid implementation and test iterations.

## D-013 - Actual Force Levels 5.6 Sol

- Date: 2026-07-26
- Status: **ACCEPTED**
- Correction: D-012 used internal English notation and incorrectly
  included `Max`, which is not in the current user interface.
- Solution: the SceneLith working scale must correspond verbatim to the model picker:
  - **Light**;
  - **Average**;
  - **High**;
  - **Very tall**;
  - **Ultra**.
- For current design of the canonical standard is used
  **"Ultra"**. For single brainstorming without fixing the solution, it is enough
  **"Very high"**.
- Distribution:
  - Ultra - standard architecture, bitstream/state freeze, integration and
    parallel adversarial review;
  - Very high - one complex algorithm, RDO or bit-exact debugging;
  - High - implementation according to an already defined specification;
  - Medium - documentation and reproducible tests;
  - Easy - trivial mechanical changes.

## D-014 - Observed Surface Memory instead of a complete completed world

- Date: 2026-07-26
- Status: **SUPERSEDED** by decision D-015 for the first experiment gate and
  solution D-017 as a core architecture candidate
- Candidate solution:
  - Main Truth Core stores only minimally sufficient observed surfaces
    fragments;
  - unknown texel is an explicit state and cannot be used aspredictor;
  - the never-output area is not transmitted or generated;
  - `CAPTURE_PROMOTE` saves already restored Truth pixels in persistent
    state without repeated texture payload;
  - the unknown, which first appeared in output, is restored objective
    `REPLACE/TruthInnovation`, after which it can be saved for reuse;
  - Full 3D and generation are optional Main v0 paths;
  - Foundry/router remains a non-standard mechanism for finding profitable fragments,
    lifecycle and representation solutions.
- Impact on timing:
  - executable skeleton — days;
  - oracle real-shot proof - 2–3 weeks optimistically, 4–6 realistically;
  - first vertical version - 4–6 weeks optimistically, 8–12 realistically;
  - GPU/MAP/basic conformance - 6–9 weeks is optimistic, 10–16 is realistic.
- Compression hypothesis versus equal-memory strong baseline:
  - 20–45% net saving on rigid/screen long-gap reuse;
  - 10–25% on puzzle-friendly natural;
  - 4–12% for mixed natural;
  - about 0% on hostile dynamic thanks to fallback.
- All numerical ranges are **HYPOTHESIS/TARGET** and not results.
- Full development: `12_OBSERVED_SURFACE_MEMORY.md`.

## D-015 — Minimal Decoded Patch Memory as reference baseline

- Date: 2026-07-26
- Status: **ACCEPTED**
- Solution:
  - the first reference-memory test remains the minimum `DPM` with
    `RESET/PROMOTE/PLACE/DROP`, rectangles and integer copy;
  - DPM is not announced by the main QINTRA architecture until the measured gain;
  - masks, depth, 3D, semantics and learned decoder are not added to save
    negative result;
  - DPM after D-017 is the control spatial-memory baseline and possible
    a way to store content for a more general time-state core.
- Full development: `13_MINIMAL_PATCH_CORE.md`.

## D-016 - SceneLith / QINTRA / MOSAIC Hierarchy

- Date: 2026-07-26
- Status: **ACCEPTED**
- Solution:
  - **SceneLith** - project, future company and ecosystem;
  - **QINTRA** — codec/bitstream family name;
  - **MOSAIC - Memory-Oriented Scalable Asymmetric Integer Codec** -
    interior architecture;
  - marketing wording:
    **“QINTRA — a SceneLith codec, powered by MOSAIC.”**
- Before the public launch, QINTRA still requires professional
  trademark/FTO checks; this does not change the accepted product hierarchy.

## D-017 - Frame is not a unit of state, reference or motion

- Date: 2026-07-26
- Status: time/state invariants - **NORMATIVE-DRAFT / HYPOTHESIS**; original
  hard-support/composition formula - **PARTIALLY SUPERSEDED** D-021/D-022
- Candidate solution:- frame remains only compatible `PresentationSample`, that is, a request
    result at a point in time, but does not change the state itself;
  - bitstream is a stream of asynchronous state events;
  - single primitive - long-lived `MOSAIC Cell`:

    \[
    Cell_i=(Content_i,\ Support_i,\ MotionLaw_i(t),\
            Lifetime_i,\ Order_i);
    \]

  - `Lifetime` eliminates per-frame signaling `unchanged`;
  - `MotionLaw(t)` amortizes motion by interval, rather than transmitting vector to
    each output sample;
  - `Content` is stored in compact coordinate-independent memory, and does not require
    frame-sized reference;
  - the form is not selected from zoo `rectangle/circle/polygon`: `Support` is
    combining fixed dyadic microtiles; boundary accuracy increases
    only where it pays off;
  - state, motion knots, Truth Innovation and display sampling have independent
    clocks;
  - a static cell does not receive events, but its already composed output tile
    MAY be saved without re-writing;
  - movement is calculated from the absolute fixed-point law relative to the unchanged
    content, not the recursive warp of the previous output;
  - the physical display still changes the light discretely or continuously during
    time; the goal is to remove frame clock from transport/state/decode, not
    state the impossible absence of temporary sampling.
- DPM becomes baseline/component rather than final Main v0.
- Full development: `14_CONTINUOUS_TIME_CELLS.md`.

## D-018 – Time of registration and applicant status

- Date: 2026-07-26
- Status: **ACCEPTED** as project order; external validity
  **OPEN/UNVERIFIED**
- Solution:
  - first select the architecture to implement, then return to Annex E and
    other external actions;
  - owner plan - apply as an independent private applicant;
  - the legal name of the owner is not recorded in the public technical register
    documentation before registration is required;
  - when accepting the architecture implementation candidate, be sure to remind
    about registration.
- Restriction: the current CfP is addressed to companies/organizations, and Annex E requires
  field `organization`. Therefore, before promising to submit from an individual, you need
  receive written confirmation from the chair/test coordinator or agree
  valid designation of an independent applicant.

## D-019 — Public repository as portfolio and team assembly point

- Date: 2026-07-26
- Status: **TARGET**
- Goal:
  - repository, proposal, architecture paper and demo must demonstrate provably
    authorship and level of systems/research engineering of the owner;
  - the project must be prepared to attract strong external
    contributors.- Limitation: one application or big idea does not guarantee market growth
  cost. We need reproducible results, a working decoder, benchmark,
  conformance, honest status `submitted/evaluated/adopted` and understandable
  contribution path.

## D-020 - Baselines and a double revolutionary goal

- Date: 2026-07-26
- Status: **ACCEPTED**
- Solution:
  - primary compression baselines are always reported separately:
    **AV2 v1.0 / AVM v1.0.0** and **VVC / H.266 (2026) / VTM**;
  - entry `AV2/VVC` without two separate results is prohibited in claims and
    benchmark tables;
  - applicable BRU, long-term-reference, Show Existing Frame, Atlas, affine,
    merge and other baseline tools must be enabled;
  - QINTRA’s goal is to radically surpass both baselines not only in bitrate, but also
    due to the simplicity of the normative decoder code;
  - AV1/HEVC/AVC and fast hardware presets can be secondary baselines, but
    defeating them does not prove achievement of the frontier goal.

## D-021 - One-equation Spacetime Basis Cell

- Date: 2026-07-26
- Status: **ARCHITECTURE CANDIDATE / HYPOTHESIS**
- Reason:
  - paper sensitivity model rejects lifetime/HOLD-only as a path to
    revolutionary mixed-natural compression;
  - against representative AV2 ledger for total gain 25% needs to be eliminated
    about 31.8% of all remaining AV2 innovation bits; at 50% cell coverage this is
    63.6% residual in the covered part, and with coverage below 31.8% the target
    is mathematically impossible for a given ledger.
- Candidate:

  \[
  (g_i,c_i)(p,t)=\sum_k a_{i,k}(t)B_{i,k}(W_i(p,t)),
  \]

  - one Cell should describe static, motion, appearance variation and
    persistent/transient Truth Innovation;
  - the only composition operation:
    \(Y_{j+1}=Clip(g_jY_j+c_j)\);
  - Cell is a bounded rate-distortion atom, not a semantic object;
  - `RESET/SET` are sufficient state grammar; presentation - read-only
    container/API query;
  - normative evaluation must be fixed-point, bounded and data-parallel;
  - unrestricted neural graph, semantic world, depth/mesh and generative Truth
    not included in Main;
  - payload synthesizer remains the main **OPEN** choice.
- Full argumentation and reproducible sensitivity model:
  `15_PAPER_KILL_TEST_AND_FREEZE.md` and
  `../experiments/paper_kill_test.py`.

## D-022 — Visible shape is not equal to storage tile

- Date: 2026-07-26
- Status: **ACCEPTED REQUIREMENT / CANDIDATE MECHANISM**
- Requirement:
  - rectangle, dyadic tile and texture allocation MAY are used only as
    invisible storage, scheduling and culling bounds;
  - the border of the storage unit MUST NOT become the visible border of the image;
  - QINTRA MUST support arbitrary binary and soft coverage, includingantialiasing, hair, transparency and motion blur;
  - lossless profile MUST have pixel-exact fallback;
  - lossy profiles MUST have RDO fallback and separate boundary-quality
    check.
- Candidate mechanism:
  - Cell synthesizes scalar gate \(g\) and color contribution \(c\);
  - outside support implicitly \(g=1,c=0\);
  - a single affine compositor \(Y'=Clip(gY+c)\) covers replace, alpha-over and
    additive correction without shape primitive zoo;
  - conservative padding and texture apron prohibit sampling seams.
- Physical limitation:
  - the absence of any artifacts cannot be guaranteed at an arbitrarily small
    lossy bitrate;
  - the absence of tile-shape artifacts and exact lossless path are guaranteed.

## D-023 — Leading payload candidate: cached integer basis synthesis

- Date: 2026-07-26
- Status: **RESEARCH CANDIDATE / OPEN**
- Candidate:
  - one fixed bounded int8/int16 synthesis graph decodes quantized latents
    in immutable Basis Content;
  - optional per-shot adaptation is limited to low-rank integer matrices;
  - all latents/adapters are included in bitrate;
  - synthesis is performed on `SET`, and not on each Presentation Query;
  - renderer remains texture-sample + temporal MAC + \(gY+c\);
  - sparse exact correction preserves objective/lossless Truth.
- Reason:
  - a regular AV2/VVC intra payload would retain their decoder code complexity;
  - a simple linear wavelet is the easiest, but has a lower chance of radical
    reduce innovation;
  - fixed integer nonlinear synthesis has better theoretical balance
    compression, a small normative decoder, and GPU/ASIC regularity.
- This does not mean adopting neural renderer: arbitrary graph, floating point,
  generative Truth and per-presentation inference remain prohibited.

## D-024 - Numerical Radical Superiority Bar

- Date: 2026-07-26
- Status: **TARGET**
- Minimum architecture-success target:
  - at least 25% net BD-rate reduction separately against AV2 v1.0/AVM and
    VVC/H.266/VTM on broad mixed corpus;
  - at the same time a simpler bounded normative decoder.
- Stretch North Star:
  - 40% against the stronger of two anchors on broad mixed/coherent corpus;
  - 50% on broad screen/UI corpus;
  - absence of tile-shape artifacts and exact lossless path.
- 5–10% universal gain is useful, but not enough to make a new claim
  revolutionary standard.

## D-025 - CBF Visual ISA adopted as implementation architecture

- Date: 2026-07-26
- Status: **ACCEPTED**
- Solution:
  - QINTRA Main is built as **CBF - Causal Basis Field visual ISA** inside
    MOSAIC;- CBF Cell is a bounded spacetime basis atom, not a semantic object;
  - one formula
    \[
    (g_i,c_i)(p,t)=\sum_k a_{i,k}(t)B_{i,k}(W_i(p,t))
    \]
    describes static, motion, appearance variation, arbitrary soft visible
    shape and persistent/transient Truth Innovation;
  - unified state grammar - `STATE_RESET / CELL_SET`; presentation is
    read-only query;
  - immutable Basis, absolute-time coordinate/parameter laws, implicit
    persistence and objective fallback are frozen semantic spine;
  - unrestricted neural renderer, semantic world graph and generative Truth are not
    are included in Main;
  - D-021 changes status from architecture candidate to **ACCEPTED** in part
    semantic spine; payload synthesizer and exact limits remain
    **NORMATIVE-DRAFT/HYPOTHESIS**.

## D-026 — Bounded composition algebra and mobile decode envelope

- Date: 2026-07-26
- Status: **ACCEPTED / NORMATIVE-DRAFT**
- Solution:
  - Cell describes affine color pair \((g,c)\);
  - the sequential composition pair is associative:
    \[
    (g_2,c_2)\circ(g_1,c_1)=
    (g_2g_1,\ g_2c_1+c_2);
    \]
  - parallel reduction MAY be used while preserving coded order;
  - internal clip after each Cell is prohibited where profile-defined
    wide accumulator and range proof allow clip on a fixed layer
    boundary; this reduces serial dependency and GPU traffic;
  - Main general target: no more than 4 non-identity Cell contributions per
    output pixel, no more than 4 fixed composition layers, no more than 8 texture
    samples and about 128 simple integer operations/pixel;
  - exact absolute limits are set by profile/level; everything above them is encoded
    objective Innovation fallback;
  - Main MAY allow bounded translation, affine and projective coordinate
    laws, but the first reference implementation starts with static/translation.

## D-027 — Consumer encoder and hardware targets

- Date: 2026-07-26
- Status: **TARGET / HYPOTHESIS**
- Solution:
  - reference Consumer/Studio encoder must run on one regular PC and
    8 GB-class GPU via spatial/temporal tiling and long-term offloading
    state in host RAM;
  - RTX 2080 Super is the first practical development target, but not
    normative dependence of the format;
  - for one minute 1080p30 working hypotheses:
    first prototype `1–6 h`, Consumer Fast `3–10 min`, Balanced
    `20–90 min`, Local Foundry `3–12 h`;
  - 1080p60 is expected to take about 2 times longer, 4K30 - 4–6 times;
  - software mobile-GPU target: flagship 1080p60 and plausible 4K30,
    mid-range 1080p30–60; CPU-only target: 720p60 or 1080p30 with low
    overlap;
  - these figures are hypotheses, not measured results or conformance
    requirements.

## D-028 — The last red-team: strong ideas without ISA extension

- Date: 2026-07-26
- Status: **ACCEPTED / RESEARCH**
- Accepted in encoder/core discipline:
  - conditional-description-length RDO instead of simple detector `changed`;
  - whole-shot bidirectional analysis and time-symmetric Foundry search,
    compiled into the same absolute laws;
  - content-addressed dedup immutable Basis inside self-contained asset;
  - persistent and ephemeral Truth use the same Cell with different Lifetime;
  - new models must be compiled in `B/W/a/g/c/SET`.
- **RESEARCH** remains until a separate net-gain gate:
  - deterministic stochastic microtexture predictor plus exact residual;
  - state-only hidden observer for future prediction;
  - shared cross-asset dictionaries;
  - learned integer Basis synthesis.
- Not added:
  - primitive zoo;
  - mandatory 3D reconstruction;
  - semantic object truth;
  - external mandatory model;
  - recursive presentation reference.

## D-029 - Video, audio and AV binding are separate objects

- Date: 2026-07-26
- Status: **ACCEPTED**
- Solution:
  - QINTRA was the then-current standalone video-codec name;
  - an independent audio codec with MAF architecture is developed separately;
    `Resonith` was the leading but not yet final name candidate;
  - SceneLith AV Bridge is a separate binding specification;
  - no standalone Truth bitstream depends on another modality;
  - AV Bridge MAY separate timeline, entity IDs, trajectories and
    room/geometry hints, but does not mix Truth reference graphs.

## D-030 - External registration reminder point reached

- Date: 2026-07-26
- Status: **ACCEPTED / ACTION DEFERRED**
- Event:
  - D-025 accepted the architecture implementation candidate, so the condition
    reminder from D-018 completed;
  - before external submission requires confirmation from the chair/test coordinator
    Admissibility of an independent private applicant and completion of the field
    `organization`;
  - technical development of audio-first continues without waiting for this
    external response.

## D-031 - Standalone audio codec name approved

- Date: 2026-07-26
- Status: **ACCEPTED**
- Solution:
  - the independent MAF Audio codec is finally called **Resonith**;
  - wording D-029 about the candidate status of the name **SUPERSEDED**;
  - QINTRA and Resonith maintain separate repositories and bitstreams;
  - SceneLith AV Bridge remains a separate binding.

## D-032 - The video codec is finally called SceneLith

- Date: 2026-07-26
- Status: **ACCEPTED**- Owner's decision:
  - final product name standalone video codec and its bitstream
    family - **SceneLith**;
  - the name **QINTRA** is removed from the current branding due to a conflict with
    an existing company in Germany;
  - D-011 and D-016 regarding the adoption of QINTRA become **SUPERSEDED**;
  - the internal name of the architecture remains
    **MOSAIC - Memory-Oriented Scalable Asymmetric Integer Codec**;
  - the first normative draft is called **SceneLith-0**;
  - individual products are called **SceneLith Video** and **Resonith Audio**;
  - SceneLith AV Bridge links them without merging bitstreams or Truth
    reference graphs;
  - recommended name of the public GitHub repository video codec -
    `scenelith`.

## D-033 - Public GitHub and secure auto-sync

- Date: 2026-07-26
- Status: **ACCEPTED**
- Solution:
  - SceneLith Video and Resonith Audio are published in separate public GitHub
    repositories `scenelith` and `resonith`;
  - every explicitly created local commit is automatically sent to
    `origin` repo-local hook;
  - background automatic addition of files or creation of commits is prohibited,
    so that incomplete data and secrets do not end up in public history;
  - before each first public push, secret/PII scan, tests and
    checking the composition of tracked files;
  - after clone, auto-synchronization is enabled by an explicit bootstrap script.

## D-034 — Public repository SceneLith created

- Date: 2026-07-26
- Status: **IMPLEMENTED**
- Result:
  - public repository:
    `https://github.com/moshkinyevhen/scenelith`;
  - default branch: `main`;
  - initial public commit: `343eb92`;
  - CI launches deterministic paper sensitivity model;
  - repo-local `post-commit` auto-push is enabled and subject to verification by this
    subsequent commit.

## D-035 — English is the sole public repository language

- Date: 2026-07-26
- Status: **ACCEPTED / IMPLEMENTED**
- Decision:
  - all public specifications, documentation, code comments, commit messages,
    issue and pull-request templates, and GitHub metadata use English;
  - conversation with the project owner may use another language, but the
    repository is the international canonical record;
  - historical material in another language remains outside the public
    repository or receives a complete English record;
  - the existing public working tree is migrated to English without rewriting
    published Git history.

## D-036 — Portable Golden Core and safe player runtime

- Date: 2026-07-26
- Status: **ACCEPTED / ENGINEERING DECISION**
- Decision:
  - the bit-exact Golden Core and production codec kernels use restricted,
    dependency-free C++20 behind a stable versioned C ABI;
  - Rust owns untrusted parsing, streaming, scheduling, capability
    negotiation, sandbox boundaries, and the cross-platform player runtime;
  - Python/PyTorch remain the research and training environment;
  - the first accelerated Studio/Foundry encoder uses C++/CUDA, while the
    format never depends on CUDA or any GPU API;
  - scalar C++ is mandatory, and SIMD, WASM, D3D12, Vulkan, and Metal are
    exactly equivalent optional acceleration backends;
  - the Core has no mandatory operating-system, filesystem, network, UI,
    machine-learning-runtime, or third-party runtime dependency;
  - supported deployment targets include Windows, Linux, macOS, iOS, Android,
    browsers, embedded/DSP systems, and future ASIC implementations;
  - cross-compiler conformance hashes, sanitizers, fuzzing, static analysis,
    reproducible builds, ABI tests, and CPU/GPU differential tests are release
    gates.
- Canonical engineering document:
  `17_IMPLEMENTATION_LANGUAGE_AND_RUNTIME.md`.

## D-037 — High-signal commenting and deterministic debug visibility

- Date: 2026-07-26
- Status: **ACCEPTED / ENGINEERING DECISION**
- Decision:
  - source comments are a maintained engineering interface for human and AI
    debugging;
  - public APIs, normative kernels, state transitions, security boundaries,
    concurrency, and non-obvious numerical behavior require concise contract
    comments;
  - complex functions use a few named logical phases when this makes the
    pipeline visibly easier to inspect;
  - comments that merely restate code, line-by-line narration, decorative
    banners, duplicated specifications, and dead commented-out code are
    prohibited;
  - every `TODO`, `FIXME`, approximation, and unexplained constant carries a
    tracked issue or decision identifier and a removal gate;
  - deterministic structured traces expose parse, validate, stage, render,
    commit, fallback, and reject phases, but are disabled by default in
    real-time loops;
  - stale comments fail review and must be updated with behavior in the same
    commit.
- Canonical contract:
  section 9 of `17_IMPLEMENTATION_LANGUAGE_AND_RUNTIME.md`.

## D-038 — Canonical public names and filename extensions

- Date: 2026-07-26
- Status: **ACCEPTED**
- Decision:
  - the standalone video codec is **SceneLith**, pronounced `seen-lit`;
  - `.scenelith` is the canonical filename extension for an independent
    SceneLith visual bitstream;
  - the standalone audio codec is **Resonith**, pronounced `re-zo-nit`, and
    uses `.resonith`;
  - the standalone player is **Orkela**, pronounced `or-ke-la`;
  - `.orka` is reserved for an Orkela synchronized media package that binds
    independent streams through the SceneLith AV Bridge;
  - an `.orka` package MUST NOT merge the Resonith and SceneLith Truth
    reference graphs or make either standalone codec depend on the other;
  - FourCC, MIME type, codec string, and package binary layout remain
    unassigned until their respective registry and conformance gates pass.
