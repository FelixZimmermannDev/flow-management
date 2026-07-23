from datetime import date, datetime

import pytest

from backend.work_day import ActiveSessionAlreadyExistsError, WorkDay
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
