from datetime import datetime

from backend.exceptions import EndBeforeStartError, PeriodAlreadyEndedError


class Period:
    def __init__(self, start_time: datetime) -> None:
        self.start_time = start_time
        self.end_time: datetime | None = None

    def set_end(self, end_time: datetime) -> None:
        if self.end_time is not None:
            raise PeriodAlreadyEndedError()

        if end_time < self.start_time:
            raise EndBeforeStartError()

        self.end_time = end_time


class WorkPeriod(Period):
    pass


class BreakPeriod(Period):
    pass
