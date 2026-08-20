from dataclasses import dataclass
from uuid import UUID

from hobby_tracker.domain.activity import ActivityNote, ActivityRepository

from ..unit_of_work import UnitOfWork
from .base import Command, CommandHandler


@dataclass(frozen=True, slots=True)
class SetActivityNoteCommand(Command):
    activity_id: UUID
    note: str


class SetActivityNoteHandler(CommandHandler[SetActivityNoteCommand]):
    def __init__(
        self,
        uow: UnitOfWork,
        activity_repo: ActivityRepository,
    ) -> None:
        self._uow = uow
        self._activity_repo = activity_repo

    def __call__(self, cmd: SetActivityNoteCommand) -> None:
        with self._uow:
            note = ActivityNote(cmd.note)
            activity = self._activity_repo.get_by_id(cmd.activity_id)
            activity.set_note(note)
            self._uow.commit()
