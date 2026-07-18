from datetime import datetime

from backend.work_period import WorkPeriod
from backend.break_period import BreakPeriod

class WorkSession:

    def __init__(self, start_time: datetime):
        first_work_period = WorkPeriod(start_time)

        self.work_periods = []
        self.break_periods = []

