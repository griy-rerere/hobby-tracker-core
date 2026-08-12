from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from hobby_tracker.domain.activity import (
    Activity,
    ActivityDuration,
    ActivityNote,
    ActivityRepository,
    ActivityStart,
)
from hobby_tracker.domain.hobby import HobbyRepository

from ..unit_of_work import UnitOfWork


@dataclass(frozen=True, slots=True)
class AddActivityCommand:
    id: UUID
    hobby_id: UUID
    started_at: datetime
    duration_minutes: int
    note: str | None


class AddActivityHandler:
    def __init__(
        self,
        uow: UnitOfWork,
        hobby_repo: HobbyRepository,
        activity_repo: ActivityRepository,
    ) -> None:
        self._uow = uow
        self._hobby_repo = hobby_repo
        self._activity_repo = activity_repo

    def __call__(self, cmd: AddActivityCommand) -> None:
        with self._uow:
            if not self._hobby_repo.exists(cmd.hobby_id):
                raise Exception(cmd.hobby_id)

            start = ActivityStart(cmd.started_at)
            duration = ActivityDuration(cmd.duration_minutes)
            note = ActivityNote(cmd.note) if cmd.note is not None else None

            activity = Activity(
                id=cmd.id,
                hobby_id=cmd.hobby_id,
                duration=duration,
                note=note,
                started_at=start,
            )
            self._activity_repo.add(activity)
