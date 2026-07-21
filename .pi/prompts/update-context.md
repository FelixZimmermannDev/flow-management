---
description: Review and update durable project context only when current evidence requires it
argument-hint: "[scope]"
---
# Flow Management Context Maintenance

Review whether durable project context must change after completed work or an explicitly confirmed decision. Requested scope, if supplied: ${ARGUMENTS:-the current work and relevant uncommitted changes}

## Core rule

Maintain project context as a concise representation of current truth, not as an append-only history or changelog. Update existing statements in place, replace obsolete direction, remove stale information, and consolidate repetition. If the inspected evidence contains no durable change, make no context edit.

## Allowed context files

- `AGENTS.md` for stable project-specific instructions about how the agent should work;
- `docs/architecture.md` for implemented architecture, confirmed direction, project-specific code-quality guidance, and clearly labelled open decisions;
- `README.md` only when the durable project direction or documented workflow actually changed.

Never edit the global `~/.pi/agent/AGENTS.md` from this command.

## Review process

1. Inspect the relevant Git diff, current code, tests, existing context files, and established decisions before proposing a context change.
2. Classify each possible update:
   - stable project-wide agent instruction -> `AGENTS.md`;
   - implemented architecture or explicitly confirmed durable architecture decision -> `docs/architecture.md`;
   - durable project purpose or workflow change -> `README.md`;
   - feature behavior -> code and tests, not persistent context;
   - temporary task status, session history, or tentative idea -> no persistent context update.
3. Ask before recording an unresolved product or architecture choice. Do not turn an inference into a decision.
4. Update context only when an existing statement became false, a durable omission would mislead future work, or Felix explicitly confirmed a reusable rule or decision.
5. Revise the existing context rather than merely adding another statement. Remove superseded plans, resolved open questions, outdated constraints, and duplicated guidance.
6. At meaningful milestones and project completion, perform a final consistency audit so the remaining context describes the finished or current project rather than its development history.

## Strong limits

- Do not generate a broad repository summary or restate information that is easy to discover from code.
- Do not add file inventories, current task lists, handover content, transient Git state, speculative designs, or generic advice already covered by the global `AGENTS.md` or the `clean-code-coach` skill.
- Keep `AGENTS.md` concise. Put detailed durable architecture in `docs/architecture.md` and load it only for relevant work.
- Modify only the allowed context files. Do not change production code, tests, dependencies, configuration, or external state.
- Make the smallest coherent documentation edit. Preserve useful context that remains true, but keep the total context clean and proportionate. If no durable update is justified, change nothing and say why.

## Result

Report:

- which evidence was inspected;
- whether context changed;
- exact files changed and the durable reason for each change;
- uncertain items deliberately not recorded.
