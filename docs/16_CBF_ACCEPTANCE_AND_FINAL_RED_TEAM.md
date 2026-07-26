# CBF принятие и финальный архитектурный red-team

Статус: semantic spine — **ACCEPTED**; численные limits — **NORMATIVE-DRAFT**;
compression estimates — **HYPOTHESIS**.

## 1. Принятое ядро

**CBF — Causal Basis Field** является visual ISA SceneLith внутри MOSAIC.

\[
(g_i,c_i)(p,t)=\sum_k a_{i,k}(t)B_{i,k}(W_i(p,t)),
\qquad
Y_{i+1}=g_iY_i+c_i.
\]

Cell не означает объект, прямоугольник, лицо или 3D surface. Это bounded
rate-distortion atom:

- `B` — immutable reusable local Truth basis;
- `W` — absolute coordinate law;
- `a` — absolute temporal coefficient law;
- `g` — arbitrary binary/soft coverage;
- `c` — color contribution;
- `Lifetime` — interval действия;
- `SET` — событие только при изменении закона.

Любая область произвольной формы задаётся Gate. Rectangle/tile является лишь
невидимым storage/culling bound. Full objective raster replacement является
точным fallback той же affine formula.

## 2. Недостающая деталь: algebra before clip

Самый сильный найденный compute-механизм не требует нового visual tool.
Affine pairs ассоциативны:

\[
(g_2,c_2)\circ(g_1,c_1)=
(g_2g_1,\ g_2c_1+c_2).
\]

Это позволяет:

- parallel prefix/tree reduction;
- один wide accumulation path;
- clip только на 2–4 фиксированных layer boundaries;
- уменьшение serial dependency;
- меньше framebuffer read/write traffic;
- deterministic GPU/DSP/ASIC scheduling.

Порядок не становится произвольным: reduction обязана сохранять coded order.
Profile задаёт bit widths и range proof.

## 3. Что даёт compression, не меняя decoder

### Conditional novelty

Encoder обновляет не «всё, что изменилось», а только информацию, которая
снижает полную conditional description length:

\[
J=R+\lambda D+\mu C+\nu M+\rho L+\kappa P.
\]

Один Atom принимается лишь когда Basis, gate, trajectory, lifetime, indexes и
checkpoint вместе дешевле objective fallback.

### Whole-shot time symmetry

Studio/Foundry MAY анализировать прошлое и будущее, собирать поверхность из
всех наблюдений и искать глобально согласованные tracks. Decoder всё равно
получает causal absolute laws и не усложняется.

### Basis dedup

Immutable Basis получает content identity и переиспользуется всеми Cells
asset-а. Повторная texture, recurring graphics, resurfacing region и
persistent innovation оплачиваются один раз. External dictionary не
обязателен.

### Independent update clocks

Gate, coordinate law, appearance coefficients и Innovation обновляются только
при собственной novelty. Presentation refresh rate не является их clock.

## 4. Что ещё может дать большой выигрыш

Только три направления сохраняют шанс на крупный дополнительный gain без
нового opcode zoo:

1. **Cached integer Basis synthesis** — encoder передаёт компактный latent,
   decoder один раз строит immutable `B`; per-pixel neural rendering
   запрещён.
2. **Deterministic stochastic field** — grain/water/foliage predictor с seed
   и sparse Truth correction; Perceptual variant никогда не reference.
3. **Predictive-only hidden observer state** — невидимое состояние для
   будущего residual, не для display; принимается только при net gain не менее
   8% на hostile natural class и bounded random access.

Все три — **RESEARCH**. Они должны компилироваться в `B/W/a/g/c/SET` либо
ждать следующую major version.

## 5. Что сознательно отвергается

- обязательный semantic scene graph;
- попытка достроить невидимый мир для Truth;
- depth/mesh/Gaussian primitive zoo в Main;
- unrestricted neural decoder;
- generative detail как reference;
- external model, без которого stream не самодостаточен;
- recursive warp предыдущего presentation;
- отдельный codec для fallback.

Эти механизмы могут быть encoder-side hypotheses или Perceptual enhancement,
но не усложняют CBF Core.

## 6. Bounded software decode target

Main general target:

- не более 4 non-identity contributions/output pixel;
- не более 4 fixed composition layers;
- не более 8 texture samples/output pixel;
- порядка 128 simple integer operations/output pixel;
- bounded Basis/Cell working set;
- translation/affine/projective laws только в profile limits;
- excess complexity переводится в objective Innovation.

Это должно позволить software GPU decode до hardware adoption. Точные значения
будут заморожены conformance experiment-ом; device-specific performance не
является нормативной гарантией.

## 7. Consumer encoder target

Первый reference encoder обязан иметь tiled режим для 8 GB-class GPU. RTX
2080 Super является development target, а не зависимостью bitstream.

Для минуты 1080p30:

| Encoder | **HYPOTHESIS** |
|---|---:|
| Первый prototype | 1–6 h |
| Consumer Fast | 3–10 min |
| Balanced | 20–90 min |
| Local Foundry | 3–12 h |

1080p60 ожидается приблизительно в 2 раза дольше, 4K30 — в 4–6 раз.

## 8. Honest compression hypothesis

Отчёт ведётся отдельно против полного AV2 и полного VVC:

| Контент | против AV2 | против VVC |
|---|---:|---:|
| Screen/UI/2D animation | 20–60% | 25–65% |
| Stable/pan/reuse | 15–40% | 20–45% |
| Mixed natural, first mature generation | 5–15% | 8–20% |
| Hostile stochastic | 0–5% | 0–8% |
| Foundry mixed-natural upper hypothesis | 15–30% | 20–35% |

Это **HYPOTHESIS**, не измеренный результат. Революционная планка остаётся
не менее 25% отдельно против обоих anchors на broad mixed corpus при более
лёгком bounded decoder.

## 9. Freeze rule

Архитектура больше не пересматривается из-за каждой новой encoder-идеи.
Заморожены:

```text
immutable Basis
absolute laws
arbitrary soft Gate
affine-pair composition
RESET / SET
implicit persistence
read-only presentation
objective Innovation fallback
non-reference Perceptual Detail
```

Открыты только basis payload, entropy, precisions, transforms, profile limits
и encoder search. Это параметры одной машины, а не новая архитектура.
