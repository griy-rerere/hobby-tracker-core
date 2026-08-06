from datetime import datetime, timezone

from hobby_tracker.application.requests import AddActivityEntryRequest
from hobby_tracker.domain import ActivityEntry
from hobby_tracker.ports import ActivityEntryRepository


class AddActivityEntry:
    _repository: ActivityEntryRepository

    def __init__(self, repository: ActivityEntryRepository) -> None:
        self._repository = repository

    def __call__(self, request: AddActivityEntryRequest) -> ActivityEntry:
        started_at = (
            datetime.now(timezone.utc)
            if request.started_at is None
            else request.started_at
        )

        entry = ActivityEntry(
            hobby_id=request.hobby_id,
            duration=request.duration,
            started_at=started_at,
            note=request.note,
        )

        self._repository.save(entry)
        return entry
