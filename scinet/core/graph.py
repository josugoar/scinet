from collections import abc
from pprint import pformat
from typing import Any, Iterable, Iterator, Mapping, Tuple, Union
from warnings import warn


__all__ = ["Graph"]


class Graph(abc.Mapping):

    __slots__ = "_adj"

    def __init__(self) -> None:
        self._adj = {}

    def add_vertex(self, vertex: Any, /) -> None:
        if vertex not in self._adj:
            self._adj[vertex] = {}

    def add_edge(self, source_vertex: Any, target_vertex: Any, key: Any = None, **data: Any) -> Any:
        for vertex in {source_vertex, target_vertex}:
            self.add_vertex(vertex)
        if target_vertex not in self._adj[source_vertex]:
            self._adj[source_vertex][target_vertex] = {}
        if data.get("directed"):
            if key not in self._adj[source_vertex][target_vertex]:
                if key is None:
                    key = 0
                    while key in self._adj[source_vertex][target_vertex]:
                        key += 1
                self._adj[source_vertex][target_vertex][key] = {}
        else:
            if source_vertex not in self._adj[target_vertex]:
                self._adj[target_vertex][source_vertex] = {}
            if not (key in self._adj[source_vertex][target_vertex] or key in self._adj[target_vertex][source_vertex]):
                if key is None:
                    key = 0
                    while key in self._adj[source_vertex][target_vertex] or key in self._adj[target_vertex][source_vertex]:
                        key += 1
            self._adj[source_vertex][target_vertex][key] = self._adj[target_vertex][source_vertex][key] = {}
        if data:
            self._adj[source_vertex][target_vertex][key].update(data)
        return key

    def remove_vertex(self, vertex: Any, /) -> None:
        try:
            del self._adj[vertex]
            for source_vertex, target_vertex in set(self.edges()):
                if target_vertex is vertex:
                    del self._adj[source_vertex][target_vertex]
        except KeyError:
            warn(f"'{vertex=}' not in '{self.__class__.__name__}'...")

    def remove_edge(self, source_vertex: Any, target_vertex: Any, *data: Any, edge: Any = None) -> None:
        try:
            if data:
                for attr in data:
                    if edge is None:
                        for key in self._adj[source_vertex][target_vertex]:
                            if attr in self._adj[source_vertex][target_vertex][key]:
                                del self._adj[source_vertex][target_vertex][key][attr]
                    else:
                        if attr in self._adj[source_vertex][target_vertex][edge]:
                            del self._adj[source_vertex][target_vertex][edge][attr]
            else:
                if edge is None:
                    del self._adj[source_vertex][target_vertex]
                else:
                    del self._adj[source_vertex][target_vertex][edge]
                    if not self._adj[source_vertex][target_vertex]:
                        del self._adj[source_vertex][target_vertex]
        except KeyError:
            warn(f"'{edge=} not in '{self.__class__.__name__}'...")

    def vertices(self) -> Iterator[Any]:
        return iter(self._adj)

    def edges(self, key: bool = False) -> Iterator[Union[Tuple[Any, Any], Tuple[Any, Any, Any]]]:
        for source_vertex, neighbors in self._adj.items():
            for target_vertex, edges in neighbors.items():
                if key:
                    for edge in edges:
                        yield source_vertex, target_vertex, edge
                else:
                    yield source_vertex, target_vertex

    def __getitem__(self, vertex: Any, /) -> Any:
        return dict(self._adj)[vertex]

    def __iter__(self) -> None:
        return self.vertices()

    def __len__(self) -> int:
        return len(self._adj)

    def __str__(self) -> str:
        return pformat(self._adj)


if __name__ == "__main__":
    G = Graph()
    # for source_vertex, target_vertex in ((i, 0) for i in range(10)):
    G.add_edge(0, 0)
    G.add_edge(1, 0, a=1)
    G.add_edge(2, 0)
    G.add_edge(3, 0)
    # G.remove_edge(0, 1, "a")
    print(list(G.edges()))
