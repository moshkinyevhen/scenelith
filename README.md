# SceneLith

**SceneLith** is a standalone video codec and an open research project for
representing dynamic visual scenes. Its internal architecture is:
**MOSAIC — Memory-Oriented Scalable Asymmetric Integer Codec**.

> **SceneLith Video — powered by MOSAIC.**

The canonical project formula is:

\[
Video(t)=Render(WorldState_t,\ Trajectories_t)
       + TruthInnovation_t
       + OptionalPerceptualDetail_t.
\]

SceneLith transmits a bounded deterministic scene state and only the new
information needed to keep that state faithful. Its accepted implementation
architecture is the **CBF — Causal Basis Field visual ISA**. A frame is not a
reference-memory, motion, or state-mutation unit: long-lived MOSAIC Cells
change asynchronously, while an image at time \(t\) is a read-only query of
the current state.

## Documentation

- [Documentation index](docs/INDEX.md)
- [Project charter](docs/00_CHARTER.md)
- [North Star and invariants](docs/01_NORTH_STAR.md)
- [MOSAIC architecture](docs/02_MOSAIC_ARCHITECTURE.md)
- [Continuous-time Cells](docs/14_CONTINUOUS_TIME_CELLS.md)
- [CBF acceptance and final red team](docs/16_CBF_ACCEPTANCE_AND_FINAL_RED_TEAM.md)
- [Implementation language and player runtime](docs/17_IMPLEMENTATION_LANGUAGE_AND_RUNTIME.md)
- [SceneLith-0 normative draft](spec/SCENELITH-0.md)
- [JVET CfP 2026 plan](docs/05_JVET_CFP_2026.md)
- [Decision log](docs/10_DECISION_LOG.md)
- [Primary sources](docs/REFERENCES.md)

## Status

The project is defining its architecture and preparing a falsifiable reference
implementation. The current external milestone is a complete
improved-compression response to the 2026 JVET call, subject to eligibility
and measured results.

All unverified compression, complexity, quality, and schedule figures are
explicitly marked as **TARGET** or **HYPOTHESIS**. They are not performance
claims.

Public repository:
[github.com/moshkinyevhen/scenelith](https://github.com/moshkinyevhen/scenelith).

## Implementation stack

- portable dependency-free C++20 Golden Core;
- stable C ABI for applications, bindings, and hardware test benches;
- Rust for secure parsing, streaming, scheduling, and the player runtime;
- Python/PyTorch for encoder research and training;
- C++/CUDA for the first accelerated Studio/Foundry encoder;
- exact scalar, SIMD, WASM, D3D12, Vulkan, and Metal decoder backends.

See
[Implementation Language and Player Runtime](docs/17_IMPLEMENTATION_LANGUAGE_AND_RUNTIME.md)
for the portability and real-time contract.

## GitHub synchronization

A repository-local `post-commit` hook automatically pushes every explicitly
created local commit to `origin`. It never stages files and never creates
commits.

Enable the hook after a fresh clone:

```powershell
.\scripts\enable-auto-sync.ps1
```

Run an explicit `fetch + pull --rebase + push`:

```powershell
.\scripts\sync.ps1
```
