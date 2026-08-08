from typing import Iterable

from hobby_tracker.domain import Activity
from hobby_tracker.ports import ActivityRepository
from hobby_tracker.queries import ActivityQuery


class GetActivities:
    _repository: ActivityRepository

    def __init__(self, repository: ActivityRepository) -> None:
        self._repository = repository

    def __call__(self, query: ActivityQuery) -> Iterable[Activity]:
        return self._repository.get_many(query)
