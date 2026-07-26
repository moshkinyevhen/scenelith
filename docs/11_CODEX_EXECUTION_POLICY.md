# Codex 5.6 Sol Usage Policy

Status: **NORMATIVE-DRAFT**
Date: 2026-07-26
Correction: Level names have been adjusted to the actual Russian interface
Codex Desktop user.

## 1. Available levels in the current interface

There are exactly five levels available in the SceneLith operating interface:

| Name in the interface | English designation | Destination |
|---|---|---|
| **Easy** | Light / `low` | Fast and fully defined actions |
| **Medium** | Medium | Routine work with moderate planning |
| **High** | High | Complex multi-step implementation and verification |
| **Very tall** | Extra High / `xhigh` | Difficult architecture, analysis of multiple tradeoffs and sources |
| **Ultra** | Ultra | Maximum depth of composite work with the possibility of parallel delegation |

`Max` is not in the current model picker and therefore **is not working
SceneLith** level. The official manual mentions it as optional
level of some configurations, but the previous recommendation is to use `Max`
in the user interface was incorrect.

## 2. Rational level right now

The current stage is not a free conversation about possibilities, but the creation of a canonical
architecture of the standard, comparison of prior art, search for contradictions and recording of solutions,
which will then define the bitstream and decoder.

> **For current work on the SceneLith standard, use “Ultra”.**

Reasons:

- an error in the semantics of state, reference safety or random access will multiply by
  the entire implementation;
- the task is divided into independent areas: prior art, bitstream, hardware,
  compression theory, failure analysis and conformance;
- it is useful to simultaneously receive an offer and an adversarial review;
- at this stage, the quality of the solution is more important than saving usage limit.

If the discussion is just quick brainstorming without taking notes or taking notes
solution, **“Very high”** is sufficient. Before translating an idea into
`NORMATIVE-DRAFT` or `ACCEPTED` should be returned to **Ultra**.

## 3. Where to use each level

| Work by SceneLith | Rational level |
|---|---|
| Renaming, searching for a string, formatting, updating a table | **Easy** |
| Gathering sources, routine documentation, running known tests | **Medium** |
| Implementation of the already frozen decoder tool, GPU kernel, test harness | **High** |
| Designing one complex tool, RDO, debugging bit-exact errors | **Very tall** |
| Architecture of the entire standard, bitstream/state freeze, full design review, CfP integration | **Ultra** |

## 4. Difference between “Very High” and “Ultra”**Very high** rational when there is one difficult, but sufficient
whole task: deduce state transition, design entropy tool,
parse regression or write a complex module.

**Ultra** rational when one result requires several different roles:
architect, prior art researcher, hardware reviewer, author
specifications and criticism. In this mode, Codex can proactively parallelize
suitable parts of the work.

Therefore, “Ultra” is not just a mandatory setting for everyone
actions. Its advantage is revealed in compound tasks.

## 5. Project working diagram

1. **Architectural sessions and solutions of the standard - Ultra.**
2. **Isolated complex studies and algorithms - Very high.**
3. **Basic implementation according to the finished specification - High.**
4. **Mechanical Tests and Documentation - Medium.**
5. **Trivial local changes - Easy.**

For a root task at the **"Ultra"** level, subtasks are assigned the minimum
sufficient level. This maintains maximum quality of coordination without
using the most expensive mode on the boilerplate.

## 6. Relationship with the date of the first version

A period of 6–12 weeks assumes:

- **Ultra** on architectural forks and integration;
- **Very high** on new compression hypotheses and heavy debugging;
- **High** on implementation;
- **Medium/Easy** on mass mechanically verified tasks;
- automatic GPU/CI workers, working regardless of model inference.

Additional reasoning does not reduce the physical time of compilation, training and
benchmark runs. It reduces the number of expensive bad branches and redundancies.
implementations.

## 7. Official basis

OpenAI recommends choosing the minimum level that gives the required
quality. High and Extra High are designed for difficult work with several
steps, sources and tradeoffs. Ultra uses maximum reasoning and
can divide complex work between subagents.

- https://learn.chatgpt.com/docs/models
- https://developers.openai.com/codex/codex-manual.md