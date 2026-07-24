# Flow Management Project Instructions

## Project direction

- Treat this repository as a learning project for building a local work-time tracking application.
- Keep domain behavior independent of terminal UI, desktop UI, and persistence concerns.
- Build the terminal UI before the desktop UI, and add SQLite only after the domain workflow is stable.
- Treat `README.md` as project direction, but verify current behavior in code and tests.

## Context loading

- Before changing or evaluating architecture, module boundaries, state ownership, responsibilities, dependencies, or significant refactorings, read `docs/architecture.md`.
- Before deciding whether tests add value or designing, writing, reviewing, running, or changing tests or test infrastructure, read `docs/testing.md`.
- For Clean Code explanation, code-quality review, or behavior-preserving refactoring, load the global `clean-code-coach` skill and apply the project-specific heuristics in `docs/architecture.md`.
- Do not load detailed architecture or testing context for unrelated questions or narrowly scoped syntax work.

## Project learning workflow

- This project specializes the global guided workflow for Flow Management; use the more specific rules below when they differ.
- Work on one externally visible domain behavior at a time. Prioritize translating ideas into explicit behavior, state changes, responsibilities, and design decisions over practicing Python syntax in isolation.
- When adding or changing a class, keep it focused on one coherent domain responsibility. Separate genuinely different reasons to change, but do not add abstractions without a concrete need.
- Begin with Felix's feature idea in plain language: what should become possible, what triggers it, and what should visibly change.
- Before implementation, clarify the required inputs, state read, state changed or returned, invalid situations, and what must remain unchanged.
- When materially useful alternatives exist, present their main trade-offs and recommend one proportional default.
- Choose implementation involvement by learning value: Felix contributes the behavior model for new core domain behavior; the agent may implement boilerplate, familiar patterns, or a complete translation of the agreed model.
- For learning-zone domain code, prefer explicit step-by-step control flow and descriptive intermediate variables over compact expressions when this materially improves traceability; avoid verbosity that only repeats the syntax.
- After implementation, verify understanding with one proportionate active check. Do not turn routine work into a quiz.
- Use type annotations on public domain APIs and keep mutation of inputs and domain state explicit.

## Context maintenance

- Use `/update-context` to review durable project context after a meaningful change or decision and for a final consistency audit when the project is completed.
- `/update-context` maintains persistent project guidance and architecture; it is not conversation summarization or context-window compaction. Use Pi's `/compact` for the current conversation.
- Maintain context as current truth, not an append-only history: correct, replace, consolidate, or remove stale statements instead of continually adding notes.
- Do not store temporary task status, session handovers, speculative designs, or details already clear from code in this file.
