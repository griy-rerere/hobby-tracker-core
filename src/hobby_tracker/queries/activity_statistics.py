from dataclasses import dataclass
from typing import Iterable
from uuid import UUID

from hobby_tracker.domain import DateRange


@dataclass(frozen=True)
class ActivityStatisticsQuery:
    hobby_ids: Iterable[UUID] | None
    date_range: DateRange | None
