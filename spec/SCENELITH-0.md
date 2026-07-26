# SceneLith-0 — черновик нормативной спецификации

Codec/bitstream family и проект: SceneLith  
Архитектура: MOSAIC  
Версия: 0.0.4  
Статус: **NORMATIVE-DRAFT**  
Дата: 2026-07-26

Этот документ пока фиксирует семантический контракт, а не окончательную
битовую раскладку.

## 1. Scope

SceneLith-0 определяет self-contained visual-state bitstream и детерминированный
decoding process для bounded continuous-time MOSAIC Cells и objective
innovation.

Frame не является единицей state mutation, motion или reference memory.
`Presentation Query` является read-only sample текущего state. Принятая
implementation architecture — **CBF: Causal Basis Field visual ISA**.
Первая reference implementation ограничена static/linear translation; syntax
MAY разрешать bounded profile-gated affine/projective law. Depth, 3D и
unrestricted learned decoder не входят в Main-0.

## 2. Термины

- **WorldState** — ограниченное нормативное состояние сцены.
- **Truth Core** — reconstruction path, допустимый для reference/state.
- **Truth Innovation** — передаваемая объективная поправка к structural render.
- **Perceptual Detail** — необязательная синтетическая display-only поправка.
- **Mutation EventBlock** — проверяемый block, содержащий State Events.
- **Read-only EventBlock** — block, не изменяющий WorldState.
- **Memory Access Point (MAP)** — точка полного независимого восстановления
  допустимого WorldState.
- **Scene Epoch** — ограниченный интервал жизни namespace и state.
- **MOSAIC Cell** — bounded state record, синтезирующий scalar gate \(g\) и
  color contribution \(c\) из immutable basis content.
- **CBF** — Causal Basis Field visual ISA, в котором Cell является bounded
  spacetime basis atom.
- **State Event** — атомарное изменение полей одной или нескольких cells в
  заданный timestamp.
- **Presentation Query** — чтение и composition state в timestamp без mutation.
- **Content Bank** — bounded coordinate-independent storage только
  подтверждённых Truth samples или inline objective payload.
- **Support** — conservative bounded union разрешённых dyadic microtiles для
  storage, scheduling и culling; его граница не является visible shape.
- **Gate** — bounded fixed-point scalar field \(g(p,t)\), определяющий, какая
  доля предыдущего Canvas сохраняется при применении Cell.
- **Contribution** — bounded fixed-point color field \(c(p,t)\).
- **Affine composition** — единственная композиционная операция
  \(Canvas'=g\,Canvas+c\) внутри bounded composition layer; clip выполняется
  на нормативной layer boundary.
- **MotionLaw** — absolute fixed-point mapping local content coordinates в
  output coordinates на заданном time interval.
- **CELL_SET** — создание, обновление либо завершение cell.
- **STATE_RESET** — очистка state и начало self-contained epoch.
- **PRESENT** — compatibility Presentation Query с optional objective Truth
  payload.
- **DPM** — отдельный экспериментальный baseline из
  `../docs/13_MINIMAL_PATCH_CORE.md`, не time/state architecture Main-0.

## 3. Conformance language

Слова MUST, MUST NOT, SHOULD, SHOULD NOT и MAY используются в смысле RFC 2119.

## 4. Основные требования

1. Decoder MUST воспроизводить Truth Core детерминированно.
2. Perceptual Detail MUST NOT участвовать в reference prediction.
3. Perceptual Detail MUST NOT менять WorldState.
4. Повреждённый или непроверенный State Event MUST NOT применяться.
5. MAP MUST позволять декодирование без пакетов, предшествующих MAP.
6. Bitstream MUST быть self-contained относительно всех ненормативных
   параметров декодирования.
7. Decoder MUST отклонять stream, превышающий profile/level limits.
8. Все переданные adapters, dictionaries и weights MUST учитываться в bitrate.
9. Main profile MUST NOT требовать произвольного исполняемого graph.
10. Main Truth reconstruction MUST NOT зависеть от device floating-point
    behaviour.
11. PRESENT MUST NOT менять WorldState.
12. Отсутствие State Event MUST означать сохранение предыдущего допустимого
    cell state; per-presentation `HOLD` syntax MUST NOT требоваться.
13. Main-0 MotionLaw MUST принадлежать profile-defined bounded набору:
    `STATIC`, absolute fixed-point `LINEAR_TRANSLATION`, `AFFINE` или
    `PROJECTIVE`; первая reference implementation MUST реализовать как минимум
    `STATIC` и `LINEAR_TRANSLATION`.
14. MotionLaw MUST вычисляться относительно immutable cell Content, а не
    рекурсивным warp предыдущего presentation output.
15. Main-0 Support MUST быть bounded union profile-defined dyadic microtiles,
    используемых только как conservative storage/culling bounds.
16. Main-0 MUST NOT иметь отдельные circle, polygon или arbitrary rasterizer
    primitives.
17. Visible footprint MUST определяться Gate, а не границей Support.
18. Любой unresolved output region MUST использовать state-independent
    objective `REPLACE` fallback.
19. `CAPTURE_TRUTH` MUST читать только завершённый, проверенный post-filter
    Truth output.
20. Concealment и Perceptual Detail MUST NOT быть source Content Bank.
21. State Events MUST применяться атомарно только после integrity/bounds checks.
22. Main-0 MUST NOT требовать depth, отдельный semantic alpha-object,
    mesh, 2.5D/3D primitives, scene semantics или learned decoder;
    scalar Gate из требования 26 не считается отдельным object type.
23. Output в timestamp, отсутствующий среди source-ground-truth timestamps,
    MUST быть обозначим как interpolated, если его fidelity не подтверждена
    отдельным Truth payload.
24. Вне Support decoder MUST использовать identity Cell value \(g=1,c=0\).
25. Cell application MUST использовать только affine pair
    \(Canvas'=g\,Canvas+c\) внутри composition layer и profile-defined clip
    на layer boundary.
26. Gate MUST позволять binary и fractional coverage с profile-defined
    precision; rectangular storage boundary MUST NOT проявляться в output.
27. Каждый interpolation footprint MUST быть полностью определён guard/apron
    samples либо закрыт objective fallback.
28. Lossless profile MUST позволять pixel-exact full-output fallback.
29. Cell evaluation MUST использовать immutable Basis и absolute parameter
    laws; recursive reference к предыдущему presentation запрещён.
30. Profile/level MUST задавать absolute maximum non-identity Cell
    contributions на output pixel и fixed composition layer count.
31. Main general level TARGET — не более 4 contributions, 4 layers,
    8 texture samples и порядка 128 simple integer operations/output pixel;
    финальные числа становятся нормативными после conformance experiment.
32. При невозможности уложиться в limits encoder MUST использовать objective
    Innovation fallback; decoder MUST отвергнуть превышающий limits stream.
33. Внутри composition layer affine pairs MAY объединяться:
    \[
    (g_2,c_2)\circ(g_1,c_1)=
    (g_2g_1,\ g_2c_1+c_2).
    \]
    Reduction MUST сохранять coded order и использовать profile-defined wide
    accumulator.
34. Clip MUST выполняться на profile-defined layer boundary. Реализация MUST
    давать output, независимый от parallel reduction tree.

## 5. Abstract decoding process

Decoder обрабатывает records строго в coded order:

1. Проверяет Event Block syntax, bounds, resource limits и integrity.
2. На `STATE_RESET(t)` очищает cells, Content Bank и namespace.
3. На `CELL_SET(t)`:
   1. истекает cells с `death_time <= t`;
   2. строит изменённые content/support/motion fields в staging;
   3. разрешает `CAPTURE_TRUTH` только после существующего подтверждённого
      Truth output;
   4. атомарно коммитит новую версию state.
4. На `PRESENT(t)`:
   1. истекает cells с `death_time <= t`;
   2. вычисляет absolute MotionLaw каждой active cell;
   3. синтезирует Gate \(g_i\) и Contribution \(c_i\) каждой Cell;
   4. order-preserving объединяет пары \((g_i,c_i)\) внутри фиксированных
      layers, применяет \(Canvas'=gCanvas+c\) и normative clip на каждой
      layer boundary;
   5. state-independent objective fallback полностью определяет unresolved
      pixels;
   6. выполняет normative in-loop/output filters;
   7. сохраняет проверенный Truth output как единственный допустимый future
      capture source;
   8. отдельно применяет или пропускает Optional Perceptual Detail;
   9. выдаёт display output, не меняя WorldState.

Host MAY запросить дополнительный timestamp в continuous-output profile.
Такой query использует только уже active state и не создаёт reference.

## 6. WorldState limits

Каждый profile/level MUST задавать:

- максимальный объём state;
- максимальное число cells;
- максимальный размер Content Bank;
- разрешённые microtile sizes и максимальное число support entries;
- максимальное число active/moving cells на output tile;
- максимальное число State Events и motion knots на time interval;
- максимальное число recent references;
- максимальную длину epoch;
- максимальный compute class;
- максимальное число changed/dirty output tiles на compatibility PRESENT.

## 7. Reference graph

- Mutation EventBlock MAY зависеть только от подтверждённого Truth State.
- Read-only EventBlock MAY зависеть от state и явно перечисленных Truth
  outputs.
- Perceptual output MUST NOT появляться в dependency graph.
- Dependency graph MUST быть ациклическим внутри independently decodable
  interval.
- PRESENT MUST читать snapshot state после всех более ранних State Events с тем
  же timestamp и до всех более поздних records в coded order.
- CELL_SET MUST NOT читать partially committed state.
- Recursive reference на предыдущий interpolated presentation запрещён.

## 8. Random access

MAP MUST:

- выполнить STATE_RESET;
- содержать self-contained cells либо full-screen objective fallback;
- полностью определить первый PRESENT;
- не использовать KEEP/CAPTURE_TRUTH до определения соответствующего source;
- не ссылаться на предыдущий epoch.

Main-0 не содержит partial state repair. Content Bank строится заново после
MAP.

## 9. Error behaviour

При integrity failure decoder:

- MUST NOT commit State Events;
- MAY вывести concealment presentation;
- MUST пометить state/output как degraded;
- MUST возобновить state-dependent decoding не ранее следующего MAP.

## 10. Main operator set — NORMATIVE-DRAFT

- fixed-width add/multiply/accumulate;
- lifting/wavelet;
- exact microtile copy;
- bounded support-list traversal;
- bounded absolute fixed-point translation/affine/projective coordinate law;
- deterministic affine-pair composition и order-preserving tree reduction;
- residual add/replacement, clamp и normative in-loop filter;
- rANS decode;
- STATE_RESET, CELL_SET и PRESENT.

Окончательные microtile sizes, precision, saturation и rounding будут
определены после первых conformance experiments.

## 11. Security requirements

Decoder MUST:

- проверять все размеры до allocation;
- иметь нормативные пределы cycles/memory;
- не исполнять код из bitstream;
- защищаться от integer overflow и malformed entropy state;
- проверять offsets и tile directories;
- поддерживать deterministic failure вместо неопределённого поведения.

## 12. Нерешённые разделы

- окончательный binary syntax;
- profile/level table;
- chroma/HDR processing;
- reference color conversion;
- conformance vectors;
- exact entropy tables;
- container mapping;
- decoder capability signaling;
- точные cell count, Content Bank и microtile limits;
- binary syntax STATE_RESET/CELL_SET/PRESENT;
- fixed-point timebase и maximum motion interval;
- clipping/coverage rule на output bounds;
- exact dirty-tile derivation;
- точный порядок in-loop filters относительно CAPTURE_TRUTH;
- continuous-output API и маркировка interpolated timestamps;
- relationship compatibility PRESENT с container sample tables.

Отложено за пределы Main v0 до measured marginal gain:

- pixel-exact persistent masks;
- partial slot update;
- depth/2.5D/3D;
- exposure integration;
- learned/generative decoder;
- state snapshots и partial repair.
