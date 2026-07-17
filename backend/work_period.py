from datetime import datetime

class PeriodError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class PeriodAlreadyEndedError(PeriodError):
    def __init__(self) -> None:
        super().__init__("Work period has already ended")


class EndBeforeStartError(PeriodError):
    def __init__(self) -> None:
        super().__init__("End time cannot be before start time")


class WorkPeriod:

    def __init__(self, start_time: datetime):
        self.start_time = start_time
        self.end_time: datetime | None = None

    def set_end(self, end_time: datetime) -> None:
        if self.end_time is not None:
            raise PeriodAlreadyEndedError()

        if end_time < self.start_time:
            raise EndBeforeStartError()

        self.end_time = end_time
