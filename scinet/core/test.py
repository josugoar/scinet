from abc import ABCMeta
from collections.abc import Mapping as Mappable
from typing import Any, Iterable, Iterator, Mapping, Tuple


class StatefulMapping(Mappable, metaclass=ABCMeta):

    __slots__ = "_state"

    def __init__(self) -> None:
        self._state = dict()

    def clear(self):
        self._state.clear()

    def __iter__(self) -> Iterator[Any]:
        return iter(self._state)

    def __len__(self) -> int:
        return len(self._state)

    def __repr__(self) -> str:
        return repr(self._state)


class network(StatefulMapping):

    __slots__ = "_edges", "_vertices"

    def __init__(self) -> None:
        super().__init__()
        self._edges = dict()
        self._vertices = dict()

    def add_edge(self, e: Iterable[Tuple[Tuple[Any, Any], Iterable[Any]]], /) -> None:
        for vertices, edges in e:
            source_vertex, target_vertex = vertices
            if not (source_vertex in self._state and target_vertex in self._state):
                raise KeyError
            for edge in edges:
                try:
                    # TODO: Overhead
                    self._state[source_vertex][target_vertex].add(edge)
                except KeyError:
                    self._state[source_vertex][target_vertex] = {edge}

    def add_vertex(self, v: Iterable[Any], /) -> None:
        for vertex in v:
            if vertex not in self._state:
                self._state[vertex] = dict()

    def remove_edge(self, e: Iterable[Tuple[Tuple[Any, Any], Iterable[Any]]], /) -> None:
        for vertices, edges in e:
            source_vertex, target_vertex = vertices
            for edge in edges:
                self._state[source_vertex][target_vertex].remove(edge)
            if not self._state[source_vertex][target_vertex]:
                del self._state[source_vertex][target_vertex]

    def remove_vertex(self, v: Iterable[Any], /) -> None:
        for vertex in v:
            del self._state[vertex]
            for source_vertex, neighbors in self._state.items():
                for target_vertex in neighbors:
                    if target_vertex is vertex:
                        del self._state[source_vertex][target_vertex]

    def __getitem__(self, vertex: Any) -> Mapping[Any, Iterable[Any]]:
        return dict(self._state[vertex])


if __name__ == "__main__":
    import fileinput
    import cProfile

    gen = (((j, j), range(j)) for j in range(10000))

    def run():
        G = network()
        G.add_vertex(range(10000))
        G.add_edge(gen)

    pr = cProfile.Profile()
    pr.enable()
    run()
    pr.create_stats()
    pr.print_stats(sort='time')
