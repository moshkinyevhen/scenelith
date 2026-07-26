# Baseline A: Minimal Decoded Patch Memory

Статус: DPM experiment **ACCEPTED**, роль основного SceneLith core
**SUPERSEDED** решением D-017, точный syntax **RESEARCH**, compression claims
**HYPOTHESIS/TARGET**.  
Дата: 2026-07-26

DPM остаётся обязательным falsification baseline и возможным compact-content
компонентом `MOSAIC Cell`, но больше не определяет time/state architecture.
Текущий кандидат:
[14_CONTINUOUS_TIME_CELLS.md](14_CONTINUOUS_TIME_CELLS.md).

Рабочие названия:

- **Decoded Patch Memory (DPM)** — нормативный механизм;
- **PROMOTE memory** — ключевое отличие;
- **geometric visual dictionary** — encoder-side интерпретация.

## 1. Жёсткий пересмотр

Background mosaic, progressive sprite, arbitrary-shape object, atlas packing,
long-term reference и layered 2D representation уже предпринимались.

Следовательно, SceneLith не должен объявлять революцией:

- сбор стены из разных кадров;
- сохранение sprite/patch;
- warp старой texture;
- progressive reveal;
- обычный atlas или scene graph.

Полная Observed Surface Memory из `12_OBSERVED_SURFACE_MEMORY.md` слишком рано
ввела `Domain/Known`, depth, 2.5D, lifecycle и другие недоказанные механизмы.
Для DPM-0 experiment она заменена более строгим вопросом:

> Может ли компактная reference-память уже декодированных patches при том же
> числе bytes существенно обогнать хранение целых long-term frames?

Если ответ отрицательный даже для oracle, дальнейшая scene complexity не
оправдана.

## 2. Парадокс простоты

DPM-0 меняет только единицу reference memory:

- conventional codec хранит целые reconstructed frames;
- DPM хранит только выбранные reconstructed rectangles;
- patch больше не привязан к координатам и lifetime исходного frame;
- один slot можно размещать в prediction canvas сколько угодно раз;
- новые pixels кодируются обычной Truth Innovation;
- никогда не показанная область вообще не существует в state.

Это можно понимать как двумерный Lempel–Ziv с геометрическим размещением:

```text
NEW INFORMATION -> один раз восстановить
PROMOTE         -> сохранить полезный decoded rectangle
PLACE           -> многократно сослаться на него
INNOVATION      -> исправить несовпадение
```

Decoder не знает, является patch домом, лицом, фоном или текстом.

## 3. Единственное состояние

```text
PatchSlot {
    valid
    size_id
    pixels[size_id]
}
```

**DPM-0:**

- фиксированный bounded bank;
- candidate sizes: `16×16`, `32×32`, `64×64`;
- максимум slots и bytes задаются profile;
- pixels являются post-filter reconstructed Truth samples;
- нет persistent mask, depth, alpha, object ID, world coordinates или
  confidence.

Первая fair comparison использует ровно тот же physical state-memory budget,
что и anchor DPB/LTR.

## 4. Четыре opcodes

```text
PM_RESET
PM_PROMOTE
PM_PLACE
PM_DROP
```

### 4.1 PM_RESET

```text
PM_RESET {}
```

- обязателен в каждом RAP;
- сбрасывает все slot validity;
- после reset старый state недоступен;
- DPM-0 не передаёт atlas snapshot и не делает partial repair.

### 4.2 PM_PROMOTE

```text
PM_PROMOTE {
    dst_slot
    size_id
    source_x
    source_y
}
```

После завершения и проверки Truth reconstruction команда точно копирует
integer-aligned rectangle из current post-filter Truth frame в `dst_slot`.

- повторного texture payload нет;
- partial slot update отсутствует;
- новое PROMOTE полностью заменяет slot;
- source должен целиком лежать внутри frame;
- perceptual или concealment output запрещён.

Именно coordinate-free compaction post-filter decoded pixels является
единственным потенциально отличительным primitive DPM-0.

### 4.3 PM_PLACE

```text
PM_PLACE {
    src_slot
    destination_x
    destination_y
}
```

- только integer translation;
- slot копируется в prediction canvas без resampling;
- команды исполняются в bitstream order;
- последняя команда перезаписывает предыдущий prediction;
- output pixels, не покрытые PLACE, остаются unresolved;
- prediction всегда исправляется Truth residual/replacement.

Никаких affine, homography, mesh или bilinear filtering в первом oracle.
Сложную форму encoder аппроксимирует несколькими rectangles либо не использует
DPM.

### 4.4 PM_DROP

```text
PM_DROP {
    slot_list
}
```

- инвалидирует slots после завершения текущего output;
- текущая unit читает immutable pre-unit bank;
- DROP/PROMOTE коммитятся атомарно для следующей unit.

Технически DROP можно заменить перезаписью slot. Он оставлен как тривиальная
операция для явной liveness и тестирования; после измерения syntax cost его
можно удалить.

## 5. Полный decoder loop

```text
for each AccessUnit:
    1. Parse и validate syntax, counts, offsets, integrity.
    2. При RAP выполнить PM_RESET; PLACE count MUST быть 0.
    3. Freeze текущий PatchBank как read-only.
    4. Prediction = 0; ResolvedMask = 0.
    5. Выполнить PM_PLACE в bitstream order:
           exact-copy pixels;
           set ResolvedMask на destination rectangle.
    6. Decode Truth payload.
    7. Для каждого pixel:
           resolved -> Prediction + objective residual;
           unresolved -> objective replacement/intra.
    8. Выполнить normative in-loop filters.
    9. Выдать Truth output.
   10. В staging применить PM_DROP и PM_PROMOTE только из post-filter Truth.
   11. Проверить bounds, duplicate writers и memory limit.
   12. Атомарно commit state для следующей AccessUnit.
   13. Optional Perceptual Detail применить только к display.
```

При повреждении state-dependent unit decoder не обновляет PatchBank и
возобновляет экспериментальный DPM path только после следующего RAP. DPM-0 не
содержит partial repair.

## 6. Как сохраняется пример с домом

1. В первом кадре encoder находит чистые прямоугольники стены вокруг человека.
2. После reconstruction они попадают в slots через `PM_PROMOTE`.
3. В следующих кадрах `PM_PLACE` собирает prediction из уже известных кусочков.
4. Человек и ещё не известные части восстанавливаются обычной Truth Innovation.
5. Когда новый кусок стены впервые становится видим, его можно PROMOTE для
   будущего reuse.
6. Никогда не открывшийся кусок не хранится и не генерируется.

Arbitrary shape в v0 является объединением rectangles. Это менее bit-efficient,
чем идеальная mask, но оставляет decoder предельно простым и даёт честный ответ,
существует ли крупный выигрыш вообще.

## 7. Чем это отличается от прошлых подходов

| Подход | Что уже умеет | Узкое возможное отличие DPM |
|---|---|---|
| MPEG-4 sprite | Panorama, warp, arbitrary-shape foreground, progressive/online sprite | Не специальный background object, а общий compact bank независимых decoded rectangles |
| VVC/AV2 LTR | Долгая жизнь reconstructed frames, block/affine prediction | Не оплачивать память за бесполезные pixels целого frame |
| AV2 BRU/composite reference | Partial update reference picture | Coordinate-free dense packing patches из многих frames при том же byte budget |
| MPEG Immersive Video | Patches, atlases, geometry, inverse placement | Только original 2D playback; нет multiview/depth/novel view |
| Layered Neural Atlases | Persistent texture, alpha, learned frame↔atlas mapping | Нет MLP, semantic layer или per-video neural decoder |

**Честный статус:** эти различия могут оказаться недостаточными для patent
novelty. `PM_PROMOTE/PLACE` — сначала compression experiment, а не claim
изобретения.

## 8. Почему предыдущие варианты не стали универсальным frame codec

- MPEG-4 sprite был специализирован background/object mode и зависел от
  качественной segmentation/authoring.
- Whole-frame LTR прост, но тратит память на pixels, которые больше не нужны.
- MIV решает более тяжёлую задачу 6DoF и платит depth/patch metadata.
- Neural atlases оптимизировались для editing/view synthesis, требуют тяжёлого
  per-video fitting и не задают массовый bit-exact decoder.
- Composite reference approaches уже показывают, что простой memory gain может
  быть лишь несколько процентов в среднем.

DPM потенциально лучше не большей «интеллектуальностью», а тем, что делает
компактную patch memory единственным новым inter-memory primitive и имеет
дешёвый per-block fallback.

## 9. Пересмотр задач

### Немедленно реализовать

1. Сильный anchor:
   - AV2 v1 с long-term references и Backwards Reference Update;
   - VVC/VTM LTR;
   - equal-byte composite/deduplicating patch-cache baseline.
2. DPM oracle:
   - rectangles `16/32/64`;
   - integer PROMOTE/PLACE;
   - exact full-rate accounting;
   - одинаковые residual/transform/entropy tools с anchor.
3. Dataset:
   - long-gap camera return;
   - moving occluder/background reveal;
   - UI/game/animation sprites;
   - repeated logos/text;
   - negative water/foliage/crowd/grain/cuts.
4. Метрики:
   - BD-rate и per-class result;
   - bytes patch bank и DPB;
   - cache hit/useful-hit;
   - PROMOTE/PLACE bits;
   - DRAM read/write per output pixel;
   - RAP penalty.

### Не добавлять в DPM-0

- `DomainMask/KnownMask`;
- arbitrary-shape persistent masks;
- canonical surface atlas;
- depth, z-buffer и owner map;
- affine/homography/mesh;
- trajectories;
- 2.5D и 3D;
- surfels/Gaussians;
- semantic objects;
- scene/world reconstruction;
- generative completion;
- learned decoder;
- atlas snapshots и partial repair;
- Foundry-router distillation.

Эти механизмы остаются в Research Radar и не получают реализации, пока
четырёхкомандное ядро не пройдёт gate.

## 10. Go/no-go

Продолжать DPM как core coding tool только если oracle при одинаковых:

- decoder memory bytes;
- random-access interval;
- latency/lookahead;
- objective quality;
- residual/transform/entropy path;
- encoder search effort для reported anchor

даёт:

- более 15% net bitrate reduction на нескольких разных long-gap категориях;
- не менее 10–15% на puzzle-friendly natural subset;
- не менее 5% на mixed corpus;
- среднюю hostile regression не более 0.5%;
- memory traffic в пределах будущего hardware profile.

Если DPM не проходит gate:

- не добавлять masks/depth/3D в попытке спасти идею;
- оставить его niche screen/sprite tool либо закрыть;
- вернуться к multi-frame innovation как основному research path.

## 11. Complexity tax для любого расширения

После успеха DPM-0 новый tool добавляется только отдельно и по одному:

1. binary `8×8` mask;
2. subpixel translation;
3. affine;
4. partial slot update;
5. trajectory parameterization.

Каждое расширение должно:

- давать не менее 3% net gain на mixed corpus либо не менее 7% на крупном
  declared subset сверх предыдущего уровня;
- не увеличивать disabled-stream syntax более чем на 0.2%;
- иметь bounded integer implementation;
- не требовать semantic inference в decoder;
- проходить отдельную ablation.

Нет измеренного marginal gain — нет syntax.

## 12. Упрощённый timeline

При параллельной круглосуточной работе:

| Срок | Результат |
|---|---|
| 2–4 дня | DPM state machine, synthetic bitstream и bit-exact CPU copy path |
| 1–2 недели | Oracle на выбранных long-gap sequences |
| 2–4 недели | Fair comparison с equal-memory LTR/BRU/composite cache |
| 4–6 недель | Решение: core, niche или kill |
| 6–10 недель | GPU/conformance work только при положительном решении |

Это существенно быстрее и дешевле полной OSM/2.5D ветки. Самое важное:
SceneLith получает проверяемый ответ до того, как недоказанная сложность
превратится в архитектурный долг.
