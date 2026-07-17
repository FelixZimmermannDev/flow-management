from datetime import datetime

class PeriodError(Exception):
    pass


class PeriodAlreadyEndedError(PeriodError):
    pass


class EndBeforeStartError(PeriodError):
    pass


class WorkPeriod:

    def __init__(self, start_time: datetime):
        self.start_time = start_time
        self.end_time = None
