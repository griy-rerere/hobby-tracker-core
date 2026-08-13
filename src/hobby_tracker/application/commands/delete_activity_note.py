from dataclasses import dataclass
from uuid import UUID

from hobby_tracker.domain.activity import ActivityRepository

from ..unit_of_work import UnitOfWork


@dataclass(frozen=True, slots=True)
class DeleteActivityNoteCommand:
    activity_id: UUID


class DeleteActivityNoteHandler:
    def __init__(
        self,
        uow: UnitOfWork,
        activity_repo: ActivityRepository,
    ) -> None:
        self._uow = uow
        self._activity_repo = activity_repo

    def __call__(self, cmd: DeleteActivityNoteCommand) -> None:
        with self._uow:
            activity = self._activity_repo.get_by_id(cmd.activity_id)
            activity.delete_note()
