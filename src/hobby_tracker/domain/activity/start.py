from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass(frozen=True, slots=True)
class ActivityStart:
    value: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def __post_init__(self) -> None:
        if self.value.tzinfo != timezone.utc:
            raise ValueError("ActivityStart must UTC datetime")

        if self.value > datetime.now(timezone.utc):
            raise ValueError("Activity cannot start in the future")
