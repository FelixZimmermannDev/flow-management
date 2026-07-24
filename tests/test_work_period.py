from datetime import datetime

import pytest

from backend.exceptions import EndBeforeStartError, PeriodAlreadyEndedError
from backend.time_period import WorkPeriod


def test_work_period_starts_open_at_given_time():
    start_time = datetime(2026, 7, 20, 9, 0)

    period = WorkPeriod(start_time)

    assert period.start_time == start_time
    assert period.end_time is None


def test_set_end_ends_open_work_period_at_given_time():
    period = WorkPeriod(datetime(2026, 7, 20, 9, 0))
    end_time = datetime(2026, 7, 20, 10, 0)

    period.set_end(end_time)

    assert period.end_time == end_time


def test_set_end_allows_end_time_equal_to_start_time():
    start_time = datetime(2026, 7, 20, 9, 0)
    period = WorkPeriod(start_time)

    period.set_end(start_time)

    assert period.end_time == start_time


def test_set_end_rejects_time_before_start_and_keeps_period_open():
    period = WorkPeriod(datetime(2026, 7, 20, 9, 0))

    with pytest.raises(EndBeforeStartError):
        period.set_end(datetime(2026, 7, 20, 8, 59))

    assert period.end_time is None


def test_set_end_rejects_second_end_and_keeps_original_end_time():
    period = WorkPeriod(datetime(2026, 7, 20, 9, 0))
    original_end_time = datetime(2026, 7, 20, 10, 0)
    period.set_end(original_end_time)

    with pytest.raises(PeriodAlreadyEndedError):
        period.set_end(datetime(2026, 7, 20, 11, 0))

    assert period.end_time == original_end_time
