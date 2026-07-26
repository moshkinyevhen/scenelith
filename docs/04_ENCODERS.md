# Энкодеры SceneLith: Live, Studio и Foundry

Статус документа: **NORMATIVE-DRAFT** для границы bitstream/decoder и
**TARGET** для всех численных бюджетов и показателей эффективности.

Числа ниже являются целями проектирования. Они не являются измеренными
результатами SceneLith и должны подтверждаться воспроизводимыми экспериментами.

## 1. Один bitstream и один декодер

**ACCEPTED:** SceneLith определяет один нормативный bitstream и один
детерминированный decoder для трёх ненормативных классов encoder:

1. **Live** — строго causal real-time кодирование на бытовой GPU;
2. **Studio** — многопроходное кодирование на рабочей станции;
3. **Foundry** — распределённый offline scene compiler с практически
   неограниченным бюджетом поиска.

Все три encoder используют один набор MOSAIC-примитивов, одинаковые ограничения
decoder ISA и одинаковую семантику WorldState. Класс encoder не меняет
реконструкцию уже созданного потока и не является условием его декодируемости.
Различаются только качество анализа, глубина поиска и выбранные encoder решения.

Foundry не может передать произвольный executable graph или скрытую модель.
Любой передаваемый scene adapter обязан использовать ограниченные нормативные
операции, размеры и числовые форматы decoder; полная стоимость adapter входит в
битрейт. Live может использовать законное подмножество syntax без adapter.

Optional Perceptual Detail при любом классе encoder остаётся нереференсным,
никогда не изменяет WorldState и не участвует в предсказании Fidelity/Truth Core.

## 2. Классы encoder

| Характеристика | Live | Studio | Foundry |
|---|---|---|---|
| Основное применение | трансляции, звонки, локальная запись, UGC | мастер-файлы, creator/VOD, архив | фильмы, каталоги, эталонный encode, исследования |
| Анализ будущего | **ACCEPTED:** 0 кадров в strict Live; optional near-live preset до 8 кадров | **TARGET:** 8–32 кадра; quality preset до 1–4 с или полный shot | полный title и связи между shots |
| Кандидаты RDO | **TARGET:** top-K 2–8 на tile/chunk | **TARGET:** top-K 8–64 и несколько проходов | распределённый beam/A*/DP search и множество λ-прогонов |
| Encoder compute | **TARGET:** 10–30 kMAC на выходной пиксель | **TARGET:** 30–300 kMAC на выходной пиксель | **TARGET:** 10–500 GPU-с на секунду исходника |
| Экстремальный режим | **TARGET:** 1× real-time и preset 2–10× медленнее | **TARGET:** 2–100 GPU-с на секунду исходника | **TARGET:** 10³–10⁴ GPU-с на секунду для hero/research encode |
| Оборудование | **TARGET:** 1080p60 на 8 GB VRAM; 4K60 на 12–16 GB | **TARGET:** 1–4 GPU, 16–96 GB суммарной VRAM | распределённый GPU-кластер |
| Адаптация | без обязательного обучения; короткая online-статистика | shot/title dictionary и ограниченный adapter | **TARGET:** 10–500 GPU-часов per-title adaptation, когда это окупается битрейтом |

Для Live бюджет 10–30 kMAC/пиксель соответствует приблизительно 5–15 TMAC/с
при 4K60. Это **TARGET**, а не заявление о достигнутой скорости. Реальная
пропускная способность также ограничивается памятью, синхронизациями, entropy
coding и загрузкой GPU.

### 2.1 Live

Live использует:

- causal MOSAIC Cell state и ограниченную историю;
- fixed-grid change detection и flow на 1/4–1/8 разрешения;
- open-ended `STATIC/LINEAR_TRANSLATION` runs;
- разрыв run, когда objective error или полный RDO перестаёт проходить gate;
- bounded online `CAPTURE_TRUTH`/eviction;
- локальную проверку кандидатов по фактически сформированным битам;
- conventional objective fallback и parallel rANS.

**TARGET:** задержка интерактивного режима — 50–250 мс, если выбранный transport
и checkpoint interval это позволяют.

### 2.2 Studio

Studio расширяет Live следующими возможностями:

- двунаправленный анализ полного shot;
- несколько проходов allocation/RDO;
- более точные flow, boundary/support и tracking;
- совместная оптимизация motion knots, cell lifetime и checkpoints;
- малые per-shot/per-title dictionaries и adapters;
- повторный encode проблемных участков после проверки метрик.

Studio является основным массовым high-quality encoder: его работа должна быть
возможна на одной мощной рабочей станции без обязательного доступа к кластеру.

### 2.3 Foundry

Foundry является encoder-only исследовательским oracle и производственным
scene compiler. Он может использовать:

- анализ полного фильма и loop closure через минуты;
- большие encoder-only vision/world models;
- глобальное сопоставление fragments и повторно появляющихся поверхностей;
- совместный поиск Cell Content/Support/MotionLaw/Lifetime, representation
  routing и rate;
- множество независимых encode trials;
- ансамбль objective, perceptual, OCR, identity, geometry и flicker metrics;
- распределённую per-title оптимизацию dictionaries и ограниченных adapters.

Foundry не является обязательным для получения полезного SceneLith-потока. Его
дополнительная роль — создавать решения teacher для ускорения Live и Studio.

### 2.4 Continuous-Time Cell pipeline

Одна encoder-задача выбирает для каждого кандидата:

```text
Content + Support + MotionLaw + Lifetime + Order + Mode
```

Pipeline:

1. detector отмечает spatiotemporal error относительно текущих active cells;
2. existing motion estimator предлагает `STATIC/LINEAR_TRANSLATION`;
3. temporal DP решает, продолжить run, поставить knot, split support или
   перейти к Truth fallback;
4. compact-memory planner решает, окупится ли `CAPTURE_TRUTH`;
5. exact RDO сравнивает полный event/support/motion/checkpoint/innovation rate
   с AV2/VVC-like raster path;
6. только положительный net candidate попадает в stream.

Live не обязан заранее знать `death_time`: он создаёт open-ended cell и
посылает новый event, когда контракт перестал быть верен. Studio знает shot и
может оптимизировать duration. Foundry ищет long-gap correspondence по title,
но decoder и bitstream одинаковы.

Foundry не сравнивает миллион samples попарно. Он выполняет shot segmentation,
low-resolution indexing, key-sample selection, local tracks и loop-closure
retrieval; full-resolution registration запускается только для shortlist.

Никогда не наблюдавшаяся область не генерируется для Truth playback. Content
становится reference только через inline objective decode или подтверждённый
`CAPTURE_TRUTH`. Display-only generation остаётся Perceptual Detail.

Полная модель:
[14_CONTINUOUS_TIME_CELLS.md](14_CONTINUOUS_TIME_CELLS.md).

### 2.5 Изменение encoder complexity

Все множители — **HYPOTHESIS/TARGET**, не измеренные результаты:

| Реализация | Относительно сильного conventional encoder |
|---|---:|
| Gate A: ideal temporal RLE/HOLD | `+5–15%` analysis |
| Gate B: fixed-grid linear motion runs | `+10–30%` Live encode time |
| Gate C: causal compact cells | `1.5–3×` Live |
| Full-shot Studio cells | `3–10×` |
| Foundry global oracle | `10–100×+`, budget-controlled |

Gate B переиспользует conventional motion candidates и добавляет temporal DP.
Gate C сложнее из-за support, capture/eviction и long-horizon value. Эти затраты
ненормативны и не переходят в decoder.

Если practical Live сохраняет менее 80% oracle net gain, tool упрощается либо
остаётся Studio/VOD-only.

## 3. Rate-distortion-compute optimization

Базовый multi-objective критерий encoder:

\[
J =
R_{\mathrm{total}}
+ \lambda D_{\mathrm{truth}}
+ \alpha D_{\mathrm{perceptual}}
+ \mu C_{\mathrm{decode}}
+ \nu M_{\mathrm{state}}
+ \rho L_{\mathrm{seek}}
+ \kappa P_{\mathrm{loss}}
+ \eta S_{\mathrm{instability}}.
\]

Где:

- \(R_{\mathrm{total}}\) включает payload, headers, memory deltas, adapters,
  checkpoints, indexes и FEC;
- \(D_{\mathrm{truth}}\) измеряет Fidelity/Truth Core;
- \(D_{\mathrm{perceptual}}\) применяется только к разрешённому нереференсному
  perceptual layer;
- \(C_{\mathrm{decode}}\) и \(M_{\mathrm{state}}\) ограничивают decoder compute
  и память;
- \(L_{\mathrm{seek}}\) штрафует дорогой random access;
- \(P_{\mathrm{loss}}\) учитывает распространение ошибок;
- \(S_{\mathrm{instability}}\) штрафует flicker, state drift и нестабильный
  representation switching.

Финальный выбор режима должен учитывать фактические полные биты. Entropy proxy
разрешён для предварительного ранжирования, но не для итогового отчёта RD.
Сравнение encoder проводится при одинаковых decoder profile, latency,
random-access и resilience constraints.

Live применяет learned proposal и точный локальный RDO. Studio увеличивает
горизонт и beam. Foundry выполняет глобальную или приближённо глобальную
оптимизацию по chunks, checkpoints и состоянию сцены.

## 4. Teacher–student distillation

Foundry сохраняет для каждого исследованного участка:

- Pareto-набор кандидатов и их фактический rate;
- выбранный representation primitive;
- Cell Content/Support и capture/reuse decisions;
- cell lifetime, update и eviction решения;
- MotionLaw knots, order и occlusion decisions;
- Q/bit allocation;
- checkpoint placement;
- полное значение компонентов \(J\);
- причины расхождения с Live/Studio.

Ненормативный student-router Live/Studio обучается:

1. imitation learning на лучших Foundry-решениях;
2. pairwise ranking кандидатов;
3. регрессии компонентов RDO;
4. DAgger/hard-negative циклом на случаях расхождения student и teacher;
5. quantization-aware training и INT8 pruning.

Student только предлагает top-K. Bit-exact RDO сохраняет право отвергнуть его
предложение. При высокой uncertainty encoder расширяет K либо использует
безопасный fallback. Веса encoder ненормативны и могут обновляться без изменения
bitstream или decoder.

Так стоимость Foundry-поиска амортизируется: однажды найденная закономерность
становится быстрым решением на бытовой GPU.

## 5. Целевой разрыв качества

Для одного контента, уровня качества и одинаковых ограничений обозначим:

- \(B_A\) — полный битрейт внешнего anchor;
- \(B_F\) — полный битрейт Foundry;
- \(B_L\) — полный битрейт Live.

Доля Foundry-выигрыша, сохранённая Live:

\[
G_{\mathrm{capture}} =
\frac{B_A - B_L}{B_A - B_F}.
\]

**TARGET:** Live должен сохранять не менее 80% Foundry-выигрыша в ранней
пригодной версии и 90% в зрелой версии на основном закрытом тестовом наборе.
Правило применяется только когда Foundry статистически значимо лучше anchor.

Дополнительные цели:

- **TARGET:** зрелый Live использует не более чем на 8–15% больше битов, чем
  Foundry, на общем видео при равном качестве и constraints;
- **TARGET:** Studio использует не более чем на 3–8% больше битов, чем Foundry;
- **TARGET:** против contemporaneous strong anchor Live достигает 25–35%
  экономии битрейта, Studio — 30–40%, Foundry — 35–45%;
- **TARGET:** существенно больший разрыв Foundry допускается как отдельный
  результат только для заранее определённых specialised classes, например
  talking-head, UI или длинного повторяющегося VOD.

Процентные цели не считаются достигнутыми без hidden-set тестирования, полного
учёта всех служебных битов и проверки независимым decoder.

Если Live систематически сохраняет менее 80% Foundry-выигрыша, проблему нельзя
маскировать обязательным облачным encode. Необходимо упростить representation
search, улучшить distillation/router либо пересмотреть syntax. Массовый успех
SceneLith требует, чтобы бытовой encoder уже давал основную часть структурного
выигрыша, а Foundry улучшал максимум, обучал быстрые encoder и обслуживал
дорогой offline VOD.
