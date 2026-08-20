from dataclasses import dataclass
from uuid import UUID

from .stats import Stats


@dataclass(frozen=True, slots=True)
class HobbyStats:
    hobby_id: UUID
    hobby_name: str
    stats: Stats
