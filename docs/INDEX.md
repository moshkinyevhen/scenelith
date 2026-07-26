# Индекс документации SceneLith

Этот каталог является канонической базой знаний проекта. Исторические тексты
могут содержать устаревшие оценки; актуальные решения определяются
`10_DECISION_LOG.md` и тематическими документами.

| Файл | Назначение |
|---|---|
| [00_CHARTER.md](00_CHARTER.md) | Устав, миссия, область проекта |
| [01_NORTH_STAR.md](01_NORTH_STAR.md) | Главная формула и инварианты |
| [02_MOSAIC_ARCHITECTURE.md](02_MOSAIC_ARCHITECTURE.md) | Архитектура MOSAIC |
| [03_BITSTREAM_AND_DECODER.md](03_BITSTREAM_AND_DECODER.md) | Черновая структура потока и декодера |
| [04_ENCODERS.md](04_ENCODERS.md) | Live, Studio и Foundry encoder |
| [05_JVET_CFP_2026.md](05_JVET_CFP_2026.md) | Текущая заявка JVET |
| [06_RESEARCH_RADAR.md](06_RESEARCH_RADAR.md) | Исследовательские направления |
| [07_METRICS_AND_ROADMAP.md](07_METRICS_AND_ROADMAP.md) | Метрики, этапы и сроки |
| [08_RISKS_AND_KILL_CRITERIA.md](08_RISKS_AND_KILL_CRITERIA.md) | Риски и критерии остановки |
| [09_NAMING_IP_AND_MOAT.md](09_NAMING_IP_AND_MOAT.md) | Название, IP и конкурентный отрыв |
| [10_DECISION_LOG.md](10_DECISION_LOG.md) | Хронология принятых решений |
| [11_CODEX_EXECUTION_POLICY.md](11_CODEX_EXECUTION_POLICY.md) | Режимы Sol и multi-agent execution |
| [12_OBSERVED_SURFACE_MEMORY.md](12_OBSERVED_SURFACE_MEMORY.md) | Историческая full OSM ветка; superseded для Main |
| [13_MINIMAL_PATCH_CORE.md](13_MINIMAL_PATCH_CORE.md) | DPM falsification baseline и equal-memory patch experiment |
| [14_CONTINUOUS_TIME_CELLS.md](14_CONTINUOUS_TIME_CELLS.md) | Принятый frame-free state/motion/display foundation SceneLith |
| [15_PAPER_KILL_TEST_AND_FREEZE.md](15_PAPER_KILL_TEST_AND_FREEZE.md) | Раздельный AV2/VVC paper kill-test и обоснование one-equation architecture |
| [16_CBF_ACCEPTANCE_AND_FINAL_RED_TEAM.md](16_CBF_ACCEPTANCE_AND_FINAL_RED_TEAM.md) | Принятая CBF visual ISA, bounded compute и финальный red-team |
| [REFERENCES.md](REFERENCES.md) | Первичные источники |

Нормативный черновик находится в
[../spec/SCENELITH-0.md](../spec/SCENELITH-0.md).

Операционный checklist текущей заявки находится в
[../cfp/2026/CHECKLIST.md](../cfp/2026/CHECKLIST.md).

Исходные материалы без редактирования хранятся в `../archive/`.

## Значение статусов

- **ACCEPTED** — принято владельцем проекта.
- **NORMATIVE-DRAFT** — кандидат в нормативное требование.
- **HYPOTHESIS** — проверяемая техническая гипотеза.
- **TARGET** — целевая, ещё не достигнутая метрика.
- **RESEARCH** — исследовательское расширение.
- **SUPERSEDED** — заменённое решение.

## Правило обновления

Каждое содержательное решение из чата должно попасть в журнал и тематический
документ до завершения текущего рабочего цикла.
