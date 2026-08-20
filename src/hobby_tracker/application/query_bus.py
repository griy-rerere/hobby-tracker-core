from typing import Any, cast

from .queries import Query, QueryHandler


class QueryBus:
    def __init__(self) -> None:
        self._handlers: dict[type[Query[Any]], QueryHandler[Any, Any]] = {}

    def register[Q: Query[Any], R](
        self, query_cls: type[Q], handler: QueryHandler[Q, R]
    ) -> None:
        self._handlers[query_cls] = handler

    def __call__[R](self, query: Query[R]) -> R:
        query_type = type(query)
        if query_type not in self._handlers:
            raise ValueError(f"No handler registered for query: {query_type.__name__}")

        handler = cast(QueryHandler[Query[R], R], self._handlers[query_type])
        return handler(query)
