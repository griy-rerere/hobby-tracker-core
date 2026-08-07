from typing import Iterable

from hobby_tracker.domain import Hobby
from hobby_tracker.ports import HobbyRepository


class GetAllHobbies:
    _repository: HobbyRepository

    def __init__(self, repository: HobbyRepository) -> None:
        self._repository = repository

    def __call__(self) -> Iterable[Hobby]:
        return self._repository.get_all()
