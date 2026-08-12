from dataclasses import dataclass
from datetime import timedelta

MINUTES_ONE_DAY = 24 * 60


@dataclass(frozen=True, slots=True)
class ActivityDuration:
    minutes: int

    def __post_init__(self) -> None:
        if self.minutes <= 0:
            raise ValueError("ActivityDuration must be positive")

        if self.minutes >= MINUTES_ONE_DAY:
            raise ValueError("ActivityDuration cannot be the whole day or more")

    def hours(self) -> float:
        return self.minutes / 60

    def timedelta(self) -> timedelta:
        return timedelta(minutes=self.minutes)
