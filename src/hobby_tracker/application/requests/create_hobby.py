from dataclasses import dataclass


@dataclass(frozen=True)
class CreateHobbyRequest:
    name: str
