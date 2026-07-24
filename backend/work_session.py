from datetime import datetime

from backend.time_period import BreakPeriod, WorkPeriod

class SessionStateError(Exception):
    pass

class SessionAlreadyEndedError(SessionStateError):
    def __init__(self) -> None:
        super().__init__("Session has already ended")

class WorkSession:

    def __init__(self, start_time: datetime) -> None:
        first_work_period = WorkPeriod(start_time)

        self.start_time = start_time
        self.end_time: datetime | None = None

        self.work_periods: list[WorkPeriod] = [first_work_period]
        self.break_periods: list[BreakPeriod] = []

        self.active_period: WorkPeriod | BreakPeriod | None = first_work_period

    # Break
    def start_break(self, break_start_time: datetime) -> None:
        if not isinstance(self.active_period, WorkPeriod):
            raise SessionStateError("A break can only start while working")

        self.active_period.set_end(break_start_time)

        new_break_period = BreakPeriod(break_start_time)
        self.break_periods.append(new_break_period)

        self.active_period = new_break_period

    # Work
    def resume_work(self, work_start_time: datetime) -> None:
        if not isinstance(self.active_period, BreakPeriod):
            raise SessionStateError("Work can only resume during a break")

        self.active_period.set_end(work_start_time)

        new_work_period = WorkPeriod(work_start_time)
        self.work_periods.append(new_work_period)

        self.active_period = new_work_period

    # Helpers
    def set_end(self, end_time: datetime) -> None:
        if self.end_time is not None:
            raise SessionAlreadyEndedError()

        if self.active_period is None:
            raise SessionStateError("Session has no active period")

        final_period = self.active_period
        final_period.set_end(end_time)

        self.end_time = end_time
        self.active_period = None

