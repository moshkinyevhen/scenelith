# Instructions for SceneLith agents

## Canonical-record rule

Any new architectural decision, syntax proposal, numerical target,
experimental result, or schedule change introduced in conversation MUST be
recorded in the project files during the same work cycle. Chat is not the
canonical record.

## Canonical locations

- `docs/INDEX.md` — documentation map.
- `docs/10_DECISION_LOG.md` — adopted, amended, and superseded decisions.
- `spec/SCENELITH-0.md` — normative format and decoder draft.
- `docs/05_JVET_CFP_2026.md` — current call requirements and response plan.
- `docs/REFERENCES.md` — primary sources.
- `archive/` — historical source material.

## Statement statuses

- **ACCEPTED** — adopted by the project owner; change only through the
  decision log.
- **NORMATIVE-DRAFT** — proposed normative requirement that is not frozen.
- **HYPOTHESIS** — falsifiable technical hypothesis.
- **TARGET** — desired but unmeasured result.
- **RESEARCH** — investigation outside the mandatory Main profile.
- **SUPERSEDED** — historical decision replaced by a newer one.

Never present a **TARGET** or **HYPOTHESIS** as a measured result.

## Immutable invariants

1. The standalone video codec, bitstream family, and project are named
   **SceneLith**.
2. The architecture is **MOSAIC — Memory-Oriented Scalable Asymmetric Integer
   Codec**.
3. Only the Truth Core may mutate `WorldState` or become a temporal reference.
4. Optional Perceptual Detail never mutates `WorldState` and is never a
   reference.
5. The normative decoder is deterministic, resource-bounded, and suitable for
   GPU, DSP, embedded, and ASIC implementation.
6. One normative bitstream and decoder support Live, Studio, and Foundry
   encoders.
7. Competitive advantage should reside primarily in the non-normative encoder
   compiler, data, RDO, and implementation quality, not in a proprietary
   decoder.

## Repository language

- English is the sole language for all public specifications,
  documentation, code comments, commit messages, issue and pull-request
  templates, and GitHub metadata.
- Established mathematical symbols and internationally recognized technical
  terms may remain unchanged.
- Historical source material may preserve another language only outside the
  public repository or when accompanied by a complete English record.

## Documentation workflow

- Record a new decision in `docs/10_DECISION_LOG.md`, then update the thematic
  document and normative draft when applicable.
- When historical material conflicts with canonical documentation, the newest
  **ACCEPTED** decision controls.
- Cite primary publications or official documents with direct links.
- Preserve the distinction between the standalone SceneLith codec, standalone
  Resonith codec, and the separate SceneLith AV Bridge.

## Source-comment contract

- Comment intent, invariants, numerical rules, ownership, state transitions,
  security boundaries, and non-obvious tradeoffs.
- Divide complex functions into a few named logical phases when this materially
  improves navigation and debugging.
- Do not narrate obvious syntax, comment every line, add decorative banners,
  or leave dead code commented out.
- Public APIs and normative kernels require concise contract comments and a
  link to the relevant specification clause.
- `TODO` and `FIXME` comments require a tracked issue or decision identifier
  and a removal gate.
- Comment drift is a defect: behavior and comments change in the same commit.
- Structured debug traces must be deterministic, optional, and absent from the
  real-time hot path by default.

## Validation

After a change, verify:

1. relative links and Markdown structure;
2. terminology, formulae, and numerical targets;
3. the separation of facts, targets, hypotheses, and measured results;
4. primary-source support for external technical claims;
5. absence of secrets, unnecessary personal data, and undocumented external
   dependencies;
6. zero Cyrillic text in tracked public files;
7. relevant tests, conformance hashes, and cross-platform build checks;
8. source comments satisfy the signal-to-noise and debug-readability contract.
