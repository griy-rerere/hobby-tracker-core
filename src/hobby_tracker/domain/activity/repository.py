from typing import Protocol
from uuid import UUID

from .activity import Activity


class ActivityRepository(Protocol):
    def add(self, hobby: Activity) -> None: ...

    def get_by_id(self, id: UUID) -> Activity: ...

    def exists(self, id: UUID) -> bool: ...

    def delete(self, hobby: Activity) -> None: ...
