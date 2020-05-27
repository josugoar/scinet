import unittest

from scinet.core import network


class TestNet(unittest.TestCase):

    def setUp(self):
        self._G = network()

    def test_init(self):
        self.assertFalse(self._G)

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
        for source_vertex, target_vertex in enumerate(range(5)):
            self._G[source_vertex][target_vertex]
            self.assertIn((source_vertex, target_vertex), self._G.edges)

    def test_remove_edge(self):
        self.test_add_edge()
        for source_vertex, target_vertex in self._G.edges:
            del self._G[source_vertex][target_vertex]
            self.assertNotIn((source_vertex, target_vertex), self._G.edges)

    def test_clear(self):
        self.test_add_vertex()
        self.test_add_edge()
        self._G.clear()
        self.assertFalse(self._G)

    def test_pop(self):
        self.assertEqual("", self._G.pop(0, default=""))
        self.test_add_vertex()
        for vertex in self._G.vertices:
            self.assertEqual(vertex, self._G.pop(vertex))
            self.assertNotIn(vertex, self._G)

    def test_popitem(self):
        self.test_add_vertex()
        for _ in self._G.vertices:
            self.assertNotIn(self._G.popitem(), self._G.items())
        self.assertRaises(KeyError, self._G.popitem)

    def test_adjacent(self):
        self.test_add_edge()
        for source_vertex, target_vertex in self._G.edges:
            self.assertIn(target_vertex, self._G[source_vertex])


if __name__ == '__main__':
    unittest.main()
