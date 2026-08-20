from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from hobby_tracker.domain.activity import ActivityRepository, ActivityStart

from ..unit_of_work import UnitOfWork
from .base import Command, CommandHandler


@dataclass(frozen=True, slots=True)
class ChangeActivityStartCommand(Command):
    activity_id: UUID
    new_start: datetime


class ChangeActivityStartHandler(CommandHandler[ChangeActivityStartCommand]):
    def __init__(
        self,
        uow: UnitOfWork,
        activity_repo: ActivityRepository,
    ) -> None:
        self._uow = uow
        self._activity_repo = activity_repo

    def __call__(self, cmd: ChangeActivityStartCommand) -> None:
        with self._uow:
            new_start = ActivityStart(cmd.new_start)
            activity = self._activity_repo.get_by_id(cmd.activity_id)
            activity.change_start(new_start)
            self._uow.commit()
