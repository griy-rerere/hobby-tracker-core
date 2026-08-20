from typing import Any, Protocol


class Query[R]:
    __slots__ = ()


class QueryHandler[Q: Query[Any], R](Protocol):
    def __call__(self, query: Q) -> R: ...
