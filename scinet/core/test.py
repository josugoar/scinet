from collections.abc import Mapping as Mappable
from typing import Any, Iterable, Iterator, Mapping, Tuple, Union


class network(Mappable):

    __slots__ = "_state"

    def __init__(self):
        self._state = dict()

    def add_edges(self, e: Mapping[Tuple[Any, Any], Iterable[Any]], /) -> None:
        for vertices, edges in e.items():
            source_vertex, target_vertex = vertices
            if not (source_vertex in self._state and target_vertex in self._state):
                raise KeyError
            for edge in edges:
                try:
                    self._state[source_vertex][target_vertex].append(edge)
                except KeyError:
                    self._state[source_vertex][target_vertex] = [edge]

    def add_vertices(self, v: Iterable[Any], /) -> None:
        for vertex in v:
            if vertex not in self._state:
                self._state[vertex] = dict()

    def remove_edges(self, e: Mapping[Tuple[Any, Any], Iterable[Any]], /) -> None:
        for vertices, edges in e.items():
            source_vertex, target_vertex = vertices
            for edge in edges:
                self._state[source_vertex][target_vertex].remove(edge)
            if not self._state[source_vertex][target_vertex]:
                del self._state[source_vertex][target_vertex]

    def remove_vertices(self, v: Iterable[Any], /) -> None:
        for vertex in v:
            del self._state[vertex]
            for source_vertex, neighbors in self._state.items():
                for target_vertex in neighbors:
                    if target_vertex is vertex:
                        del self._state[source_vertex][target_vertex]

    def __getitem__(self, vertex):
        return dict(self._state[vertex])

    def __delitem__(self, vertex):
        self.remove_vertices([vertex])

    def __iter__(self):
        return iter(self._state)

    def __len__(self):
        return len(self._state)

    def __repr__(self):
        return repr(self._state)


if __name__ == "__main__":
    G = network()
    G.add_vertices([1, 2, 3])
    G.add_edges({(1, 2): [1, 2], (3, 3): [1, 2, 3]})
    # G.remove_edges({(1, 2): [1, 2]})
    G.remove_vertices([1])
    print(G)
