from datetime import date, datetime

import pytest

from backend.time_period import EndBeforeStartError
from backend.work_day import ActiveSessionAlreadyExistsError, NoActiveSession, WorkDay
from backend.work_session import WorkSession


def test_start_session_creates_stores_and_returns_work_session():
    work_day = WorkDay(date(2026, 7, 20))
    start_time = datetime(2026, 7, 20, 9, 0)

    session = work_day.start_session(start_time)

    assert isinstance(session, WorkSession)
    assert session.start_time == start_time
    assert work_day.work_sessions == [session]


def test_start_session_rejects_second_active_session_and_keeps_existing_session():
    work_day = WorkDay(date(2026, 7, 20))
    existing_session = work_day.start_session(datetime(2026, 7, 20, 9, 0))
    original_active_period = existing_session.active_period

    with pytest.raises(ActiveSessionAlreadyExistsError):
        work_day.start_session(datetime(2026, 7, 20, 10, 0))

    assert work_day.work_sessions == [existing_session]
    assert existing_session.end_time is None
    assert existing_session.active_period is original_active_period


def test_end_session_ends_active_session_and_returns_it():
    work_day = WorkDay(date(2026, 7, 20))
    session = work_day.start_session(datetime(2026, 7, 20, 9, 0))
    original_active_period = session.active_period
    end_time = datetime(2026, 7, 20, 17, 0)

    ended_session = work_day.end_session(end_time)

    assert ended_session is session
    assert session.end_time == end_time
    assert original_active_period is not None
    assert original_active_period.end_time == end_time
    assert session.active_period is None
    assert work_day.work_sessions == [session]


def test_end_session_rejects_missing_active_session_and_keeps_work_day_empty():
    work_day = WorkDay(date(2026, 7, 20))

    with pytest.raises(NoActiveSession):
        work_day.end_session(datetime(2026, 7, 20, 17, 0))

    assert work_day.work_sessions == []


def test_end_session_rejects_end_before_start_and_keeps_session_active():
    work_day = WorkDay(date(2026, 7, 20))
    session = work_day.start_session(datetime(2026, 7, 20, 9, 0))
    original_active_period = session.active_period

    with pytest.raises(EndBeforeStartError):
        work_day.end_session(datetime(2026, 7, 20, 8, 59))

    assert work_day.work_sessions == [session]
    assert session.end_time is None
    assert session.active_period is original_active_period
    assert original_active_period is not None
    assert original_active_period.end_time is None
