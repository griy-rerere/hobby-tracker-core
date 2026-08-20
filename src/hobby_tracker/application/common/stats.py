from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Stats:
    total_hours: float
    activities: int
    hours_per_day: float
