from datetime import datetime

class WorkPeriod:

    def __init__(self, start_time: datetime):
        self.start_time = start_time
        self.end_time = None
