import unittest

from pynet.index import net


class TestNet(unittest.TestCase):

    def setUp(self):
        self._G = net()

    def test_add_edge(self):
        ...

    def test_remove_edge(self):
        ...

    def test_add_vertex(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_remove_vertex(self):
        ...

    def test_adjacent(self):
        ...

    def test_neighbors(self):
        ...

    def test_clear(self):
        ...

    def test_pop(self):
        ...

    def test_popitem(self):
        ...

    def test_iter(self):
        ...


if __name__ == '__main__':
    unittest.main()

# G = net()
# # Add vertex
# G[1]
# print(f"Add vertex: {G}", end="\n\n")
# # Remove vertex
# del G[1]
# print(f"Remove vertex: {G}", end="\n\n")
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
