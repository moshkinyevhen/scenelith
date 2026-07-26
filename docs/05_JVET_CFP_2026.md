# JVET CfP 2026: официальный контур заявки SceneLith

Статус документа: **NORMATIVE-DRAFT** для ветки `SceneLith-CfP-2026`.

Дата проверки первичного источника: **2026-07-26**.

Этот документ отделяет внешние требования JVET от целей и гипотез SceneLith:

- **FACT — JVET**: требование или факт из утверждённого Call for Proposals.
- **ACCEPTED — SceneLith**: принятое ограничение проектной ветки.
- **TARGET — SceneLith**: срок или результат, который ещё не достигнут.
- **HYPOTHESIS — SceneLith**: техническая идея, требующая измерения.

Главный первичный источник — утверждённый документ
[ITU-T SG21 TD 348/PLEN, JVET-AQ2021-v1](https://www.itu.int/md/T25-SG21-260706-TD-PLEN-0348/en)
([прямой DOCX](https://www.itu.int/dms_pub/itu-t/md/25/sg21/td/260706/PLEN/T25-SG21-260706-TD-PLEN-0348%21%21MSW-E.docx)).
Официальная [страница JVET](https://www.itu.int/en/ITU-T/studygroups/2025-2028/21/video/Pages/jvet.aspx)
подтверждает выпуск совместного CfP в июле 2026 года. Параллельная официальная запись ISO/IEC
находится на странице MPEG
[Enhanced compression beyond VVC capability](https://www.mpeg.org/standards/Explorations/41/).

## 1. Предмет CfP

**FACT — JVET.** CfP ищет поколение video compression technology, существенно превосходящее
VVC Main 10 не только по compression efficiency, но также по:

- implementability encoder и decoder;
- разнообразию контента и применений;
- latency и robustness;
- scalability и дополнительной функциональности;
- практической скорости encoding.

**FACT — JVET.** Формальная оценка proposal запланирована на 45-м заседании JVET в январе
2027 года. Первый prospective test model предполагается начать выбирать в январе 2027 года,
закончить initial selection не позднее октября 2027 года и завершить первую версию стандарта
в октябре 2029 года.

## 2. Официальный календарь

| Дата | FACT — JVET |
|---|---|
| 2026-05-31 | Доступны VTM anchors, runtime-constrained VTM encodings, дополнительные VTM encodings с RPR и конфигурации encoder. |
| 2026-07-17 | Выпущен Call for Proposals. Утверждённый TD датирован 2026-07-15. |
| 2026-08-01 | Открывается formal registration. |
| 2026-09-01 | Закрывается formal registration. |
| 2026-09-07 | Определяется итоговая testing fee; test coordinator направляет formal offer. |
| 2026-10-26 | Main submission package должен быть получен test coordinator; к этой же дате требуется подтверждение purchase order. |
| 2026-11-02 | Начинается formal subjective assessment; плановое окончание — 2026-12-21. |
| 2026-11-02 | Proponents получают дополнительный скрытый набор sequences. |
| 2026-11-30 | Main package предоставляется cross-checkers; участие proponents в cross-check обязательно. |
| 2026-12-21 | Supplemental package по дополнительному набору должен быть получен test coordinator. |
| 2026-12-23 | Supplemental package предоставляется cross-checkers; проверку требуется завершить к 2027-01-13. |
| 2027-01-06 | Дедлайн регистрации и подачи документов с техническим описанием proposal. |
| 2027-01-06 | Дедлайн отчёта о cross-check main package. |
| 2027-01-13 | Proponents и JVET получают summary subjective и objective results. |
| 2027-01-13—22 | Evaluation of proposals на заседании JVET. |

**FACT — JVET.** Критический дедлайн исполняемого кодека — не январь, а **2026-10-26**:
к этому дню нужны работающие binaries, все основные bitstreams и реконструкции.

## 3. Регистрация и участие

**FACT — JVET.** Annex E нужно отправить не позднее **2026-09-01** обоим адресатам:

- Jens-Rainer Ohm, JVET chair — `ohm@ient.rwth-aachen.de`;
- Mathias Wien, test coordinator — `wien@lfb.rwth-aachen.de`.

Форма содержит:

- organization;
- contact person и email;
- выбор unrestricted improved-compression test case;
- выбор runtime-constrained test cases;
- предполагаемые runtime targets: `0.2x`, `1x`, `5x`;
- число test cases, запрашиваемых для subjective test;
- подтверждение encoder/decoder executables для Ubuntu 24.04 x86-64 либо запрос другой
  платформы у coordinator;
- отметку о proposal дополнительной функциональности по Section 6;
- remarks.

**FACT — JVET.** CfP приглашает companies и organizations. Предварительное членство в JVET
не объявлено условием регистрации. Chair прямо обещает помощь submitters outside JVET с
участием в январском заседании.

**FACT — ITU.** Для постоянного участия и подачи вкладов через ITU-T доступны Sector Member,
Associate выбранной Study Group и Academia. Актуальные права участия описаны на
[официальной странице ITU](https://www.itu.int/hub/membership/become-a-member/participation/),
а сборы — на странице
[ITU-T Categories and Fees](https://www.itu.int/en/ITU-T/membership/Pages/Categories-and-Fees.aspx).

**ACCEPTED — SceneLith, D-018.** Внешнюю регистрацию отложить до выбора
architecture implementation candidate. План владельца — регистрация как
независимого частного заявителя; юридическое имя не хранить в публичном
техническом repository до необходимости оформления.

**OPEN / UNVERIFIED.** Это намерение ещё не означает допустимость: CfP
приглашает companies/organizations, а Annex E требует поле `organization`.
Сразу после принятия architecture candidate, и достаточно заранее до
2026-09-01, письменно запросить у chair/test coordinator:

1. допускается ли independent individual как proponent;
2. что писать в `organization`, если юридического лица нет;
3. proponent ID;
4. test sequences, anchors и configuration information;
5. точную delivery logistics;
6. порядок participation submitter outside JVET в январе 2027 года.

**TARGET:** внутренний go/no-go по registration route — не позднее
2026-08-20, чтобы возможный ответ chair не оказался на critical path к
2026-09-01.

## 4. Test cases

### 4.1 Обязательная полнота

**FACT — JVET.** Определены четыре test cases:

1. unrestricted improved compression;
2. improved compression при encoder runtime около `5x` default VTM;
3. improved compression при encoder runtime около `1x` default VTM;
4. improved compression при encoder runtime около `0.2x` default VTM.

Участвовать во всех четырёх не обязательно. Однако для каждого выбранного test case требуется
полный результат по **всем семи категориям**. Incomplete proposal может не рассматриваться.

**FACT — JVET.** Один полный test case содержит:

- 30 test sequences;
- 5 rate points на sequence;
- **150 main bitstreams**;
- соответствующие 150 reconstructed sequences;
- aggregate и per-frame результаты;
- скрытый supplemental set объёмом не более 50% основного содержимого.

### 4.2 Полный основной набор

Все bitrates ниже приведены в kbit/s и перечислены как `R1 / R2 / R3 / R4 / R5`.

#### SDR RA UHD/4K

Формат категории: 3840×2160, YCbCr 4:2:0 BT.709, 10 bit, random access.

| SID | Sequence | Frames @ fps | Target bitrates |
|---|---|---:|---:|
| SRU1 | CrowdRun | 500 @ 50 | 700 / 1500 / 3200 / 7000 / 14000 |
| SRU2 | DrivingPOV3 | 600 @ 60 | 300 / 600 / 1200 / 2400 / 4800 |
| SRU3 | FireDance | 250 @ 25 | 400 / 800 / 1500 / 2500 / 5000 |
| SRU4 | HallwayScene | 250 @ 25 | 150 / 250 / 500 / 1000 / 2000 |

#### SDR RA HD

Формат категории: 1920×1080, YCbCr 4:2:0 BT.709, random access.

| SID | Sequence | Bit depth | Frames @ fps | Target bitrates |
|---|---|---:|---:|---:|
| SRH1 | DucksTakeOff | 8 | 500 @ 50 | 300 / 900 / 2400 / 4000 / 8000 |
| SRH2 | TravellerSwim | 10 | 500 @ 50 | 150 / 300 / 600 / 1200 / 2400 |
| SRH3 | Seeking | 8 | 500 @ 50 | 200 / 400 / 800 / 1600 / 3200 |
| SRH4 | Umbrella | 8 | 500 @ 50 | 300 / 600 / 1400 / 3500 / 7000 |

#### SDR LB HD

Формат категории: landscape 1920×1080 либо portrait 1080×1920, YCbCr 4:2:0 BT.709,
low-delay B-picture configuration.

| SID | Sequence | Orientation / bit depth | Frames @ fps | Target bitrates |
|---|---|---:|---:|---:|
| SLH1 | Beatriz | L / 8 | 500 @ 50 | 70 / 140 / 280 / 550 / 1100 |
| SLH2 | GregoryCactus2 | P / 10 | 300 @ 30 | 200 / 600 / 1500 / 4000 / 8000 |
| SLH3 | GregoryScarf2 | P / 10 | 300 @ 30 | 200 / 600 / 1800 / 5000 / 10000 |
| SLH4 | OfficeWalkAtWall | L / 8 | 300 @ 30 | 90 / 200 / 450 / 1000 / 2000 |

#### HDR-PQ RA UHD

Формат категории: YCbCr 4:2:0, 10 bit, BT.2100 PQ, random access. UHD/4K/8K sources
cropped до 3840×2160 для оценки.

| SID | Sequence | Transfer | Frames @ fps | Target bitrates |
|---|---|---|---:|---:|
| HPQ1 | ChandelierCropBR | HDR10 PQ | 360 @ 60 | 300 / 650 / 1300 / 2800 / 5600 |
| HPQ2 | FashionLadyCrop1 | HDR10 PQ | 380 @ 60 | 250 / 650 / 1700 / 4500 / 9000 |
| HPQ3 | MeridianHDR2 | P3 PQ 4000 nits | 600 @ 60 | 150 / 300 / 600 / 1200 / 2400 |
| HPQ4 | SparksWelding | HDR10 PQ 1000 nits | 600 @ 60 | 400 / 1000 / 2500 / 6000 / 12000 |

#### HDR-HLG RA UHD

Формат категории: YCbCr 4:2:0, 10 bit, BT.2100 HLG, random access. UHD/4K/8K sources
cropped до 3840×2160 для оценки.

| SID | Sequence | Frames @ fps | Target bitrates |
|---|---|---:|---:|
| HLG1 | WaterfallForest | 500 @ 50 | 1000 / 2500 / 6000 / 14000 / 28000 |
| HLG2 | WomenFootball | 500 @ 50 | 300 / 600 / 1100 / 2000 / 4000 |
| HLG3 | AMS06 | 600 @ 60 | 600 / 1300 / 3500 / 8000 / 16000 |
| HLG4 | SeaWalk | 500 @ 50 | 200 / 400 / 800 / 1800 / 3600 |

#### Gaming LB HD/UHD

Формат категории: YCbCr 4:2:0 BT.709, low-delay B-picture configuration.

| SID | Sequence | Raster / bit depth | Frames @ fps | Target bitrates |
|---|---|---:|---:|---:|
| GLH1 | DOTA2s360 | 1920×1080 / 8 | 550 @ 60 | 180 / 300 / 550 / 1000 / 2000 |
| GLH2 | GTAVs090 | 1920×1080 / 8 | 600 @ 60 | 400 / 900 / 2000 / 3600 / 7200 |
| GLH3 | Level1 | 1920×1080 / 10 | 600 @ 60 | 400 / 1000 / 2000 / 4000 / 8000 |
| GLH4 | Minecraft | 1920×1080 / 8 | 600 @ 60 | 300 / 600 / 1200 / 2400 / 4800 |
| GLU5 | Wukong2 | 3840×2160 / 10 | 600 @ 60 | 1000 / 2400 / 6000 / 14000 / 28000 |
| GLU6 | Carla5 | 3840×2160 / 8 | 600 @ 60 | 1100 / 2200 / 4300 / 8500 / 17000 |

#### UGC RA

Формат категории: landscape 1920×1080 либо portrait 1080×1920, YCbCr 4:2:0 BT.709,
8 bit, random access.

| SID | Sequence | Orientation | Frames @ fps | Target bitrates |
|---|---|---:|---:|---:|
| URH1 | Camellia | P | 600 @ 60 | 200 / 400 / 800 / 1600 / 3200 |
| URH2 | Hobby-w5xz-backpack | P | 240 @ 24 | 90 / 160 / 280 / 500 / 1000 |
| URH3 | Sports-76a2-iceball | L | 600 @ 60 | 80 / 160 / 250 / 400 / 800 |
| URH4 | VerticalVideo-3709-snow | P | 300 @ 30 | 80 / 160 / 300 / 500 / 1000 |

MD5 исходных sequences являются частью официальных таблиц CfP и должны сверяться
непосредственно с TD 348 и материалами, полученными от coordinator.

## 5. Anchors и coding configurations

**FACT — JVET.**

- Anchor описывается VVC Test Model 23 и документом JVET-AO2002.
- SDR common test conditions и software reference configurations заданы JVET-AP2010.
- HDR/WCG conditions заданы JVET-AO2011.
- Default VTM является базой для relative compression performance и runtime.
- Для runtime curve предоставлены high-performance VTM configuration примерно `2x` default
  и три reduced-time variants примерно `0.2x`—`0.75x` default.
- Дополнительно доступны VTM encodings с reference picture resampling.
- Официальный reference implementation находится в
  [VVCSoftware_VTM](https://vcgit.hhi.fraunhofer.de/jvet/VVCSoftware_VTM).

**FACT — JVET.** Для random-access categories:

- intra refresh period anchor равен 32 для 24/25/30 fps;
- intra refresh period anchor равен 64 для 50/60 fps;
- proposal обязан предоставлять random access не реже;
- после random-access point decoder обязан восстановить поток после удаления **всей**
  информации, предшествующей этому point.

**ACCEPTED — SceneLith.** Каждый CfP random-access point содержит самодостаточный
WorldState checkpoint. Никакое состояние до RAP не требуется. Optional Perceptual Detail
не участвует в checkpoint, prediction или изменении WorldState.

**FACT — JVET.** Для low-delay categories:

- output picture reordering не применяется;
- overall structural delay proposal не превышает anchor;
- encoder и preprocessing обрабатывают pictures в display order;
- picture look-ahead запрещён.

## 6. Общие правила encoding

**FACT — JVET.**

1. Bitstream не должен превышать target bitrate.
2. Все rate points кодируются в полном input resolution. Если reduced-resolution coding является
   частью алгоритма, его нужно описать.
3. Quantization/RD settings должны оставаться статическими. Разрешено одно небольшое изменение
   только в сторону меньшего bitrate для оставшейся части stream; его нужно документировать.
4. Ручная и per-sequence оптимизация discouraged и должна быть раскрыта.
5. Ни одна часть test sequences не может использоваться для обучения entropy tables, VQ
   codebooks, transforms, predictors, filters, neural models и иных частей codec.
6. Training material для обученных частей алгоритма обязательно раскрывается.
7. Preprocessing, postprocessing, perceptual optimization и multi-pass encoding, а также их
   влияние на compression performance, должны быть описаны.
8. Время preprocessing включается в encoder runtime; требуемое postprocessing включается в
   decoder runtime.
9. Если proposal использует особую оптимизацию, рекомендуется представить anchor с
   эквивалентной оптимизацией.

### Runtime measurement

**FACT — JVET.**

- При multithreading runtime равен сумме времени всех threads, а не wall-clock time.
- При segment-wise parallelism рекомендуется суммировать runtime segments.
- Anchor и proposal измеряются одной методикой.
- Для sequence сначала суммируется время всех rate points; затем берётся geometric mean по
  sequences; затем считается ratio к anchor.
- У runtime-constrained cases цели равны `5x`, `1x`, `0.2x` aggregate default VTM runtime.
- Точного совпадения не требуется, но точки должны покрывать сопоставимую runtime/compression
  curve.
- Decoder runtime target отсутствует, однако runtime и implementation complexity обязательно
  сообщаются и учитываются.

**FACT — JVET.** Unrestricted improved-compression case не вводит жёсткого лимита encoder
runtime. Это разрешает очень тяжёлый offline encoder, но не исключает runtime из оценки:
полное время и degree of optimization требуется раскрыть.

## 7. Main submission package — 2026-10-26

**FACT — JVET.** Материалы доставляются на SSD по адресу test coordinator. Получение должно
состояться не позднее дедлайна; риск доставки и отказа носителя несёт proponent.

Обязательны:

1. bitstreams для всех sequences, rate points и выбранных test cases;
2. encoder binaries и соответствующие configuration settings;
3. один decoder executable для всех выбранных test cases;
4. инструкция по command line и configuration parameters;
5. reconstructed 10-bit YUV 4:2:0 sequences;
6. Annex D CSV с aggregate objective metrics;
7. отдельный per-frame CSV для каждой комбинации sequence/rate;
8. MD5 checksums всех файлов, предпочтительно в одном manifest;
9. подтверждённый purchase order на subjective testing.

**FACT — JVET.**

- Executables следует собирать для **Ubuntu 24.04, x86-64-v3**. Для иной платформы нужно
  заранее согласовать порядок с coordinator.
- Один decoder должен принимать bitstream и output path, например
  `decoder -b input.bit -o output.yuv`.
- Decoder выдаёт 10-bit 4:2:0 `.yuv` либо `.pyuv`.
- Proposal bitstream имеет расширение `.bit`.
- Bitstream может быть proprietary, но обязан содержать всю информацию для decoding.
  Внешние parameter/model files не допускаются.

Именование:

```text
xxxx_Pyy_Rz_Cw.eee
```

где `xxxx` — SID, `yy` — proponent ID, `z` — rate 1…5, `w` — test case:

- `C0`: unrestricted improved compression;
- `C1`: runtime `5x`;
- `C2`: runtime `1x`;
- `C3`: runtime `0.2x`.

`P00` зарезервирован для VVC anchor. Расширения: `bit`, `pyuv`, `csv`.

## 8. Hidden supplemental set

**FACT — JVET.**

- Additional sequences выдаются **2026-11-02**, после main binaries и bitstreams.
- Объём материала ожидается не более 50% основного test content.
- Разрешения, content types, structural delay и bitrate ranges будут аналогичны main set.
- Supplemental bitstreams должны попадать в диапазон 80%—100% заданного target bitrate.
- Те же binaries, отправленные в main package, должны кодировать и декодировать hidden set.
- До **2026-12-21** отправляются bitstreams, configs, reconstructions, CSV и MD5.
- Новые encoder/decoder executables не входят в список supplemental package.

**ACCEPTED — SceneLith.** Decoder и bitstream semantics для CfP замораживаются до main
submission. Нельзя полагаться на hard-coded test sequence knowledge или ручное
per-sequence обучение. Hidden-set generalization является release gate.

## 9. Cross-check

**FACT — JVET.**

- Cross-checking проверяет binaries, configs, воспроизводимость reconstruction и корректность
  metrics.
- Packages распределяются между другими сторонами без раскрытия proposing party.
- Участие каждого proponent в проверке чужого package обязательно.
- Main package передаётся cross-checkers 2026-11-30.
- Main cross-check report требуется 2027-01-06.
- Supplemental cross-check должен завершиться к 2027-01-13.

## 10. Technical proposal document — 2027-01-06

**FACT — JVET.** Документ должен позволять экспертам концептуально понять proposal,
воспроизвести эквивалентную performance и оценить степень optimization. Обязательны:

- все data-processing paths и компоненты, формирующие bitstream;
- implementation languages, external libraries и supported build platforms;
- random-access behaviour и maximum pictures-to-access;
- encoding/decoding delay, reordering, buffering, multipass decisions и parallelization;
- encoder/decoder runtime относительно VTM на одинаковой среде;
- заполненный complexity reporting template;
- степень parallel processing;
- дополнительная функциональность: resilience, scalability, 4:4:4 и прочее.

## 11. Source code, training и IPR

**FACT — JVET.** Main submission принимает binaries, но если technology выбрана для
дальнейшего исследования:

- relevant source code становится условием участия в core experiments и возможного включения
  в reference software;
- source должен воспроизводить результаты proposal;
- relevant technology может включать training scripts или equations получения parameters;
- ожидается доступность training materials для проверки либо retraining на доступном JVET
  материале;
- действует
  [Common Patent Policy for ITU-T/ITU-R/ISO/IEC](https://www.itu.int/ITU-T/dbase/patent/patent-policy.html).

## 12. Formal subjective assessment

**FACT — JVET.**

- Formal subjective testing проводится только для R1—R4 main package.
- R5 используется для objective metrics и runtime.
- Все sequences и rates, включая hidden set, проходят objective evaluation.
- При большом числе proposals chair и coordinator могут выбрать representative subset для
  subjective testing.
- Метод — DCR/DSIS: uncompressed reference, затем processed sequence.
- Планируется 11-level impairment scale от `0` — severely annoying до `10` — imperceptible.
- Native resolution обязателен; viewing distance — `1.5H`.
- Публикуются MOS и confidence interval отдельно для каждой sequence; разные sequences не
  объединяются в один graph.

Методика ссылается на
[ITU-R BT.500](https://www.itu.int/rec/R-REC-BT.500) и
[ITU-T P.910](https://www.itu.int/rec/T-REC-P.910).

## 13. Testing fee

**FACT — JVET.**

- Fee покрывает formal subjective assessment.
- Ожидаемый максимум — **EUR 20 000 за каждый test case**, включённый в subjective test.
- Partial test case считается полным при определении fee.
- Proponent указывает, сколько submitted cases он хочет включить в subjective assessment.
- Финальный набор решается на 44-м заседании JVET для максимальной comparability.
- Итоговая сумма сообщается 2026-09-07; подтверждение purchase order требуется к 2026-10-26.

## 14. Узкая стратегия SceneLith-CfP-2026

### 14.1 Scope

**ACCEPTED — SceneLith.** Для текущего CfP готовится один полный `C0` unrestricted
improved-compression test case. Runtime-constrained `C1`—`C3` не входят в initial response.
Это уменьшает deliverables с потенциальных 600 до 150 main bitstreams, не ослабляя
формальную полноту выбранного case.

**ACCEPTED — SceneLith.** CfP-ветка не пытается реализовать весь будущий MOSAIC. Она обязана
сохранить каноническую модель:

\[
Video(t)=Render(WorldState_t,\ Trajectories_t)
       +TruthInnovation_t
       +OptionalPerceptualDetail_t
\]

но ограничивается минимальным проверяемым набором:

1. bounded deterministic WorldState;
2. самодостаточный checkpoint на каждом RAP;
3. bounded `MOSAIC Cell` с Support, Lifetime и
   `STATIC/LINEAR_TRANSLATION` MotionLaw;
4. objective TruthInnovation residual;
5. self-contained bitstream;
6. один reproducible decoder;
7. Optional Perceptual Detail только если он не угрожает objective reconstruction,
   сроку и hidden-set generalization.

### 14.2 Fastest implementation path

**HYPOTHESIS — SceneLith.** Наиболее быстрый путь к полной заявке — использовать
проверенный VTM-compatible residual backend как transport/fallback и добавить
малый SceneLith subset: asynchronous `CELL_SET`, persistent linear motion runs,
compact `CAPTURE_TRUTH` content и read-only `PRESENT`. Это измеряет эффект
frame-free state без одновременного изобретения каждого слоя codec.

**HYPOTHESIS — SceneLith.** Foundry encoder может получить дополнительный
выигрыш через многопроходный анализ всей RA epoch, flow, support/lifetime
search, compact-content reuse и RDO. Depth/3D/semantic decoder не входят в
fastest path.

**TARGET — SceneLith.** Любой gain должен считаться по полному bitstream, включая:

- WorldState checkpoint;
- Cell Content/Support/Lifetime events;
- MotionLaw knots и presentation metadata;
- embedded parameters/weights;
- TruthInnovation;
- headers, indexes и checksums.

### 14.3 CfP release gates

**TARGET — SceneLith.**

1. Все 150 main bitstreams декодируются одним Ubuntu binary.
2. Повторный decode даёт byte-identical output и MD5.
3. Каждый RA stream стартует без данных до RAP.
4. Low-delay categories не используют look-ahead.
5. Каждый bitstream укладывается в target; hidden streams — в 80%—100%.
6. Training provenance полностью документирован; CfP material не входит в training.
7. Full runtime включает preprocessing, multipass и postprocessing.
8. Package воспроизводится независимым cross-check runner.
9. Hidden set проходит теми же frozen binaries.
10. Offline encoder complexity раскрывается честно и не маскируется wall-clock parallelism.

## 15. Project buffer dates

Это внутренние цели, а не даты JVET.

| TARGET — SceneLith | Результат |
|---|---|
| 2026-08-01 | Отправлена formal registration; получены/запрошены proponent ID и assets. |
| 2026-08-07 | Anchor pipeline и Annex D metrics воспроизводятся локально. |
| 2026-08-21 | Первый self-contained `.bit` round trip на Ubuntu 24.04. |
| 2026-09-01 | Registration подтверждена; выбран ровно один `C0` case. |
| 2026-09-15 | Заморожены decoder ISA, syntax и WorldState checkpoint semantics. |
| 2026-09-30 | Работает полный 30-sequence distributed encoding pipeline. |
| 2026-10-09 | Все 150 candidate streams прошли decode/MD5/rate validation. |
| 2026-10-16 | Main package frozen, SSD собран и проверен на независимой Ubuntu machine. |
| 2026-10-19 | SSD отправлен с отслеживаемой доставкой; сохранена verified duplicate. |
| 2026-10-26 | Официальный main deadline без использования внутреннего буфера. |
| 2026-11-02 | Hidden-set encoding запускается автоматически frozen toolchain. |
| 2026-12-14 | Supplemental package frozen за неделю до официального срока. |

## 16. Section 6 fallback, не равный formal proposal

**FACT — JVET.** Дополнительную функциональность можно представить отдельным вкладом к
document deadline 45-го заседания. Такой материал:

- не входит в main submission package;
- не участвует в formal subjective test;
- не требует обязательного pre-meeting cross-check;
- может получить expert viewing или informal demonstration.

**TARGET — SceneLith.** Даже при срыве полного `C0` подготовить Section 6 contribution о:

- persistent scene state;
- compute/scalability dimensions;
- truth-preserving base и non-reference perceptual detail;
- state checkpointing и error recovery.

Это страховка присутствия SceneLith в обсуждении, но **не** замена полноценному formal
compression response.
