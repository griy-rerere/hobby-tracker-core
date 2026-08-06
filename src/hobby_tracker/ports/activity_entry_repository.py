from datetime import timedelta
from typing import Protocol
from uuid import UUID

from hobby_tracker.domain import ActivityEntry, DateRange


class ActivityEntryRepository(Protocol):
    def save(self, activity_entry: ActivityEntry) -> None: ...

    def get_hobby_sum(self, hobby_id: UUID, date_range: DateRange) -> timedelta: ...
