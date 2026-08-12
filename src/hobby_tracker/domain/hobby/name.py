from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class HobbyName:
    value: str

    def __post_init__(self) -> None:
        name = self.value.strip()

        if not name:
            raise ValueError("Hobby name cannot be empty")
        if len(name) > 50:
            raise ValueError("Hobby name is too long")

        object.__setattr__(self, "value", name)

    def __str__(self) -> str:
        return self.value
