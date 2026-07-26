# Черновая структура bitstream и decoder

Статус: **NORMATIVE-DRAFT**  
Bit-level syntax ещё не заморожен.

## 1. Иерархия

Предлагаемая структура:

1. `SequenceHeader`
2. `MemoryAccessPoint`
3. `SceneEpoch`
4. `EventBlock`
5. `PayloadTile`
6. optional `ModelSet` extension
7. `EndOfSequence`

## 2. SequenceHeader

Минимальные поля:

- magic и bitstream version;
- profile/level;
- coded/display dimensions;
- chroma format, bit depth и nominal color space;
- integer timebase и scene duration;
- optional compatibility presentation schedule;
- color primaries, transfer и matrix;
- maximum state bytes;
- maximum cells, content bytes и support entries;
- maximum State Events и moving cells;
- maximum model bytes, если extension включён;
- maximum MAC/output-pixel class;
- enabled tool flags;
- integrity mode;
- model-set identifier/hash.

Все данные, необходимые для декодирования, находятся в stream или в
нормативно определённом baseline decoder. Внешние parameter files запрещены.

## 3. ModelSet — optional extension

Main-0 не требует learned ModelSet. Если extension включён:

- фиксированный нормативный operator graph;
- baseline weights или переданные self-contained quantized weights в пределах
  профиля;
- cryptographic/content hash;
- явный совместимый version identifier.

Произвольный исполняемый код или динамический graph запрещены.

## 4. MemoryAccessPoint

`MemoryAccessPoint` обеспечивает random access:

- очищает или полностью заменяет предыдущее state;
- содержит self-contained active MOSAIC Cells/Content либо full-screen
  objective fallback;
- не ссылается на пакеты до точки доступа;
- завершает проверкой восстановленного state hash.

CfP-ветка обязана соблюдать RAP cadence соответствующего anchor.

## 5. SceneEpoch

Epoch ограничивает lifetime state и содержит:

- epoch identifier;
- cell/content namespace;
- memory budget;
- deterministic eviction policy;
- optional scene-level adapter;
- initial state hash.

Любой adapter полностью учитывается в bitrate.

## 6. EventBlock

`EventBlock` имеет:

- timestamp interval;
- exact record count и offsets независимых entropy lanes;
- ordered `STATE_RESET`, `CELL_SET` и `PRESENT` records;
- inline/captured content directories;
- `TRUTH_INNOVATION`;
- optional `PERCEPTUAL_DETAIL`;
- integrity check и post-state hash, если block меняет state.

`PERCEPTUAL_DETAIL` всегда опционален и не входит в reference path.

State events внутри проверенного block применяются в coded order. PRESENT
читает все более ранние events с тем же timestamp и не видит более поздние.

## 7. PayloadTile

Payload tile имеет:

- фиксированную геометрию, предварительно 128×128 или 256×256;
- halo policy;
- content/innovation mode;
- offsets независимых entropy lanes;
- integrity check;
- cell/support ownership metadata;
- optional ROI priority.

Support является bounded union разрешённых dyadic microtiles. Рекурсивное
неограниченное quadtree-разбиение не является базовой моделью MOSAIC.

## 8. Decoder state machine

Высокоуровневый порядок:

1. Parse и проверить `SequenceHeader`.
2. Инициализировать profile limits.
3. Загрузить/проверить optional `ModelSet`, если он разрешён profile.
4. На `MemoryAccessPoint` очистить и self-contained восстановить `WorldState`.
5. Для каждого EventBlock:
   1. проверить directory/integrity и resource bounds;
   2. получить entropy parameters и декодировать lanes;
   3. применить `STATE_RESET/CELL_SET` атомарно в coded order;
   4. на `PRESENT(t)` вычислить absolute MotionLaw active cells;
   5. выполнить deterministic composition;
   6. добавить Truth Innovation и objective fallback;
   7. сформировать post-filter Truth output;
   8. сохранить его только как допустимый future `CAPTURE_TRUTH` source;
   9. отдельно применить необязательный Perceptual Detail;
   10. выдать output, не меняя state самим PRESENT.
6. При ошибке не применять неподтверждённые State Events.

## 9. Bit-exact arithmetic

Нужно нормативно определить:

- signed/unsigned widths;
- rounding direction;
- saturation;
- overflow behaviour;
- accumulator width;
- interpolation coefficients;
- LUT values;
- rANS normalization;
- PRNG и seed для optional stochastic tools.

Плавающая точка не должна участвовать в Main reference reconstruction.

## 10. Параллелизм

- Несколько независимых rANS lanes.
- Tile directory известна до payload decode.
- Read-only presentation tiles могут выполняться параллельно.
- Только ordered State Event commit требует сериализации.
- Cross-tile зависимости ограничены нормативным halo.

## 11. Профили

Предварительно:

- `Main-Fidelity` — event-retained state и универсальная детерминированная
  реконструкция;
- `Live` — causal/low-delay, bounded state, loss repair;
- `Perceptual` — Main-Fidelity плюс нереференсный shell;
- `VOD-Adaptive` — scene adapters/dictionaries с полным учётом bits;
- `Screen` — text/vector/sprite и optional exact refinement.
- `Continuous-Output` — host queries arbitrary timestamps; неподтверждённые
  source timestamps явно маркируются interpolated.

CfP-2026 использует отдельное минимальное подмножество, описанное в
`05_JVET_CFP_2026.md`.

## 12. Открытые вопросы

- Нормативный размер tile.
- Maximum duration/events per EventBlock.
- Разделение State, Motion, Innovation и Presentation clocks.
- Binary syntax `STATE_RESET/CELL_SET/PRESENT`.
- Microtile Support coding.
- Continuous-output API и container presentation mapping.
- Baseline weights в binary или в bitstream.
- Модель обновления model-set после аппаратного выпуска.
- Точная lattice/FSQ схема.
- Формат depth/visibility после Main-0 gate.
- Допустимые виды splat.
- Структура lossless enhancement.
- Conformance tolerance: строго bit-exact или отдельный bounded-error профиль.
