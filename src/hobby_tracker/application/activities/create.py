from datetime import datetime, timezone

from hobby_tracker.application.requests import CreateActivityRequest
from hobby_tracker.domain import Activity
from hobby_tracker.ports import ActivityRepository


class CreateActivity:
    _repository: ActivityRepository

    def __init__(self, repository: ActivityRepository) -> None:
        self._repository = repository

    def __call__(self, request: CreateActivityRequest) -> Activity:
        started_at = (
            datetime.now(timezone.utc)
            if request.started_at is None
            else request.started_at
        )

        entry = Activity(
            hobby_id=request.hobby_id,
            duration=request.duration,
            started_at=started_at,
            note=request.note,
        )

        self._repository.save(entry)
        return entry
