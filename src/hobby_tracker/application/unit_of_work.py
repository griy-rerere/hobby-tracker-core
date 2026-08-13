# from hobby_tracker.domain.hobby import HobbyRepository
# from hobby_tracker.domain.activity import ActivityRepository

from typing import Any, Protocol, Self


class UnitOfWork(Protocol):
    # hobby_repo: HobbyRepository
    # activity_repo: ActivityRepository

    def __enter__(self) -> Self: ...

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> bool: ...

    def commit(self) -> None: ...

    def rollback(self) -> None: ...
