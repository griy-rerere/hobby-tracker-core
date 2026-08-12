from typing import Protocol
from uuid import UUID

from .hobby import Hobby


class HobbyRepository(Protocol):
    def add(self, hobby: Hobby) -> None: ...

    def get_by_id(self, id: UUID) -> Hobby: ...

    def exists(self, id: UUID) -> bool: ...

    def delete(self, hobby: Hobby) -> None: ...
