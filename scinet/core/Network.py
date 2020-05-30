from abc import ABCMeta
from collections.abc import Mapping as Mappable
from collections.abc import MutableMapping
from typing import Any, Iterable, Iterator, Mapping, Tuple, Union

__all__ = ["network"]


class StatefulMapping(Mappable, metaclass=ABCMeta):

    __slots__ = "_store"

    def __init__(self):
        self._store = dict()

    def __iter__(self) -> Iterator[Any]:
        return iter(self._store)

    def __len__(self) -> int:
        return len(self._store)

    def __repr__(self) -> str:
        return repr(self._store)


# TODO: edge directed property
# TODO: multigraph dict list
class network(StatefulMapping, MutableMapping):

    class _adj(StatefulMapping, MutableMapping):

        __slots__ = "_network", "_source_vertex"

        def __init__(self, network: "network", source_vertex: Any):
            super().__init__()
            network[source_vertex] = self
            self._network = network
            self._source_vertex = source_vertex

        def __getitem__(self, target_vertex: Any) -> Mapping[str, Any]:
            return self._store[target_vertex]

        def __setitem__(self, target_vertex: Any, data: Mapping[str, Any]) -> None:
            try:
                self._store[target_vertex] = dict(**data)
                self._network[target_vertex]
                self._network._edges[(self._source_vertex, target_vertex)] = data
            except TypeError as e:
                raise TypeError(f"'data: {data}' not of type 'Mapping[str, Any]'...") from e

        def __delitem__(self, target_vertex: Any) -> None:
            del self._store[target_vertex]
            del self._network._edges[(self._source_vertex, target_vertex)]

    __slots__ = "_vertices", "_edges"

    def __init__(self):
        super().__init__()
        self._vertices = dict()
        self._edges = dict()

    def add_vertex(self, vertex, **data):
        try:
            self._vertices[vertex] = dict(**data)
            self[vertex] = self._adj(network=self, source_vertex=vertex)
        except TypeError as e:
            raise TypeError(f"'data: {data}' not of type 'Mapping[str, Any]'...") from e

    def add_vertices(self, *vertices):
        pass

    def add_edge(self, edge, **data):
        pass

    def add_edges(self, *edges):
        pass

    def vertices(self, data: bool = False) -> Union[Mapping[Any, Mapping[str, Any]], Iterable[Any]]:
        return dict(self._vertices) if data else list(self._vertices)

    def edges(self, data: bool = False) -> Union[Mapping[Tuple[Any, Any], Mapping[str, Any]], Iterable[Tuple[Any, Any]]]:
        return dict(self._edges) if data else list(self._edges)

    def __getitem__(self, vertex: Any) -> Mapping[Any, Mapping[str, Any]]:
        return self._store[vertex]

    def __setitem__(self, vertex: Any, data: Mapping[str, Any]) -> None:
        if isinstance(data, self._adj):
            self._store[vertex] = data
        else:
            try:
                self._vertices[vertex] = dict(**data)
                self[vertex] = self._adj(network=self, source_vertex=vertex)
            except TypeError as e:
                raise TypeError(f"'data: {data}' not of type 'Mapping[str, Any]'...") from e

    def __delitem__(self, vertex: Any) -> None:
        try:
            del self._store[vertex]
            del self._vertices[vertex]
            for source_vertex, target_vertex in self.edges():
                if source_vertex is vertex or target_vertex is vertex:
                    del self._edges[(source_vertex, target_vertex)]
                    if target_vertex is vertex and vertex in self:
                        del self[source_vertex][target_vertex]
        except KeyError as e:
            raise KeyError(f"'vertex: {vertex}' not in 'network'...") from e


if __name__ == "__main__":
    G = network()
    G[1] = {}
    G[2] = {}
    G[1][2] = {}
    # G.clear()
    print(len(G))
    print(G.vertices())
    print(G.edges())
