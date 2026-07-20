from datetime import datetime

from backend.break_period import BreakPeriod
from backend.work_period import (
    WorkPeriod,
    EndBeforeStartError,
    PeriodAlreadyEndedError,
)

class SessionStateError(Exception):
    def __init__(self):
        super().__init__("A break can only start while working.")

class WorkSession:

    def __init__(self, start_time):
        first_work_period = WorkPeriod(start_time)

        self.start_time = start_time
        self.end_time: datetime | None = None

        self.work_periods = [first_work_period]
        self.break_periods = []

        self.active_period: WorkPeriod | BreakPeriod | None = None

    #Break
    def start_break(self, break_start_time: datetime) -> None:
        if not isinstance(self.active_period, WorkPeriod): #Is WorkPeriod stored in self.active_period?
            raise SessionStateError()

        self.active_period.set_end(break_start_time)

        new_break_period = BreakPeriod(break_start_time)
        self.break_periods.append(new_break_period)

        self.active_period = new_break_period

    #Work
    def resume_work(self, start_time: datetime):
        if not isinstance(self.active_period, BreakPeriod):
            raise SessionStateError()

        self.active_period.set_end(start_time)

        new_work_period = WorkPeriod(start_time)
        self.work_periods.append(new_work_period)

        self.active_period = new_work_period

    #Helpers
    def set_end(self, end_time: datetime) -> None:
        if self.end_time is not None:
            raise PeriodAlreadyEndedError()

        if end_time < self.start_time:
            raise EndBeforeStartError()

        self.end_time = end_time
