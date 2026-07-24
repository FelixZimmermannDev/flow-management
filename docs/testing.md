# Flow Management Testing

This document defines the project's testing responsibilities, test levels, workflow, and correction rules. It is the source of truth for deciding whether tests add value and for designing, writing, running, or reviewing tests.

Detailed feature behavior belongs in production code and tests, not in this document.

## Responsibilities

Felix defines and reviews intended behavior in plain language. He is not required to write or validate `pytest` syntax.

The agent is responsible for:

- deciding whether the behavior is test-worthy;
- translating the agreed behavior into a plain-language test plan;
- checking that the plan tests the feature rather than merely copying the implementation;
- writing and running the test code;
- reporting what was covered, what was omitted, and what passed or failed.

A product or architecture decision that cannot be derived technically remains Felix's decision.

## Three-phase testing workflow

### 1. Define what should be tested

Inspect the implemented behavior, relevant surrounding code, and existing tests. Describe the behavior contract in this review format:

1. Main task of the function
2. Normal case + expected result
3. Edge case + expected result
4. What must remain unchanged

Clarify unresolved product decisions before encoding an expected result in a test.

### 2. Review the planned coverage

Before writing test code:

- decide whether tests add meaningful protection;
- map each relevant part of the behavior contract to a planned test;
- include important state changes, return values, exceptions, and unchanged state;
- check existing tests to avoid unnecessary duplication;
- present the planned cases to Felix in plain language so he can verify the intended feature behavior without reading test syntax.

If a test would add no meaningful protection, explain why and do not create one merely for coverage.

### 3. Write and verify the tests

The agent writes focused `pytest` tests using the standards below, then runs:

1. the narrowest relevant test file or test selection;
2. the full test suite when practical.

For a critical state transition or regression, verify test sensitivity when practical by confirming that a small temporary fault makes the relevant test fail. Restore the production code immediately and rerun the focused and full tests.

Report the tested behavior, commands, results, omissions, and remaining risks in plain language.

## Test levels

### Level 0: Behavior contract

Always use the four-part behavior contract for test-worthy domain behavior. The statements must be atomic and have an unambiguous expected result.

### Level 1: Focused domain behavior

This is the default executable level during the current pure-domain phase. Test one public domain operation and its externally visible result, including the relevant normal case, invalid case, and unchanged state.

### Level 2: Domain workflow

Use selectively when several stable operations must cooperate, for example starting a session, taking a break, resuming work, and ending the session. These tests complement focused tests rather than replacing them.

### Level 3: Adapter integration

Introduce when terminal UI or SQLite adapters exist. Test that an adapter calls the domain correctly or that persistence stores and restores the required state. Prefer a real temporary SQLite database over extensive persistence mocks.

### Level 4: End-to-end workflow

Introduce only when the interfaces and persistence workflow are stable. Exercise a complete user workflow through the real application boundary. Keep these tests fewer because they are slower and harder to diagnose.

For the current project phase, Levels 0 and 1 are the default; Level 2 is selective. Levels 3 and 4 are deferred.

## When tests add value

Tests normally add value for:

- domain rules and calculations;
- state transitions and mutations;
- invalid operations and exception behavior;
- regressions and bug fixes;
- cooperation between domain objects.

Tests normally do not add value for empty placeholders, documentation-only changes, formatting, or behavior-free scaffolding.

## Test quality standards

- Test externally visible behavior through public APIs, not private helpers or implementation steps.
- Give each test one clear behavioral purpose and a descriptive name.
- Use deterministic inputs such as fixed dates and times.
- Verify the exact relevant exception type.
- For rejected mutations, verify that important prior state remains unchanged.
- Verify object identity or collection contents when preserving the same domain object is part of the behavior.
- Keep tests independent; one test must not depend on another test having run first.
- Avoid mocks for the current pure domain model unless a real external boundary requires one.
- Do not add cases solely to maximize a coverage percentage. Coverage can reveal unexecuted code but cannot prove correct behavior.
- Automatically cover obvious technical edge cases, but never invent a product expectation when multiple outcomes are valid.

## Testing modes

### Default: Test-after

The current learning workflow is:

```text
agree on behavior
→ implement
→ understand the implementation
→ plan tests in plain language
→ write and run tests
```

### Optional: TDD

Use test-driven development only when Felix explicitly requests it:

```text
agree on behavior
→ write a focused test
→ confirm the expected failure
→ implement
→ rerun tests
```

### Bug fixes

For a bug fix, add a reproducing regression test before the correction when practical. This proves that the test observes the bug and that the production change fixes it; it does not change the default feature workflow to TDD.

## Correction rules

- The agreed behavior contract is authoritative; do not derive the expected result solely from current code.
- Never weaken, delete, or skip a valid test merely to obtain a passing result.
- When a valid test fails, correct production code.
- If the expected behavior or quality check appears wrong, classify the discrepancy before changing anything:
  - `SPEC`: the agreed requirement is missing, ambiguous, or incorrect;
  - `CODE`: production code violates a valid requirement;
  - `CHECKER`: a test or static check encodes the wrong rule;
  - `HARNESS`: test discovery, setup, environment, or execution is faulty.
- Document intentional checker exceptions rather than distorting production code to satisfy a false positive.
- Do not claim that behavior works without reporting the command that verified it.

## Result report

After testing, report:

```text
Behavior reviewed:
- ...

Tests added or changed:
- contract item → test case

Verification:
- command → result

Not covered or still open:
- ...
```

## Maintenance

Update this document only when the durable testing workflow, active test levels, responsibilities, or correction rules change. Do not record temporary test status, individual feature cases, session history, or details already clear from tests.
