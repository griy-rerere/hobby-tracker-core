from typing import Protocol
from uuid import UUID

from hobby_tracker.domain import Hobby


class HobbyRepository(Protocol):
    def save(self, hobby: Hobby) -> None: ...

    def get(self, id: UUID) -> Hobby: ...
