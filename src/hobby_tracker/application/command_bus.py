from typing import Any

from .commands import Command, CommandHandler


class CommandBus:
    def __init__(self) -> None:
        self._handlers: dict[type[Command], CommandHandler[Any]] = {}

    def register[C: Command](
        self, command_cls: type[C], handler: CommandHandler[C]
    ) -> None:
        self._handlers[command_cls] = handler

    def __call__(self, command: Command) -> None:
        command_type = type(command)
        if command_type not in self._handlers:
            raise ValueError(
                f"No handler registered for command: {command_type.__name__}"
            )

        handler = self._handlers[command_type]
        handler(command)
