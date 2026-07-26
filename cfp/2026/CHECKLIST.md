# SceneLith-CfP-2026: исполнимый checklist

Статус: **TARGET**. Ни один пункт без отметки `[x]` не считается выполненным.

Официальная основа:
[ITU-T SG21 TD 348/PLEN — JVET-AQ2021-v1](https://www.itu.int/md/T25-SG21-260706-TD-PLEN-0348/en).
Полное толкование требований хранится в
[JVET CfP 2026](../../docs/05_JVET_CFP_2026.md).

## 0. Зафиксированный scope

- [ ] **ACCEPTED:** подаём один полный `C0` unrestricted improved-compression test case.
- [ ] Не заявляем runtime-constrained `C1` `5x`, `C2` `1x`, `C3` `0.2x` без отдельного
  решения и готовых полных deliverables.
- [ ] Подтверждено: `C0` включает все 7 categories, 30 sequences и 5 rates.
- [ ] Подтверждено: требуется **150 main `.bit` files** и 150 main reconstructions.
- [ ] Назначен один ответственный за final package; только он меняет release manifest.
- [ ] Создан risk register: registration, organization, fee, compute, Ubuntu portability,
  storage/shipping, hidden set, cross-check, training/IPR.

## 1. После architecture candidate: applicant route, contacts, assets

- [ ] **D-018:** architecture implementation candidate принят; напоминание о
  registration выполнено.
- [ ] Не позднее 2026-08-20 решён internal go/no-go по applicant route.
- [ ] У chair подтверждено, допускается ли independent individual как
  proponent и что указывать в обязательном поле `organization`.
- [ ] Определён submitting applicant/organization и плательщик, способный
  подтвердить purchase order.
- [ ] Написано письмо Jens-Rainer Ohm — `ohm@ient.rwth-aachen.de`.
- [ ] Написано письмо Mathias Wien — `wien@lfb.rwth-aachen.de`.
- [ ] Запрошены VTM anchors, all test sequences и official configuration information.
- [ ] Запрошена exact SSD delivery address и packaging procedure.
- [ ] Запрошен порядок участия submitter outside JVET в заседании января 2027.
- [ ] Зарезервирован бюджет до **EUR 20 000** на один formal subjective test case.
- [ ] Зарезервированы SSD primary, SSD verified duplicate и tracked international shipping.
- [ ] Проверена возможность purchase order confirmation не позднее 2026-10-26.

## 2. Formal registration: 2026-08-01—2026-09-01

- [ ] Annex E заполнен: organization.
- [ ] Annex E заполнен: contact person и email.
- [ ] Отмечен `Test case on improved compression`.
- [ ] Runtime-constrained test cases не отмечены.
- [ ] Указано число cases для subjective evaluation: `1`.
- [ ] Подтверждены encoder/decoder executables для Ubuntu 24.04 x86-64.
- [ ] Если платформа отличается, получено письменное согласование coordinator.
- [ ] При необходимости отмечен отдельный Section 6 additional-functionality contribution.
- [ ] Registration отправлена обоим contact persons не позднее 2026-09-01.
- [ ] Получено подтверждение registration и proponent ID `Pyy`.
- [ ] 2026-09-07 получена final fee/formal offer.
- [ ] Formal offer согласована submitting organization.

## 3. Official test matrix

### SDR RA UHD/4K

- [ ] SRU1 CrowdRun: R1—R5.
- [ ] SRU2 DrivingPOV3: R1—R5.
- [ ] SRU3 FireDance: R1—R5.
- [ ] SRU4 HallwayScene: R1—R5.
- [ ] RAP interval: 32 для 25 fps; 64 для 50/60 fps.

### SDR RA HD

- [ ] SRH1 DucksTakeOff: R1—R5.
- [ ] SRH2 TravellerSwim: R1—R5.
- [ ] SRH3 Seeking: R1—R5.
- [ ] SRH4 Umbrella: R1—R5.
- [ ] RAP interval не превышает anchor.

### SDR LB HD

- [ ] SLH1 Beatriz: R1—R5.
- [ ] SLH2 GregoryCactus2: R1—R5.
- [ ] SLH3 GregoryScarf2: R1—R5.
- [ ] SLH4 OfficeWalkAtWall: R1—R5.
- [ ] Encoder и preprocessing принимают pictures только в display order.
- [ ] Picture look-ahead отсутствует.
- [ ] Structural delay не превышает anchor.
- [ ] Output picture reordering отсутствует.

### HDR-PQ RA UHD

- [ ] HPQ1 ChandelierCropBR: R1—R5.
- [ ] HPQ2 FashionLadyCrop1: R1—R5.
- [ ] HPQ3 MeridianHDR2: R1—R5.
- [ ] HPQ4 SparksWelding: R1—R5.
- [ ] HDRTools 0.26 path и PQ metrics проверены.

### HDR-HLG RA UHD

- [ ] HLG1 WaterfallForest: R1—R5.
- [ ] HLG2 WomenFootball: R1—R5.
- [ ] HLG3 AMS06: R1—R5.
- [ ] HLG4 SeaWalk: R1—R5.
- [ ] HLG reconstruction и display metadata проверены.

### Gaming LB HD/UHD

- [ ] GLH1 DOTA2s360: R1—R5.
- [ ] GLH2 GTAVs090: R1—R5.
- [ ] GLH3 Level1: R1—R5.
- [ ] GLH4 Minecraft: R1—R5.
- [ ] GLU5 Wukong2: R1—R5.
- [ ] GLU6 Carla5: R1—R5.
- [ ] LB no-lookahead и structural-delay constraints проверены.

### UGC RA

- [ ] URH1 Camellia: R1—R5.
- [ ] URH2 Hobby-w5xz-backpack: R1—R5.
- [ ] URH3 Sports-76a2-iceball: R1—R5.
- [ ] URH4 VerticalVideo-3709-snow: R1—R5.
- [ ] Portrait и landscape paths проходят один decoder binary.

### Matrix completion

- [ ] `30 sequences × 5 rates = 150` rows присутствуют в release manifest.
- [ ] Для каждого row есть `.bit`, reconstruction, aggregate CSV, per-frame CSV и MD5.
- [ ] Ни один bitstream не превышает target bitrate.
- [ ] Все sources сверены с official MD5 из CfP/assets coordinator.

## 4. Anchor and evaluation harness

- [ ] Зафиксирована точная VTM 23 revision, применённая coordinator.
- [ ] Зафиксированы JVET-AP2010 SDR configurations.
- [ ] Зафиксированы JVET-AO2011 HDR/WCG configurations.
- [ ] Default VTM anchors декодируются локально.
- [ ] Anchor metrics воспроизводятся HDRTools 0.26 с требуемой precision.
- [ ] VTM runtime measurement воспроизводится на выбранной CPU machine.
- [ ] Proposal и anchor измеряются одной методикой и на одной среде.
- [ ] Aggregate runtime: sum rate points per sequence → geometric mean sequences → anchor ratio.
- [ ] Multithread runtime считается как сумма CPU-time threads, не wall-clock.
- [ ] Все preprocessing/multipass operations включены в encoder runtime.
- [ ] Всё обязательное postprocessing включено в decoder runtime.
- [ ] Peak encoder и decoder memory собираются.
- [ ] PSNR Y/U/V и MS-SSIM Y/U/V собираются.
- [ ] wPSNR Y/U/V собираются для HDR-PQ.

## 5. SceneLith-CfP codec core

- [ ] Self-contained `.bit`: никаких внешних model/parameter files.
- [ ] Bounded deterministic WorldState.
- [ ] Full WorldState checkpoint в каждом random-access point.
- [ ] Decode после RAP не читает ни одного байта/состояния до RAP.
- [ ] Trajectory/warp syntax имеет фиксированные bounds.
- [ ] TruthInnovation всегда имеет objective fallback.
- [ ] Optional Perceptual Detail не является reference.
- [ ] Optional Perceptual Detail не меняет WorldState.
- [ ] Один decoder обслуживает SDR/HDR, portrait/landscape, RA/LB, HD/UHD.
- [ ] Все normative operations дают bit-exact output на повторном decode.
- [ ] Embedded fixed weights учтены в binary; stream-specific parameters находятся в `.bit`.
- [ ] Full bitrate включает state, checkpoints, masks, trajectories, parameters, headers и indexes.

## 6. Encoder strategy

- [ ] Foundry/offline encoder разрешён только в `C0`; отсутствие runtime cap не скрывает
  complexity reporting.
- [ ] Каждый preprocessing stage перечислен и измеряется.
- [ ] Каждый multipass stage перечислен и измеряется.
- [ ] Representation search/RDO воспроизводимы из config.
- [ ] Нет ручной настройки, не отражённой в config и technical description.
- [ ] Per-sequence optimization либо отсутствует, либо явно задокументирована.
- [ ] Rate control допускает только документированное однократное снижение RD setting.
- [ ] Full-resolution coding используется либо reduced-resolution concept описан.
- [ ] Encoder автоматически обрабатывает unknown hidden sequences.
- [ ] Для каждой encode job сохраняются command line, config hash, binary hash и logs.

## 7. Training provenance

- [ ] CfP test sequences и их части отсутствуют во всех training sets.
- [ ] Проверены duplicates/near-duplicates между training corpus и CfP material.
- [ ] Для каждой learned component указан training corpus.
- [ ] Сохранены training scripts, configs, checkpoints и dependency versions.
- [ ] Определено, какие training materials можно предоставить JVET.
- [ ] Для недоступных материалов подготовлен retraining plan на разрешённых данных.
- [ ] Model license и dataset license проверены.
- [ ] Training equations/parameter derivation готовы к раскрытию после отбора.

## 8. Ubuntu binaries

- [ ] Чистая Ubuntu 24.04 x86-64-v3 runner создана.
- [ ] Encoder запускается без network access.
- [ ] Decoder запускается без network access.
- [ ] Decoder command line поддерживает `-b input.bit -o output.yuv`.
- [ ] Один decoder binary обрабатывает все 150 streams.
- [ ] Все dynamic libraries перечислены; missing dependency test пройден.
- [ ] CPU feature detection не выходит за x86-64-v3.
- [ ] Output — 10-bit YUV 4:2:0 `.yuv` либо `.pyuv`.
- [ ] Двойной decode каждого stream даёт одинаковый MD5.
- [ ] Corrupt/truncated input завершается контролируемой ошибкой.
- [ ] README с command line и configs проверен независимым оператором.

## 9. Metrics and naming

- [ ] Filenames соответствуют `xxxx_Pyy_Rz_C0.eee`.
- [ ] `Pyy` совпадает с proponent ID coordinator.
- [ ] `.bit` содержит всю decoder information.
- [ ] Aggregate CSV использует `;` separator и required decimal precision.
- [ ] Per-frame CSV присутствует для каждого stream.
- [ ] Per-frame bit counts согласуются с complete stream size.
- [ ] Recon MD5 в CSV совпадает с фактическим `.yuv`.
- [ ] MD5 manifest покрывает все package files.
- [ ] Formal subjective material подготовлен для R1—R4.
- [ ] R5 включён в objective/runtime evaluation.

## 10. Main package freeze and SSD: official deadline 2026-10-26

- [ ] Внутренний decoder/syntax freeze: **TARGET 2026-09-15**.
- [ ] Distributed pipeline ready: **TARGET 2026-09-30**.
- [ ] Все 150 streams validated: **TARGET 2026-10-09**.
- [ ] Encoder executables и relevant configs включены.
- [ ] Один decoder executable включён.
- [ ] 150 self-contained `.bit` files включены.
- [ ] 150 packed 10-bit 4:2:0 reconstructions включены.
- [ ] Aggregate и per-frame CSV включены.
- [ ] Instructions включены.
- [ ] MD5 manifest включён и проверен после копирования на SSD.
- [ ] Purchase order confirmation получено.
- [ ] SSD проверен на независимой Ubuntu machine: **TARGET 2026-10-16**.
- [ ] Verified duplicate SSD сохранён отдельно.
- [ ] Primary SSD отправлен tracked delivery: **TARGET 2026-10-19**.
- [ ] Test coordinator подтвердил получение до **2026-10-26**.

## 11. Hidden supplemental set: 2026-11-02—2026-12-21

- [ ] Frozen binaries и configs сохранены с cryptographic hashes.
- [ ] Hidden sequences получены 2026-11-02 и зарегистрированы без помещения в training corpus.
- [ ] Запущен полностью автоматический encode pipeline.
- [ ] Каждый hidden stream попадает в 80%—100% target bitrate.
- [ ] Используются те же main encoder/decoder binaries.
- [ ] Новые внешние parameters/models не используются.
- [ ] Подготовлены hidden `.bit`, configs, reconstructions, CSV и MD5.
- [ ] Supplemental package frozen: **TARGET 2026-12-14**.
- [ ] Supplemental package получен coordinator до **2026-12-21**.
- [ ] Supplemental package передан cross-checkers 2026-12-23.

## 12. Mandatory cross-check

- [ ] Получено назначение main package другой стороны.
- [ ] Cross-check выполняется в изолированной среде.
- [ ] Проверены encoder configs, decoder output, MD5 и metrics.
- [ ] Несоответствия сообщены chair/coordinator, не публикуя identity proponent.
- [ ] Main cross-check report отправлен до 2027-01-06.
- [ ] Получено назначение supplemental package.
- [ ] Supplemental cross-check завершён до 2027-01-13.
- [ ] Наш package успешно воспроизведён назначенным cross-checker.

## 13. Technical document: official deadline 2027-01-06

- [ ] Conceptual overview объясняет все data paths.
- [ ] Bitstream и decoder architecture описаны достаточно для equivalent implementation.
- [ ] Языки, libraries, platforms и build process перечислены.
- [ ] Training material и provenance раскрыты.
- [ ] Preprocessing, postprocessing, perceptual optimization и multipass описаны.
- [ ] Random-access structure и maximum pictures-to-access описаны.
- [ ] LB structural delay, buffering и reordering описаны.
- [ ] Runtime относительно VTM измерен на одинаковой среде.
- [ ] Complexity reporting template заполнен.
- [ ] Peak memory и parallel-processing capability описаны.
- [ ] Error resilience, scalability и другие функции описаны без недоказанных claims.
- [ ] TARGET/HYPOTHESIS не представлены как measured result.
- [ ] JVET input document зарегистрирован и подан до 2027-01-06.
- [ ] Presenter зарегистрирован на заседание 2027-01-13—22.

## 14. Source and IPR readiness

- [ ] Выделен relevant source, который воспроизводит submitted output.
- [ ] Reference source не содержит secrets, credentials и запрещённых dependencies.
- [ ] Training scripts/equations подготовлены для core experiments.
- [ ] License inventory готов.
- [ ] Patent landscape review проведён.
- [ ] Common Patent Policy obligations рассмотрены counsel/authorized representative.
- [ ] Определена позиция по licensing essential claims.
- [ ] Исправления после submission не меняют результаты без согласования JVET.

## 15. Subjective test and January evaluation

- [ ] Fee оплачена/оформлена по formal offer.
- [ ] Проверены R1—R4 subjective reconstructions.
- [ ] Проверен native-resolution playback 24/25/30/50/60 fps.
- [ ] Внутренний DCR/DSIS dry run проведён.
- [ ] Внутренние MOS не выдаются за официальный JVET result.
- [ ] Получен JVET MOS/CI summary 2027-01-13.
- [ ] Objective results и runtime table сверены.
- [ ] Presentation отделяет measured facts от targets/hypotheses.
- [ ] Команда готова отвечать по complexity, training, RAP, LB delay, source и IPR.

## 16. Section 6 fallback

- [ ] Отдельно подготовлен additional-functionality document о persistent WorldState.
- [ ] Описаны scalability и compute-bounded decoding.
- [ ] Описано разделение Truth Core и non-reference Perceptual Detail.
- [ ] Описаны checkpoint, repair и error-resilience semantics.
- [ ] Материал не называется formal compression response без полного `C0`.
- [ ] Document подан к deadline 45-го JVET meeting, если основной `C0` сорван.

## 17. Final go/no-go

- [ ] **GO:** registration подтверждена.
- [ ] **GO:** fee и physical delivery обеспечены.
- [ ] **GO:** все 150 main streams валидны.
- [ ] **GO:** один frozen Ubuntu decoder воспроизводит все MD5.
- [ ] **GO:** RAP/LB constraints доказаны тестами.
- [ ] **GO:** training/IPR provenance готов.
- [ ] **GO:** hidden-set pipeline не требует code changes.
- [ ] **GO:** independent package rehearsal пройден.

Если любой обязательный GO-пункт не выполнен к internal freeze, package не объявляется
полноценной JVET CfP submission; запускается Section 6 fallback и фиксируется причина.
