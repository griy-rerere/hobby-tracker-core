from typing import Protocol
from uuid import UUID

from .hobby import Hobby
from .name import HobbyName


class HobbyRepository(Protocol):
    def add(self, hobby: Hobby) -> None: ...

    def get_by_id(self, id: UUID) -> Hobby:
        """
        Repository must track itself all the changes with loaded entities
        like Python list

        Raises:
            HobbyNotFound(id) if hobby not found
        """
        ...

    def exists(self, id: UUID) -> bool: ...

    def name_exists(self, name: HobbyName) -> bool: ...

    def delete(self, hobby: Hobby) -> None:
        """
        Only tracking hobby is allowed to delete

        Raises:
            HobbyDeleteError if try to delete hobby not from Repository
        """
        ...
