# Риски и критерии остановки

Статус: **ACCEPTED**

## 1. Continuous-Time Cells не окупаются

Риски:

- event/support/motion/checkpoint bits съедают экономию;
- AV2 skip/merge/BRU/LTR/Atlas уже забирают почти весь доступный gain;
- MotionLaw runs слишком коротки;
- lighting/deformation делает старый Content бесполезным;
- bounded memory слишком быстро забывает сцену.

Проверка:

- отдельный reappearance/occlusion dataset;
- ablation `HOLD`, `HOLD+LINEAR`, compact Content;
- отдельно tool-complete AV2 v1.0 BRU/LTR/Atlas и VVC/H.266 baseline;
- equal-memory deduplicating decoded patch cache;
- ideal temporal RLE существующих mode maps;
- полный учёт metadata.

Kill/pivot:

- Main-0 против AV2: <10% broad screen, <5% puzzle или <2% mixed;
- Main-0 против VVC: <12% broad screen, <7% puzzle или <3% mixed;
- persistent TruthInnovation добавляет <7% screen или <5% puzzle сверх
  Main-0 после собственных state/checkpoint bits;
- отсутствие gain против decoded patch cache означает pivot к простому cache;
- practical encoder сохраняет <70% oracle net gain;
- event/support/checkpoint >20% gross saving;
- частые крупные false references.

Непереходимые cell-инварианты:

- PRESENT не меняет state;
- отсутствие event означает persistence;
- только проверенный Truth output может быть источником `CAPTURE_TRUTH`;
- MotionLaw является absolute и не warp'ит предыдущий interpolated output;
- uncorrected never-observed pixels в Truth Core: ровно 0.

Если rate gain <3%, но decoder/DRAM energy падает >25–30% на крупном screen
profile, механизм может остаться low-power profile, но не объявляется
универсальной compression revolution.

## 2. Chaotic content

Классы:

- вода;
- огонь/дым;
- плёнка и sensor grain;
- листва;
- толпа;
- rapid cuts;
- сложный sports motion.

Защита:

- objective residual fallback;
- tile-level representation routing;
- запрет принудительного scene mode;
- no-regression gates.

## 3. State drift

Причины:

- arithmetic mismatch;
- corrupted delta;
- concealment попал в reference;
- ошибочная eviction;
- потерянный asynchronous event заморозил cell;
- model version mismatch.

Защита:

- integer bit-exact path;
- state hashes;
- commit only after integrity;
- MAP/full state reset;
- repair units;
- conformance across CPU/GPU vendors.

## 4. Random access penalty

Полный cell/content checkpoint может быть дорогим.

**TARGET:**

- overhead <8%;
- RA 0.25–0.5 секунды в основном продукте;
- CfP cadence не реже anchor;
- после RAP никакой зависимости от предыдущего state.

Если checkpoint систематически уничтожает основной выигрыш, state должен быть
упрощён или разделён на independently refreshable cell groups.

## 5. Decoder слишком сложен

Риски:

- DRAM traffic важнее MAC;
- много мелких kernels;
- fragmented support и слишком много moving cells;
- entropy stalls;
- непредсказуемый peak state.

Защита:

- compute/memory/traffic как нормативные level axes;
- fixed microtiles;
- fused integer kernels;
- multi-lane entropy;
- baseline fallback graph;
- early GPU profiler и FPGA model.

## 6. Consumer encoder слишком слаб

Если Foundry находит выигрыш, который нельзя предсказывать маленьким router,
массовый продукт провалится.

Критерий:

- зрелый Studio должен сохранять 80–90% Foundry delta;
- early gap >30% требует distillation/redesign;
- устойчивый gap >20% после обучения является основанием исключить tool из
  Main profile или оставить его VOD-only.

## 7. Генеративные галлюцинации

Риски:

- изменение текста, лица или факта;
- temporal identity drift;
- пользователь не знает, что деталь синтезирована;
- generative error отравляет следующие frames.

Непереходимые правила:

- Perceptual Shell не reference;
- provenance mask обязателен;
- evidence profiles отключают shell;
- OCR/identity/geometry gates;
- Truth-only decode всегда доступен.

## 8. Training leakage и generalization

- Официальные test sequences не используются для обучения.
- Training corpus раскрывается там, где это требует CfP.
- Hidden set обрабатывается теми же binaries.
- Ручная per-sequence настройка не считается универсальным результатом.
- Все adapters входят в bitrate.

## 9. Неверные сравнения

Опасности:

- сравнить LD с RA;
- не учитывать delay;
- исключить model bits;
- сравнить reference encoder с production preset без пояснения;
- выдать VMAF/LPIPS за достоверность.

Каждый результат проходит fair-comparison checklist из
`07_METRICS_AND_ROADMAP.md`.

## 10. IP и стандартизация

Риски:

- скрытые патентные claims;
- несовместимая лицензия training/code;
- закрытые weights мешают conformance;
- не выполнены formal CfP logistics.

Защита:

- source/license inventory;
- prior-art search до freeze;
- узкие patent claims и RF/FRAND strategy;
- отдельный submission checklist;
- partner/organization для JVET.

## 11. Deadline risk CfP

Критический результат к 26 октября — не научная презентация, а:

- один decoder;
- encoder/configs;
- 150 main streams для выбранного полного test case;
- reconstructed sequences;
- metrics/MD5;
- self-contained package на физическом SSD.

При нехватке времени сокращается число экспериментальных tools, но не
conformance, reproducibility или completeness.

## 12. Visible tile seams и произвольные границы

Риск:

- storage rectangle либо dyadic support становится видимым как квадратный
  contour;
- binary mask даёт aliasing;
- bilinear taps читают padding другой поверхности;
- hair, smoke, transparency и motion blur порождают mask churn, который
  уничтожает bitrate gain;
- spatially приемлемая ошибка мерцает во времени.

Непереходимые требования:

- storage/culling Support не является visible shape;
- вне Support Cell строго identity: \(g=1,c=0\);
- видимая форма задаётся scalar Gate с fractional coverage;
- каждый sampling footprint имеет canonical apron либо objective fallback;
- lossless test воспроизводится pixel-exact;
- изменение внутренней tile partition при тех же decoded fields не меняет
  output;
- encoder может отказаться от persistent shape и использовать short-lived
  exact Truth Cell.

Adversarial shape suite:

- diagonal/subpixel lines;
- вращающийся antialiased disc;
- текст и тонкие glyph strokes;
- hair/fur;
- glass/transparency;
- smoke/shadow;
- motion-blurred silhouette;
- границы chroma subsampling;
- медленное subpixel движение, выявляющее temporal shimmer.

Kill gates:

- любой seam, коррелирующий с storage tile boundary, является correctness bug;
- lossless mismatch — немедленный stop;
- boundary-weighted distortion или temporal-edge flicker хуже отдельно
  настроенного AV2/VVC baseline — Cell mode отключается для данного region;
- forced persistent shape на chaotic boundary ожидаемо может проигрывать;
  automatic RDO fallback обязан ограничить total regression.
