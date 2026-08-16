from dataclasses import dataclass
from uuid import UUID

from hobby_tracker.domain.exceptions import HobbyAttributeDuplicate
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
            if self._hobby_repo.name_exists(name):
                raise HobbyAttributeDuplicate(repr(name))
            if self._hobby_repo.exists(cmd.id):
                raise HobbyAttributeDuplicate(cmd.id)

            hobby = Hobby(id=cmd.id, name=name)

            self._hobby_repo.add(hobby)
            self._uow.commit()
