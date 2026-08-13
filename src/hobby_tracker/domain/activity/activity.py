from uuid import UUID

from .duration import ActivityDuration
from .note import ActivityNote
from .start import ActivityStart


class Activity:
    def __init__(
        self,
        *,
        id: UUID,
        hobby_id: UUID,
        duration: ActivityDuration,
        started_at: ActivityStart | None = None,
        note: ActivityNote | None = None,
    ) -> None:
        self._id = id
        self._hobby_id = hobby_id
        self._duration = duration
        self._started_at = started_at if started_at is not None else ActivityStart()
        self._note = note

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def hobby_id(self) -> UUID:
        return self._hobby_id

    @property
    def duration(self) -> ActivityDuration:
        return self._duration

    @property
    def started_at(self) -> ActivityStart:
        return self._started_at

    @property
    def note(self) -> ActivityNote | None:
        return self._note

    def change_start(self, new_start: ActivityStart) -> None:
        self._started_at = new_start

    def change_duration(self, new_duration: ActivityDuration) -> None:
        self._duration = new_duration

    def set_note(self, note: ActivityNote) -> None:
        self._note = note

    def delete_note(self) -> None:
        self._note = None
