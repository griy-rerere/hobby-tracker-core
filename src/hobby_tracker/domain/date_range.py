from dataclasses import dataclass
from datetime import date, datetime


@dataclass(frozen=True)
class DateRange:
    """
    Date range with inclusive boundaries.
    """

    start: date
    end: date

    def __post_init__(self) -> None:
        if self.start > self.end:
            raise ValueError("Start date cannot be after end date")

    def __contains__(self, dt: datetime) -> bool:
        return self.start <= dt.date() <= self.end
