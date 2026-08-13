from uuid import UUID

from .name import HobbyName


class Hobby:
    def __init__(self, *, id: UUID, name: HobbyName) -> None:
        self._id = id
        self._name = name

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def name(self) -> HobbyName:
        return self._name

    def rename(self, new_name: HobbyName) -> None:
        self._name = new_name
