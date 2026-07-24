class DomainError(Exception):
    pass


class PeriodError(DomainError):
    pass


class PeriodAlreadyEndedError(PeriodError):
    def __init__(self) -> None:
        super().__init__("Period has already ended")


class EndBeforeStartError(PeriodError):
    def __init__(self) -> None:
        super().__init__("End time cannot be before start time")


class SessionStateError(DomainError):
    pass


class SessionAlreadyEndedError(SessionStateError):
    def __init__(self) -> None:
        super().__init__("Session has already ended")


class CannotStartBreakError(SessionStateError):
    def __init__(self) -> None:
        super().__init__("A break can only start while working")


class CannotResumeWorkError(SessionStateError):
    def __init__(self) -> None:
        super().__init__("Work can only resume during a break")


class NoActivePeriodError(SessionStateError):
    def __init__(self) -> None:
        super().__init__("Session has no active period")


class WorkDayStateError(DomainError):
    pass


class ActiveSessionAlreadyExistsError(WorkDayStateError):
    def __init__(self) -> None:
        super().__init__("An active session already exists")


class NoActiveSessionError(WorkDayStateError):
    def __init__(self) -> None:
        super().__init__("No active session exists")
