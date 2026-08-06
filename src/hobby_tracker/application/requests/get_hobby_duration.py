from dataclasses import dataclass
from uuid import UUID

from hobby_tracker.domain import DateRange


@dataclass(frozen=True)
class GetHobbyDurationRequest:
    hobby_id: UUID
    date_range: DateRange
