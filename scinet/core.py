from collections import defaultdict, namedtuple
from typing import Any, Iterator, List, Mapping, Optional, Tuple, Union


__all__ = ["network"]


# TODO: Implement edge directed property
class network(defaultdict):
    """Network science abstract data type

    Extends:
        defaultdict
    """

    # TODO: Create DictList data structure to be able to store multiple edges pointing to same target vertex
    class _adj(defaultdict):
        """Adjacency list

        Extends:
            defaultdict
        """

        def __init__(self, network: "network", source_vertex: Any) -> None:
            """Initialize new adjacency list

            Arguments:
                network {network}
                source_vertex {Any}
            """
            super().__init__(lambda: network.default_edge)
            network[source_vertex] = self
            self.__network = network
            self.__source_vertex = source_vertex

        def __getitem__(self, target_vertex: Any) -> Mapping[str, Any]:
            """Create new vertex if vertex not in network and edge if edge not in adjacency list and return edge data

            Arguments:
                target_vertex {Any}

            Returns:
                Mapping[str, Any]
            """
            self.__network[target_vertex]
            return super().__getitem__(target_vertex)

        def __setitem__(self, target_vertex: Any, data: Mapping[str, Any]) -> None:
            """Create new vertex if vertex not in network and edge if edge not in adjacency list and set edge data

            Arguments:
                vertex {Any}
                data {Mapping[str, Any]}

            Raises:
                TypeError: if data not of type Mapping[str, Any]
            """
            try:
                dict(**data)
            except TypeError as e:
                raise TypeError(f"'data: {data}' not of type 'Mapping[str, Any]'...") from e
            self.__network[target_vertex]
            self.__network._edges[(self.__source_vertex, target_vertex)] = data
            super().__setitem__(target_vertex, data)

        def __delitem__(self, target_vertex: Any) -> None:
            """Delete edge from adjacency list

            Arguments:
                target_vertex {Any}
            """
            del self.__network._edges[(self.__source_vertex, target_vertex)]
            super().__delitem__(target_vertex)

        def __repr__(self) -> str:
            """Return adjacency list dictionary representation

            Returns:
                str
            """
            return dict.__repr__(self)

    def __init__(self, default_vertex: Mapping[str, Any] = {}, default_edge: Mapping[str, Any] = {}) -> None:
        """Initialize new network

        Keyword Arguments:
            default_vertex {Mapping[str, Any]} -- (default: {dict()})
            default_edge {Mapping[str, Any]} -- (default: {dict()})
        """
        super().__init__(lambda vertex: network._adj(network=self, source_vertex=vertex))
        self._vertices = {}
        self._edges = {}
        self.default_vertex = default_vertex
        self.default_edge = default_edge

    # TODO: Implement
    def subgraph(self, vertices=[], edges=[]):
        pass

    def clear(self) -> None:
        """Remove network vertices and edges
        """
        super().clear()
        self._vertices.clear()
        self._edges.clear()

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
        """Return deleted vertex adjacency list pair from network in LIFO order

        Raises:
            KeyError: if not network

        Returns:
            Tuple[Any, Mapping[str, Any]]
        """
        if not self:
            raise KeyError("'network' is empty...")
        vertex, adj = next(reversed(self.items()))
        del self[vertex]
        return vertex, adj

    # TODO: Implement
    def setdefault(self, data, default=None):
        if data in self.values():
            return data
        return default

    # TODO: Implement
    def update(self, vertices=None, edges=None):
        super().update()

    def vertices(self, data: bool = False) -> Union[Mapping[Any, Mapping[str, Any]], List[Any]]:
        """Return network vertices

        Keyword Arguments:
            data {bool} -- (default: {False})

        Returns:
            Union[Mapping[Any, Mapping[str, Any]], List[Any]]
        """
        return dict(self._vertices) if data else list(self._vertices)

    def edges(self, data: bool = False) -> Union[Mapping[Tuple[Any, Any], Mapping[str, Any]], List[Tuple[Any, Any]]]:
        """Return network edges

        Keyword Arguments:
            data {bool} -- (default: {False})

        Returns:
            Union[Mapping[Tuple[Any, Any], Mapping[str, Any]], List[Tuple[Any, Any]]]
        """
        return dict(self._edges) if data else list(self._edges)

    @property
    def default_vertex(self) -> Mapping[str, Any]:
        """Return default vertex

        Returns:
            Mapping[str, Any]
        """
        return self.__default_vertex

    @default_vertex.setter
    def default_vertex(self, default_vertex: Mapping[str, Any]) -> None:
        """Set default vertex

        Arguments:
            default_vertex {Mapping[str, Any]}

        Raises:
            TypeError: if default_vertex not of type Mapping[str, Any]
        """
        try:
            self.__default_vertex = dict(**default_vertex)
        except TypeError as e:
            raise TypeError(f"'default_edge: {default_vertex}' not of type 'Mapping[str, Any]'...") from e

    @property
    def default_edge(self) -> Mapping[str, Any]:
        """Return default edge

        Returns:
            Mapping[str, Any]
        """
        return self.__default_edge

    @default_edge.setter
    def default_edge(self, default_edge: Mapping[str, Any]) -> None:
        """Set default edge

        Arguments:
            default_edge {Mapping[str, Any]}

        Raises:
            TypeError: if default_edge not of type Mapping[str, Any]
        """
        try:
            self.__default_edge = dict(**default_edge)
        except TypeError as e:
            raise TypeError(f"'default_edge: {default_edge}' not of type 'Mapping[str, Any]'...") from e

    # TODO: Implement
    def __getitem__(self, vertex: Any) -> Mapping[str, Any]:
        """Create new vertex if vertex not in network and return vertex

        Arguments:
            vertex {Any}

        Returns:
            Mapping[str, Any]
        """
        if isinstance(vertex, slice):
            pass
        return super().__getitem__(vertex)

    def __setitem__(self, vertex: Any, data: Mapping[str, Any]) -> None:
        """Create new vertex if vertex not in network and set vertex data

        Arguments:
            vertex {Any}
            data {Mapping[str, Any]}

        Raises:
            TypeError: if data not of type Mapping[str, Any]
        """
        if isinstance(data, self._adj):
            super().__setitem__(vertex, data)
            self._vertices[vertex] = self.__default_vertex
        else:
            try:
                self[vertex]
                self._vertices[vertex] = dict(**data)
            except TypeError as e:
                raise TypeError(f"'data: {data}' not of type 'Mapping[str, Any]'...") from e

    def __delitem__(self, vertex: Any) -> None:
        """Delete vertex from network

        Arguments:
            vertex {Any}

        Raises:
            KeyError: if vertex not in network
        """
        try:
            super().__delitem__(vertex)
            del self._vertices[vertex]
            for source_vertex, target_vertex in self.edges():
                if target_vertex is vertex:
                    del self[source_vertex][target_vertex]
        except KeyError as e:
            raise KeyError(f"'vertex: {vertex}' not in 'network'...") from e

    def __missing__(self, vertex: Any) -> Mapping[str, Any]:
        """Create new adjacency list and return vertex adjacency list

        Arguments:
            vertex {Any}

        Raises:
            KeyError: if default_factory is None

        Returns:
            Mapping[str, Any]
        """
        if self.default_factory is None:
            raise KeyError(vertex)
        return self.default_factory(vertex)  # pylint: disable=not-callable

    # TODO: Implement
    def __iter__(self, order: Optional[str] = None) -> Iterator[Any]:
        """Return network vertex iterator

        Keyword Arguments:
            order {Optional[str]} -- (default: {None})

        Returns:
            Iterator[Any]
        """
        if order is not None:
            pass
        return super().__iter__()

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


if __name__ == "__main__":
    G = network()
    G[1]
    G[2][1]
    G.pop(1)
    print(G)
