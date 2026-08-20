from dataclasses import dataclass
from uuid import UUID

from hobby_tracker.domain.hobby import HobbyRepository

from ..unit_of_work import UnitOfWork
from .base import Command, CommandHandler


@dataclass(frozen=True, slots=True)
class DeleteHobbyCommand(Command):
    hobby_id: UUID


class DeleteHobbyHandler(CommandHandler[DeleteHobbyCommand]):
    def __init__(self, uow: UnitOfWork, hobby_repo: HobbyRepository) -> None:
        self._uow = uow
        self._hobby_repo = hobby_repo

    def __call__(self, cmd: DeleteHobbyCommand) -> None:
        with self._uow:
            hobby = self._hobby_repo.get_by_id(cmd.hobby_id)
            self._hobby_repo.delete(hobby)
            self._uow.commit()
