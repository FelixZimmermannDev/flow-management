from datetime import date

from backend.work_day import WorkDay


def test_work_day_starts_for_given_day_without_sessions():
    day = date(2026, 7, 20)

    work_day = WorkDay(day)

    assert work_day.day == day
    assert work_day.work_sessions == []
