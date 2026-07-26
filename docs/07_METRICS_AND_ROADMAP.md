# Метрики и roadmap

Статус: сроки — **TARGET**, контрольные пороги — **ACCEPTED**.

## 1. Два параллельных трека

### Track A — SceneLith-CfP-2026

Цель: формально полный unrestricted improved-compression proposal к
26 октября 2026 года.

### Track B — SceneLith Main

Цель: массовый GPU/ASIC-friendly format с Live, Studio и Foundry encoder.

CfP-ветка не должна замораживать ошибочные компромиссы во всём будущем
формате. Полезные инструменты переносятся в Main только после экспериментов.

## 2. Агрессивный календарь реализации

Отсчёт: 2026-07-26.

| Срок | TARGET deliverable |
|---|---|
| 48–72 часа | Репозиторий, charter, spec skeleton, CI и benchmark harness |
| 2–3 недели | Self-contained bitstream skeleton, CPU decoder, wavelet/residual, multi-lane rANS |
| 6–8 недель | SceneLith-0: bounded Cells, MotionLaw, MAP/checkpoints, GPU path |
| 12–13 недель | Полный CfP main package и честные RD results |
| 4 месяца | Multi-frame learned innovation prototype |
| 6 месяцев | 1080p60 Alpha, bit-exact CPU/GPU |
| 9 месяцев | Loss repair, HDR/screen modes, experimental Perceptual Shell |
| 12 месяцев | Main v1 Candidate |
| 18 месяцев | 4K60, independent tests, conformance suite, FPGA preparation |
| 24–36 месяцев | Standard-grade specification/implementation |

Формальный стандарт и массовый silicon остаются многолетней внешней задачей.

### 2.1 Critical path Continuous-Time Cells

| Результат | TARGET от старта реализации |
|---|---:|
| Event/state simulator и synthetic demo | 1–3 дня |
| Dirty-tile renderer, bit-exact linear translation | 4–7 дней |
| Gate A и первый Gate B oracle | 1–2 недели |
| Fair AV2/VVC run comparison | 2–4 недели |
| Compact `CAPTURE_TRUTH` Gate C | 3–6 недель |
| GPU multi-refresh demo | 4–8 недель |
| Broad RD/power corpus и architecture verdict | 8–16 недель |

Демонстрация новой time semantics возможна за дни; сильный общий compression
claim требует tool-complete AV2/VVC baselines, полного bit accounting и
многократных corpus runs. Подробности:
[14_CONTINUOUS_TIME_CELLS.md](14_CONTINUOUS_TIME_CELLS.md).

## 3. Fidelity metrics

Обязательные:

- bitrate, включая все side information;
- PSNR-Y, PSNR-YUV;
- MS-SSIM;
- VMAF с зафиксированной версией;
- BD-rate;
- per-frame rate и quality;
- HDR-compatible objective metrics;
- random-access penalty;
- decoder runtime, MAC/pixel, peak memory и traffic.

Ни одна одна метрика не является достаточной.

## 4. Perceptual/truth metrics

- blind MOS/DCR/DSIS;
- LPIPS/DISTS только как дополнительные perceptual показатели;
- OCR accuracy и character error rate;
- face/identity consistency;
- geometry/edge displacement;
- temporal flicker;
- color/HDR consistency;
- provenance coverage;
- synthetic-region false-negative rate.

Perceptual результаты публикуются отдельно от Fidelity.

## 5. Двенадцатимесячные цели

**TARGET:**

- bit-exact 1080p60 GPU decoder;
- не менее −25% BD-rate отдельно к AVM AV2 v1.0 и VTM VVC/H.266 на закрытом
  broad validation set; stretch −40% к более сильному anchor;
- compact cells дают не менее 10% total-rate improvement на reappearance
  subset;
- innovation bits уменьшаются не менее чем на 20% на том же subset;
- checkpoint/address overhead меньше 8%;
- ни один основной content class не ухудшается более чем на 10%.

## 6. Двадцатичетырёхмесячные цели

**TARGET:**

- 4K60 desktop GPU;
- −35% к VTM-RA;
- минимум −10% к сильнейшему воспроизводимому learned anchor того же класса
  latency/random access;
- Perceptual Shell: ≥2× bitrate reduction при равном blind MOS;
- обязательные OCR, identity, geometry и flicker gates.

## 7. Тридцатишестимесячный stretch

**TARGET:**

- −40…−45% к VTM-RA;
- минимум −15% к современному воспроизводимому learned codec;
- ни один крупный content class не хуже anchor более чем на 5%;
- 2–3× perceptual reduction при равном blind MOS;
- 4–10× только для специализированных VOD/UI/talking-head режимов;
- Main High ≤5 kMAC/output-pixel;
- Low Compute ≤1.5 kMAC/output-pixel;
- weights ≤32 MB;
- persistent state ≤64 MB;
- random access 0.25–0.5 секунды;
- state repair ≤250 мс.

## 8. Consumer encoder requirements

**ACCEPTED:**

- зрелый Studio encoder должен извлекать 80–90% полной экономии Foundry;
- Main profile отклоняется как массовый, если качественный поток возможно
  получить только астрономическим поиском;
- real-time preset является частью архитектуры с первого прототипа, а не
  поздней оптимизацией.

Пример TARGET:

- anchor: 100 условных bits;
- Foundry: 55–65;
- Studio: 62–70;
- Live: 70–80.

Это иллюстративные цели, не измеренные результаты.

## 9. Fair-comparison protocol

Каждое публичное сравнение фиксирует:

- exact commit/version anchors;
- test sequences и запрет training leakage;
- RA/LB configuration;
- GOP/intra period;
- structural delay/lookahead;
- bit depth/chroma/color;
- encoder и decoder hardware;
- preprocessing/postprocessing;
- model/adaptor/checkpoint bits;
- wall time и суммарное CPU/GPU time;
- командные строки и hashes outputs.

## 10. Go/no-go

- После первого полного reappearance experiment:
  - baseline обязан включать AV2 BRU/LTR/Atlas, VVC и equal-memory decoded
    patch cache;
  - если Gate B даёт <12% на scroll/sprite, <7% broad screen или <3% mixed,
    не включать persistent motion runs в universal core;
  - если compact-cell oracle даёт <15% на puzzle subset или <5% mixed,
    redesign/kill compact reference path;
  - если он не бьёт equal-memory patch cache, оставить простой cache;
  - если events/support/checkpoints съедают >20% gross saving, менять syntax.
- Через 12 месяцев:
  - отсутствие измеримого универсального выигрыша требует смены core
    representation.
- Через 18 месяцев:
  - если нет ≥25% честного выигрыша отдельно над AV2 и VVC и нет
    принципиально новой функциональности, отдельный новый стандарт не
    оправдан.

Срок не является основанием скрывать отрицательный результат.
