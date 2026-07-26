# SceneLith

**SceneLith** — standalone видеокодек и открытый проект нового формата
представления динамической визуальной сцены. Внутреннее имя архитектуры:
**MOSAIC — Memory-Oriented Scalable Asymmetric Integer Codec**.

> **SceneLith Video — powered by MOSAIC.**

Каноническая формула проекта:

\[
Video(t)=Render(WorldState_t,\ Trajectories_t)
       +TruthInnovation_t
       +OptionalPerceptualDetail_t
\]

SceneLith передаёт ограниченное детерминированное состояние сцены и поток новой
информации о ней. Принятая implementation architecture —
**CBF: Causal Basis Field visual ISA**. Frame удалён из роли state/reference/
motion unit: долгоживущие MOSAIC Cells обновляются асинхронно, а изображение
является read-only запросом состояния в момент \(t\).

## Где искать информацию

- [Индекс документации](docs/INDEX.md)
- [Устав и принятые цели](docs/00_CHARTER.md)
- [Канонические принципы](docs/01_NORTH_STAR.md)
- [Архитектура MOSAIC](docs/02_MOSAIC_ARCHITECTURE.md)
- [Frame-free Continuous-Time Cells](docs/14_CONTINUOUS_TIME_CELLS.md)
- [Принятие CBF и финальный red-team](docs/16_CBF_ACCEPTANCE_AND_FINAL_RED_TEAM.md)
- [Черновик нормативной спецификации SceneLith-0](spec/SCENELITH-0.md)
- [План заявки JVET CfP 2026](docs/05_JVET_CFP_2026.md)
- [Журнал решений](docs/10_DECISION_LOG.md)
- [Источники и исследования](docs/REFERENCES.md)

## Статус

Проект находится на стадии архитектурного определения и подготовки
экспериментальной ветки `SceneLith-CfP-2026`.

Текущая deadline-цель: подготовить полный unrestricted improved-compression
response для JVET CfP beyond VVC к 26 октября 2026 года.

Все численные показатели эффективности в документации являются целями или
гипотезами, пока они не подтверждены воспроизводимым экспериментом.

## GitHub-синхронизация

Репозиторий использует безопасный `post-commit` hook: каждый явно созданный
локальный commit автоматически отправляется в `origin`. Hook никогда сам не
добавляет файлы и не создаёт commits. После нового clone режим включается
командой:

```powershell
.\scripts\enable-auto-sync.ps1
```

Для явного `fetch + pull --rebase + push` используется:

```powershell
.\scripts\sync.ps1
```
