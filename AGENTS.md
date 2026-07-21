# Flow Management Project Instructions

## Project direction

- Treat this repository as a learning project for building a local work-time tracking application.
- Keep domain behavior independent of terminal UI, desktop UI, and persistence concerns.
- Build the terminal UI before the desktop UI, and add SQLite only after the domain workflow is stable.
- Treat `README.md` as project direction, but verify current behavior in code and tests.

## Context loading

- Before changing or evaluating architecture, module boundaries, state ownership, responsibilities, dependencies, or significant refactorings, read `docs/architecture.md`.
- For Clean Code teaching, code-quality reviews, or behavior-preserving refactoring, load the global `clean-code-coach` skill and apply the project-specific heuristics in `docs/architecture.md`.
- Do not load detailed architecture context for unrelated questions or narrowly scoped syntax work.

## Development boundaries

- Work on one externally visible domain behavior at a time and use the guided workflow from the global `AGENTS.md`.
- Use `pytest` for focused behavior tests.
- Do not treat planned classes, empty files, or documentation as proof that behavior is implemented.

## Context maintenance

- Use `/update-context` to review durable project context after a meaningful change or decision and for a final consistency audit when the project is completed.
- Maintain context as current truth, not an append-only history: correct, replace, consolidate, or remove stale statements instead of continually adding notes.
- Do not store temporary task status, session handovers, speculative designs, or details already clear from code in this file.
