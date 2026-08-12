from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ActivityNote:
    text: str

    def __post_init__(self) -> None:
        if len(self.text) > 500:
            raise ValueError("Note is too long")

    def __str__(self) -> str:
        return self.text
