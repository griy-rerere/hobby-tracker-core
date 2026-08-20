from unittest.mock import Mock

import pytest

from hobby_tracker.application import QueryBus
from hobby_tracker.application.queries import Query, QueryHandler


@pytest.fixture
def bus() -> QueryBus:
    bus = QueryBus()
    return bus


def test_register(bus: QueryBus) -> None:
    mock_query = Mock(spec=Query)
    mock_handler = Mock(spec=QueryHandler)

    bus.register(type(mock_query), mock_handler)
    assert bus._handlers[type(mock_query)] is mock_handler


@pytest.mark.parametrize("handler_exists", [True, False])
def test_call(bus: QueryBus, handler_exists: bool) -> None:
    mock_query = Mock(spec=Query)
    if not handler_exists:
        with pytest.raises(
            ValueError,
            match=f"No handler registered for query: {type(mock_query).__name__}",
        ):
            bus(mock_query)
        return

    mock_result = Mock()
    mock_handler = Mock(spec=QueryHandler)
    mock_handler.return_value = mock_result
    bus._handlers[type(mock_query)] = mock_handler

    res = bus(mock_query)

    assert res is mock_result
    mock_handler.assert_called_once_with(mock_query)
