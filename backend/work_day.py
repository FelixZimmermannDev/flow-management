from datetime import date, datetime

from backend.exceptions import ActiveSessionAlreadyExistsError, NoActiveSessionError
from backend.work_session import WorkSession


class WorkDay:

    def __init__(self, day: date) -> None:
        self.day = day
        self.work_sessions: list[WorkSession] = []

    def start_session(self, start_time: datetime) -> WorkSession:
        active_session_exists = False

        for stored_session in self.work_sessions:
            if stored_session.end_time is None:
                active_session_exists = True
                break

        if active_session_exists:
            raise ActiveSessionAlreadyExistsError()

        new_session = WorkSession(start_time)
        self.work_sessions.append(new_session)
        return new_session

    def end_session(self, end_time: datetime) -> WorkSession:
        active_session = None

        for stored_session in self.work_sessions:
            if stored_session.end_time is None:
                active_session = stored_session
                break

        if active_session is None:
            raise NoActiveSessionError()

        active_session.set_end(end_time)
        return active_session

    def start_break(self, start_time: datetime) -> WorkSession:
        active_session: WorkSession | None = None

        for stored_session in self.work_sessions:
            if stored_session.end_time is None:
                active_session = stored_session
                break

        if active_session is None:
            raise NoActiveSessionError()

        active_session.start_break(start_time)
        return active_session
