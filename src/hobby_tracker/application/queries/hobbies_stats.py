from dataclasses import dataclass
from datetime import date
from typing import Mapping, Protocol


@dataclass(frozen=True, slots=True)
class HobbiesStatsQuery:
    date_from: date
    date_to: date


@dataclass(frozen=True, slots=True)
class Stats:
    total_hours: float
    activities: int
    hours_per_day: float


@dataclass(frozen=True, slots=True)
class HobbiesStatsView:
    hobbies_stats: Mapping[str, Stats]
    common_stats: Stats


class HobbiesStatsHandler(Protocol):
    def __call__(self, query: HobbiesStatsQuery) -> HobbiesStatsView: ...
