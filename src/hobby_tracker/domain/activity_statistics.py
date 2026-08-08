from dataclasses import dataclass
from datetime import timedelta


@dataclass(frozen=True)
class ActivityStatistics:
    total_duration: timedelta
    activity_count: int
    avg_duration: timedelta
