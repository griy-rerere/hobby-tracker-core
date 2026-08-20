from typing import Protocol


class Command:
    __slots__ = ()


class CommandHandler[C: Command](Protocol):
    def __call__(self, command: C) -> None: ...
