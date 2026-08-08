from hobby_tracker.domain import ActivityStatistics
from hobby_tracker.ports import ActivityRepository
from hobby_tracker.queries import ActivityStatisticsQuery


class GetActivityStatistics:
    _repository: ActivityRepository

    def __init__(self, repository: ActivityRepository) -> None:
        self._repository = repository

    def __call__(self, query: ActivityStatisticsQuery) -> ActivityStatistics:
        return self._repository.calculate_statistics(query)
