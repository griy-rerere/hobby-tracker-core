from dataclasses import dataclass
from uuid import UUID

from hobby_tracker.domain.activity import ActivityRepository

from ..unit_of_work import UnitOfWork
from .base import Command, CommandHandler


@dataclass(frozen=True, slots=True)
class DeleteActivityCommand(Command):
    activity_id: UUID


class DeleteActivityHandler(CommandHandler[DeleteActivityCommand]):
    def __init__(
        self,
        uow: UnitOfWork,
        activity_repo: ActivityRepository,
    ) -> None:
        self._uow = uow
        self._activity_repo = activity_repo

    def __call__(self, cmd: DeleteActivityCommand) -> None:
        with self._uow:
            activity = self._activity_repo.get_by_id(cmd.activity_id)
            self._activity_repo.delete(activity)
            self._uow.commit()
