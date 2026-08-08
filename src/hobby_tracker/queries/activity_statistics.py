from dataclasses import dataclass
from typing import Iterable
from uuid import UUID

from hobby_tracker.domain import DateRange


@dataclass(frozen=True)
class ActivityStatisticsQuery:
    date_range: DateRange
    hobby_ids: Iterable[UUID] | None = None
