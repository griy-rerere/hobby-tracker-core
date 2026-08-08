from uuid import UUID

from hobby_tracker.domain import Activity
from hobby_tracker.ports import ActivityRepository


class GetActivity:
    _repository: ActivityRepository

    def __init__(self, repository: ActivityRepository) -> None:
        self._repository = repository

    def __call__(self, uuid: UUID) -> Activity:
        return self._repository.get(uuid)
