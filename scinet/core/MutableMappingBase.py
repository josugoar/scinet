from collections.abc import MutableMapping
from typing import Any, Iterator


__all__ = ["MutableMappingBase"]


class MutableMappingBase(MutableMapping):

    __slots__ = "_store"

    def __init__(self):
        self._store = dict()

    def __iter__(self) -> Iterator[Any]:
        return iter(self._store)

    def __len__(self) -> int:
        return len(self._store)

    def __repr__(self) -> str:
        return repr(self._store)
