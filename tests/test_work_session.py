from datetime import datetime

import pytest

from backend.break_period import BreakPeriod
from backend.work_period import EndBeforeStartError, WorkPeriod
from backend.work_session import (
    SessionAlreadyEndedError,
    SessionStateError,
    WorkSession,
)


def at(hour: int, minute: int = 0) -> datetime:
    return datetime(2026, 7, 20, hour, minute)


def test_session_starts_with_one_active_work_period():
    session = WorkSession(at(9))

    assert session.start_time == at(9)
    assert session.end_time is None
    assert len(session.work_periods) == 1
    assert session.break_periods == []
    assert session.active_period is session.work_periods[0]
    assert session.active_period.start_time == at(9)
    assert session.active_period.end_time is None


def test_start_break_ends_work_period_and_starts_break():
    session = WorkSession(at(9))

    session.start_break(at(10))

    assert session.work_periods[0].end_time == at(10)
    assert len(session.break_periods) == 1
    assert session.active_period is session.break_periods[0]
    assert isinstance(session.active_period, BreakPeriod)
    assert session.active_period.start_time == at(10)
    assert session.active_period.end_time is None
    assert session.end_time is None


def test_resume_work_ends_break_and_starts_new_work_period():
    session = WorkSession(at(9))
    session.start_break(at(10))

    session.resume_work(at(10, 15))

    assert session.break_periods[0].end_time == at(10, 15)
    assert len(session.work_periods) == 2
    assert session.active_period is session.work_periods[1]
    assert isinstance(session.active_period, WorkPeriod)
    assert session.active_period.start_time == at(10, 15)
    assert session.active_period.end_time is None
    assert session.end_time is None


def test_set_end_while_working_ends_period_and_session():
    session = WorkSession(at(9))
    final_period = session.active_period

    session.set_end(at(11))

    assert final_period.end_time == at(11)
    assert session.end_time == at(11)
    assert session.active_period is None


def test_set_end_during_break_ends_break_and_session():
    session = WorkSession(at(9))
    session.start_break(at(10))
    final_break = session.active_period

    session.set_end(at(10, 15))

    assert final_break.end_time == at(10, 15)
    assert session.end_time == at(10, 15)
    assert session.active_period is None


def test_start_break_while_breaking_is_rejected_without_changing_session():
    session = WorkSession(at(9))
    session.start_break(at(10))
    active_break = session.active_period

    with pytest.raises(SessionStateError, match="only start while working"):
        session.start_break(at(10, 5))

    assert session.active_period is active_break
    assert active_break.end_time is None
    assert len(session.work_periods) == 1
    assert len(session.break_periods) == 1


def test_resume_work_while_working_is_rejected_without_changing_session():
    session = WorkSession(at(9))
    active_work_period = session.active_period

    with pytest.raises(SessionStateError, match="only resume during a break"):
        session.resume_work(at(10))

    assert session.active_period is active_work_period
    assert active_work_period.end_time is None
    assert len(session.work_periods) == 1
    assert session.break_periods == []


def test_set_end_rejects_ending_session_twice():
    session = WorkSession(at(9))
    session.set_end(at(10))

    with pytest.raises(SessionAlreadyEndedError, match="already ended"):
        session.set_end(at(11))

    assert session.end_time == at(10)
    assert session.active_period is None


@pytest.mark.parametrize("operation", ["start_break", "resume_work"])
def test_period_transitions_are_rejected_after_session_ends(operation):
    session = WorkSession(at(9))
    session.set_end(at(10))

    with pytest.raises(SessionStateError):
        getattr(session, operation)(at(11))

    assert session.end_time == at(10)
    assert session.active_period is None
    assert len(session.work_periods) == 1
    assert session.break_periods == []


def test_set_end_before_active_period_start_keeps_session_active():
    session = WorkSession(at(9))
    session.start_break(at(10))
    session.resume_work(at(10, 15))
    active_work_period = session.active_period

    with pytest.raises(EndBeforeStartError):
        session.set_end(at(10, 10))

    assert session.end_time is None
    assert session.active_period is active_work_period
    assert active_work_period.end_time is None


def test_session_allows_ending_at_active_period_start_time():
    session = WorkSession(at(9))

    session.set_end(at(9))

    assert session.work_periods[0].end_time == at(9)
    assert session.end_time == at(9)
    assert session.active_period is None
