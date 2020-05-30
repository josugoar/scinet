import unittest

from scinet import network


class TestNetwork(unittest.TestCase):

    def setUp(self):
        self.G = network()

    def test_init(self):
        self.assertFalse(self.G)

    def test_add_vertex(self):
        for vertex in range(5):
            self.G[vertex]
            self.assertIn(vertex, self.G)

    def test_remove_vertex(self):
        self.test_add_vertex()
        for vertex in self.G.vertices():
            del self.G[vertex]
            self.assertNotIn(vertex, self.G)

    def test_add_edge(self):
        for source_vertex, target_vertex in enumerate(range(5)):
            self.G[source_vertex][target_vertex]
            self.assertIn((source_vertex, target_vertex), self.G.edges())

    def test_remove_edge(self):
        self.test_add_edge()
        for source_vertex, target_vertex in self.G.edges():
            del self.G[source_vertex][target_vertex]
            self.assertNotIn((source_vertex, target_vertex), self.G.edges())

    def test_adjacent(self):
        self.test_add_edge()
        for source_vertex, target_vertex in self.G.edges():
            self.assertIn(target_vertex, self.G[source_vertex])

    def test_clear(self):
        self.test_add_vertex()
        self.test_add_edge()
        self.G.clear()
        self.assertFalse(self.G)


if __name__ == '__main__':
    unittest.main()
