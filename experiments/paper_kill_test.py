#!/usr/bin/env python3
"""
SceneLith paper kill-test.

This is a deterministic sensitivity model, not a codec benchmark.  It answers:

    Given an assumed bit-rate ledger for an already strong baseline codec,
    how much can a SceneLith mechanism save before any implementation exists?

Every baseline is normalized to 1.0:

    baseline_rate = control + motion + innovation

SceneLith gain is:

    control * saved_control
  + motion * saved_motion
  + innovation * saved_innovation
  - scenelith_overhead

The parameter intervals are explicit hypotheses.  They must later be replaced
by component measurements from AVM v1.0.0 and VTM instrumentation.
"""

from __future__ import annotations

from dataclasses import dataclass
import random
from typing import Dict, Iterable, Tuple


Range = Tuple[float, float]


@dataclass(frozen=True)
class Scenario:
    control_share: Range
    motion_share: Range
    saved_control: Range
    saved_motion: Range
    saved_innovation: Range
    scenelith_overhead: Range


def sample(rng: random.Random, interval: Range) -> float:
    return rng.uniform(*interval)


def percentile(values: list[float], p: float) -> float:
    ordered = sorted(values)
    position = (len(ordered) - 1) * p
    lo = int(position)
    hi = min(lo + 1, len(ordered) - 1)
    fraction = position - lo
    return ordered[lo] * (1.0 - fraction) + ordered[hi] * fraction


def simulate(scenario: Scenario, seed: int, trials: int = 200_000) -> list[float]:
    rng = random.Random(seed)
    gains: list[float] = []
    for _ in range(trials):
        control = sample(rng, scenario.control_share)
        motion = sample(rng, scenario.motion_share)
        innovation = 1.0 - control - motion
        if innovation <= 0:
            raise ValueError("Invalid rate ledger: non-positive innovation share")

        gain = (
            control * sample(rng, scenario.saved_control)
            + motion * sample(rng, scenario.saved_motion)
            + innovation * sample(rng, scenario.saved_innovation)
            - sample(rng, scenario.scenelith_overhead)
        )
        gains.append(gain)
    return gains


# These are deliberately conservative thought-experiment priors.
# AV2 receives narrower/lower savings because BRU, long-term references,
# Show Existing Frame, advanced motion tools and Atlas already attack part of
# the persistence problem.  VVC is still a separate, strong baseline.
SCENARIOS: Dict[str, Dict[str, Scenario]] = {
    "AV2 v1.0 / AVM v1.0.0": {
        "mixed: lifetime + linear law": Scenario(
            (0.05, 0.10), (0.035, 0.08),
            (0.10, 0.30), (0.15, 0.40), (0.00, 0.01), (0.015, 0.035),
        ),
        "mixed: compact persistent Cell": Scenario(
            (0.05, 0.10), (0.035, 0.08),
            (0.15, 0.35), (0.20, 0.45), (0.00, 0.025), (0.02, 0.05),
        ),
        "mixed: persistent TruthInnovation only": Scenario(
            (0.05, 0.10), (0.035, 0.08),
            (0.25, 0.50), (0.30, 0.60), (0.02, 0.10), (0.04, 0.09),
        ),
        "mixed: low-rank basis target envelope": Scenario(
            (0.05, 0.10), (0.035, 0.08),
            (0.25, 0.50), (0.30, 0.60), (0.10, 0.32), (0.06, 0.13),
        ),
        "coherent pan/occlusion: compact Cell": Scenario(
            (0.05, 0.10), (0.04, 0.10),
            (0.20, 0.45), (0.30, 0.60), (0.02, 0.10), (0.035, 0.075),
        ),
        "screen/UI/scroll: compact Cell": Scenario(
            (0.08, 0.18), (0.04, 0.14),
            (0.30, 0.60), (0.40, 0.70), (0.02, 0.15), (0.04, 0.09),
        ),
        "stable arbitrary/soft silhouette": Scenario(
            (0.05, 0.11), (0.04, 0.10),
            (0.20, 0.50), (0.30, 0.65), (0.02, 0.10), (0.035, 0.08),
        ),
        "hair/smoke/chaotic boundary: forced Cell": Scenario(
            (0.05, 0.10), (0.06, 0.15),
            (0.05, 0.20), (0.05, 0.25), (0.00, 0.03), (0.04, 0.12),
        ),
        "hostile dynamic: forced Cell": Scenario(
            (0.05, 0.10), (0.06, 0.14),
            (0.05, 0.15), (0.05, 0.20), (0.00, 0.005), (0.015, 0.04),
        ),
    },
    "VVC / H.266 (2026) / VTM": {
        "mixed: lifetime + linear law": Scenario(
            (0.065, 0.12), (0.045, 0.10),
            (0.15, 0.40), (0.20, 0.50), (0.00, 0.015), (0.015, 0.035),
        ),
        "mixed: compact persistent Cell": Scenario(
            (0.065, 0.12), (0.045, 0.10),
            (0.20, 0.45), (0.25, 0.55), (0.00, 0.035), (0.02, 0.05),
        ),
        "mixed: persistent TruthInnovation only": Scenario(
            (0.065, 0.12), (0.045, 0.10),
            (0.30, 0.60), (0.40, 0.70), (0.03, 0.13), (0.04, 0.09),
        ),
        "mixed: low-rank basis target envelope": Scenario(
            (0.065, 0.12), (0.045, 0.10),
            (0.30, 0.60), (0.40, 0.70), (0.12, 0.38), (0.06, 0.13),
        ),
        "coherent pan/occlusion: compact Cell": Scenario(
            (0.065, 0.12), (0.05, 0.12),
            (0.25, 0.50), (0.35, 0.65), (0.03, 0.12), (0.035, 0.075),
        ),
        "screen/UI/scroll: compact Cell": Scenario(
            (0.10, 0.22), (0.05, 0.16),
            (0.40, 0.70), (0.50, 0.80), (0.03, 0.20), (0.04, 0.09),
        ),
        "stable arbitrary/soft silhouette": Scenario(
            (0.07, 0.13), (0.05, 0.12),
            (0.30, 0.60), (0.40, 0.70), (0.03, 0.14), (0.035, 0.08),
        ),
        "hair/smoke/chaotic boundary: forced Cell": Scenario(
            (0.065, 0.12), (0.07, 0.17),
            (0.05, 0.22), (0.05, 0.28), (0.00, 0.04), (0.04, 0.12),
        ),
        "hostile dynamic: forced Cell": Scenario(
            (0.065, 0.12), (0.07, 0.16),
            (0.05, 0.18), (0.05, 0.22), (0.00, 0.008), (0.015, 0.04),
        ),
    },
}


def required_innovation_saving(
    target_gain: float,
    control: float,
    motion: float,
    saved_control: float,
    saved_motion: float,
    overhead: float,
) -> float:
    innovation = 1.0 - control - motion
    return (
        target_gain
        + overhead
        - control * saved_control
        - motion * saved_motion
    ) / innovation


def print_table() -> None:
    print("PAPER SENSITIVITY MODEL — NOT A CODEC BENCHMARK")
    print("All results are net rate reduction at equal distortion, in percent.")
    print()
    for baseline_index, (baseline, scenarios) in enumerate(SCENARIOS.items()):
        print(baseline)
        print("-" * len(baseline))
        print(f"{'scenario':47} {'p10':>7} {'p50':>7} {'p90':>7} {'P(g>=25%)':>11}")
        for scenario_index, (name, scenario) in enumerate(scenarios.items()):
            gains = simulate(
                scenario,
                seed=0x51CE_0000 + baseline_index * 100 + scenario_index,
            )
            p10 = 100.0 * percentile(gains, 0.10)
            p50 = 100.0 * percentile(gains, 0.50)
            p90 = 100.0 * percentile(gains, 0.90)
            p25 = 100.0 * sum(g >= 0.25 for g in gains) / len(gains)
            print(f"{name:47} {p10:7.2f} {p50:7.2f} {p90:7.2f} {p25:10.2f}%")
        print()


def print_thresholds() -> None:
    # Representative mixed-natural ledger for a strong AV2 baseline.
    ledger = {
        "control": 0.075,
        "motion": 0.0575,
        "saved_control": 0.375,
        "saved_motion": 0.45,
        "overhead": 0.08,
    }
    print("REPRESENTATIVE AV2 MIXED-NATURAL THRESHOLD")
    print("------------------------------------------")
    print(
        "Assumption: control=7.5%, motion=5.75%, "
        "Cell saves 37.5%/45% of them, new overhead=8%."
    )
    for target in (0.10, 0.25, 0.40):
        needed_global = required_innovation_saving(target_gain=target, **ledger)
        print(
            f"For {target * 100:>4.0f}% total gain, SceneLith must remove "
            f"{needed_global * 100:>5.1f}% of all remaining AV2 innovation bits."
        )
        local = []
        for coverage in (0.30, 0.50, 0.80, 1.00):
            required_on_covered = needed_global / coverage
            label = (
                "impossible"
                if required_on_covered > 1.0
                else f"{required_on_covered * 100:.1f}%"
            )
            local.append(f"coverage {coverage * 100:.0f}% -> {label}")
        print("    " + "; ".join(local))


if __name__ == "__main__":
    print_table()
    print_thresholds()
