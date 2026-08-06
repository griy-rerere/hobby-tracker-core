from hobby_tracker.application.requests import CreateHobbyRequest
from hobby_tracker.domain import Hobby
from hobby_tracker.ports import HobbyRepository


class CreateHobby:
    _repository: HobbyRepository

    def __init__(self, repository: HobbyRepository) -> None:
        self._repository = repository

    def __call__(self, request: CreateHobbyRequest) -> Hobby:
        hobby = Hobby(name=request.name)
        self._repository.save(hobby)
        return hobby
