from dataclasses import dataclass
from datetime import date

from ..common import HobbyStats
from .base import Query


@dataclass(frozen=True, slots=True)
class HobbyStatsView:
    stats_chart: bytes
    stats: HobbyStats


@dataclass(frozen=True, slots=True)
class HobbyStatsQuery(Query[HobbyStatsView]):
    date_from: date
    date_to: date
