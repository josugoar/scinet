from collections.abc import MutableMapping
from typing import Any, Iterable, Iterator, Mapping, NoReturn, Optional, Tuple, Union

from .MutableMappingBase import MutableMappingBase


__all__ = ["network"]


class network(MutableMappingBase):

    class _adj(MutableMappingBase):

        __slots__ = "_network", "_source_vertex"

        def __init__(self, network: "network", source_vertex: Any):
            super().__init__()
            network[source_vertex] = self
            self._network = network
            self._source_vertex = source_vertex

        def __getitem__(self, target_vertex: Any) -> Mapping[str, Any]:
            try:
                return self._store[target_vertex]
            except KeyError:
                self[target_vertex] = self._network._default_edge()
                self._network[target_vertex]
                return self[target_vertex]

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

    _default_vertex = _default_edge = dict

    __slots__ = "_vertices", "_edges"

    def __init__(self):
        super().__init__()
        self._vertices = dict()
        self._edges = dict()

    def vertices(self, data: bool = False) -> Union[Mapping[Any, Mapping[str, Any]], Iterable[Any]]:
        return dict(self._vertices) if data else list(self._vertices)

    def edges(self, data: bool = False) -> Union[Mapping[Tuple[Any, Any], Mapping[str, Any]], Iterable[Tuple[Any, Any]]]:
        return dict(self._edges) if data else list(self._edges)

    def clear(self) -> None:
        super().clear()
        self._vertices.clear()
        self._edges.clear()

    def __getitem__(self, vertex: Any) -> Mapping[Any, Mapping[str, Any]]:
        try:
            return self._store[vertex]
        except KeyError:
            self[vertex] = self._adj(network=self, source_vertex=vertex)
            return self[vertex]

    def __setitem__(self, vertex: Any, data: Mapping[str, Any]) -> None:
        if isinstance(data, self._adj):
            self._store[vertex] = data
            self._vertices[vertex] = self._default_vertex()
        else:
            try:
                self._vertices[vertex] = dict(**data)
                self[vertex]
            except TypeError as e:
                raise TypeError(f"'data: {data}' not of type 'Mapping[str, Any]'...") from e

    def __delitem__(self, vertex: Any) -> None:
        try:
            del self._store[vertex]
            del self._vertices[vertex]
            for source_vertex, target_vertex in self.edges():
                if target_vertex is vertex:
                    del self[source_vertex][target_vertex]
        except KeyError as e:
            raise KeyError(f"'vertex: {vertex}' not in 'network'...") from e


if __name__ == "__main__":
    G = network()
    G[1]
    print(G)
