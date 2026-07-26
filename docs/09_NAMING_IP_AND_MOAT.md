# Naming, IP и конкурентный отрыв

Статус: названия — **ACCEPTED**, IP-модель — **NORMATIVE-DRAFT**.

## 1. Принятый naming

- Standalone video codec и bitstream family: **SceneLith**.
- Проект и открытая video-codec экосистема: **SceneLith**.
- Внутренняя архитектура: **MOSAIC**.
- Расшифровка:
  **Memory-Oriented Scalable Asymmetric Integer Codec**.
- Маркетинговая формулировка:
  **“SceneLith Video — powered by MOSAIC.”**

Смысл SceneLith: сцена, «высеченная» в компактном потоке и пригодная для
реализации в кремнии.

## 2. Исторические кандидаты

- KineStrand;
- TemporalStrand;
- VISTRAL;
- QINTRA;
- MOSAIC как публичный бренд.

Они не являются текущим названием, но сохраняются для истории и возможных
подсистем.

## 2.1 Отказ от QINTRA и принятие SceneLith Video — 2026-07-26

Статус роли codec/bitstream family: **ACCEPTED** решением D-032.  
Статус trademark/FTO SceneLith: **OPEN / UNVERIFIED**.

QINTRA коротко и ударно звучит как имя кодека, но владелец проекта отказался
от него до публичного запуска. Причина — визуальная и фонетическая коллизия с
существующей компанией в Германии и другими Quintra/Qintra technology names.
Решения D-011 и D-016 в части принятия QINTRA имеют статус **SUPERSEDED**.

SceneLith лучше отражает основной объект стандарта: долговечное состояние
визуальной сцены, «высеченное» в компактном bitstream и пригодное для
реализации в кремнии. Одно имя используется для video codec, bitstream family
и открытого проекта вокруг него.

### Принятое распределение ролей

- **SceneLith Video** — standalone video codec и bitstream family;
- **Resonith Audio** — standalone audio codec;
- **MOSAIC** — внутренняя архитектура SceneLith Video;
- **SceneLith AV Bridge** — отдельная binding specification.

> SceneLith — video codec  
> Resonith — audio codec  
> MOSAIC — внутренняя video-архитектура

Имя QINTRA сохраняется только в исторических материалах и superseded-записях.
Продуктовое решение не заменяет профессиональную проверку SceneLith и
Resonith перед регистрацией и публичным запуском.

## 3. Неутверждённые идентификаторы

Пока не выбирать без проверки:

- FourCC;
- расширение файла;
- MIME type;
- codec string;
- product logo;
- юридическое имя компании.

Перед публичным запуском нужны:

- WIPO Global Brand Database;
- EUIPO;
- USPTO;
- национальные реестры;
- IANA/MIME;
- MP4RA/FourCC и container registries;
- поиск конфликтующих software/package names и доменов.

Предварительный web search не является юридической trademark clearance.

## 4. Стандарто-дружественная IP-модель

Цель — не закрывать conforming decoder.

Возможная модель:

- открытая спецификация и conformance vectors;
- доступный baseline decoder;
- royalty-free либо заранее понятная FRAND-лицензия normative claims;
- патентование узких действительно новых механизмов;
- отдельная лицензия/секретность ненормативного Foundry encoder;
- юридически чистые training datasets и dependencies.

Требуется отдельный профессиональный patent/FTO review до публичного freeze.

## 5. Что можно защищать

Кандидаты для prior-art/patent analysis:

- motion-lifetime MOSAIC Cell, единым contract амортизирующая Content,
  Support, MotionLaw и state lifetime;
- независимые State/Motion/Innovation/Presentation clocks при objective
  natural-video fallback;
- direct cell-to-display incremental execution contract;
- bounded persistent visual state с нормативными checkpoint/update rules;
- dual-contract rule, запрещающий generative detail входить в reference;
- temporal spine/read-only chunk state mutation;
- compute-scalable syntax и bounded tensor/render ISA;
- teacher–student transfer RDO traces между Foundry и consumer encoder;
- loss repair, не допускающий concealment в state;
- combination atlas/trajectory/innovation under one state contract.

Наличие идеи в этом списке не означает её патентоспособность.

## 6. Реальный moat

Открытый decoder можно реализовать конкуренту. Практический отрыв создают:

1. Foundry world extractor.
2. Representation router.
3. Exact multi-objective RDO.
4. Накопленные traces оптимальных решений.
5. Distillation в consumer encoder.
6. Subjective/OCR/identity/flicker datasets.
7. Per-title adaptation.
8. CUDA/Vulkan/ASIC kernels.
9. Test farm, fuzzing и conformance corpus.
10. Streaming/browser/chip partnerships.

Целевой эффект:

> Любой может декодировать SceneLith; долгое время никто не кодирует SceneLith
> так же эффективно.

## 7. Что разрушит adoption

- обязательный секретный decoder model;
- непредсказуемые royalties;
- arbitrary code execution из bitstream;
- device-dependent output;
- отсутствие baseline fallback;
- чрезмерная state/compute стоимость;
- выдача генеративных деталей за исходную истину.
