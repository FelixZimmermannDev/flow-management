# Flow Management Architecture

This document records durable architecture direction and project-specific code-quality guidance. The architecture is still evolving; implemented behavior, intended direction, and open decisions are separated below.

## Project purpose

Flow Management is a local Python application for tracking work time as work days, work sessions, work periods, and break periods. Domain behavior is developed before interfaces and persistence.

## Currently implemented domain model

- `WorkPeriod` and `BreakPeriod` store a start time and an optional end time. They reject a second end and an end before the start.
- `WorkSession` starts with an active `WorkPeriod` and owns its work periods and break periods.
- `WorkSession.start_break()` and `WorkSession.resume_work()` close the active period, create the next period, store it, and make it active.
- `WorkSession.set_end()` closes the active period, records the session end, and clears the active period.
- `WorkDay` stores a date and its work sessions. `start_session()` creates, stores, and returns a session while rejecting a second active session. `end_session()` finds the active session, delegates its state transition to `WorkSession.set_end()`, and returns the same session object.
- `FlowManager` is currently a placeholder without implemented coordination behavior.

## Agreed architecture direction

These decisions describe the intended direction but are not all implemented yet:

```text
FlowManager
└── selects or coordinates WorkDay objects
    └── owns WorkSession objects
        ├── owns WorkPeriod objects
        └── owns BreakPeriod objects
```

- `WorkSession` owns session-level state transitions; ending it changes the same in-memory object held by its `WorkDay`.
- `WorkDay` owns the sessions belonging to its date. It does not observe the clock or detect calendar changes itself.
- `FlowManager` will coordinate the appropriate `WorkDay` when date-based application flow is introduced.
- Terminal and desktop interfaces depend on the domain layer rather than containing domain rules.
- SQLite persistence will be introduced only after the in-memory domain workflow is stable.

## Project-specific code-quality heuristics

Use these as proportional heuristics, not absolute rules:

- Prefer precise domain names and explicit state transitions over clever or implicit behavior.
- Keep mutation and invalid states visible, especially when active periods and sessions change.
- Keep each class focused on one coherent responsibility, but do not split code merely because it has grown by a few lines.
- Accept small duplication until the shared concept is stable; do not create an abstraction only to satisfy DRY.
- Preserve comments that explain reasons, constraints, or unresolved domain decisions; avoid comments that merely narrate syntax.
- Make the smallest behavior-preserving change and avoid unrelated cleanup.

## Open architecture decisions

Do not treat these as settled without Felix's decision:

- How should sessions that cross midnight be assigned to work days?
- What exact public operations should `FlowManager` expose?
- When and how should SQLite entities relate `WorkDay`, `WorkSession`, and periods?

## Maintenance rule

Update this document only when implemented architecture or an explicitly confirmed durable decision makes it incomplete or incorrect. Temporary task progress belongs in the Pi session or a handover, and detailed feature behavior belongs in tests and code.
