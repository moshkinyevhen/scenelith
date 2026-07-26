# Журнал решений SceneLith

Последнее обновление: 2026-07-26

## D-001 — Название и архитектура

- Дата: 2026-07-26
- Статус: **ACCEPTED**
- Решение:
  - проект называется **SceneLith**;
  - архитектура называется
    **MOSAIC — Memory-Oriented Scalable Asymmetric Integer Codec**.

## D-002 — Главная формула

- Дата: 2026-07-26
- Статус: **ACCEPTED**
- Решение:

\[
Video(t)=Render(WorldState_t,\ Trajectories_t)
       +TruthInnovation_t
       +OptionalPerceptualDetail_t
\]

## D-003 — Корень проекта

- Дата: 2026-07-26
- Статус: **ACCEPTED**
- Решение: все материалы и код проекта хранятся в `G:\SceneLith`.

## D-004 — Reference safety

- Дата: 2026-07-26
- Статус: **ACCEPTED**
- Решение: только детерминированный Fidelity/Truth Core может менять
  `WorldState` и использоваться как temporal reference. Perceptual Shell
  всегда нереференсный и отключаемый.

## D-005 — Новый объект стандартизации

- Дата: 2026-07-26
- Статус: **ACCEPTED**
- Решение: SceneLith стандартизует ограниченную visual scene machine и поток
  innovation, а не является очередным расширением блочного hybrid codec.

## D-006 — Deadline текущего JVET CfP

- Дата: 2026-07-26
- Статус: **ACCEPTED**, заменяет прежнюю оценку
- Решение: подготовить полный формальный unrestricted improved-compression
  response к 26 октября 2026 года.
- Supersedes: утверждение из первоначального текста, что подача полного
  proposal в это окно «нереальна». Теперь это классифицируется как
  экстремально рискованная, но формально выполнимая deadline-миссия.

## D-007 — Отдельная CfP-ветка

- Дата: 2026-07-26
- Статус: **ACCEPTED**
- Решение: создать `SceneLith-CfP-2026` с узким детерминированным ядром:
  bounded state, trajectories, multi-frame innovation, обязательные RAP
  checkpoints и надёжный residual fallback. Не блокировать ветку попыткой
  одновременно реализовать весь будущий MOSAIC.

## D-008 — Три класса encoder

- Дата: 2026-07-26
- Статус: **ACCEPTED**
- Решение: один decoder/bitstream обслуживает:
  - `Live` — causal real-time;
  - `Studio` — бытовой GPU с lookahead и ограниченным multipass;
  - `Foundry` — распределённый hyperscale/offline scene compiler.

## D-009 — Foundry как teacher

- Дата: 2026-07-26
- Статус: **ACCEPTED**
- Решение: RDO traces Foundry используются для distillation маленького
  consumer-router. Бытовой encoder должен извлекать не менее 80–90% общей
  дельты Foundry после созревания.

## D-010 — Документация является канонической

- Дата: 2026-07-26
- Статус: **ACCEPTED**
- Решение: все новые стандарты и идеи из чата записываются в файлы проекта.
  Исторические исходники сохраняются в `archive/`; изменения отражаются через
  этот журнал, а не через молчаливое переписывание истории.

## D-011 — Повторная оценка QINTRA

- Дата: 2026-07-26
- Статус: **SUPERSEDED** решением D-016
- Вопрос: не использовать ли QINTRA вместо SceneLith из-за более короткого и
  запоминающегося звучания.
- Предварительный вывод:
  - QINTRA действительно ударнее как имя кодека;
  - SceneLith лучше передаёт центральную идею и предварительно уникальнее;
  - QINTRA фонетически конфликтует с существующим technology/software именем
    Quintra и требует профессиональной trademark-проверки.
- Исторический вывод D-011: SceneLith оставался именем проекта, а роль QINTRA
  ещё не была принята. Этот вывод заменён D-016.

## D-012 — Рекомендуемый режим Codex Sol

- Дата: 2026-07-26
- Статус: **SUPERSEDED** решением D-013
- Рекомендация:
  - для корневой задачи SceneLith использовать Sol Ultra;
  - для единственного режима без делегации использовать Sol XHigh;
  - Max резервировать для freeze и hardest single-problem reviews;
  - High/XHigh использовать для основной реализации;
  - Medium/Low использовать для механически проверяемых массовых задач.
- Причина: максимальный project throughput требует сочетать глубокое reasoning
  на необратимых решениях с быстрыми итерациями реализации и тестов.

## D-013 — Фактические уровни усилия 5.6 Sol

- Дата: 2026-07-26
- Статус: **ACCEPTED**
- Исправление: D-012 использовал внутренние английские обозначения и ошибочно
  включал `Max`, которого нет в текущем интерфейсе пользователя.
- Решение: рабочая шкала SceneLith должна дословно соответствовать model picker:
  - **Лёгкий**;
  - **Средний**;
  - **Высокий**;
  - **Очень высокий**;
  - **Ультра**.
- Для текущего проектирования канонического стандарта используется
  **«Ультра»**. Для одиночного brainstorming без фиксации решения достаточно
  **«Очень высокого»**.
- Распределение:
  - Ультра — архитектура стандарта, bitstream/state freeze, интеграция и
    параллельный adversarial review;
  - Очень высокий — один сложный алгоритм, RDO или bit-exact debugging;
  - Высокий — реализация по уже определённой спецификации;
  - Средний — документация и воспроизводимые тесты;
  - Лёгкий — тривиальные механические изменения.

## D-014 — Observed Surface Memory вместо полного дорисованного мира

- Дата: 2026-07-26
- Статус: **SUPERSEDED** решением D-015 для первого experiment gate и
  решением D-017 как кандидатом основной архитектуры
- Решение-кандидат:
  - Main Truth Core хранит только минимально достаточные наблюдавшиеся surface
    fragments;
  - неизвестный texel является явным состоянием и не может использоваться как
    predictor;
  - никогда не выводимая область не передаётся и не генерируется;
  - `CAPTURE_PROMOTE` сохраняет уже восстановленные Truth pixels в persistent
    state без повторного texture payload;
  - неизвестное, впервые появившееся в output, восстанавливается objective
    `REPLACE/TruthInnovation`, после чего может быть сохранено для reuse;
  - Full 3D и generation не являются обязательными Main v0 paths;
  - Foundry/router остаётся ненормативным механизмом поиска выгодных fragment,
    lifecycle и representation решений.
- Влияние на сроки:
  - executable skeleton — дни;
  - oracle real-shot proof — 2–3 недели оптимистично, 4–6 реалистично;
  - первая вертикальная версия — 4–6 недель оптимистично, 8–12 реалистично;
  - GPU/MAP/basic conformance — 6–9 недель оптимистично, 10–16 реалистично.
- Compression hypothesis против equal-memory strong baseline:
  - 20–45% net saving на rigid/screen long-gap reuse;
  - 10–25% на puzzle-friendly natural;
  - 4–12% на mixed natural;
  - около 0% на hostile dynamic благодаря fallback.
- Все численные диапазоны являются **HYPOTHESIS/TARGET**, а не результатами.
- Полная проработка: `12_OBSERVED_SURFACE_MEMORY.md`.

## D-015 — Minimal Decoded Patch Memory как контрольный baseline

- Дата: 2026-07-26
- Статус: **ACCEPTED**
- Решение:
  - первым тестом reference-memory остаётся минимальный `DPM` с
    `RESET/PROMOTE/PLACE/DROP`, rectangles и integer copy;
  - DPM не объявляется основной архитектурой QINTRA до измеренного выигрыша;
  - masks, depth, 3D, semantics и learned decoder не добавляются для спасения
    отрицательного результата;
  - DPM после D-017 является контрольным spatial-memory baseline и возможным
    способом хранения content для более общего time-state core.
- Полная проработка: `13_MINIMAL_PATCH_CORE.md`.

## D-016 — Иерархия SceneLith / QINTRA / MOSAIC

- Дата: 2026-07-26
- Статус: **ACCEPTED**
- Решение:
  - **SceneLith** — проект, будущая компания и экосистема;
  - **QINTRA** — имя codec/bitstream family;
  - **MOSAIC — Memory-Oriented Scalable Asymmetric Integer Codec** —
    внутренняя архитектура;
  - маркетинговая формулировка:
    **“QINTRA — a SceneLith codec, powered by MOSAIC.”**
- До публичного запуска QINTRA всё равно требует профессиональной
  trademark/FTO-проверки; это не отменяет принятую продуктовую иерархию.

## D-017 — Кадр не является единицей state, reference или движения

- Дата: 2026-07-26
- Статус: time/state invariants — **NORMATIVE-DRAFT / HYPOTHESIS**; исходная
  hard-support/composition formula — **PARTIALLY SUPERSEDED** D-021/D-022
- Решение-кандидат:
  - frame остаётся только совместимым `PresentationSample`, то есть запросом
    результата в момент времени, но не изменяет state сам по себе;
  - bitstream является потоком асинхронных state events;
  - единый primitive — долгоживущая `MOSAIC Cell`:

    \[
    Cell_i=(Content_i,\ Support_i,\ MotionLaw_i(t),\
            Lifetime_i,\ Order_i);
    \]

  - `Lifetime` устраняет per-frame сигнализацию `unchanged`;
  - `MotionLaw(t)` амортизирует motion на интервал, а не передаёт vector на
    каждый output sample;
  - `Content` хранится в compact coordinate-independent memory, а не требует
    frame-sized reference;
  - форма не выбирается из zoo `rectangle/circle/polygon`: `Support` является
    объединением фиксированных dyadic microtiles; точность границы повышается
    только там, где это окупается;
  - state, motion knots, Truth Innovation и display sampling имеют независимые
    clocks;
  - статичная cell не получает событий, а её уже скомпозированный output tile
    MAY сохраняться без повторной записи;
  - движение вычисляется из absolute fixed-point law относительно неизменного
    content, а не рекурсивным warp предыдущего output;
  - физический display всё равно меняет свет дискретно или непрерывно во
    времени; цель — убрать frame clock из transport/state/decode, а не
    заявлять невозможное отсутствие временного sampling.
- DPM становится baseline/component, а не окончательным Main v0.
- Полная проработка: `14_CONTINUOUS_TIME_CELLS.md`.

## D-018 — Момент регистрации и статус заявителя

- Дата: 2026-07-26
- Статус: **ACCEPTED** как порядок проекта; внешняя допустимость
  **OPEN / UNVERIFIED**
- Решение:
  - сначала выбрать архитектуру для реализации, затем вернуться к Annex E и
    другим внешним действиям;
  - план владельца — подаваться как независимый частный заявитель;
  - юридическое имя владельца не записывается в публичную техническую
    документацию до необходимости оформления;
  - при принятии architecture implementation candidate обязательно напомнить
    о регистрации.
- Ограничение: текущий CfP адресован companies/organizations, а Annex E требует
  поле `organization`. Поэтому до обещания подачи от физического лица нужно
  получить письменное подтверждение chair/test coordinator либо согласовать
  допустимое обозначение независимого заявителя.

## D-019 — Public repository как portfolio и точка сборки команды

- Дата: 2026-07-26
- Статус: **TARGET**
- Цель:
  - repository, proposal, architecture paper и demo должны доказуемо показывать
    авторство и уровень systems/research engineering владельца;
  - проект должен быть подготовлен для привлечения сильных external
    contributors.
- Ограничение: одна заявка или громкая идея не гарантирует рост рыночной
  стоимости. Нужны воспроизводимые результаты, работающий decoder, benchmark,
  conformance, честный статус `submitted/evaluated/adopted` и понятный
  contribution path.

## D-020 — Baselines и двойная революционная цель

- Дата: 2026-07-26
- Статус: **ACCEPTED**
- Решение:
  - primary compression baselines всегда отчётны отдельно:
    **AV2 v1.0 / AVM v1.0.0** и **VVC / H.266 (2026) / VTM**;
  - запись `AV2/VVC` без двух отдельных результатов запрещена в claims и
    benchmark tables;
  - применимые BRU, long-term-reference, Show Existing Frame, Atlas, affine,
    merge и другие baseline tools должны быть включены;
  - цель QINTRA — радикально превзойти оба baseline не только по bitrate, но и
    по простоте нормативного decoder code;
  - AV1/HEVC/AVC и быстрые hardware presets могут быть secondary baselines, но
    победа над ними не доказывает достижение frontier target.

## D-021 — One-equation Spacetime Basis Cell

- Дата: 2026-07-26
- Статус: **ARCHITECTURE CANDIDATE / HYPOTHESIS**
- Причина:
  - paper sensitivity model отвергает lifetime/HOLD-only как путь к
    революционному mixed-natural compression;
  - против representative AV2 ledger для total gain 25% требуется устранить
    около 31.8% всех оставшихся AV2 innovation bits; при 50% cell coverage это
    63.6% residual в покрытой части, а при coverage ниже 31.8% цель
    математически невозможна для данного ledger.
- Кандидат:

  \[
  (g_i,c_i)(p,t)=\sum_k a_{i,k}(t)B_{i,k}(W_i(p,t)),
  \]

  - одна Cell должна описывать static, motion, appearance variation и
    persistent/transient Truth Innovation;
  - единственная composition operation:
    \(Y_{j+1}=Clip(g_jY_j+c_j)\);
  - Cell является bounded rate-distortion atom, не semantic object;
  - `RESET/SET` являются достаточной state grammar; presentation — read-only
    container/API query;
  - normative evaluation должен быть fixed-point, bounded и data-parallel;
  - unrestricted neural graph, semantic world, depth/mesh и generative Truth
    не входят в Main;
  - payload synthesizer остаётся главным **OPEN** выбором.
- Полная аргументация и воспроизводимая sensitivity model:
  `15_PAPER_KILL_TEST_AND_FREEZE.md` и
  `../experiments/paper_kill_test.py`.

## D-022 — Visible shape не равна storage tile

- Дата: 2026-07-26
- Статус: **ACCEPTED REQUIREMENT / CANDIDATE MECHANISM**
- Требование:
  - rectangle, dyadic tile и texture allocation MAY использоваться только как
    невидимые storage, scheduling и culling bounds;
  - граница storage unit MUST NOT становиться видимой границей изображения;
  - QINTRA MUST поддерживать arbitrary binary и soft coverage, включая
    antialiasing, hair, transparency и motion blur;
  - lossless profile MUST иметь pixel-exact fallback;
  - lossy profiles MUST иметь RDO fallback и отдельную boundary-quality
    проверку.
- Кандидат-механизм:
  - Cell синтезирует scalar gate \(g\) и color contribution \(c\);
  - вне support неявно \(g=1,c=0\);
  - единый affine compositor \(Y'=Clip(gY+c)\) покрывает replace, alpha-over и
    additive correction без shape primitive zoo;
  - conservative padding и texture apron запрещают sampling seams.
- Физическое ограничение:
  - отсутствие любых artifacts нельзя гарантировать при произвольно малом
    lossy bitrate;
  - гарантируются отсутствие tile-shape artifacts и exact lossless path.

## D-023 — Ведущий payload candidate: cached integer basis synthesis

- Дата: 2026-07-26
- Статус: **RESEARCH CANDIDATE / OPEN**
- Кандидат:
  - один fixed bounded int8/int16 synthesis graph декодирует quantized latents
    в immutable Basis Content;
  - необязательный per-shot adaptation ограничен low-rank integer matrices;
  - все latents/adapters входят в bitrate;
  - synthesis выполняется на `SET`, а не на каждом Presentation Query;
  - renderer остаётся texture-sample + temporal MAC + \(gY+c\);
  - sparse exact correction сохраняет objective/lossless Truth.
- Причина:
  - обычный AV2/VVC intra payload сохранил бы их decoder code complexity;
  - простой linear wavelet наиболее лёгок, но имеет меньший шанс радикально
    уменьшить innovation;
  - fixed integer nonlinear synthesis имеет лучший теоретический баланс
    compression, small normative code и GPU/ASIC regularity.
- Это не означает принятия neural renderer: arbitrary graph, floating point,
  generative Truth и per-presentation inference остаются запрещены.

## D-024 — Численная планка радикального превосходства

- Дата: 2026-07-26
- Статус: **TARGET**
- Minimum architecture-success target:
  - не менее 25% net BD-rate reduction отдельно против AV2 v1.0/AVM и
    VVC/H.266/VTM на broad mixed corpus;
  - одновременно более простой bounded normative decoder.
- Stretch North Star:
  - 40% против более сильного из двух anchors на broad mixed/coherent corpus;
  - 50% на broad screen/UI corpus;
  - отсутствие tile-shape artifacts и exact lossless path.
- 5–10% universal gain полезен, но недостаточен для заявления о новом
  революционном стандарте.

## D-025 — CBF Visual ISA принят как implementation architecture

- Дата: 2026-07-26
- Статус: **ACCEPTED**
- Решение:
  - QINTRA Main строится как **CBF — Causal Basis Field visual ISA** внутри
    MOSAIC;
  - CBF Cell является bounded spacetime basis atom, а не semantic object;
  - одна формула
    \[
    (g_i,c_i)(p,t)=\sum_k a_{i,k}(t)B_{i,k}(W_i(p,t))
    \]
    описывает static, motion, appearance variation, arbitrary soft visible
    shape и persistent/transient Truth Innovation;
  - единая state grammar — `STATE_RESET / CELL_SET`; presentation является
    read-only query;
  - immutable Basis, absolute-time coordinate/parameter laws, implicit
    persistence и objective fallback являются замороженным semantic spine;
  - unrestricted neural renderer, semantic world graph и generative Truth не
    входят в Main;
  - D-021 меняет статус с architecture candidate на **ACCEPTED** в части
    semantic spine; payload synthesizer и точные limits остаются
    **NORMATIVE-DRAFT / HYPOTHESIS**.

## D-026 — Bounded composition algebra и mobile decode envelope

- Дата: 2026-07-26
- Статус: **ACCEPTED / NORMATIVE-DRAFT**
- Решение:
  - Cell описывает affine color pair \((g,c)\);
  - последовательная композиция pair является ассоциативной:
    \[
    (g_2,c_2)\circ(g_1,c_1)=
    (g_2g_1,\ g_2c_1+c_2);
    \]
  - parallel reduction MAY использоваться при сохранении coded order;
  - внутренний clip после каждой Cell запрещается там, где profile-defined
    wide accumulator и range proof позволяют clip на фиксированной layer
    boundary; это уменьшает serial dependency и GPU traffic;
  - Main general target: не более 4 non-identity Cell contributions на
    output pixel, не более 4 fixed composition layers, не более 8 texture
    samples и порядка 128 simple integer operations/pixel;
  - точные absolute limits задаёт profile/level; всё сверх них кодируется
    objective Innovation fallback;
  - Main MAY разрешать bounded translation, affine и projective coordinate
    laws, но первая reference implementation начинает со static/translation.

## D-027 — Consumer encoder и hardware targets

- Дата: 2026-07-26
- Статус: **TARGET / HYPOTHESIS**
- Решение:
  - reference Consumer/Studio encoder должен работать на одном обычном PC и
    8 GB-class GPU посредством spatial/temporal tiling и выгрузки long-term
    state в host RAM;
  - RTX 2080 Super является первым practical development target, но не
    нормативной зависимостью формата;
  - для одной минуты 1080p30 рабочие гипотезы:
    first prototype `1–6 h`, Consumer Fast `3–10 min`, Balanced
    `20–90 min`, Local Foundry `3–12 h`;
  - 1080p60 ожидается примерно в 2 раза дольше, 4K30 — в 4–6 раз;
  - software mobile-GPU target: flagship 1080p60 и plausible 4K30,
    mid-range 1080p30–60; CPU-only target — 720p60/1080p30 при малом overlap;
  - числа не являются измеренными результатами и не входят в conformance.

## D-028 — Последний red-team: сильные идеи без расширения ISA

- Дата: 2026-07-26
- Статус: **ACCEPTED / RESEARCH**
- Принимается в encoder/core discipline:
  - conditional-description-length RDO вместо простого detector `changed`;
  - whole-shot bidirectional analysis и time-symmetric Foundry search,
    компилируемые в те же absolute laws;
  - content-addressed dedup immutable Basis внутри self-contained asset;
  - persistent и ephemeral Truth используют одну Cell с разным Lifetime;
  - новые модели обязаны компилироваться в `B/W/a/g/c/SET`.
- Остаётся **RESEARCH** до отдельного net-gain gate:
  - deterministic stochastic microtexture predictor плюс exact residual;
  - state-only hidden observer для будущего prediction;
  - shared cross-asset dictionaries;
  - learned integer Basis synthesis.
- Не добавляется:
  - primitive zoo;
  - обязательная 3D reconstruction;
  - semantic object truth;
  - external mandatory model;
  - recursive presentation reference.

## D-029 — Video, audio и AV binding являются отдельными объектами

- Дата: 2026-07-26
- Статус: **ACCEPTED**
- Решение:
  - QINTRA — standalone video codec;
  - самостоятельный audio codec с архитектурой MAF разрабатывается отдельно;
    `Resonith` является ведущим, но не финальным кандидатом его имени;
  - SceneLith AV Bridge — отдельная binding specification;
  - ни один standalone Truth bitstream не зависит от другой modality;
  - AV Bridge MAY разделять timeline, entity IDs, trajectories и
    room/geometry hints, но не смешивает Truth reference graphs.

## D-030 — Точка напоминания о внешней регистрации достигнута

- Дата: 2026-07-26
- Статус: **ACCEPTED / ACTION DEFERRED**
- Событие:
  - D-025 принял architecture implementation candidate, поэтому условие
    напоминания из D-018 выполнено;
  - до внешней подачи требуется подтвердить у chair/test coordinator
    допустимость независимого частного заявителя и заполнение поля
    `organization`;
  - техническая разработка audio-first продолжается без ожидания этого
    внешнего ответа.

## D-031 — Имя самостоятельного аудиокодека утверждено

- Дата: 2026-07-26
- Статус: **ACCEPTED**
- Решение:
  - самостоятельный MAF Audio codec окончательно называется **Resonith**;
  - формулировка D-029 о кандидатном статусе имени **SUPERSEDED**;
  - QINTRA и Resonith сохраняют отдельные repositories и bitstreams;
  - SceneLith AV Bridge остаётся отдельным binding.

## D-032 — Видеокодек окончательно называется SceneLith

- Дата: 2026-07-26
- Статус: **ACCEPTED**
- Решение владельца:
  - окончательное продуктовое имя standalone video codec и его bitstream
    family — **SceneLith**;
  - имя **QINTRA** выводится из актуального брендинга из-за коллизии с
    существующей компанией в Германии;
  - D-011 и D-016 в части принятия QINTRA становятся **SUPERSEDED**;
  - внутреннее имя архитектуры остаётся
    **MOSAIC — Memory-Oriented Scalable Asymmetric Integer Codec**;
  - первый нормативный черновик называется **SceneLith-0**;
  - отдельные продукты называются **SceneLith Video** и **Resonith Audio**;
  - SceneLith AV Bridge связывает их, не объединяя bitstreams или Truth
    reference graphs;
  - рекомендуемое имя публичного GitHub repository видеокодека —
    `scenelith`.

## D-033 — Публичный GitHub и безопасная автосинхронизация

- Дата: 2026-07-26
- Статус: **ACCEPTED**
- Решение:
  - SceneLith Video и Resonith Audio публикуются в отдельных public GitHub
    repositories `scenelith` и `resonith`;
  - каждый явно созданный локальный commit автоматически отправляется в
    `origin` repo-local hook-ом;
  - фоновое автоматическое добавление файлов или создание commits запрещено,
    чтобы незавершённые данные и секреты не попадали в public history;
  - перед каждым первым public push выполняются secret/PII scan, тесты и
    проверка состава tracked files;
  - после clone автосинхронизация включается явным bootstrap script.
