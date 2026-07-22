from datetime import datetime

from backend.time_period import BreakPeriod, WorkPeriod
from backend.work_session import WorkSession


def test_work_session_starts_with_active_work_period():
    session = WorkSession(datetime(2026, 7, 20, 9, 0))

    assert isinstance(session.active_period, WorkPeriod)
    assert session.work_periods == [session.active_period]
    assert session.break_periods == []


def test_start_break_replaces_active_work_period_with_break_period():
    session = WorkSession(datetime(2026, 7, 20, 9, 0))
    original_work_period = session.active_period
    break_start_time = datetime(2026, 7, 20, 10, 0)

    session.start_break(break_start_time)

    assert original_work_period is not None
    assert original_work_period.end_time == break_start_time
    assert isinstance(session.active_period, BreakPeriod)
    assert session.break_periods == [session.active_period]


def test_resume_work_replaces_active_break_period_with_work_period():
    session = WorkSession(datetime(2026, 7, 20, 9, 0))
    session.start_break(datetime(2026, 7, 20, 10, 0))
    original_break_period = session.active_period
    work_start_time = datetime(2026, 7, 20, 10, 15)

    session.resume_work(work_start_time)

    assert original_break_period is not None
    assert original_break_period.end_time == work_start_time
    assert isinstance(session.active_period, WorkPeriod)
    assert session.work_periods == [session.work_periods[0], session.active_period]
