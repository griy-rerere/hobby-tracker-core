from dataclasses import dataclass
from uuid import UUID

from hobby_tracker.domain.hobby import Hobby, HobbyName, HobbyRepository

from ..unit_of_work import UnitOfWork


@dataclass(frozen=True, slots=True)
class AddHobbyCommand:
    id: UUID
    name: str


class AddHobbyHandler:
    def __init__(self, uow: UnitOfWork, hobby_repo: HobbyRepository) -> None:
        self._uow = uow
        self._hobby_repo = hobby_repo

    def __call__(self, cmd: AddHobbyCommand) -> None:
        with self._uow:
            name = HobbyName(cmd.name)
            hobby = Hobby(id=cmd.id, name=name)

            self._hobby_repo.add(hobby)
