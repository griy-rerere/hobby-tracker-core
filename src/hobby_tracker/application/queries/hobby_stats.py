from dataclasses import dataclass
from datetime import date
from uuid import UUID

from ..common import HobbyStats
from .base import Query


@dataclass(frozen=True, slots=True)
class HobbyStatsView:
    stats_chart: bytes
    stats: HobbyStats


@dataclass(frozen=True, slots=True)
class HobbyStatsQuery(Query[HobbyStatsView]):
    hobby_id: UUID
    date_from: date
    date_to: date
