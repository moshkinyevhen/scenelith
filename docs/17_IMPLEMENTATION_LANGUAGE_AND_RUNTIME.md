# Implementation Language and Player Runtime

Status: **ENGINEERING DECISION**
Date: 2026-07-26

## 1. Decision

SceneLith is implemented as several deliberately separated layers:

1. **Portable freestanding-style C++20** is the bit-exact Golden Core:
   bitstream primitives, bounded state machine, integer Truth reconstruction,
   scalar renderer, conformance model, and ASIC-close kernels.
2. **A stable versioned C ABI** is the only mandatory integration boundary.
3. **Rust** owns untrusted package and network parsing, streaming,
   capability negotiation, resource scheduling, sandbox boundaries, and the
   cross-platform player runtime.
4. **Python 3.12+ and PyTorch** own representation research, oracle search,
   training, corpus tooling, visualization, and encoder experiments.
5. **C++20 plus CUDA** owns the first high-performance Studio/Foundry encoder
   for NVIDIA hardware. Portable CPU and Vulkan-compute encoder paths follow.
6. **HLSL, Vulkan compute/SPIR-V, and Metal compute** are non-normative,
   bit-exact acceleration backends for the decoder and player compositor.

The syntax and mathematical specification remain normative. No language,
compiler, GPU API, operating system, model runtime, or UI framework is part of
the format.

## 2. Portability invariant

The Golden Core MUST compile without a dependency on:

- a window system or presentation API;
- filesystem, sockets, or threads;
- a GPU API;
- a machine-learning runtime;
- exceptions or RTTI;
- an application allocator during decode;
- Python, Rust, or any UI toolkit.

The host provides bounded memory arenas, input spans, output surfaces,
timestamps, and optional acceleration callbacks. The same conformance vectors
MUST produce identical Truth samples on every target.

## 3. Why this is not a single-language project

Python is ideal for changing the encoder's representation search quickly, but
it is not an embedded or real-time decoder substrate. C++20 gives direct
control over fixed-point arithmetic, SIMD, GPU sharing, and vendor toolchains,
but a large C++ network-facing player would create avoidable memory-safety
risk. Rust is therefore the safe orchestration layer around a deliberately
small native codec core.

The C ABI prevents the project from coupling its public interface to either a
C++ or Rust ABI. It also enables Swift, Kotlin/Java, C#, JavaScript/WASM,
FFmpeg-like frameworks, game engines, browser hosts, and silicon validation
benches.

## 4. Repository layout target

```text
spec/                    language-independent format and decoder semantics
include/scenelith/       stable public C API
reference/cpp/           portable C++20 Golden Core
runtime/rust/            secure player and streaming runtime
bindings/python/         bindings to the exact Golden Core
research/python/         encoder oracle, RDO, training, and experiments
kernels/cuda/            NVIDIA encoder acceleration
kernels/shaders/         HLSL, Vulkan-compute, and Metal decoder kernels
players/                 thin desktop, mobile, browser, and CLI shells
tests/conformance/       golden vectors and cross-platform state hashes
tests/fuzz/              bitstream, state-machine, and scheduler fuzz targets
```

Final encoder RDO MUST call the exact Golden Core. A Python renderer may exist
as an independent oracle, but it may not silently define decoded behavior.

## 5. Player architecture

```text
native UI and platform services
              |
Rust player, scheduler, demux, security, and synchronization
              |
stable C ABI and bounded command queues
              |
C++20 SceneLith Core + optional exact compute backend
              |
display, audio, clock, storage, and network adapters
```

The UI is replaceable. Native UI, Qt/QML, Flutter, or a browser shell may be
chosen per product without changing the codec library or player runtime.

The player presents ordinary raster frames to existing monitors. A later
SceneLith-aware display controller may consume persistent cells and
trajectories directly, but such hardware is an optional optimization and is
never required for bitstream compatibility.

## 6. Platform matrix

| Target | Decode and compute | Presentation |
|---|---|---|
| Windows x86-64/ARM64 | scalar/SIMD C++20, D3D12 or Vulkan compute | DXGI/D3D12, Vulkan |
| macOS/iOS ARM64 | scalar/NEON C++20, Metal compute | Metal/CoreAnimation |
| Android ARM64 | scalar/NEON C++20, Vulkan compute | Surface/MediaCodec integration |
| Linux x86-64/ARM64 | scalar/SIMD C++20, Vulkan compute | Wayland/X11/DRM adapters |
| Browser | WASM32 Core, WASM SIMD128, WebGPU | Canvas/WebGPU |
| Embedded/DSP | bounded C ABI, scalar or vendor SIMD | DMA/display-controller adapter |
| Hardware model | bit-exact kernel model | RTL/ASIC conformance harness |

GPU acceleration is optional. Every Main profile has a mandatory portable
scalar path and explicit complexity limits so that low-resource software can
reject unsupported levels before allocating state.

## 7. Deterministic Core subset

Truth reconstruction MUST use:

- exact-width unsigned arithmetic and explicitly defined signed helpers;
- normative saturation, clipping, division, shift, and rounding operations;
- explicit endianness and alignment-independent loads;
- deterministic iteration and event ordering;
- bounded loops, state, payloads, and scratch memory;
- no undefined overflow or implementation-dependent shifts;
- no floating-point normative state and no fast-math;
- no heap allocation, I/O, logging, locks, or lazy initialization in the
  render loop.

SIMD, shader, and hardware paths are accelerators only. They may reorganize
work but may not alter rounding, visibility, compositing, or Truth state.

## 8. Modern engineering quality gates

Every native Core change must pass:

1. MSVC, Clang, and GCC builds through versioned CMake Presets and Ninja.
2. Windows, Linux, macOS, Android, iOS, and WASM compile checks.
3. Identical conformance hashes across x86-64, ARM64, and WASM.
4. ASan, UBSan, TSan where applicable, and MSVC runtime checks.
5. libFuzzer/AFL++ fuzzing of parsing, state transitions, checkpoints, and
   resource-limit enforcement.
6. Property tests for random access, temporal sampling, chunk reordering,
   recovery, and backend equivalence.
7. clang-tidy, CodeQL, dependency auditing, SBOM generation, reproducible
   builds, and signed release artifacts.
8. Stable-ABI compatibility tests and semantic versioning.
9. GPU validation with API validation layers and CPU/GPU differential tests.
10. Real-time tests for allocation, lock contention, deadline misses, memory
    bandwidth, and worst-case level compliance.

The Golden Core keeps zero mandatory third-party runtime dependencies.
Dependencies used by applications or research tooling remain outside the
normative and conformance boundary.

## 9. Implementation sequence

1. Keep Python paper/oracle experiments fast to modify.
2. Freeze the smallest useful Main-0 arithmetic and command subset.
3. Implement the portable C++20 scalar Golden Core and C API.
4. Generate shared golden vectors and require exact Python/C++ parity.
5. Build the Rust parser, scheduler, and command-line player around the C API.
6. Add x86, ARM, and WASM SIMD without changing output.
7. Add Vulkan, D3D12, and Metal differential-tested compute backends.
8. Move measured encoder bottlenecks to C++/CUDA, retaining Python
   orchestration.
9. Ship thin native player shells and an independent decoder implementation.

This sequence preserves research velocity while making every frozen semantic
decision immediately executable on production-class targets.
