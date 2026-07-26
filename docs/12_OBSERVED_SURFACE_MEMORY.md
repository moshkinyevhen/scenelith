# Observed Surface Memory: Evidence Atlas

Статус: **RESEARCH / SUPERSEDED FOR MAIN-0** решениями D-015 и D-017.
Семантика `Domain/Known`, 2.5D и полная OSM не входит в первый implementation
gate. DPM baseline находится в
[13_MINIMAL_PATCH_CORE.md](13_MINIMAL_PATCH_CORE.md), текущий time/state
candidate — в
[14_CONTINUOUS_TIME_CELLS.md](14_CONTINUOUS_TIME_CELLS.md). Все показатели
здесь остаются **HYPOTHESIS/TARGET**.  
Дата: 2026-07-26

Рабочие названия:

- **Observed Surface Memory (OSM)** — нормативная подсистема `WorldState`;
- **Evidence Atlas** или **Witness Atlas** — разговорное/internal название;
- **Minimal Sufficient Scene** — encoder-only принцип построения представления.

Термин `Atlas` уже используется AV2 и immersive standards для других
конструкций. В публичной syntax предпочтительно **Observed Surface Memory**,
пока терминологический и IP review не завершён.

## 1. Что меняется

SceneLith не должен восстанавливать полный физически правильный или
правдоподобно дорисованный мир. Для воспроизведения заданного видео достаточно
минимального набора фрагментов поверхностей, которые действительно участвуют в
целевых кадрах.

**NORMATIVE-DRAFT:**

- никогда не наблюдавшаяся и никогда не выводимая область не требует bits;
- неизвестность является явным состоянием, а не чёрным, прозрачным или
  синтезированным texel;
- `Truth` renderer не имеет права читать неизвестный sample;
- видимые фрагменты могут после Truth reconstruction быть сохранены в
  долгоживущую память и повторно использоваться;
- любое место, которое невозможно предсказать из определённого состояния,
  кодируется `REPLACE/TruthInnovation`;
- генеративный display-only слой никогда не делает неизвестный texel
  нормативно известным.

Это переносит основную сложность из decoder-side world generation в
encoder-only correspondence, segmentation, geometry estimation и RDO.

## 2. Модель фрагмента

Для поверхности \(i\):

\[
F_i=(T_i,\Omega_i,W_i(t),V_i(t),Z_i(t),P_i),
\]

где:

- \(T_i\) — реконструированная каноническая текстура;
- \(\Omega_i\) — разреженная область определённых samples;
- \(W_i(t)\) — integer warp, mesh или trajectory;
- \(V_i(t)\) — visibility;
- \(Z_i(t)\) — depth/order;
- \(P_i\) — provenance class.

Для каждого atlas texel используются `DomainMask D` и `KnownMask K`:

| D | K | Значение |
|---|---|---|
| 0 | 0 | texel не объявлен частью поверхности |
| 1 | 0 | поверхность существует, sample неизвестен |
| 1 | 1 | sample нормативно восстановлен и доступен |
| 0 | 1 | запрещённое состояние |

`UNKNOWN` не равен прозрачности. Если неизвестная передняя поверхность
окклюдирует фон, decoder не должен показать задний слой сквозь неё. Такой
output region получает `REPLACE` или безопасный frame-based fallback.

Для filtered sampling все taps footprint должны быть известны. В первом
профиле integer bilinear sample допустим только при `K=1` у всех четырёх taps.

## 3. Ключевая операция: CAPTURE_PROMOTE

Главный практический primitive:

```text
CAPTURE_PROMOTE {
    source_truth_slot
    source_instance_id
    destination_surface
    destination_page
    destination_mask
    destination_to_source_integer_map
    capture_mask_mode          // DERIVED_VISIBLE | EXPLICIT | BOTH
    capture_filter_id
    write_mode                  // NEW_ONLY | REFRESH
}
```

После полного восстановления и проверки Truth frame decoder копирует выбранные
reconstructed pixels в atlas. Texture payload уже был оплачен текущим кадром;
повторно передаются только mask, mapping и lifecycle metadata.

Для destination texel \(d\), отображаемого в frame coordinate \(F(d)\):

\[
CaptureValid(d)=M(d)\land
\bigwedge_{q\in Footprint(F(d))}
Owner(q)=source\_instance.
\]

Ни один tap не должен принадлежать foreground object или другому surface.
Decoder не проверяет семантическое утверждение «это дом»; он проверяет только
нормативную ownership/mask согласованность. Ошибка encoder ухудшает будущий
rate, но не меняет bit-exact output.

Encoder SHOULD захватывать guard ring шириной в один source texel для bilinear
reuse. Decoder MUST NOT самостоятельно делать dilation, edge replication или
clamp-to-known. Отсутствующий guard делает будущую выборку `UNRESOLVED`.

Порядок:

1. Decoder читает неизменяемый pre-access-unit state.
2. Structural render создаёт prediction и `ResolvedMask`.
3. Truth Innovation восстанавливает objective output.
4. Integrity и bounds проверяются.
5. `CAPTURE_PROMOTE` строит новую страницу в staging memory.
6. Проверяется post-state hash.
7. Memory Delta коммитится атомарно и становится доступен следующей Spine Unit.

Повреждённый, concealment-generated или perceptual output не может быть
источником `CAPTURE_PROMOTE`.
Все target writes одной транзакции должны быть непересекающимися; sources
читаются только из immutable pre-state или завершённых Truth outputs.

## 4. Пример: человек проходит вдоль дома

1. Encoder связывает видимые части стены в разных кадрах с одной поверхностью.
2. Силуэт человека исключается capture-mask.
3. По мере движения человека вновь раскрытые части стены сохраняются через
   `CAPTURE_PROMOTE`.
4. Никогда не показанные части стены остаются `UNKNOWN` и не занимают texture
   payload.
5. Стена рендерится из atlas через homography или bounded mesh warp.
6. Человек кодируется отдельным patch/deformable layer либо обычным motion
   fallback.
7. Тени, отражения, волосы, motion blur и изменения освещения исправляются
   ephemeral layer и Truth Innovation.
8. Если фрагмент больше не повторится, RDO может не сохранять его вообще.

Никакая семантическая «модель дома» decoder не нужна. Достаточна компрессионная
геометрия, которая дёшево воспроизводит исходную траекторию камеры.

## 5. GPU/ASIC-friendly произвольная форма

Произвольный фрагмент не должен означать pointer-rich pixel list.

**NORMATIVE-DRAFT кандидаты:**

- логические atlas pages фиксированного размера;
- sparse microtiles;
- прямоугольный texture resource и компактные `Domain/Known` bitmasks;
- bounded per-output-tile draw list;
- affine/projective или piecewise-affine inverse mapping;
- integer depth либо compact explicit owner map;
- детерминированные fill, tie-break, interpolation, rounding и saturation;
- generation counters для защиты от use-after-free старой страницы.

**CANDIDATE:** page `128×128`, microtile `8×8`, по одному 64-битному слову
`DomainMask` и `KnownMask` на microtile. Эти размеры не заморожены.

Decoder не выполняет segmentation, SLAM, depth inference, object recognition
или generative completion.

## 6. Иерархия режимов

Encoder выбирает самый дешёвый режим для каждого region/chunk:

1. recent-frame motion compensation;
2. equal-memory long-term decoded reference;
3. decoded patch cache;
4. 2D Evidence Atlas;
5. layered 2.5D atlas с depth/alpha/mesh;
6. sparse 3D surfels/splats для подходящих сцен;
7. intra/innovation replacement.

Main v0 начинает с 2D и ограниченного 2.5D. Полный 3D и INR не являются
обязательными режимами.

## 7. Encoder и миллион кадров

Миллион frames нельзя сравнивать попарно: это порядка \(10^{12}\) пар.
Практический Foundry pipeline иерархичен:

1. scene-cut и shot segmentation;
2. low-resolution features для всех кадров;
3. keyframe selection;
4. local tracks через flow/masks;
5. loop-closure retrieval по компактному index;
6. full-resolution registration только для небольшого списка кандидатов;
7. observation graph и глобальный hardware-aware RDO.

Live строит atlas causal по уже полученным наблюдениям. Studio анализирует shot.
Foundry может анализировать весь title и выбирать лучшие наблюдения, но decoder
и bitstream у них одинаковы.

Foundry-router не заменяется:

- OSM определяет, **что можно хранить и рендерить**;
- router предлагает, **когда создать/расширить/использовать/удалить fragment**;
- точный RDO проверяет, что полный rate действительно ниже fallback.

## 8. Полная rate-модель

Для surface reuse:

\[
\begin{aligned}
R_{\mathrm{OSM}}={}&R_{\mathrm{capture}}+R_{\mathrm{domain}}
+R_{\mathrm{geometry}}+R_{\mathrm{visibility}}\\
&+R_{\mathrm{updates}}+R_{\mathrm{checkpoints}}
+R_{\mathrm{residual,OSM}},\\
R_{\mathrm{baseline}}={}&R_{\mathrm{motion}}+R_{\mathrm{ref\_management}}
+R_{\mathrm{residual,baseline}}.
\end{aligned}
\]

OSM выбирается только если на горизонте reuse:

\[
G=R_{\mathrm{baseline}}-R_{\mathrm{OSM}}>0.
\]

Сравнение обязательно выполняется с **equal-memory long-term reference** и
decoded patch cache. Иначе выигрыш может оказаться следствием большей памяти, а
не новой scene representation.

## 9. Почему потолок сжатия меняется

Для устойчивой поверхности, используемой \(q\) раз:

\[
R_{\mathrm{OSM}}(q)
\approx R_{\mathrm{texture\ once}}
+q(R_{\mathrm{pose}}+R_{\mathrm{visibility}}+R_{\mathrm{small\ residual}}).
\]

У frame-based baseline повторная texture mismatch обычно продолжает создавать
residual. Если сцена идеально повторяема и innovation стремится к нулю, texture
cost SceneLith амортизируется один раз. Поэтому максимальный выигрыш не имеет
единого процента: на искусственном периодическом content отношение может расти
с продолжительностью ролика.

Это не означает универсальное бесконечное сжатие. Первый уникальный sample
должен быть:

- однажды передан;
- либо получен нормативным predictor и objective correction;
- либо уже существовать в подтверждённом Truth state.

## 10. Диапазоны для экспериментов

Все числа ниже — **HYPOTHESIS/TARGET**, не результаты. `Net saving` означает
полную дельту bitrate после geometry, masks, state updates, checkpoints и
residual при одинаковом objective quality.

| Content | Рабочая TARGET net saving | HYPOTHESIS ceiling |
|---|---:|---:|
| Static/planar, всё уже помещается в equal-memory LTR | 0–8% | 10–15% |
| Rigid/screen с long-gap revisit, sprite reuse или working set больше frame-reference coverage | 20–45% | 45–65% |
| Puzzle-friendly natural: длинный shot, repeated surfaces, умеренный parallax/light | 10–25% | 25–40% |
| Смешанный uncurated natural corpus | 4–12% | 12–20% |
| Fire/water/foliage/crowds/grain/reflections/cuts | 0–1% с fallback | 1–3% на редких periodic regions |

При self-contained random access около 1 секунды нижняя/средняя часть этих
диапазонов вероятнее: state snapshot повторно тарифицирует texture и metadata.

На искусственном infinite-GOP ролике, где почти весь inter payload является
повторным вводом вытесненных поверхностей, можно теоретически убрать 70–95%
этого inter payload, а предел при \(T\to\infty\) приближается к 100%. Это не
означает 70–95% полного bitrate на natural video и не является product claim.
Если нужная texture уже доступна equal-memory LTR с точным warp, выигрыш OSM
может быть почти нулевым.

Полный SceneLith может сочетать OSM с multi-frame innovation, quantization и
entropy tools. Проценты отдельных модулей нельзя механически складывать.

## 11. Обновлённый инженерный timeline

Оценка предполагает 3–4 параллельных workstreams, круглосуточное продолжение
работы, готовые flow/depth/segmentation components и узкий первый профиль:
opaque patches, affine/bounded mesh, bilinear filter, без diffusion decoder.

| Результат | Оптимистично | Реалистично |
|---|---:|---:|
| Исполняемый synthetic skeleton с known masks/warps | 48–72 часа | 4–7 дней |
| Oracle experiment с полным bit accounting на выбранных real shots | 2–3 недели | 4–6 недель |
| Первый end-to-end stream: encoder → syntax → CPU Truth output | 4–6 недель | 8–12 недель |
| GPU decode, `CAPTURE/PROMOTE`, basic MAP и conformance | 6–9 недель | 10–16 недель |
| Устойчивая research platform с practical Studio encoder | 8–12 недель | 14–22 недели |
| Proposal-grade evidence на широком corpus | 12–20 недель | 24–40 недель |

Прежние **6–12 недель** остаются правдоподобными для первой вертикальной
версии, а не для доказанного стандарта. Новая формулировка не уничтожает
timeline; она:

- даёт исполняемый skeleton за дни;
- позволяет убить неверную гипотезу oracle-тестом до тяжёлой ML-разработки;
- исключает из Main v0 универсальную 3D reconstruction, генерацию невидимого и
  neural world decoder;
- делает 6–12-недельную версию существенно более содержательной и
  стандартизуемой.

Версия с честным общим BD-rate, GPU path, masks, checkpoints и несколькими
content classes реалистичнее оценивается в **10–16 недель**. Полный стандарт и
silicon-ready профиль не превращаются в недельную задачу из-за datasets,
interoperability, corpus runs и последовательных bit-exact/RD gates.

Главная экономия времени относительно полного world model — не нужно сначала
решать универсальную monocular 3D reconstruction, генерацию невидимых областей
и тяжёлый neural decoder. Сложность остаётся в practical encoder и
доказательстве выигрыша, но теперь её можно вводить ступенчато.

### 11.1 Изменение сложности

| Свойство | Frame codec | OSM SceneLith | Full generative world model |
|---|---|---|---|
| Persistent state | DPB frames | Sparse pages, masks, lifecycle | 3D/neural latent world |
| Decoder analysis | Нет | Нет | Часто model inference/rendering |
| Decoder operations | MC, filters, transforms | Integer warp, mask, depth/owner, capture, residual | Большой tensor graph/neural renderer |
| Bit-exactness | Отработана | Достижима фиксированной integer ISA | Существенно труднее |
| Encoder analysis | Motion/RDO | Global tracking, stitching, observation graph, state RDO | World reconstruction, inference/training и RDO |
| ASIC path | Доказан | Реалистичен через texture/cache/mask blocks | Высокий риск до заморозки моделей |

**HYPOTHESIS для планирования, не измеренный результат:**

- OSM reference decoder — примерно `1.3–2×` инженерной сложности минимального
  conventional research decoder; это не прогноз silicon area или runtime;
- early Live encoder pipeline — порядка `2–5×` conventional Live по числу
  analysis stages;
- early Studio pipeline — порядка `5–20×` conventional Studio;
- Foundry может быть на порядки тяжелее, не изменяя нормативный decoder;
- full generative world decoder ожидается существенно тяжелее OSM и хуже
  подходит для первого bit-exact ASIC profile.

OSM не обязан добавляться поверх всех VVC tools. Цель — заменить часть сложной
frame-based prediction более регулярными GPU-native операциями, поэтому
сложность итогового decoder определяется после удаления проигравших tools.

## 12. Kill gates

1. Oracle с perfect camera/depth/visibility должен дать после всех side bits:
   - не менее 30% на ideal long-gap revisit;
   - не менее 15% на puzzle subset;
   - не менее 5% на mixed set против equal-memory AVM/VTM-class LTR.
2. Против equal-memory deduplicating decoded patch cache OSM должен дать не
   менее 10% на puzzle subset и 3–5% на mixed set. Иначе оставить простой
   patch cache и убрать лишнюю world geometry.
3. Practical estimator должен сохранить не менее 65–70% oracle **net** delta.
4. Geometry, masks и updates на active puzzle regions должны составлять не
   более 8% baseline rate; вся non-residual OSM side information — не более
   12%.
5. Checkpoint overhead должен оставаться не более 8% при 1 s random access и
   4–5% при 2 s.
6. Средняя regression hostile class после fallback — не более 0.5%, p95 clip —
   не более +3%, ни один clip — не более +5%.
7. OSM syntax overhead при отключённом mode — не более 0.3%.
8. Uncorrected never-observed pixels в Truth Core: ровно 0.
9. Если полный 3D даёт менее 7–10% сверх 2.5D после geometry/checkpoint bits,
   он исключается из Main.
10. Median admitted page должна окупить insertion, mapping, masks, updates и
    checkpoint allocation не позднее 2–3 uses.

## 13. Prior art и потенциальная новизна

Сами по себе background mosaic, arbitrary-shape object, progressive sprite
reveal, layered atlas, occupancy map и 3D splat не являются новыми.

Потенциально отличительная комбинация SceneLith:

- неизвестность как нормативное состояние reference memory;
- evidence-bounded fragment вместо обязательного полного объекта;
- `CAPTURE_PROMOTE` без повторного texture payload;
- явный visibility/filter-footprint contract;
- transactional sparse GPU memory с bounded lifetime/checkpoints;
- global RDO, учитывающий всю стоимость state;
- один universal fallback codec path;
- строгая граница Truth и generative display shell.

Новизна этой комбинации должна подтверждаться отдельным patent/prior-art
search до syntax freeze.

Дополнительный терминологический риск: AV2 уже использует `Atlas` как virtual
2D image для decoded layers/multistream composition. Поэтому рабочее
нормативное имя модуля — `Observed Surface Memory`, не просто `Atlas`.
