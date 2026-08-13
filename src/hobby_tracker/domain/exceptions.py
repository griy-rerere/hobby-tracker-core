class HobbyTrackerException(Exception):
    pass


class HobbyNotFound(HobbyTrackerException):
    pass


class HobbyAttributeDuplicate(HobbyTrackerException):
    pass


class HobbyDeleteError(HobbyTrackerException):
    pass


class ActivityNotFound(HobbyTrackerException):
    pass


class ActivityAttributeDuplicate(HobbyTrackerException):
    pass


class ActivityDeleteError(HobbyTrackerException):
    pass
