# Архитектура MOSAIC

Статус: смесь **ACCEPTED**, **NORMATIVE-DRAFT** и **HYPOTHESIS**.  
Нормативные формулировки уточняются в `../spec/SCENELITH-0.md`.

## 1. Общая модель

MOSAIC — ограниченная visual scene machine. Encoder компилирует видео в:

1. снимки и дельты `WorldState`;
2. непрерывные или кусочно-непрерывные `Trajectories`;
3. проверяемый `TruthInnovation`;
4. необязательный `PerceptualDetail`.

Декодер выполняет небольшой фиксированный набор integer render/tensor
операций. Сложные depth, segmentation, tracking, re-identification и global
optimization являются encoder-only.

**ACCEPTED — D-025:** MOSAIC использует
**CBF — Causal Basis Field visual ISA**. Долгосрочная формула не означает
тяжёлый world model. Один unified primitive — долгоживущая `MOSAIC Cell` —
объединяет immutable Basis, invisible tiled Support, arbitrary soft Gate,
absolute coordinate/appearance laws, Lifetime и Truth contribution. Frame
является только read-only presentation sample. 2.5D, tensor renderer и
semantic scene graph не входят в Main.

## 2. WorldState

### 2.1 Состав состояния

Main v0:

- bounded table `MOSAIC Cells`;
- bounded coordinate-independent `Content Bank`;
- fixed microtile Support;
- bounded absolute `STATIC`, `LINEAR_TRANSLATION` и profile-gated
  affine/projective coordinate laws;
- arbitrary-lifetime state events;
- compatibility PRESENT и objective fallback;
- integrity metadata;
- полный state reset в RAP.

Research после положительного cell gate:

- fine persistent masks и partial content updates;
- canonical surface atlas;
- 2.5D/depth/visibility;
- feature planes/latent tokens;
- surfels/Gaussian splats;
- semantic object/surface identifiers;
- state snapshots и partial repair.

**NORMATIVE-DRAFT:** ненаблюдавшийся fragment не получает Content вообще.
Main-0 не представляет «неизвестную часть объекта»; Support перечисляет только
определённые microtiles. Undefined output обязан получить objective fallback.

### 2.2 Ограничения

**TARGET:**

- persistent state: не более 64 MB для 4K profile;
- строго ограниченное число recent frames;
- никаких внешних state/model files;
- полный state reset в random-access point.

Пределы должны задаваться level/profile, чтобы аппаратный декодер мог заранее
выделить SRAM/DRAM.

### 2.3 Изменение состояния

Только проверенные mutation `EventBlock` могут применять State Events.
Read-only presentation/quality blocks используют уже подтверждённое состояние
и могут декодироваться параллельно или отбрасываться.

Порядок mutation:

1. Проверить EventBlock/payload integrity.
2. Восстановить Truth Core.
3. Проверить state hash.
4. Применить подтверждённый `MemoryDelta`.
5. Вычислить новый state hash.
6. Только после этого разрешить зависимые EventBlocks/Presentation Queries.

Повреждённый или concealment-generated материал не применяется к state.

## 3. Representation primitives

Encoder выбирает один или комбинацию режимов на tile/region/chunk.

### 3.1 Structural modes

Main v0:

- active MOSAIC Cell с static/linear absolute mapping;
- compact Content capture из подтверждённого Truth;
- recent-frame fallback, если он оставлен экспериментальным profile;
- state-independent replacement.

Research extensions:

- mask;
- mesh/deformation;
- depth/visibility;
- surfel/Gaussian splat;
- screen/vector/text primitive.

### 3.2 Innovation modes

- integer 5/3 wavelet base;
- transform/residual fallback;
- optional exact/lossless residual.

Research после core gate:

- shallow learned latent transform;
- progressive objective refinement.

### 3.3 Continuous-Time MOSAIC Cells

Main-0 имеет три semantic records:

- `STATE_RESET`;
- `CELL_SET`: атомарно создать/изменить/завершить cell;
- `PRESENT`: read-only sample state в timestamp.

`CELL_SET` объединяет Content, Support, MotionLaw, Lifetime, Order и Mode.
Отсутствие события означает implicit persistence; отдельный per-frame HOLD не
кодируется. `CAPTURE_TRUTH` сохраняет уже восстановленные objective samples без
повторной texture. Полная семантика:
[14_CONTINUOUS_TIME_CELLS.md](14_CONTINUOUS_TIME_CELLS.md).

DPM остаётся отдельным spatial-memory baseline:
[13_MINIMAL_PATCH_CORE.md](13_MINIMAL_PATCH_CORE.md).

### 3.4 Representation routing

Решение encoder оценивается по полному функционалу:

\[
J=R+\lambda D+\mu C_{decode}+\nu B_{memory}
  +\rho L_{seek}+\sigma Risk_{loss}
\]

где учитываются все address, mask, model, adapter, checkpoint и side-information
bits.

### 3.5 Bounded affine-pair composition

CBF Cell синтезирует пару \((g,c)\). Pair composition ассоциативна:

\[
(g_2,c_2)\circ(g_1,c_1)=(g_2g_1,\ g_2c_1+c_2).
\]

Decoder MAY выполнять order-preserving tree reduction в wide integer
accumulator и clip только на fixed layer boundary. Main target ограничивает
весь active overlap четырьмя non-identity contributions/output pixel, четырьмя
composition layers, восемью texture samples и примерно 128 simple integer
operations/pixel. Точные значения определяет level.

Полная фиксация:
[16_CBF_ACCEPTANCE_AND_FINAL_RED_TEAM.md](16_CBF_ACCEPTANCE_AND_FINAL_RED_TEAM.md).

## 4. Chunk-native temporal model — после cell gates

**RESEARCH:** Main-0 уже имеет bounded static/linear MotionLaw, но не требует
multi-frame latent, deformable trajectories или temporal tensor graph.
Следующие подразделы описывают возможный следующий этап.

### 4.1 Chunk

**NORMATIVE-DRAFT:** основной multi-frame chunk содержит 8–16 display frames
в Main RA-профиле. Конкретный диапазон ещё не заморожен.

Chunk использует:

- общий spatiotemporal latent;
- полностью вычисляемый до entropy decoding hyperprior;
- параллельное восстановление read-only frames;
- отдельно обозначенный spine output/state update.

### 4.2 Low-delay

Для Live/LB применяется causal variant:

- кадры поступают в display order;
- lookahead отсутствует там, где запрещён configuration;
- state update ограничен уже полученными кадрами;
- decoder output reordering не требуется.

### 4.3 Time-continuous trajectories

Для когерентного движения Main-0 передаёт редкие absolute linear knots вместо
per-frame vectors. Возможные расширения:

- camera/global motion;
- rigid object motion;
- deformable mesh/surface motion;
- lighting/exposure trajectory.

Decoder интерполирует их нормативной integer-функцией. Для участков, где
trajectory representation дороже residual, encoder выбирает fallback.

## 5. Два контракта качества

### 5.1 Fidelity/Truth Core

**ACCEPTED:**

- детерминирован и bit-exact;
- единственный источник reference/state;
- сохраняет структуру, текст, лица и измеряемые детали настолько, насколько
  это обеспечивает выбранный rate;
- поддерживает objective enhancement;
- декодируется без Perceptual Shell.

### 5.2 Optional Perceptual Detail

**RESEARCH / NORMATIVE-DRAFT:**

- одношаговый distilled diffusion или rectified-flow renderer;
- display-only;
- seeded deterministically внутри конкретного model-set;
- не влияет на base entropy contexts;
- сопровождается provenance/uncertainty mask;
- отключается в evidence, medical, scientific и archive profiles.

Perceptual-выигрыш измеряется blind MOS и специализированными identity/OCR/
flicker gates, отдельно от PSNR/MS-SSIM fidelity.

## 6. Decoder ISA

Main v0:

- exact microtile copy;
- bounded support-list traversal;
- absolute fixed-point linear translation;
- deterministic opaque composition;
- fixed-width residual add/clamp;
- integer transform/lifting fallback;
- normative in-loop filter;
- multi-lane rANS;
- STATE_RESET, CELL_SET и PRESENT.

Research после cell gate:

- INT8/INT4 tensor operators;
- integer bilinear/affine warp;
- mesh deformation;
- splat/blend;
- pixel shuffle;
- finite scalar/lattice/vector quantization.

Запрещается в Main:

- arbitrary downloadable graph;
- device-dependent floating-point reference loop;
- full-resolution attention;
- softmax-dependent normative reconstruction;
- динамические неограниченные циклы;
- обязательный многошаговый diffusion decoder;
- full-resolution autoregressive entropy.

## 7. Entropy и quantization

### Main v0

- scalar quantization;
- independent/interleaved rANS lanes;
- chunk/tile directory с точными offsets;
- CDF, доступные до начала соответствующего entropy decode.

### Research only

- lattice/progressive VQ;
- non-autoregressive learned hyperprior;
- relative-entropy coding;
- bits-back;
- reverse-channel coding;
- shared-prior sample indices.

Эти методы допускаются только для restartable low-KL microblocks/adapters,
пока не доказана ограниченная worst-case complexity.

## 8. Loss-native resilience

- Независимые tile/chunk entropy streams.
- CRC или более сильная integrity check для state/base.
- Unequal FEC: state и Truth Base защищаются сильнее enhancement.
- полный Cell/Content state reset в каждом Main v0 RAP.
- Concealment никогда не становится reference.

Research:

- State snapshot/delta checkpoints.
- Erasure-trained concealment.
- Partial repair access unit.

**TARGET:** восстановление после рассинхронизации состояния не более 250 мс в
Live profile.

## 9. Hardware mapping

Предполагаемые аппаратные блоки:

- multi-lane rANS engine;
- exact-copy/translation compositor;
- bounded SRAM cell table и DRAM Content Bank;
- support/dirty-tile scheduler;
- optional display/overlay trajectory handoff;
- wavelet/lifting block;
- residual compositor;
- integrity/reset engine.

Research extensions MAY reuse texture/warp, tensor и splat hardware только
после измеренного marginal gain.

Главные ограничения проектируются по MAC/pixel, state memory и off-chip
traffic, а не только по числу синтаксических tools.

## 10. Скалируемость

Один stream должен в перспективе позволять:

- temporal scalability;
- spatial scalability;
- quality scalability;
- compute scalability;
- ROI/tile decode;
- отключение Perceptual Shell;
- discardable enhancement;
- разные resolution/FPS outputs из одного truth state без объявления
  синтезированного novel view достоверным исходником.
