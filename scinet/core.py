from collections import defaultdict, namedtuple
from typing import Any, Dict, Mapping, FrozenSet, Set, Tuple, Union


class network(defaultdict):
    """Network science abstract data type

    Extends:
        defaultdict
    """

    # TODO: Create DictList data structure to be able to store multiple edges pointing to same target vertex
    class __adj(defaultdict):
        """Adjacency list

        Extends:
            defaultdict
        """

        def __init__(self, G: "network") -> None:
            """Initialize new adjacency list

            Arguments:
                G {network}
            """
            super().__init__(lambda: self.__G.default_edge)
            self.__G = G

        def __getitem__(self, vertex: Any) -> Mapping[str, Any]:
            """Return vertex edge and create new vertex if not in network

            Arguments:
                vertex {Any}

            Returns:
                Mapping[str, Any]
            """
            if vertex not in self.__G:
                self.__G[vertex]
            return super().__getitem__(vertex)

        def __setitem__(self, vertex: Any, edge: Mapping[str, Any]) -> None:
            """Set vertex edge and create new vertex if not in network

            Arguments:
                vertex {Any}
                edge {Mapping[str, Any]}
            """
            if vertex not in self.__G:
                self.__G[vertex]
            super().__setitem__(vertex, edge)

        def __repr__(self) -> str:
            """Return dictionary representation of adjacency list

            Returns:
                str
            """
            return dict.__repr__(self)

    def __init__(self, default_vertex: Mapping[str, Any] = dict(), default_edge: Mapping[str, Any] = dict()) -> None:
        """Initialize new network

        Keyword Arguments:
            default_vertex {Mapping[str, Any]} -- (default: {dict()})
            default_edge {Mapping[str, Any]} -- (default: {dict()})
        """
        super().__init__(lambda: self.__adj(self))
        self.default_vertex = default_vertex
        self.default_edge = default_edge
        self.__vertices = dict()
        # TODO: Use edges dict
        self.__edges = dict()

    def add_vertex(self, vertex: Any, **data: Any) -> Mapping[str, Any]:
        """Add vertex to network or update data if vertex in network

        Arguments:
            vertex {Any}

        Keyword Arguments:
            data {Any}

        Returns:
            Mapping[str, Any]
        """
        if data:
            if vertex in self:
                self.__vertices[vertex].update(data)
            else:
                self[vertex] = data
        return self[vertex]

    def remove_vertex(self, vertex: Any) -> None:
        """Remove vertex from network

        Arguments:
            vertex {Any}
        """
        del self[vertex]

    def add_edge(self, source_vertex: Any, target_vertex: Any, **data: Any) -> Mapping[str, Any]:
        """Add edge to network or update if edge in network

        Arguments:
            source_vertex {Any}
            target_vertex {Any}

        Keyword Arguments:
            data {Any}

        Returns:
            Mapping[str, Any]
        """
        if data:
            if target_vertex in self[source_vertex]:
                self[source_vertex][target_vertex].update(data)
            else:
                self[source_vertex][target_vertex] = data
        return self[source_vertex][target_vertex]

    def remove_edge(self, source_vertex: Any, target_vertex: Any) -> None:
        """Remove edge from network

        Arguments:
            source_vertex {Any}
            target_vertex {Any}
        """
        del self[source_vertex][target_vertex]

    def adjacent(self, source_vertex: Any, target_vertex: Any) -> bool:
        """Return whether source vertex and target vertex are adjacent

        Arguments:
            source_vertex {Any}
            target_vertex {Any}

        Raises:
            KeyError: if not (source_vertex in network and target_vertex in network)

        Returns:
            bool
        """
        if not (source_vertex in self and target_vertex in self):
            raise KeyError
        return target_vertex in self[source_vertex]

    def neighbors(self, vertex: Any) -> Tuple[Tuple[Any, Any], ...]:
        """Return neighbors of vertex

        Arguments:
            vertex {Any}

        Raises:
            KeyError: if vertex not in network

        Returns:
            Tuple[Tuple[Any, Any], ...]
        """
        if vertex not in self:
            raise KeyError
        return tuple(neighbor for neighbor in self[vertex].items())

    def clear(self) -> None:
        """Clear network
        """
        super().clear()
        self.__vertices.clear()

    def pop(self, vertex: Any, default: Any = None) -> Any:
        """Return deleted vertex from network or default if vertex not in network

        Arguments:
            vertex {Any}

        Keyword Arguments:
            default {Any} -- (default: {None})

        Returns:
            Any
        """
        if vertex in self:
            del self[vertex]
            return vertex
        return default

    def popitem(self) -> Tuple[Any, Mapping[str, Any]]:
        """Return delete vertex edge pair from network in insertion order

        Raises:
            KeyError: if not bool(network)

        Returns:
            Tuple[Any, Mapping[str, Any]]
        """
        if not bool(self):
            raise KeyError
        o = next(iter(self.items()))
        del self[o[0]]
        return o

    def get_vertices(self, data: bool = False) -> Union[Mapping[Any, Mapping[str, Any]], FrozenSet[Any]]:
        """Return network vertices

        Keyword Arguments:
            data {bool} -- (default: {False})

        Returns:
            Union[Mapping[Any, Mapping[str, Any]], FrozenSet[Any]]
        """
        return self.__vertices if data else frozenset(self.__vertices.keys())

    def del_vertices(self) -> None:
        """Delete network vertices data
        """
        self.__vertices.update(dict.fromkeys(self.__vertices, self.__default_vertex))

    # TODO: Fix
    def get_edges(self, data: bool = False) -> Union[Mapping[Tuple[Any, Any], Mapping[str, Any]], Set[Tuple[Any, Any]]]:
        """Return network edges

        Keyword Arguments:
            data {bool} -- (default: {False})

        Returns:
            Union[Mapping[Tuple[Any, Any], Mapping[str, Any]], Set[Tuple[Any, Any]]]
        """
        Edge = namedtuple("Edge", "source_vertex target_vertex")
        edges = dict() if data else set()
        for v, e in self.items():
            for u in e:
                edges.update({Edge(v, u): e[u]}) if data else edges.add(Edge(v, u))
        return edges

    def del_edges(self) -> None:
        """Delete network edge data
        """
        for edge in self.values():
            edge.update(dict.fromkeys(edge, self.__default_edge))

    @property
    def default_vertex(self) -> Mapping[str, Any]:
        """Return default vertex used for vertex addition

        Returns:
            Mapping[str, Any]
        """
        return self.__default_vertex

    @default_vertex.setter
    def default_vertex(self, default_vertex: Mapping[str, Any]) -> None:
        """Set default vertex used for vertex addition

        Arguments:
            default_vertex {Mapping[str, Any]}
        """
        self.__default_vertex = default_vertex

    @property
    def default_edge(self) -> Mapping[str, Any]:
        """Return default edge used for edge addition

        Returns:
            Mapping[str, Any]
        """
        return self.__default_edge

    @default_edge.setter
    def default_edge(self, default_edge: Mapping[str, Any]) -> None:
        """Set default edge used for edge addition

        Arguments:
            default_edge {Mapping[str, Any]}
        """
        self.__default_edge = default_edge

    def __setitem__(self, vertex: Any, data: Any) -> None:
        """Add vertex to network and create new vertex if not in network

        Arguments:
            vertex {Any}
            data {Any}
        """
        if isinstance(data, self.__adj):
            super().__setitem__(vertex, data)
            self.__vertices[vertex] = self.__default_vertex
        else:
            if vertex not in self:
                self[vertex]
            self.__vertices[vertex] = data

    def __delitem__(self, vertex: Any) -> None:
        """Delete vertex from network

        Arguments:
            vertex {Any}

        Raises:
            KeyError: if vertex not in network
        """
        if vertex not in self:
            raise KeyError
        super().__delitem__(vertex)
        del self.__vertices[vertex]
        for source_vertex, target_vertex in self.edges:
            if target_vertex is vertex:
                del self[source_vertex][target_vertex]

    def __repr__(self) -> str:
        """Return network attribute representation

        Returns:
            str
        """
        return f"{self.__class__.__name__}(<{self.__default_vertex=}, {self.__default_edge=}>, {self})"

    def __str__(self) -> str:
        """Return network dictionary representation

        Returns:
            str
        """
        return dict.__repr__(self)

    vertices = property(fget=get_vertices, fdel=del_vertices)
    edges = property(fget=get_edges, fdel=del_edges)


if __name__ == "__main__":
    G = network(default_vertex=dict(name=""), default_edge=dict(weight=0))
    G[1] = dict(name="JoshGoA")
    G[2] = dict(name="Lol")
    G[1][2] = dict(name="LAAol")
    del G.edges
    print(G)
    print(G.get_vertices(data=True))
    print(G.get_edges(data=True))
