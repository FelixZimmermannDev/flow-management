from backend.work_period import WorkPeriod
from datetime import date

class WorkDay:

    def __init__(self, day: date):
        self.day = day

        self.work_periods = []
        self.break_periods = []

    def add_work_period(self, work_period: WorkPeriod):
        self.work_periods.append(work_period)
        #The Object WorkPeriod is later given right, therefore add doesnt need to bind via work = WorkPeriod(start_time) for now or does it???
