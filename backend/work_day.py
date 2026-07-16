from backend.work_session import WorkPeriod
from datetime import datetime

class WorkDay:

    def __init__(self, date: datetime):
        self.date = date

        self.work_periods = []
        self.break_periods = []

    def add_work_period(self, work_period: WorkPeriod):
        self.work_periods.append(work_period)
        #The Object WorkPeriod is later given right, therefore add doesnt need to bind via work = WorkPeriod(start_time) for now or does it???
