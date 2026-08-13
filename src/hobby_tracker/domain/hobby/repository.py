from typing import Protocol
from uuid import UUID

from .hobby import Hobby


class HobbyRepository(Protocol):
    def add(self, hobby: Hobby) -> None: ...

    """
    Raises:
        HobbyAttributeDuplicate if UUID or HobbyName duplicate
    """

    def get_by_id(self, id: UUID) -> Hobby: ...

    """
    Repository must track itself all the changes with loaded entities like Python list

    Raises:
        HobbyNotFound(id) if hobby not found
    """

    def exists(self, id: UUID) -> bool: ...

    def delete(self, hobby: Hobby) -> None: ...

    """
    Only tracking hobby is allowed to delete
    
    Raises:
        HobbyDeleteError if try to delete hobby not from Repository
    """
