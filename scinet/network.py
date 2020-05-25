from collections import defaultdict
from typing import Any, Dict, Iterator, List, Set, Tuple, Union


class net(defaultdict):

    class __adj(dict):

        def __init__(self, G: "net") -> None:
            self.__G = G

        def __getitem__(self, v: Any) -> Any:
            # TODO: Create with default_edge
            super().__getitem__(v)

        def __setitem__(self, v: Any, e: Dict[str, Any]) -> None:
            super().__setitem__(v, e)
            self.__G[v]

    def __init__(self, default_edge: Dict[str, Any] = dict(), default_vertex: Dict[str, Any] = dict()) -> None:
        super().__init__(lambda: self.__adj(self))
        self.default_edge = default_edge
        self.default_vertex = default_vertex
        self.__V = dict()

    @property
    def default_edge(self) -> Dict[str, Any]:
        return self.__default_edge

    @default_edge.setter
    def default_edge(self, default_edge: Dict[str, Any]) -> None:
        self.__default_edge = default_edge

    @property
    def default_vertex(self) -> Dict[str, Any]:
        return self.__default_vertex

    @default_vertex.setter
    def default_vertex(self, default_vertex: Dict[str, Any]) -> None:
        self.__default_vertex = default_vertex

    def get_edges(self, o: bool = False) -> Union[Dict[Tuple[Any, Any], Dict[str, Any]], Set[Tuple[Any, Any]]]:
        edges = dict() if o else set()
        for v, e in self:
            for u in e:
                edges.update({tuple(v, u): e[u]}) if o else edges.add(tuple(v, u))
        return edges

    def del_edges(self) -> None:
        for _, e in self:
            e = e.fromkeys(e, self.__default_edge)

    def get_vertices(self, o: bool = False) -> Union[Dict[Any, Dict[str, Any]], set]:
        return self.__V if o else set(self.__V.keys())

    def del_vertices(self) -> None:
        self.__V = self.__V.fromkeys(self.__V, self.__default_vertex)

    def adjacent(self, v: Any, u: Any) -> bool:
        for n in dict(self)[v]:
            if n is u:
                return True
        return False

    def neighbors(self, v: Any) -> Iterator[Any]:
        for n in dict(self)[v]:
            yield n

    # def add_vertex(self):
    #     ...

    # def remove_vertex(self):
    #     ...

    # def add_edge(self):
    #     ...

    # def remove_edge(self):
    #     ...

    # def get_edge_data(self):
    #     ...

    # def set_edge_data(self):
    #     ...

    def clear(self) -> None:
        super().clear()
        self.__V.clear()

    def pop(self, v: Any, default: Any = None) -> Any:
        if v in self:
            self.__delitem__(v)
            return v
        return default

    def popitem(self) -> Tuple[Any, Dict[str, Any]]:
        if not bool(self):
            raise KeyError("popitem(): dictionary is empty")
        v = next(iter(self))
        self.__delitem__(v[0])
        return v

    def __setitem__(self, v: Any, o: Any) -> None:
        if isinstance(o, self.__adj):
            super().__setitem__(v, o)
            self.__V[v] = self.__default_vertex
        else:
            self.__V[v] = o

    def __delitem__(self, v: Any) -> None:
        super().__delitem__(v)
        del self.__V[v]
        for _, u in self:
            counter = set()
            for e in u:
                if e is v:
                    counter.add(e)
            for e in counter:
                del u[e]

    def __iter__(self) -> Iterator:
        return iter(self.items())

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(default_vertex={self.__default_vertex}, default_edge={self.__default_vertex}, G={self})"

    def __str__(self) -> str:
        return dict(self).__str__()

    vertices = property(fget=get_vertices, fdel=del_vertices)
    edges = property(fget=get_edges)
