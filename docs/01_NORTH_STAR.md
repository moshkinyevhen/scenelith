# North Star и архитектурные инварианты

Статус: **ACCEPTED**

## Основная идея

SceneLith кодирует не последовательность
независимых изображений, а программу изменения ограниченной визуальной сцены:

\[
\hat{V}_t=Render(S_t,\tau_t)+\Delta^{truth}_t+\Delta^{perceptual}_t
\]

где:

- \(S_t\) — `WorldState`;
- \(\tau_t\) — `Trajectories`;
- \(\Delta^{truth}_t\) — `TruthInnovation`;
- \(\Delta^{perceptual}_t\) — `OptionalPerceptualDetail`.

## Нормативные инварианты

### N1. Ограниченное состояние

`WorldState` имеет нормативные пределы памяти, lifetime, идентификаторы страниц,
правила eviction, контрольные hash и полные/дельта-checkpoints.

Никакого неограниченного накопления истории.

### N2. Детерминированность истины

`Render(WorldState, Trajectories) + TruthInnovation` должен быть bit-exact для
всех conforming decoder одной версии профиля.

### N3. Генеративный слой не является reference

`OptionalPerceptualDetail`:

- не меняет `WorldState`;
- не используется для temporal prediction;
- не влияет на entropy context базового потока;
- может быть отброшен без нарушения последующего декодирования;
- должен иметь provenance/uncertainty marking.

### N4. Random access восстанавливает состояние

Каждая random-access point обязана содержать всё необходимое для
восстановления допустимого `WorldState` без доступа к предыдущим пакетам.

### N5. Универсальный fallback

Если atlas, geometry, latent memory или trajectory неэффективны, encoder может
перейти к независимому objective innovation/residual режиму. Ни один класс
контента не должен быть обязан использовать scene representation.

### N6. Декодер ограничен, encoder свободен

Стандарт определяет bitstream и decoding process. Encoder может применять
сколь угодно тяжёлые модели и поиск, если создаёт conforming stream.

### N7. Один поток — разные бюджеты encoder

Live, Studio и Foundry используют один нормативный синтаксис. Foundry не имеет
права передавать произвольный decoder graph, отсутствующий в Main profile.

### N8. GPU/ASIC-first

Main profile строится из фиксированных integer tensor/render operations,
параллельных chunks/tiles и независимых entropy lanes. Полноэкранная
авторегрессия и произвольные динамические графы запрещены.

### N9. Presentation не является state mutation

**NORMATIVE-DRAFT:** запрос output в момент \(t\) читает `WorldState`, но сам
по себе не изменяет его. State, motion knots, Truth Innovation и presentation
sampling имеют независимые clocks.

Статичная область остаётся действительной без per-frame `HOLD`. Плавное
движение задаётся absolute fixed-point law на интервал и не вычисляется
рекурсивным warp предыдущего output. Подробности:
[14_CONTINUOUS_TIME_CELLS.md](14_CONTINUOUS_TIME_CELLS.md).

## Фундаментальные гипотезы

### H1. Битрейт следует за новой информацией

**HYPOTHESIS:** на когерентной сцене стоимость потока должна в основном
определяться изменениями сцены, а не произведением `width × height × FPS`.

### H2. Долговременное повторное использование

**HYPOTHESIS:** повторное появление поверхности после окклюзии или ухода камеры
может кодироваться ссылкой на сохранённое состояние дешевле повторного
pixel-domain intra/inter coding.

### H3. Временная непрерывность

**HYPOTHESIS:** spline/trajectory description позволяет увеличивать частоту
кадров существенно дешевле линейного роста битрейта для гладкого движения.

Уточнение D-017: частота presentation samples не обязана быть частотой
bitstream events. Для источника с дискретным ground truth новые timestamps
считаются interpolated/synthetic, пока не подтверждены дополнительным
наблюдением или Truth Innovation.

### H4. Асимметрия полезна

**HYPOTHESIS:** дорогой encoder может компилировать сложное видео в небольшой
ограниченный decoder ISA без переноса основной сложности на клиент.

## Правила честности

1. Fidelity и perceptual результаты публикуются раздельно.
2. Синтезированные детали не называются восстановленными исходными деталями.
3. Все side information, weights, adapters, checkpoints и metadata входят в
   итоговый bitrate.
4. Encoder preprocessing и multipass учитываются в runtime.
5. Сравнения выполняются при сопоставимых latency, GOP, random-access,
   resolution, chroma format и bit depth.
