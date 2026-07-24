# Flow Management Project Instructions

## Project direction

- Treat this repository as a learning project for building a local work-time tracking application.
- Keep domain behavior independent of terminal UI, desktop UI, and persistence concerns.
- Build the terminal UI before the desktop UI, and add SQLite only after the domain workflow is stable.
- Treat `README.md` as project direction, but verify current behavior in code and tests.

## Context loading

- Before changing or evaluating architecture, module boundaries, state ownership, responsibilities, dependencies, or significant refactorings, read `docs/architecture.md`.
- For Clean Code explanation, code-quality review, or behavior-preserving refactoring, load the global `clean-code-coach` skill and apply the project-specific heuristics in `docs/architecture.md`.
- Do not load detailed architecture context for unrelated questions or narrowly scoped syntax work.

## Project learning workflow

- This project specializes the global guided workflow for Flow Management; use the more specific rules below when they differ.
- Work on one externally visible domain behavior at a time. Prioritize translating ideas into explicit behavior, state changes, responsibilities, and design decisions over practicing Python syntax in isolation.
- When adding or changing a class, keep it focused on one coherent domain responsibility. Treat SRP as a heuristic: separate genuinely different reasons to change, but do not create extra classes or abstractions without a concrete need.
- Begin with Felix's feature idea in plain language: what should become possible, what triggers it, and what should visibly change.
- Before tests or implementation, clarify the required inputs, state read, state changed or result returned, invalid situations, and what must remain unchanged.
- When a decision has multiple materially useful solutions, present only the relevant alternatives, their main trade-offs, and one recommended default for this project. Do not manufacture alternatives for routine details.
- Use the review format as a behavior contract before implementation:
  1. Main task of the function
  2. Normal case + expected result
  3. Edge case + expected result
  4. What must remain unchanged
- This project uses a test-after workflow rather than test-driven development: agree on the behavior contract, implement the behavior, review and understand the implementation, and then write tests when they add value.
- Choose the implementation mode by learning value:
  - For boilerplate, UI/framework integration, configuration, repetitive work, and familiar patterns, the agent implements directly.
  - For new core domain behavior, Felix actively contributes the behavior model, conditions, pseudocode, comments, or a small skeleton; the agent may then translate it into complete code.
  - Use occasional small first-hand implementations as deliberate practice, not as the default requirement for every domain function.
  - If Felix is blocked or overwhelmed, the agent may provide the complete implementation and explain its decisive parts without exhausting a fixed hint ladder.
- After implementation, verify understanding actively with one proportionate step: explain a state transition, predict an outcome, make a small change, add an edge case, or debug a bounded fault. Do not turn routine work into a quiz.
- The agent then writes focused `pytest` tests from the previously agreed behavior contract. Felix reviews whether they express the intended behavior rather than merely copying the implementation.
- Run focused tests after each coherent tested change and broader tests when practical. Do not treat planned classes, empty files, or documentation as proof that behavior is implemented.

## Quality correction boundary

- Treat agreed behavior, tests, and confirmed architecture decisions as constraints. Do not change an expected result merely to match the current implementation.
- When a valid test or quality check fails, correct production code. If a specification, test, or check appears wrong, explain the discrepancy and classify it as `SPEC`, `CODE`, `CHECKER`, or `HARNESS` before changing the responsible rule.
- Never weaken, delete, or skip a valid test or architecture rule merely to obtain a passing result.
- Use type annotations on public domain APIs and keep mutation of inputs and domain state explicit.

## Context maintenance

- Use `/update-context` to review durable project context after a meaningful change or decision and for a final consistency audit when the project is completed.
- `/update-context` maintains persistent project guidance and architecture; it is not conversation summarization or context-window compaction. Use Pi's `/compact` for the current conversation.
- Maintain context as current truth, not an append-only history: correct, replace, consolidate, or remove stale statements instead of continually adding notes.
- Do not store temporary task status, session handovers, speculative designs, or details already clear from code in this file.
