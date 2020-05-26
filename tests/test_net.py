import unittest

from scinet.core import network


class TestNet(unittest.TestCase):

    def setUp(self):
        self._G = network()

    def test_init(self):
        self.assertFalse(self._G)

    def test_add_edge(self):
        # for v in range(5):
        #     self._G[v]
        ...

    def test_remove_edge(self):
        ...

    def test_add_vertex(self):
        for v in range(5):
            self._G[v]
            self.assertIn(v, self._G)

    def test_remove_vertex(self):
        self.test_add_vertex()
        for v in self._G.vertices:
            del self._G[v]
            self.assertNotIn(v, self._G)

    def test_adjacent(self):
        ...

    def test_neighbors(self):
        ...

    def test_clear(self):
        ...

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

    def test_iter(self):
        ...


if __name__ == '__main__':
    unittest.main()

# # Pop vertex
# G[1]
# print(G.pop(1))
# print(f"Pop vertex: {G}", end="\n\n")
# # Popitem vertex
# G[1]
# G[1][2] = dict(weight=0)
# print(G.popitem())
# print(f"Popitem vertex: {G}", end="\n\n")
# # Add edge
# G[1][2] = dict(weight=0)
# print(f"Add edge: {G}", end="\n\n")
# # Remove edge
# del G[1][2]
# print(f"Remove edge: {G}", end="\n\n")
# # Range through vertex
# G[1][2] = dict(weight=0)
# G[1][3] = dict(weight=0)
# G[1][4] = dict(weight=0)
# for v, e in G:
#     print(v, e)
# print(f"Range through vertex: {G}", end="\n\n")
# # Range through vertex neighbors
# for v in G[1]:
#     print(v)
# print(f"Range through vertex neighbors: {G}", end="\n\n")
# # dict().pop()
# # dict().popitem()
# # dict().update()
