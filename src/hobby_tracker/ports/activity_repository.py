from typing import Iterable, Protocol
from uuid import UUID

from hobby_tracker.domain import Activity, ActivityStatistics
from hobby_tracker.queries import ActivityQuery, ActivityStatisticsQuery


class ActivityRepository(Protocol):
    def save(self, activity: Activity) -> None: ...

    def get(self, id: UUID) -> Activity: ...

    def get_many(self, query: ActivityQuery) -> Iterable[Activity]: ...

    def calculate_statistics(
        self, query: ActivityStatisticsQuery
    ) -> ActivityStatistics: ...
