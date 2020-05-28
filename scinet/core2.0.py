from collections.abc import MutableMapping
from typing import Any, Mapping, Tuple


class network(MutableMapping):

    def pop(self, vertex: Any, default: Any = None) -> Any:
        pass

    def popitem(self) -> Tuple[Any, Mapping[str, Any]]:
        pass

    def clear(self) -> None:
        pass

    def update(self, vertices: Mapping[Any, Mapping[str, Any]], edges: Mapping[Tuple[Any, Any], Mapping[str, Any]]):
        pass

    def setdefault(self, vertex: Any, default: Mapping[str, Any] = None):
        pass

    def __getitem__(self, vertex: Any):
        pass

    def __setitem__(self, vertex: Any, data: Mapping[str, Any]):
        pass

    def __delitem__(self, vertex: Any):
        pass

    def __iter__(self):
        pass

    def __len__(self):
        pass


if __name__ == "__main__":
    G = network()
    print(G.keys())
