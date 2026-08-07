from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from uuid import UUID, uuid7


@dataclass(frozen=True)
class Activity:
    hobby_id: UUID
    duration: timedelta
    started_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    note: str | None = None
    id: UUID = field(default_factory=uuid7)

    def __post_init__(self) -> None:
        if self.duration <= timedelta(0):
            raise ValueError("Activity duration must be positive")

        if self.note is not None and len(self.note) > 500:
            raise ValueError("Note is too long")
