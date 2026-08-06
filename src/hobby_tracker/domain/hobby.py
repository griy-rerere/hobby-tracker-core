from dataclasses import dataclass, field
from uuid import UUID, uuid7


@dataclass(frozen=True)
class Hobby:
    name: str
    id: UUID = field(default_factory=uuid7)

    def __post_init__(self) -> None:
        name = self.name.strip()

        if not name:
            raise ValueError("Hobby name cannot be empty")
        if len(name) > 50:
            raise ValueError("Hobby name is too long")

        object.__setattr__(self, "name", name)
