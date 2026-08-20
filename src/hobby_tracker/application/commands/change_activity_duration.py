from dataclasses import dataclass
from uuid import UUID

from hobby_tracker.domain.activity import ActivityDuration, ActivityRepository

from ..unit_of_work import UnitOfWork
from .base import Command, CommandHandler


@dataclass(frozen=True, slots=True)
class ChangeActivityDurationCommand(Command):
    activity_id: UUID
    new_duration_minutes: int


class ChangeActivityDurationHandler(CommandHandler[ChangeActivityDurationCommand]):
    def __init__(
        self,
        uow: UnitOfWork,
        activity_repo: ActivityRepository,
    ) -> None:
        self._uow = uow
        self._activity_repo = activity_repo

    def __call__(self, cmd: ChangeActivityDurationCommand) -> None:
        with self._uow:
            new_duration = ActivityDuration(cmd.new_duration_minutes)
            activity = self._activity_repo.get_by_id(cmd.activity_id)
            activity.change_duration(new_duration)
            self._uow.commit()
