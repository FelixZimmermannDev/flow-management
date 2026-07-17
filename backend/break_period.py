from datetime import datetime

from backend.work_period import (
    EndBeforeStartError,
    PeriodAlreadyEndedError,
)

class BreakPeriod:

    def __init__(self, start_time: datetime):
        self.start_time = start_time
        self.end_time: datetime | None = None

    def set_end(self, end_time: datetime) -> None:
        if self.end_time is not None:
            raise PeriodAlreadyEndedError()

        if end_time < self.start_time:
            raise EndBeforeStartError()

        self.end_time = end_time
