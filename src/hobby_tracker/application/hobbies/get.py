from uuid import UUID

from hobby_tracker.domain import Hobby
from hobby_tracker.ports import HobbyRepository


class GetHobby:
    _repository: HobbyRepository

    def __init__(self, repository: HobbyRepository) -> None:
        self._repository = repository

    def __call__(self, uuid: UUID) -> Hobby:
        return self._repository.get(uuid)
