from datetime import timedelta

from hobby_tracker.application.requests import GetHobbyDurationRequest
from hobby_tracker.ports import ActivityEntryRepository


class GetHobbyDuration:
    _repository: ActivityEntryRepository

    def __init__(self, repository: ActivityEntryRepository) -> None:
        self._repository = repository

    def __call__(self, request: GetHobbyDurationRequest) -> timedelta:
        return self._repository.get_hobby_sum(request.hobby_id, request.date_range)
