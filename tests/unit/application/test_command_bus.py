from unittest.mock import Mock

import pytest

from hobby_tracker.application import CommandBus
from hobby_tracker.application.commands import Command, CommandHandler


@pytest.fixture
def cmd_bus():
    bus = CommandBus()
    return bus


def test_register(cmd_bus: CommandBus) -> None:
    mock_cmd = Mock(spec=Command)
    mock_handler = Mock(spec=CommandHandler)

    cmd_bus.register(type(mock_cmd), mock_handler)
    assert cmd_bus._handlers[type(mock_cmd)] is mock_handler


@pytest.mark.parametrize("handler_exists", [True, False])
def test_call(cmd_bus: CommandBus, handler_exists: bool) -> None:
    mock_cmd = Mock(spec=Command)
    if not handler_exists:
        with pytest.raises(
            ValueError,
            match=f"No handler registered for command: {type(mock_cmd).__name__}",
        ):
            cmd_bus(mock_cmd)
        return

    mock_handler = Mock(spec=CommandHandler)
    cmd_bus._handlers[type(mock_cmd)] = mock_handler

    cmd_bus(mock_cmd)

    mock_handler.assert_called_once_with(mock_cmd)
