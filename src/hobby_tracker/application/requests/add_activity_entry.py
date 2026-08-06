from dataclasses import dataclass
from datetime import datetime, timedelta
from uuid import UUID


@dataclass(frozen=True)
class AddActivityEntryRequest:
    hobby_id: UUID
    duration: timedelta
    started_at: datetime | None = None
    note: str | None = None
