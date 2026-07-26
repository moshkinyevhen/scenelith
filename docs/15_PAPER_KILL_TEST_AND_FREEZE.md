# Бумажный kill-test и обоснование архитектурной заморозки

Дата: 2026-07-26  
Статус: paper model — **HYPOTHESIS**; semantic spine — **ACCEPTED** решением
D-025; payload и числа — **NORMATIVE-DRAFT / TARGET**.  
Связанные решения: D-017, D-020, D-021, D-022, D-023, D-025, D-026

## 1. Что именно требуется превзойти

SceneLith сравнивается не с абстрактным «современным codec» и не с одним
объединённым baseline.

Главные baselines измеряются **отдельно**:

1. **AV2 v1.0 / AVM v1.0.0**, опубликованный AOMedia 28 мая 2026 года;
2. **VVC / H.266 (редакция 2026 года) / VTM**.

Для AV2 должны быть включены все применимые инструменты, включая BRU,
long-term references, Show Existing Frame и Atlas. Для VVC должны быть включены
все применимые inter, merge, affine и long-term-reference инструменты.

Сравнение считается честным только при одинаковых:

- исходнике, bit depth и chroma format;
- объективном или явно объявленном perceptual quality criterion;
- latency и lookahead class;
- random-access interval;
- decoder/reference memory limit;
- encoder effort class;
- учёте всех dictionaries, adapters, weights, checkpoints и container overhead.

Сравнение с AV1, HEVC, AVC либо быстрым hardware preset может публиковаться
дополнительно, но не доказывает победу над frontier baseline.

## 2. Почему мыслительный эксперимент полезен, но не является benchmark

Он может:

- вывести верхний предел syntax-only идеи;
- показать, какую долю residual/innovation обязательно нужно устранить;
- отвергнуть архитектуру, которая даже при благоприятных предположениях не
  достигает цели;
- проверить универсальность и bounded decoder complexity.

Он не может узнать:

- реальное распределение битов AVM/VTM на неизвестном corpus;
- насколько хороший encoder найдёт spacetime decomposition;
- реальную энтропию residual после такой decomposition;
- BD-rate при конкретной метрике качества.

Следовательно, бумажная модель используется для выбора архитектуры, а не для
публичного заявления о достигнутом выигрыше.

## 3. Нормализованная rate model

Для каждого baseline отдельно принимается:

\[
R_B=C_B+M_B+I_B=1,
\]

где:

- \(C_B\) — partition, mode, reference и control syntax;
- \(M_B\) — motion signalling;
- \(I_B\) — sample innovation: coefficients, new texture, refresh и прочая
  информация, которую нельзя получить из текущего predictor state.

Гипотетический net gain SceneLith:

\[
G =
C_Bs_C + M_Bs_M + I_Bs_I - O_Q,
\]

где \(s_C,s_M,s_I\) — устранённые доли соответствующих компонент, а \(O_Q\) —
новые support, lifecycle, event, checkpoint и content-state bits.

`framebuffer work` в эту формулу не входит: это преимущество по энергии и
memory traffic, а не по bitrate.

Главное следствие:

> Если \(s_I\) близко к нулю, lifetime и trajectory могут экономить только
> небольшие control/motion компоненты. Радикальное сжатие требует уменьшить
> именно innovation bits.

## 4. Детерминированная sensitivity simulation

Канонический скрипт:
[`../experiments/paper_kill_test.py`](../experiments/paper_kill_test.py).

Он выполняет 200 000 deterministic Monte-Carlo samples на scenario. Интервалы
являются явными инженерными предположениями, а не измеренной статистикой.

### 4.1 Результат против AV2 v1.0 / AVM v1.0.0

| Scenario | p10 | median | p90 |
|---|---:|---:|---:|
| Mixed: только lifetime + linear law | -0.3% | 1.0% | 2.3% |
| Mixed: compact persistent Cell | -0.4% | 1.3% | 3.1% |
| Mixed: persistent TruthInnovation only | 0.6% | 4.1% | 7.6% |
| Mixed: low-rank basis target envelope | 6.2% | 14.1% | 22.0% |
| Coherent pan/occlusion: compact Cell | 1.8% | 5.2% | 8.6% |
| Screen/UI/scroll: compact Cell | 5.7% | 11.0% | 16.0% |
| Stable arbitrary/soft silhouette | 1.9% | 5.5% | 9.0% |
| Hair/smoke/chaotic boundary: forced Cell | -7.7% | -4.3% | -0.9% |
| Hostile dynamic: forced Cell | -1.8% | -0.6% | 0.7% |

### 4.2 Результат против VVC / H.266 / VTM

| Scenario | p10 | median | p90 |
|---|---:|---:|---:|
| Mixed: только lifetime + linear law | 1.5% | 3.2% | 5.0% |
| Mixed: compact persistent Cell | 1.7% | 3.8% | 6.1% |
| Mixed: persistent TruthInnovation only | 4.2% | 8.4% | 12.5% |
| Mixed: low-rank basis target envelope | 10.6% | 19.6% | 28.5% |
| Coherent pan/occlusion: compact Cell | 4.7% | 8.4% | 12.1% |
| Screen/UI/scroll: compact Cell | 11.2% | 17.7% | 23.8% |
| Stable arbitrary/soft silhouette | 6.0% | 10.4% | 14.7% |
| Hair/smoke/chaotic boundary: forced Cell | -6.8% | -3.2% | 0.4% |
| Hostile dynamic: forced Cell | -1.2% | 0.2% | 1.6% |

Отрицательный forced result в настоящем encoder должен быть ограничен почти
нулём через exact fallback. Fallback предотвращает проигрыш, но не создаёт
выигрыш.

`Low-rank basis target envelope` — не ожидаемый результат. Его prior намеренно
предполагает, что новая модель уже устраняет 10–32% оставшихся innovation bits
AV2 либо 12–38% VVC. Строка отвечает на вопрос «что будет, если главная
гипотеза сработает», а не доказывает, что она сработает.

### 4.3 Порог революционного результата против AV2

Для representative mixed-natural ledger:

- control: 7.5%;
- motion: 5.75%;
- устранение control: 37.5%;
- устранение motion: 45%;
- новый SceneLith overhead: 8%.

Тогда нужно устранить следующую долю **оставшихся AV2 innovation bits**:

| Цель total bitrate reduction | От всех AV2 innovation | При coverage 50% | При coverage 80% |
|---:|---:|---:|---:|
| 10% | 14.5% | 29.0% покрытого residual | 18.2% |
| 25% | 31.8% | 63.6% покрытого residual | 39.8% |
| 40% | 49.1% | 98.2% покрытого residual | 61.4% |

При coverage 30% цель 25% уже математически невозможна в этом ledger: даже
полное устранение residual на покрытых областях недостаточно.

Это главный результат paper kill-test:

> Cells, которые только живут дольше и передают trajectory реже, не могут быть
> революционным Main. Для 25% против AV2 новая модель должна убрать примерно
> треть всех innovation bits, которые уже остались после AV2 prediction; при
> 50% coverage это почти две трети residual в покрытых областях.

## 5. Отвергнутые варианты Main

### 5.1 `HOLD` или разные region refresh rates

Полезны для power и screen content, но современные codecs уже почти бесплатно
кодируют unchanged blocks. Это component, не архитектурное ядро.

### 5.2 Object/mesh/depth/world reconstruction

Может дать выигрыш на отдельных сценах, но вводит segmentation, topology,
occlusion repair и branch-heavy decoder. Это нарушает цель минимального
нормативного ядра и пересекается с MPEG-4 object coding и AV2 Atlas.

### 5.3 Неограниченный neural graph или shader VM

Упрощает публикацию новых моделей, но уничтожает bounded complexity,
детерминизм, security audit и шанс на дешёвый ASIC.

### 5.4 Generative completion внутри Truth state

Может резко улучшить perceptual bitrate, но не сохраняет объективную истину и
загрязняет future prediction. Допускается только как Optional Perceptual Detail.

### 5.5 Conventional residual per output sample

Если каждый display/source timestamp снова получает почти полный residual
AV2/VVC, frame-free state становится красивой оболочкой с небольшим выигрышем.

## 6. Рекомендуемый кандидат: одна Spacetime Basis Cell

Cell не является semantic object. Это только найденный encoder-ом
rate-distortion atom.

Для output coordinate \(p=(x,y)\) Cell синтезирует scalar gate \(g_i\) и
premultiplied либо signed color contribution \(c_i\):

\[
\left(g_i(p,t),c_i(p,t)\right)=
\sum_{k=0}^{K_i-1}
a_{i,k}(t)\,
B_{i,k}\!\left(W_i(p,t)\right),
\qquad p\in S_i.
\]

где:

- \(B_{i,k}\) — immutable decoded integer basis fields;
- \(S_i\) — консервативная bounded union dyadic microtiles только для хранения,
  scheduling и culling;
- \(W_i(p,t)\) — absolute fixed-point coordinate law;
- \(a_{i,k}(t)\) — bounded fixed-point temporal coefficient laws;
- `(order_key, cell_id)` задаёт deterministic order.

Вне \(S_i\) Cell является тождественным no-op: \(g_i=1,c_i=0\).
Единственная runtime composition operation:

\[
Y_0(p,t)=0,\qquad
Y_{j+1}(p,t)=
Clip\left(g_j(p,t)Y_j(p,t)+c_j(p,t)\right).
\]

Это одна машина, а не zoo инструментов:

- static opaque texture: \(g=0\), \(K=1\), constant \(W\), constant \(a\);
- moving texture: \(g=0\), \(K=1\), time-varying \(W\);
- fade или illumination change: несколько bases и меняющиеся \(a_k(t)\);
- soft arbitrary shape: \(g=1-\alpha,\ c=\alpha F\);
- persistent additive correction: \(g=1,\ c=E\);
- hard replace: \(g=0,\ c=F\);
- arbitrary raster fallback: full-output Cell на один source interval.

Таким образом `TruthInnovation` не обязана быть отдельным frame residual codec.
Она представляется тем же affine-composition Cell primitive.

### 6.1 Произвольная форма без прямоугольных артефактов

Dyadic tiles и rectangular texture allocation **не являются видимой формой**.
Они только ограничивают область, где Cell может отличаться от identity.

Видимый footprint задаёт sampled gate \(g(p,t)\):

- binary opaque silhouette;
- subpixel antialiased edge;
- hair/fur coverage;
- transparency;
- motion-blur edge;
- smoke или shadow contribution.

Gate кодируется тем же basis/payload mechanism, а не polygon/circle/spline zoo.
На границе обязательны:

- conservative support padding;
- profile-defined texture apron для всех interpolation taps;
- identity \(g=1,c=0\) до внешней границы support;
- objective innovation там, где compact gate predictor недостаточен.

Поэтому coarse tiles не могут проявиться как квадраты. Для mathematically
lossless profile последняя short-lived Cell может поставить \(g=0\) и точное
\(c=Truth\) на любых ошибочных pixels.

Нельзя обещать отсутствие любых distortion artifacts при произвольно низком
lossy bitrate: это нарушило бы rate-distortion limit. Нормативная цель:

- никаких артефактов, вызванных формой storage tiles;
- lossless exact mode;
- visually transparent mode с отдельным строгим boundary metric;
- RDO fallback, если coding gate дороже обычной innovation.

Sensitivity model показывает, почему fallback обязателен:

- стабильная произвольная/мягкая граница имеет положительную гипотетическую
  median: 5.5% против AV2 и 10.4% против VVC;
- forced Cell на волосах/дыме/хаотической границе имеет отрицательную median:
  -4.3% против AV2 и -3.2% против VVC.

Следствие: arbitrary shape всегда поддерживается без видимого rectangle, но
отдельный persistent shape используется только когда RDO выигрывает. В
противном случае Truth кодируется короткоживущей универсальной Cell без
архитектурного переключения.

### 6.2 Почему это сильнее предыдущей Cell

Предыдущая Cell амортизировала control и motion, но обычно оставляла почти тот
же residual.

Spacetime Basis Cell пытается снизить residual тремя способами:

1. motion-aligned texture платится один раз;
2. изменение appearance во времени описывается несколькими coefficient laws;
3. повторяющийся residual становится persistent/low-rank basis, а не новой
   таблицей coefficients на каждый sample.

Это warped low-rank plus sparse decomposition, но decoder не выполняет
segmentation, neural reasoning или world completion. Всю тяжёлую оптимизацию
делает asymmetric encoder.

## 7. Минимальный decoder contract

Кандидат state grammar имеет только:

```text
RESET(epoch_time)
SET(event_time, cell_id, alive, changed_fields, payload_or_reference)
```

- `alive=0` удаляет Cell;
- отсутствие `SET` означает бесконечное сохранение текущего state;
- checkpoint является `RESET + SET*`, а не новым primitive;
- presentation schedule находится в container/API track;
- `PresentationQuery(t)` читает state, но не является mutation opcode.

Нормативный render loop:

1. entropy-decode изменённые payload/state fields;
2. evaluate fixed-point \(W_i(p,t)\);
3. sample не более profile-bounded \(K\) basis textures;
4. выполнить fixed-point multiply-accumulate;
5. выполнить один affine-composition FMA \(gY+c\);
6. clip и output.

### 7.1 Main targets, ещё не принятые limits

- \(K\le4\) либо другое малое profile-bound значение;
- dyadic support используется только для culling/storage, не как visible shape;
- произвольная видимая форма задаётся bounded gate field;
- piecewise-linear coefficient laws;
- static/translation/affine fixed-point coordinate law;
- одна affine-composition operation \(gY+c\);
- никаких depth, mesh, semantics и arbitrary graph;
- не более восьми типов fused GPU/ASIC kernels;
- auditable normative decoder core target: не более 15 kLOC без platform,
  container и test code.

`kLOC` и kernel count — TARGET, не измеренный результат и не замена complexity
model.

## 8. Единственный крупный открытый выбор

Basis textures всё равно нужно сильно сжимать. Использование AV2/VVC intra
сохранило бы их code complexity и нарушило бы цель проекта.

Нужен один bounded payload synthesizer вместо mode zoo. Кандидаты:

1. integer multiscale lifting transform + entropy coder;
2. fixed integer nonlinear synthesis transform с малым числом регулярных
   convolution/GEMM operations;
3. fixed dictionary/residual vector quantization.

Выбор нельзя делать по эстетике. Он должен отдельно показать:

- objective RD против AV2/VVC intra;
- deterministic cross-device output;
- small code and ASIC area;
- low memory traffic;
- отсутствие content-specific weights вне полного bitrate accounting.

Per-shot adapters MAY исследоваться, но все их bits считаются; arbitrary
transmitted graph запрещён.

### 8.1 Ведущий кандидат: cached integer basis synthesizer

Наиболее сильный путь к одновременной compression и code simplicity:

\[
B=D_{\mathrm{int}}\!\left(z;\theta_0+UV^\mathsf{T}\right)+e.
\]

Где:

- \(D_{\mathrm{int}}\) — один фиксированный bounded synthesis graph;
- \(\theta_0\) — profile-defined immutable integer weights;
- \(z\) — переданные quantized latents;
- \(UV^\mathsf{T}\) — необязательный bounded low-rank per-shot adapter;
- \(e\) — sparse exact correction для objective/lossless profile.

Критическое решение: synthesizer выполняется **только при `SET` нового Basis
Content**, а результат кэшируется как immutable \(B_k\). Presentation loop не
запускает neural renderer; он делает только texture sample, temporal MAC и
\(gY+c\).

Это даёт:

- один регулярный int8/int16 convolution/GEMM pipeline вместо сотен
  block-level tool combinations;
- deterministic CPU/GPU/ASIC output;
- adaptive content model без transmitted arbitrary graph;
- тяжёлый encoder может искать \(z,U,V\), не усложняя normative renderer;
- exact correction не позволяет learned synthesis загрязнять Truth.

Это всё ещё **HYPOTHESIS**, а не выбранная технология. Первичные результаты
показывают только практическую возможность направления:

- [integer-only variable-rate image compression](https://doi.org/10.1016/j.jvcir.2025.104634)
  сообщает 19.2% bitrate reduction против VTM-17.2 intra в условиях той работы;
- [PNVC](https://doi.org/10.1609/aaai.v39i3.32315) сообщает около 5% выигрыша
  против VTM-20.0 LD и 20+ FPS для 1080p;
- [LotteryCodec](https://proceedings.mlr.press/v267/wu25e.html) демонстрирует
  per-instance subnetwork search для image compression.

Эти цифры нельзя переносить на SceneLith, AV2 или mixed-video benchmark. Они лишь
опровергают утверждение, что deterministic/instance-adaptive synthesis
принципиально нереализуем.

Leading payload candidate отклоняется, если:

- его full bit accounting не превосходит отдельные AV2/VVC intra anchors;
- update-time energy/latency выше profile limit;
- weights/adapters занимают больше сэкономленного bitrate;
- exact correction систематически возвращает почти весь residual;
- software reference и silicon model не дают bit-exact output.

## 9. Что заморозить до реализации

Можно заморозить сейчас:

- frame не является единицей state;
- Cell — не object, а bounded spacetime basis atom;
- одна формула для static, motion, appearance и innovation;
- `RESET/SET`, implicit persistence и read-only presentation;
- immutable Truth content и запрет perceptual contamination;
- fixed-point bounded evaluation;
- exact arbitrary-video fallback;
- отдельные отчёты против AV2 и VVC.

Нельзя честно заморозить без короткого oracle:

- \(K\), tile sizes и transform sizes;
- translation против affine в обязательном профиле;
- linear lifting против integer nonlinear payload synthesizer;
- entropy contexts;
- точные memory/profile limits.

Это не архитектурные метания. Это параметры одной и той же машины. Stable
семантический spine позволяет менять их, не переписывая event/state model.

### 9.1 Правило семантического замыкания

После принятия candidate новая идея не добавляет opcode или renderer tool, если
её можно скомпилировать в существующие поля:

| Исследовательская идея | Компиляция в одну Cell |
|---|---|
| Multi-observation canonical memory | новое/уточнённое immutable \(B_k\) |
| Trajectory-aligned innovation tube | набор \(B_k\) и temporal laws \(a_k(t)\) |
| Low-rank illumination/appearance | дополнительные \(B_k,a_k(t)\) |
| Arbitrary/soft shape | Gate component \(g\) |
| Static/motion/affine placement | coordinate law \(W\) |
| Persistent residual dictionary | \(g=1\), signed \(c\) |
| Full raster escape | \(g=0\), full-output \(c\) |

Если идея не выражается через `B / W / a / g / c / SET`, она:

1. остаётся encoder-only analysis;
2. откладывается в Optional Perceptual Detail;
3. либо ждёт следующую major version.

Это правило позволяет продолжать исследования без изменения нормативной
архитектуры в процессе реализации.

## 10. Критерий принятия архитектуры

Кандидат становится implementation architecture только если все условия
выполняются одновременно:

1. бумажная модель не имеет syntax-only ceiling;
2. arbitrary input представим exact fallback без второго codec;
3. decoder остаётся bounded, integer и data-parallel;
4. AV2-specific model допускает путь к 25% только через измеримое сокращение
   innovation, а не через нечестный baseline;
5. payload engine имеет реалистичный путь к малому decoder code;
6. все сильные расширения выражаются той же Cell equation, а не новыми
   normative object types.

До фактического benchmark корректная формулировка:

> SceneLith имеет архитектурный путь к победе над AV2/VVC, но победа не доказана.
> Lifetime-only путь уже бумажно отвергнут; решающая гипотеза — warped
> low-rank spacetime innovation при одном bounded decoder kernel.
