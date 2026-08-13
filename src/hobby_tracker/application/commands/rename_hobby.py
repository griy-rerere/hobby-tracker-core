from dataclasses import dataclass
from uuid import UUID

from hobby_tracker.domain.hobby import HobbyName, HobbyRepository

from ..unit_of_work import UnitOfWork


@dataclass(frozen=True, slots=True)
class RenameHobbyCommand:
    hobby_id: UUID
    new_name: str


class RenameHobbyHandler:
    def __init__(self, uow: UnitOfWork, hobby_repo: HobbyRepository) -> None:
        self._uow = uow
        self._hobby_repo = hobby_repo

    def __call__(self, cmd: RenameHobbyCommand) -> None:
        with self._uow:
            new_name = HobbyName(cmd.new_name)
            hobby = self._hobby_repo.get_by_id(cmd.hobby_id)
            hobby.rename(new_name)
