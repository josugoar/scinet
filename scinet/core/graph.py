from collections import abc
from json import dumps
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

    def add_edge(self, source_vertex: Any, target_vertex: Any, /, edge: Any = None, directed: bool = False, weight: Union[int, float] = 0):
        for vertex in {source_vertex, target_vertex}:
            self.add_vertex(vertex)
        if target_vertex not in self._adj[source_vertex]:
            self._adj[source_vertex][target_vertex] = {}
        u = self._adj[source_vertex][target_vertex]
        if directed:
            if edge not in u:
                if edge is None:
                    edge = 0
                    while edge in u:
                        edge += 1
                u[edge] = {}
            elif not u[edge]["directed"]:
                u[edge] = u[edge].copy()
        else:
            if source_vertex not in self._adj[target_vertex]:
                self._adj[target_vertex][source_vertex] = {}
            v = self._adj[target_vertex][source_vertex]
            if not (edge in u or edge in v):
                if edge is None:
                    edge = 0
                    while edge in u or edge in v:
                        edge += 1
                u[edge] = v[edge] = {}
            elif edge not in u and edge in v:
                u[edge] = v[edge]
            elif edge in u and edge not in v:
                v[edge] = u[edge]
        u[edge].update(directed=directed, weight=weight)
        return edge

    def remove_vertex(self, vertex: Any, /) -> None:
        try:
            del self._adj[vertex]
            for source_vertex, target_vertex in set(self.edges()):
                if target_vertex is vertex:
                    del self._adj[source_vertex][target_vertex]
        except KeyError:
            warn(f"'{vertex=}' not in '{self.__class__.__name__}'...")

    def remove_edge(self, source_vertex: Any, target_vertex: Any, /, edge: Any = None) -> None:
        try:
            if edge is None:
                del self._adj[source_vertex][target_vertex]
            else:
                u = self._adj[source_vertex][target_vertex]
                if not u[edge]["directed"]:
                    v = self._adj[target_vertex][source_vertex]
                    del v[edge]
                    if not v:
                        del self._adj[target_vertex][source_vertex]
                del u[edge]
                if not u:
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
        return dumps(self._adj, indent=2)
