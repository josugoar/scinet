from collections import abc, defaultdict
from typing import Any, Iterable, Iterator, Mapping, Tuple, Union
from warnings import warn


# NAMED TUPLES
# TODO: Add directed/undirected edges
# TODO: Optional dict edge key
class Network(abc.MutableMapping):

    __slots__ = "_adj", "_edge", "_node"

    def __init__(self) -> None:
        self._adj = {}
        self._edge = {}
        self._node = {}

    def add_edge(self, source_node: Any, target_node: Any, edge: Any = None, **data: Any) -> Any:
        self.add_nodes({source_node, target_node})
        if target_node not in self._adj[source_node]:
            self._adj[source_node][target_node] = set()
            self._edge[(source_node, target_node, edge)] = {}
        # if edge is None:
        #     try:
        #         keydict = self._adj[u][v]
        #     except KeyError:
        #         return 0
        #     key = len(keydict)
        #     while key in keydict:
        #         key += 1
        else:
            edge_key = edge
        self._adj[source_node][target_node].add(edge)
        if data:
            self._edge[(source_node, target_node, edge)].update(data)
        return edge_key

    def add_edges(self, e: Mapping[Tuple[Iterable[Any], Tuple[Any, Any]], Mapping[str, Any]], /) -> None:
        edge_keys = set()
        for edges, data in e.items():
            edge, vertices = edges
            edge_key = self.add_edge(edge, *vertices, data=data)
            edge_keys.add(edge_key)
        return edge_keys

    def add_node(self, node: Any, /, **data: Any):
        if node not in self._node:
            self._adj[node] = {}
            self._node[node] = {}
        if data:
            self._node[node].update(data)

    def add_nodes(self, n: Iterable[Union[Any, Tuple[Any, Mapping[str, Any]]]], /, **data: Any) -> None:
        for node in n:
            try:
                node_key, node_data = node
                if data:
                    node_data.update(data)
            except TypeError:
                node_key, node_data = node, data
            finally:
                self.add_node(node_key, **node_data)

    def remove_edge(self, edge: Any, /, source_vertex: Any, target_vertex: Any) -> None:
        try:
            self._adj[source_vertex][target_vertex].remove(edge)
            del self._edge[(edge, (source_vertex, target_vertex))]
            if not self._adj[source_vertex][target_vertex]:
                del self._adj[source_vertex][target_vertex]
        except KeyError:
            warn(f"'{edge=} not in '{self.__class__.__name__}'...")

    def remove_edges(self, e: Iterable[Tuple[Any, Tuple[Any, Any]]], /) -> None:
        for edge, vertices in e:
            self.remove_edge(edge, *vertices)

    def remove_node(self, node: Any, /) -> None:
        try:
            del self._adj[node]
            del self._node[node]
            for edge in self._edge:
                source_node, target_node, _ = edge
                if target_node is node:
                    del self._adj[source_node][target_node]
                    del self._edge[edge]
        except KeyError:
            warn(f"'{node}' not in '{self.__class__.__name__}'...")

    def remove_nodes(self, n: Iterable[Any], /) -> None:
        for node in n:
            self.remove_node(node)

    def edge(self, data=False) -> Union[Mapping[Any, Mapping[str, Any]], Iterable[Any]]:
        return dict(self._edge) if data else set(self._edge)

    def node(self, data=False) -> Union[Mapping[Any, Mapping[str, Any]], Iterable[Any]]:
        return dict(self._node) if data else set(self._node)

    def __getitem__(self, vertex: Any) -> Mapping[Any, Iterable[Any]]:
        if vertex not in self._node:
            raise KeyError
        return dict(self._adj[vertex])  # MappingView Proxy

    def __setitem__(self, vertex: Any, data: Mapping[str, Any]) -> None:
        self.add_node(vertex, **data)

    def __delitem__(self, vertex: Any) -> None:
        self.remove_node(vertex)

    def __iter__(self) -> Iterator[Any]:
        return iter(self._adj)

    def __len__(self) -> int:
        return len(self._adj)

    def __str__(self) -> None:
        return str(dict(self))


if __name__ == "__main__":

    def profile(func=None, number=1, sort="cumtime", verbose=False):

        import cProfile
        from functools import wraps, partial

        if not func:
            return partial(profile, number=number, sort=sort, verbose=verbose)

        pr = cProfile.Profile()
        rets = []

        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(number):
                pr.enable()
                ret = func(*args, **kwargs)
                pr.disable()
                rets.append(ret)
                if verbose:
                    pr.print_stats(sort)
            return rets

        return wrapper

    G = Network()
    profile(G.add_nodes, verbose=True)((i for i in range(50)), c=2, b=1)
    # profile(G.add_edges, verbose=False)({(j, (j, j)): {"a": j} for j in range(100)})
    print(G._node)
