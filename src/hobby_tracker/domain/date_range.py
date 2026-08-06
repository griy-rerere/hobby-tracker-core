from dataclasses import dataclass
from datetime import date


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
