from typing import Protocol
from uuid import UUID

from .activity import Activity


class ActivityRepository(Protocol):
    def add(self, activity: Activity) -> None: ...

    def get_by_id(self, id: UUID) -> Activity:
        """
        Repository must track itself all the changes with loaded entities
        like Python list

        Raises:
            ActivityNotFound(id) if activity not found
        """
        ...

    def exists(self, id: UUID) -> bool: ...

    def delete(self, activity: Activity) -> None:
        """
        Only tracking activity is allowed to delete

        Raises:
            ActivityDeleteError if try to delete activity not from Repository
        """
        ...
