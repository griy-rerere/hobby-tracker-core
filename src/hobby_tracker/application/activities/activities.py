from hobby_tracker.ports import ActivityRepository

from .create import CreateActivity
from .get import GetActivity
from .get_many import GetActivities
from .get_statistics import GetActivityStatistics


class Activities:
    def __init__(self, activity_repo: ActivityRepository) -> None:
        self.create = CreateActivity(activity_repo)
        self.get = GetActivity(activity_repo)
        self.get_many = GetActivities(activity_repo)
        self.get_statistics = GetActivityStatistics(activity_repo)
