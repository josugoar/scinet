import unittest

from scinet.core import network


class DataOrientedAPI:
    pass


class FunctionalAPI:
    pass


class TestNetwork(unittest.TestCase):

    def setUp(self):
        self._G = network()

    def test_init(self):
        self.assertFalse(self._G)

    def test_add_vertex(self):
        for v in range(5):
            self._G[v]
            self.assertIn(v, self._G)

    def test_pop(self):
        self.assertEqual("", self._G.pop(0, default=""))
        self.test_add_vertex()
        for v in self._G.vertices:
            self.assertEqual(v, self._G.pop(v))
            self.assertNotIn(v, self._G)

    def test_popitem(self):
        self.test_add_vertex()
        for _ in self._G.vertices:
            self.assertNotIn(self._G.popitem(), self._G.items())
        self.assertRaises(KeyError, self._G.popitem)


class TestNetworkDataOrientedAPI(unittest.TestCase):

    def setUp(self):
        self._G = network()

    def test_add_vertex(self):
        for vertex in range(5):
            self._G.add_vertex(vertex)
            self.assertIn(vertex, self._G)

    def test_add_vertex_data(self):
        self._G.add_vertex(0)
        self.assertDictEqual(self._G.default_vertex, self._G.get_vertices(data=True)[0])
        self._G.add_vertex(0, a=1)
        self.assertDictEqual(dict(a=1), self._G.get_vertices(data=True)[0])
        self._G.add_vertex(0, b=2)
        self.assertDictContainsSubset(dict(a=1), self._G.get_vertices(data=True)[0])

    def test_remove_vertex(self):
        self.test_add_vertex()
        for vertex in self._G.vertices:
            # self._G.remove_vertex(vertex)
            self.assertNotIn(vertex, self._G)

    def test_add_edge(self):
        for vertex in range(5):
            # self._G.add_edge(vertex, vertex + 1)
            self.assertIn(vertex + 1, self._G)

    def test_remove_edge(self):
        self.test_add_edge()
        for source_vertex, target_vertex in self._G.edges:
            ...
            # self._G.remove_edge(source_vertex, target_vertex)
        for vertex in self._G.vertices:
            self.assertFalse(self._G[vertex])

    def test_adjacent(self):
        self.test_add_edge()
        for source_vertex, target_vertex in self._G.edges:
            self.assertTrue(self._G.adjacent(source_vertex, target_vertex))


class TestNetworkFunctionalAPI(unittest.TestCase):

    def setUp(self):
        self._G = network()

    def test_add_vertex(self):
        for vertex in range(5):
            self._G[vertex]
            self.assertIn(vertex, self._G)

    def test_remove_vertex(self):
        self.test_add_vertex()
        for vertex in self._G.vertices:
            del self._G[vertex]
            self.assertNotIn(vertex, self._G)

    def test_add_edge(self):
        for vertex in range(5):
            self._G[vertex][vertex + 1]
            self.assertIn(vertex + 1, self._G)

    def test_remove_edge(self):
        self.test_add_edge()
        for source_vertex, target_vertex in self._G.edges:
            del self._G[source_vertex][target_vertex]
        for vertex in self._G.vertices:
            self.assertFalse(self._G[vertex])

    def test_adjacent(self):
        self.test_add_edge()
        for source_vertex, target_vertex in self._G.edges:
            self.assertTrue(target_vertex in self._G[source_vertex])
