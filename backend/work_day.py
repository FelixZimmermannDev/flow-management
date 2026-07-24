from datetime import date, datetime

from backend.work_session import WorkSession


class WorkDayStateError(Exception):
    pass


class ActiveSessionAlreadyExistsError(WorkDayStateError):
    def __init__(self) -> None:
        super().__init__("An active session already exists")

class NoActiveSession(WorkDayStateError):
    def __init__(self) -> None:
        super().__init__("No active session exists")

class WorkDay:

    def __init__(self, day: date) -> None:
        self.day = day
        self.work_sessions: list[WorkSession] = []

    def start_session(self, start_time: datetime) -> WorkSession:
        for session in self.work_sessions:
            if session.end_time is None:
                raise ActiveSessionAlreadyExistsError()

        session = WorkSession(start_time)
        self.work_sessions.append(session)
        return session

    def end_session(self, end_time: datetime) -> WorkSession:
        for session in self.work_sessions:
            if session.end_time is None:
                session.set_end(end_time)
                return session

        raise NoActiveSession()
