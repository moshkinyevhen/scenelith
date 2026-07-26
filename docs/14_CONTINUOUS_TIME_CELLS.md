# Frame-free core: Continuous-Time MOSAIC Cells

Статус: frame-free time/state principles — **ACCEPTED** решением D-025;
hard dyadic visible support и `REPLACE/ADD` formula — **SUPERSEDED** решениями
D-021/D-022; физические ограничения и карта prior art — **FACT**; численные
пороги — **TARGET**.  
Дата: 2026-07-26  
Решение: D-017.

Принятая one-equation CBF architecture и раздельный AV2/VVC kill-test:
[`15_PAPER_KILL_TEST_AND_FREEZE.md`](15_PAPER_KILL_TEST_AND_FREEZE.md).

Рабочие термины:

- **MOSAIC Cell** — единый долгоживущий visual-state primitive;
- **State Event** — асинхронное изменение полей cell;
- **Presentation Query** — чтение сцены в момент \(t\), не меняющее state;
- **Continuous-Time Retained Video (CTRV)** — описательное имя модели, не
  принятое продуктовое название.

Продуктовая иерархия:

> **SceneLith — a SceneLith codec, powered by MOSAIC.**

## 1. Главный переворот

Кадр не должен быть:

- единицей reference memory;
- единицей изменения state;
- единицей описания движения;
- обязательным тактом bitstream;
- причиной повторного декодирования или записи статичных pixels.

Кадр может остаться только совместимым результатом:

> `PresentationQuery(t)` спрашивает, как выглядит подтверждённая сцена в момент
> \(t\), но сам запрос ничего в ней не меняет.

Нормативный поток должен описывать, **что изменилось и как долго действует
описание**, а display выбирает моменты наблюдения.

## 2. Физический предел: «без кадров» не означает «без времени»

Нельзя показать движение, вообще не меняя испускаемый экраном свет. Любой
реальный display:

- обновляет pixels дискретно;
- сканирует строки;
- либо поддерживает аналоговое/событийное изменение с конечной полосой.

Поэтому честная цель SceneLith:

> Убрать frame clock из transport, reference state, motion syntax и основной
> decoder work. Последний display sampling остаётся физической необходимостью.

На обычном 60/120/240 Hz дисплее controller вычисляет сцену в его timestamps.
На будущем event-driven panel он сможет применять только действительно
изменившиеся regions. Один и тот же SceneLith stream не обязан иметь заранее
впаянный FPS.

Для исходника, снятого обычной камерой с дискретными frames, значения между
моментами съёмки математически не определены однозначно. Результат в новом
timestamp является интерполяцией/синтезом, если он не подтверждён:

- более частой съёмкой;
- event sensor;
- другим ground truth;
- либо явно переданной `TruthInnovation`.

Это ограничение нельзя скрывать маркетингом.

## 3. Один primitive, устраняющий три повторные платы

Каждая активная cell имеет:

\[
Cell_i=
\left(
Content_i,\ Support_i,\ MotionLaw_i(t),\
[birth_i,death_i),\ Order_i,\ Mode_i
\right).
\]

Где:

- `Content` — texture или signed objective correction, переданная один раз
  либо захваченная из уже декодированного Truth output;
- `Support` — множество локальных microtiles, для которых content определён;
- `MotionLaw(t)` — абсолютное fixed-point отображение local coordinates в
  output space;
- `Lifetime` — интервал действия, в том числе open-ended;
- `Order` — детерминированный порядок opaque composition;
- `Mode` — `REPLACE` либо `ADD_TRUTH`.

Один и тот же механизм убирает:

| Повторная стоимость frame codec | Поле MOSAIC Cell | Почему платится один раз |
|---|---|---|
| `unchanged/skip` на каждом frame | `Lifetime` | Без события состояние сохраняется неограниченно |
| ref/MV/mode на каждом frame | `MotionLaw(t)` | Один segment действует на много display queries |
| frame-sized reference buffers | `Content + Support` | Хранятся только полезные coordinate-independent samples |

Важная граница: если cell не уменьшает полный
`content + support + motion + event + checkpoint + innovation` rate, encoder её
не использует.

Сравнение одного coherent interval:

\[
R_{\mathrm{frame}} \approx
\sum_{t}
\left(
R_{\mathrm{partition}}+
R_{\mathrm{ref/mode/MV}}+
R_{\mathrm{residual}}
\right),
\]

\[
R_{\mathrm{cell}} \approx
R_{\mathrm{content}}+
R_{\mathrm{support}}+
R_{\mathrm{motion\ law}}+
R_{\mathrm{events/checkpoints}}+
\sum_t R_{\mathrm{innovation}}.
\]

SceneLith выигрывает только если одноразовые cell costs амортизируются, а
`TruthInnovation` не возвращает почти весь residual anchor. Иначе новый state
contract является лишь другой упаковкой тех же bits.

## 4. Четыре независимых clock

Современный frame codec обычно сводит разные процессы к одному picture cadence.
MOSAIC разделяет:

1. **State clock** — content/support/order/lifetime меняются только по событиям.
2. **Motion clock** — новый knot приходит, когда прежний закон движения перестал
   быть достаточно точным.
3. **Innovation clock** — objective correction появляется там и тогда, где
   structural render недостаточен.
4. **Presentation clock** — display или compatibility container спрашивает
   результат в произвольные timestamps.

Статичная стена может иметь ноль state и motion events после появления.
Плавно движущийся logo может иметь один motion segment на секунду и 240
presentation queries. Рот говорящего может получать частые innovation events,
а его одежда — редкие. Это разные clocks внутри одной сцены, а не отдельные
полные video streams.

## 5. State и output equations

\[
WorldState(t^+)=ApplyEvents(WorldState(t^-),E_t).
\]

\[
\hat V(p,t)=
Compose_{i:\ birth_i\le t<death_i}
Sample(Content_i,Support_i,MotionLaw_i(t),p).
\]

\[
V(p,t)=
\hat V(p,t)+TruthInnovation(p,t)+OptionalPerceptualDetail(p,t).
\]

Это является конкретизацией принятой формулы:

\[
Video(t)=Render(WorldState_t,\ Trajectories_t)
       +TruthInnovation_t
       +OptionalPerceptualDetail_t.
\]

`PresentationQuery(t)` читает \(WorldState(t)\), но не выполняет
`ApplyEvents`.

## 6. Как показать статику без перерисовки

### 6.1 В bitstream

Статичная cell:

```text
MotionLaw = IDENTITY
death_time = INFINITE
```

После `CELL_SET` не передаются `HOLD`, skip flags или пустые per-frame records.
Молчание означает сохранение состояния.

### 6.2 В decoder/compositor

Каждая cell и каждый output microtile имеют generation/version. Реализация
кэширует уже скомпозированный tile и пересчитывает его только если:

- изменился contributing cell;
- через tile прошла moving cell;
- пришла Truth Innovation;
- изменились color/display parameters.

Dirty set:

\[
D(t)=ChangedFootprints(t)\cup SweptMovingFootprints(t)
     \cup InnovationFootprints(t).
\]

Работа incremental compositor должна масштабироваться с \(|D(t)|\), а не с
\(Width\times Height\).

На legacy display полный scanout может сохраниться, но decoder/GPU не обязан
снова декодировать и переписывать статичные framebuffer tiles. При panel
self-refresh статичная часть может не пересылаться и по display link. Это
отдельная energy/memory-traffic метрика, не подмена bitrate.

## 7. Как показать движение без encoded FPS

### 7.1 Absolute motion law

Первый минимальный закон:

\[
x(t)=x_0+v_x(t-t_0), \qquad
y(t)=y_0+v_y(t-t_0).
\]

Возможное следующее расширение — линейная интерполяция bounded integer affine
matrix между двумя knots.

Motion всегда вычисляется относительно неизменного stored `Content`, а не
путём warp предыдущего output. Поэтому число presentation queries не создаёт
recursive blur или numerical drift.

### 7.2 Event вместо vectors

```text
CELL_SET {
    event_time
    cell_id
    changed_fields = MOTION | LIFETIME
    motion_model = LINEAR_TRANSLATION
    x0, y0, vx, vy
    motion_end_time
}
```

До `motion_end_time` никакой новой motion syntax не нужна. Если движение
изменилось, приходит новый knot. Если модель стала невыгодной, короткоживущая
Truth cell или raster fallback исправляет output.

### 7.3 Display execution

Display controller получает active content, trajectory и layer order. Для
каждого собственного presentation time он:

1. вычисляет absolute transform;
2. определяет old/new/swept dirty footprint;
3. читает только затронутые source tiles;
4. обновляет только pixels, свет которых должен измениться.

Движущийся объект физически требует обновления pixels в своём старом и новом
footprint. Устранить эту работу невозможно; устранить full-screen decode,
full-frame write и per-frame CPU/GPU command — возможно.

### 7.4 Exposure

Естественный motion blur зависит не от мгновенного \(t\), а от интеграла по
exposure interval. Возможный future tool:

\[
V_\Delta(p,t)=\frac{1}{\Delta}
\int_{t-\Delta/2}^{t+\Delta/2}V(p,\tau)\,d\tau.
\]

Main-0 не стандартизует дорогой arbitrary integration. Он использует sample at
\(t\), а blur исходных samples сохраняет Truth Innovation. Fixed integer
shutter integration рассматривается только после отдельного RD/compute gate.

## 8. Почему не rectangles, circles или arbitrary polygon zoo

Rectangle был выбран в DPM как самый дешёвый falsification test:

- contiguous storage;
- один descriptor;
- coalesced GPU copy;
- существующий blit hardware;
- простые bounds.

Circle не является более общим ответом:

- большинство реальных границ не круговые;
- нужен отдельный rasterizer/coverage rule;
- rotation, aliasing и chroma boundary всё равно требуют определения;
- следующий объект потребует ещё один primitive.

Полный polygon/mask точен, но может съесть выигрыш topology/mask bits и
нерегулярным execution.

Решение-кандидат:

> Shape не является типом. `Support` — только bounded множество одинаковых
> dyadic microtiles.

- внутренняя область кодируется крупными tile runs;
- граница уточняется меньшими tiles только при положительном RDO;
- круг, человек или буква являются объединением тех же cells;
- первый профиль начинает с одной coarse grid;
- pixel mask допускается лишь как отдельное расширение после measured gain;
- boundary error закрывается объективной innovation, а не новым shape engine.

На GPU `Support` разворачивается один раз при state event в dense owner map или
compact active-tile list. Presentation не обходит pointer-rich tree.

## 9. Минимальная семантика bitstream

Количество opcodes само по себе не является критерием простоты. Один opcode с
десятками скрытых режимов хуже трёх ясных операций. Минимальный semantic set:

```text
STATE_RESET(t)
CELL_SET(t, cell_id, changed_fields, ...)
PRESENT(t, optional_truth_payload)
```

### `STATE_RESET`

- начинает self-contained epoch;
- очищает все cells;
- запрещает references в прошлый epoch.

### `CELL_SET`

Создаёт cell либо атомарно меняет перечисленные поля:

```text
CELL_SET {
    event_time
    cell_id
    alive
    changed_fields

    if CONTENT:
        source = INLINE | CAPTURE_TRUTH | KEEP
        payload_or_capture_address

    if SUPPORT:
        bounded_microtile_set

    if MOTION:
        STATIC | LINEAR_TRANSLATION
        parameters
        motion_end_time

    if LIFETIME:
        death_time_or_infinite

    if COMPOSITION:
        REPLACE | ADD_TRUTH
        order_key
}
```

- `alive=0` завершает cell;
- `death_time` делает отдельный DROP необязательным;
- `KEEP` меняет движение без повторной texture;
- `CAPTURE_TRUTH` сохраняет только проверенные post-filter Truth samples;
- Optional Perceptual Detail и concealment не могут быть source;
- новая версия коммитится только после integrity check.

### `PRESENT`

- задаёт compatibility output timestamp либо проверяемый source sample;
- не меняет state;
- может содержать short-lived objective innovation;
- в continuous-output profile host MAY делать query в другом timestamp, но
  такой output считается interpolated, если для него нет ground truth.

## 10. Универсальность и fallback

Любой raster video представим:

- full-screen opaque `REPLACE` cell;
- lifetime до следующего source timestamp;
- новая cell перед каждым `PRESENT`.

Это дорогой, но корректный fallback. Хорошо моделируемое video вместо этого
имеет длинные lifetimes, compact content и редкие motion/innovation events.

Chaotic water, fire, foliage, hair, reflections, grain и cuts не должны
насильно превращаться в тысячи tiny persistent cells. Encoder выбирает
short-lived raster/innovation representation.

## 11. Occlusion без полного 3D

Первый профиль использует только deterministic opaque order:

```text
(order_key, cell_id)
```

Когда foreground cell уходит, лежащая ниже background cell снова видна без
повторной передачи. Никогда не наблюдавшаяся область background не создаётся:
если она впервые становится видимой, Truth Innovation восстанавливает её, после
чего encoder MAY выполнить `CAPTURE_TRUTH`.

Depth, alpha, mesh и semantic object identity не нужны для первого gate.
Ошибка encoder prediction всегда исправляется Truth path.

## 12. Hardware contract

Main-0 candidate использует:

- bounded cell table;
- bounded compact content bank;
- fixed microtile size;
- fixed-point absolute translation;
- exact copy или один существующий interpolation filter;
- deterministic opaque composition;
- residual/replacement path;
- multi-lane entropy;
- tile generation map и dirty list;
- atomic state event commit.

Нет:

- arbitrary shaders;
- unbounded scene graph;
- device floating point;
- segmentation/SLAM в decoder;
- per-pixel linked lists;
- recursive output warp;
- обязательного neural model;
- генерации невидимого мира.

Future ASIC может соединить decoder state bank с display/overlay controller.
Тогда trajectory задаётся один раз, статичные tiles остаются в local memory, а
controller выполняет только dirty/swept composition.

## 13. Что уже было и что нельзя объявлять новизной

**FACT:**

- conditional replenishment передавал только существенно изменившиеся части
  picture уже в [ITU-T H.120](https://www.itu.int/rec/T-REC-H.120/en);
- [MPEG-4 Visual](https://mpeg.chiariglione.org/standards/mpeg-4/video.html)
  поддерживал arbitrary-shaped Video Object Planes и sprites;
- [MPEG-4 BIFS](https://mpeg.chiariglione.org/standards/mpeg-4/scene-description-and-application-engine.html)
  передавал команды insert/delete/replace для динамического scene graph;
- разные temporal rates объектов исследовались в
  [Asynchronous Rate Control for Multi-Object Videos](https://doi.org/10.1109/TCSVT.2005.852415);
- event cameras и
  [time-encoding video](https://arxiv.org/abs/2206.04341) уже используют
  асинхронные per-pixel events;
- [ADΔER](https://arxiv.org/abs/2408.06248) транскодирует framed video в
  sparse asynchronous intensity representation;
- motion-aligned spatiotemporal tubes исследовались в
  [Tube-based video coding](https://doi.org/10.1016/S0923-5965(96)00034-3);
- финальный [AV2 v1.0](https://av2.aomedia.org/v1.0.0/index.html) уже имеет
  partial Backwards Reference Update, long-term references, output существующих
  reference frames, multistream layers и Atlas composition.

Следовательно, не являются самостоятельной революцией:

- dirty rectangles;
- region-specific FPS;
- object layers;
- arbitrary masks;
- sprites;
- partial reference update;
- scene graph;
- continuous affine animation;
- event stream сам по себе.

Потенциальное отличие SceneLith требует prior-art/FTO review. Оно формулируется как
единый bounded natural-video contract:

1. frame-free state events;
2. motion-lifetime cell, одновременно амортизирующая state, motion и compact
   content reference;
3. objective innovation в той же time domain;
4. observed-only capture с reference provenance;
5. независимый presentation clock;
6. incremental GPU/display execution;
7. битрейт, random access, loss и hardware limits в одном RDO.

Новизна комбинации пока **HYPOTHESIS**, не патентный вывод.

## 14. Почему HOLD alone недостаточен

Современный codec уже передаёт static block через очень дешёвый skip/merge без
residual. Если SceneLith убирает только skip flags, потолок невелик.

Иллюстрация **не как измеренный результат**: 4K содержит около 510 blocks
`128×128`. Даже один условный bit на block при 60 Hz — около 30.6 kbit/s.
На многомегабитном natural video это меньше нескольких процентов.

Поэтому cell обязана амортизировать одновременно:

- partition/support;
- reference choice;
- motion law;
- lifecycle;
- texture после occlusion/reappearance;
- decoder writes.

Иначе механизм остаётся полезным power optimization для screen content, но не
compression revolution.

## 15. Честные рабочие гипотезы

Это диапазоны первого минимального `STATIC + LINEAR_TRANSLATION` Main-0,
не claims SceneLith. Baselines нельзя объединять:

| Класс | Против AV2 v1.0 | Против VVC/H.266 |
|---|---:|---:|
| Полный повтор output | 0–1% | 0–2% |
| Ideal rigid/screen | 5–15% | 8–18% |
| Puzzle-friendly natural | 2–8% | 3–10% |
| Mixed natural | 0–3% | 0–4% |
| Hostile dynamic с fallback | около 0% | около 0% |

Это не потолок полного MOSAIC. Compact observed content, occlusion reuse,
multi-frame innovation и новые transforms могут дать дополнительный выигрыш,
но проценты нельзя складывать без end-to-end measurement.

Главный потенциально большой результат может быть двухмерным:

- bitrate reduction;
- decoder/DRAM/display work reduction.

Они измеряются и публикуются отдельно.

### 15.1 Рабочая оценка для «среднего видео»

До oracle результат неизвестен. Текущая инженерная гипотеза:

- только lifetime/HOLD syntax: около `0–1%` broad mixed natural;
- compact persistent Cell на mixed: `0–3%` против AV2 и `0–4%` против VVC;
- persistent TruthInnovation без настоящего low-rank residual reduction:
  `2–6%` против AV2 и `3–8%` против VVC;
- двузначный выигрыш наиболее правдоподобен на screen/UI, scrolling, 2D
  animation, static-camera и long-gap reappearance;
- больше 10% на truly mixed natural нельзя обещать до измерения.

Чтобы SceneLith дал революционные `25%+` в среднем, Cells должны сочетаться с
существенно лучшим Truth Innovation/transform/entropy path и действительно
снижать residual, а не только служебную syntax.

Раздельная sensitivity model, coverage thresholds и новый Spacetime Basis Cell
candidate находятся в
[`15_PAPER_KILL_TEST_AND_FREEZE.md`](15_PAPER_KILL_TEST_AND_FREEZE.md).

### 15.2 Изменение сложности encoder

`STATIC/LINEAR` runs могут переиспользовать conventional motion candidates.
Дополнительная задача — temporal dynamic programming: насколько долго выгодно
сохранить law и когда разорвать run.

Рабочие **HYPOTHESIS/TARGET**:

- Gate A: `+5–15%` analysis;
- Gate B Live: `+10–30%` encode time;
- Gate C Live с compact content: `1.5–3×`;
- full-shot Studio: `3–10×`;
- Foundry global oracle: `10–100×+`, но это ненормативный регулируемый budget.

Live не должен знать будущее: он открывает cell без конечного срока и посылает
event при превышении objective-error/RDO threshold. Studio/Foundry выигрывают
за счёт знания будущего lifetime.

### 15.3 Изменение decoder power

Нужно различать peak capability и среднее потребление.

- **Peak compute не исчезает:** universal fallback обязан декодировать
  full-screen hostile 4K/8K content. Массовый chip нельзя уменьшить только на
  основании спокойных scenes.
- **Initial software decoder MAY быть медленнее** на `0–20%`, пока cell
  scheduling и composition не слиты в GPU kernels.
- **ASIC target:** cell control state не более десятков KB, без дополнительного
  DPB для Gate B, worst-case control/compute overhead не более `2–5%`.
- **Mixed natural target:** `0–15%` меньше average decoder/DRAM work; это может
  оказаться нулём, если почти весь screen постоянно dirty.
- **Sparse screen/UI target:** `20–60%` меньше decoder/compositor energy.
- При dirty area менее 10% идеальный incremental path может убрать
  `50–90%+` output-buffer writes, но это не равно такому же снижению полного
  wall power: остаются scanout, source reads, panel и OS.

Для полностью неизменного кадра AV2/VVC уже очень дёшевы. Дополнительная
экономия SceneLith появляется прежде всего в отсутствии repeated composition/
framebuffer writes и при panel self-refresh, а не в чудесном устранении
residual, которого там и так нет.

### 15.4 Обычные мониторы и переходный период

Новый монитор **не нужен**, чтобы декодировать и демонстрировать SceneLith:

1. Player хранит Cell state.
2. В каждый VSync обычного 60/120/144/240 Hz monitor он вычисляет
   `PresentationQuery(t)`.
3. Обновляет dirty tiles обычного GPU framebuffer.
4. Передаёт стандартный raster output через HDMI/DisplayPort.

На 60 Hz движение будет физически показано в 60 samples/s; на 240 Hz тот же
MotionLaw можно sample'ить 240 раз без 4× motion syntax. Новые timestamps всё
равно маркируются interpolated, если source Truth был только 60 Hz.

Уже существующие interfaces частично поддерживают нужный путь:

- [Vulkan `VK_KHR_incremental_present`](https://registry.khronos.org/vulkan/specs/latest/man/html/VK_KHR_incremental_present.html)
  передаёт presentation engine список изменённых rectangles;
- [DXGI dirty rectangles/scroll metadata](https://learn.microsoft.com/en-us/windows/win32/direct3ddxgi/dxgi-1-2-presentation-improvements)
  уменьшают memory bandwidth и related power;
- [Windows multiplane overlay/direct scanout](https://learn.microsoft.com/en-us/windows/win32/comp_swapchain/comp-swapchain)
  может избежать лишней desktop composition;
- [VESA eDP Panel Self Refresh](https://vesa.org/featured-articles/vesa-publishes-embedded-displayport-standard-version-1-5/)
  уже позволяет panel хранить static image и получать частичные updates.

На обычном внешнем monitor scanout часто продолжит идти с полной refresh rate,
поэтому главный ранний выигрыш будет в transport/decode/GPU writes, а не во
всей панели.

Новый display/controller нужен только для максимальной версии:

- принять Cells/trajectories напрямую;
- локально хранить texture;
- самостоятельно sample'ить MotionLaw;
- обновлять только изменившиеся pixels.

Это перспективный hardware profile, а не условие запуска codec.

## 16. Implementation ladder: простота до сложности

### Gate A — Temporal syntax oracle

- fixed `128×128` screen grid;
- persistent `HOLD`;
- ideal temporal RLE существующих partition/ref/mode решений;
- никаких compact textures, masks или object semantics.

Цель: измерить абсолютный потолок удаления per-frame unchanged syntax.

### Gate B — Persistent motion runs

- `STATIC` и `LINEAR_TRANSLATION`;
- fixed decoded reference;
- maximum run 256 ticks;
- conventional Truth override;
- до примерно 16 KB control state для 4K candidate profile.

Цель: проверить амортизацию motion/ref/partition syntax без нового renderer.

### Gate C — Compact content cells

- `CAPTURE_TRUTH`;
- coordinate-independent microtile content bank;
- equal memory против AV2 BRU/LTR/Atlas и decoded patch cache;
- opaque order и disocclusion.

Цель: убрать frame-sized reference waste и повторную texture после long gap.

### Gate D — Frame-free decoder API

- arbitrary `PresentationQuery(t)`;
- incremental dirty-tile compositor;
- один stream выводится на 60/120/240 Hz;
- original timestamps проверяются objective Truth;
- interpolated timestamps маркируются отдельно.

Цель: доказать новую функциональность и energy scaling, не только rate.

### Только после успеха

По одному, с отдельной ablation:

- subpixel translation;
- bounded affine;
- finer boundary support;
- exposure integration;
- partial checkpoint/repair;
- illumination trajectory;
- learned innovation transform.

Depth, mesh, 3D, semantics и generative core не добавляются, чтобы спасать
провал Gates A–C.

## 17. Experiments и baselines

Обязательные baselines:

1. финальный AV2/AVM с BRU, skip/merge, global/affine motion, long-term
   references, SEF/implicit output и Atlas/multistream там, где применимо;
2. VVC/VTM с сильным inter/merge/affine/LTR;
3. equal-memory decoded patch cache;
4. ideal temporal RLE существующих mode maps;
5. native multi-layer screen stream, если source layers доступны;
6. flattened raster отдельно, без смешения результатов.

Dataset axes:

- changed area: `0.1/1/5/20/50/100%`;
- lifetime: `2/4/8/16/32/64/256` ticks;
- static/constant velocity/acceleration/nonlinear motion;
- stable и churning boundaries;
- occlusion/reappearance;
- sensor noise, exposure change и motion blur;
- packet loss и random access;
- slides, cursor, IDE, terminal, scrolling, 2D game/animation, surveillance;
- broad natural и hostile water/foliage/crowd/cuts.

Считать:

- полный bitstream;
- state/event/motion/support/checkpoint bits;
- residual/innovation;
- state bytes;
- DRAM reads/writes;
- pixels recomposited per presentation;
- energy estimate;
- latency;
- random-access penalty;
- loss freeze/repair time.

## 18. Kill gates

### Gate A

- `HOLD/RLE` даёт не менее 5% на sparse screen suite и 0.5% на mixed natural;
- иначе оставить как implementation-only power optimization.

### Gate B

`STATIC + LINEAR_TRANSLATION` против tool-complete baseline:

- не менее 12% на scroll/sprite;
- не менее 7% на broad screen suite;
- не менее 3% на mixed natural;
- не менее 5% сверх ideal temporal RLE на target subset;
- event/checkpoint syntax не более 20% gross saving;
- hostile mean regression не более 0.2%, любой clip не более +1%.

### Gate C

Compact cells против equal-memory AV2 BRU/LTR/Atlas и decoded patch cache:

- не менее 15% на puzzle/reappearance subset;
- не менее 5% на mixed corpus;
- median admitted content окупает insertion/support/checkpoint не позже трёх
  uses;
- practical encoder сохраняет не менее 80% oracle net gain.

### Architecture gate

Новый стандарт оправдан, если после сочетания выигравших tools выполняется хотя
бы одно:

- не менее 25% universal gain против contemporaneous anchor;
- новый continuous-output class с materially lower bitrate/latency/energy,
  который нельзя получить эквивалентной конфигурацией AV2/VVC;
- не менее 25–30% decoder/DRAM energy reduction на крупном declared profile
  при отсутствии существенной rate regression.

Отрицательный gate нельзя спасать добавлением depth, masks и neural decoder.

## 19. Агрессивный, но проверяемый timeline

При параллельной круглосуточной работе:

| От старта реализации | TARGET |
|---|---|
| 1–3 дня | Event/state simulator, `SET/PRESENT`, synthetic static/motion demo |
| 4–7 дней | Dirty-tile renderer и bit-exact fixed-point translation |
| 1–2 недели | Gate A и первый perfect-lookahead Gate B oracle |
| 2–4 недели | Fair AV2/VVC temporal-run comparison и negative classes |
| 3–6 недель | Gate C compact `CAPTURE_TRUTH` memory experiment |
| 4–8 недель | GPU incremental compositor и multi-refresh demo |
| 8–16 недель | Broad RD/power corpus, random access, loss и architecture verdict |

Демонстрация frame-free state возможна за дни. Доказательство универсального
compression claim остаётся дольше из-за сильных baselines, corpus runs,
bit-accounting и conformance, а не из-за объёма opcodes.

## 20. Пересмотр задач

Немедленно:

1. реализовать tiny event/state simulator;
2. построить ideal temporal RLE control;
3. проверить `HOLD + LINEAR_TRANSLATION`;
4. сравнить с AV2 BRU/SEF/LTR/Atlas и VVC;
5. измерить dirty pixels/DRAM отдельно от bitrate;
6. только затем включить compact `CAPTURE_TRUTH` cells.

Не делать сейчас:

- full 3D world;
- semantic object decoder;
- arbitrary circle/polygon zoo;
- per-pixel asynchronous event stream;
- neural renderer;
- diffusion;
- alpha/depth/mesh;
- сложный scene graph;
- новый transform до доказательства state/motion thesis.

Главный парадокс простоты:

> Не обновлять изображение быстрее. Дать каждому фрагменту один
> пространственно-временной контракт и молчать, пока контракт верен.
