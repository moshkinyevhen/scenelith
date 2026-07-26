# Research Radar

Статус: **RESEARCH**  
Назначение: отделять практически внедряемые технологии от высокорисковых
исследований и не превращать Main profile в набор несвязанных модных tools.

## 1. Main / внедрять сейчас

### Continuous-Time MOSAIC Cells

Почему:

- один lifetime убирает per-presentation `unchanged`;
- absolute MotionLaw амортизирует motion на интервал;
- compact Content устраняет обязательную frame-sized reference memory;
- Presentation Query отделён от state mutation;
- static output tiles могут не декодироваться и не переписываться;
- минимальный decoder использует fixed microtiles и integer translation.

Порядок gates: temporal RLE/HOLD → linear motion runs → compact
`CAPTURE_TRUTH` cells → incremental GPU/display compositor. Полная модель:
[14_CONTINUOUS_TIME_CELLS.md](14_CONTINUOUS_TIME_CELLS.md).

### Multi-frame chunk coding

Почему:

- убирает часть frame-by-frame autoregression;
- хорошо параллелится на GPU;
- позволяет общий temporal latent;
- совместимо с read-only temporal layers.

Сигнал практичности: DCVC-UF сообщает real-time/выше real-time результаты для
1080p и 4K и крупный выигрыш в low-delay configuration.

### Integer learned transforms

Почему:

- bit-exact cross-device;
- прямой путь к NPU/ASIC;
- управляемый compute;
- уже продемонстрирована real-time работа DCVC-RT.

### Bounded 2.5D scene memory — только после cell gates

Компоненты:

- atlas pages;
- depth/visibility;
- sparse splats/surfels;
- patch dictionary;
- deterministic lifetime/eviction/checkpoints.

Главный эксперимент: повторное появление поверхности после окклюзии или
возврата камеры.

### Lattice/finite scalar quantization

Почему:

- лучше учитывает многомерную структуру latent;
- возможна почти scalar complexity;
- нет необходимости в гигантском learned codebook search.

Исследовать FSQ, OLVQ и adaptive lattice VQ в группах 4–32 измерений.

### Parallel entropy

- 16–64 interleaved rANS lanes;
- tile/chunk offsets;
- non-autoregressive hyperprior;
- ограниченные restart points.

## 2. Main после ограниченного прототипа

### One-dimensional flexible latent memory

GVC1D показывает крупный perceptual bitrate reduction благодаря 1D tokens и
long-term memory. Для Main нужна переработка:

- bounded token count;
- отсутствие full-resolution attention;
- non-autoregressive decode;
- integer implementation;
- независимые restartable chunks.

### Sparse Gaussian/surfel mode

Использовать как региональный primitive для устойчивых поверхностей и
предсказуемого движения. Не делать единственным представлением: текущие методы
не универсальны, а encoder optimization может быть медленным.

### Multiple descriptions / erasure training

Base/state делятся на независимо декодируемые части; loss concealment никогда
не обновляет state. Исследовать NeuralMDC/GRACE-подобные принципы без тяжёлого
многошагового decoder.

## 3. Optional profile

### Per-scene adaptation

- low-rank adapter;
- ограниченный размер, предварительно 32–128 KB/epoch;
- полная стоимость входит в bitrate;
- преимущественно VOD/long-form/talking-head/UI.

Instance-adaptive работы показывают значительный потенциал, но требуют
медленного finetuning и могут плохо обобщаться между datasets.

### One-step perceptual renderer

- distilled diffusion/rectified flow;
- только display-only;
- fact/identity/OCR/flicker gates;
- synthetic provenance;
- никогда не reference.

### Screen primitives

Text/vector/sprite representation может дать существенно больший эффект на UI,
slides и games, но требует отдельного fidelity contract и exact fallback.

## 4. Высокий потенциал, не Main v1

### Relative-entropy / reverse-channel coding

Теоретически кодирует sample относительно общего prior примерно по KL-cost.
Практическое ограничение — быстро растущая вычислительная сложность.

Разрешённая область исследования:

- KL-capped microblocks;
- маленькие adapters;
- perceptual texture shell;
- independently restartable units.

### Bits-back recurrent stream

Не включать в основной temporal loop до решения:

- initial seed cost;
- serial chain;
- catastrophic state corruption;
- random access.

### Full video foundation model as codec

Использовать как encoder-only oracle, data generator или optional research
profile. Не включать multi-step DiT/world generator в нормативный Main decoder
из-за compute, model drift, nondeterminism и hallucination.

### Per-video INR

Подходит для специализированного VOD и архива. Не Main из-за:

- медленной оптимизации;
- нестабильности между sequence classes;
- необходимости передавать model/adapters;
- сложного random access.

## 5. Запрещённые короткие пути

- Считать LPIPS/DISTS выигрыш доказательством fidelity.
- Исключать weights/adapters из bitrate.
- Обучаться на официальных test sequences.
- Использовать generative output как reference.
- Добавлять произвольный загружаемый graph.
- Делать full-resolution autoregressive entropy.
- Объявлять semantic prompt реконструкцией исходного видео.

## 6. Порядок экспериментов

1. Ideal temporal RLE/HOLD control.
2. `STATIC + LINEAR_TRANSLATION` persistent runs.
3. Compact `CAPTURE_TRUTH` cells против AV2 BRU/Atlas и patch cache.
4. Incremental GPU/display compositor.
5. Chunk-native learned innovation.
6. Integerization и bit-exact conformance.
7. Lattice/FSQ.
8. Sparse splat regional mode.
9. Consumer routing/distillation.
10. Perceptual Shell.
11. REC/INR и другие optional extensions.

Такой порядок сначала проверяет центральную гипотезу, а затем добавляет
исследовательские ставки.
