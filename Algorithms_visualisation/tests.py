import unittest
from graph_representation import AdjacencyList, AdjacencyMatrix
from MST_algorithms import MinimumSpanningTree, UnionFind


class TestAdjacencyList(unittest.TestCase):

    def setUp(self):
        self.L = AdjacencyList()

        for v in ['A', 'B', 'C', 'D']:
            self.L.insert_vertex(v)

        self.L.insert_edge('A', 'B', 1)
        self.L.insert_edge('B', 'D', 2)
        self.L.insert_edge('C', 'D', 45)
        self.L.insert_edge('C', 'A', 4)

    def test_insert_vertex_and_edge(self):
        r = {0: [(1, 1)], 1: [(3, 2)], 2: [(3, 45), (0, 4)], 3: []}
        self.assertEqual(self.L.lst_nei, r)

    def test_delete_vertex(self):
        self.L.delete_vertex('C')
        expected_result = {0: [(1, 1)], 1: [(2, 2)], 2: []}
        self.assertEqual(self.L.lst_nei, expected_result)

    def test_delete_vertex2(self):
        self.L.insert_vertex('Kappa')
        insert_edges = [('A', 'Kappa', 8), ('B', 'Kappa', 3), ('C', 'Kappa', 1)]

        for v_start, v_end, cost in insert_edges:
            self.L.insert_edge(v_start, v_end, cost)
            self.L.insert_edge(v_end, v_start, cost)

        self.L.delete_vertex('A')

        result = {0: [(2, 2), (3, 3)],  # B
                  1: [(2, 45), (3, 1)],  # C
                  2: [],  # D
                  3: [(0, 3), (1, 1)]}  # Kappa

        self.assertEqual(self.L.lst_nei, result)

    def test_delete_edge(self):
        self.L.delete_edge('A', 'B')
        self.L.delete_edge('C', 'D')

        r = {0: [], 1: [(3, 2)], 2: [(0, 4)], 3: []}

        self.assertEqual(self.L.lst_nei, r)

    def test_get_vertex_idx(self):
        self.assertIs(self.L.get_vertex_idx('C'), 2)

    def test_get_vertex(self):
        self.assertIs(self.L.get_vertex(1), 'B')

    def test_neighbours(self):
        result = self.L.neighbours(2)
        self.assertEqual(result, [(3, 45), (0, 4)])

    def test_order(self):
        for v in ['Z', 'Zz', 'ZzZ']:
            self.L.insert_vertex(v)
        n = self.L.order()

        self.assertEqual(n, 7)

    def test_size(self):
        self.assertEqual(self.L.size(), 4)

    def test_edges(self):
        expected_result = [('A', 'B', 1), ('B', 'D', 2), ('C', 'D', 45), ('C', 'A', 4)]
        self.assertEqual(self.L.edges(), expected_result)


class TestAdjacencyMatrix(unittest.TestCase):

    def setUp(self) -> None:
        self.M = AdjacencyMatrix()

        vertexes = ['A', 'B', 'C', 'D', 'E']
        edges = [('A', 'B', 5), ('C', 'D', 1), ('C', 'E', 2), ('B', 'D', 4)]

        for vertex in vertexes:
            self.M.insert_vertex(vertex)

        for v_start, v_end, weight in edges:
            self.M.insert_edge(v_start, v_end, weight)
            self.M.insert_edge(v_end, v_start, weight)

    def test_insert_vertex_and_edges(self):
        M = [[0, 1, 0, 0, 0],
             [1, 0, 0, 1, 0],
             [0, 0, 0, 1, 1],
             [0, 1, 1, 0, 0],
             [0, 0, 1, 0, 0]]

        W = [[0, 5, 0, 0, 0],
             [5, 0, 0, 4, 0],
             [0, 0, 0, 1, 2],
             [0, 4, 1, 0, 0],
             [0, 0, 2, 0, 0]]

        self.assertEqual(self.M.matrix, M)
        self.assertEqual(self.M.edge_weight, W)

    def test_delete_vertex(self):
        self.M.delete_vertex('A')

        M = [[0, 0, 1, 0],
             [0, 0, 1, 1],
             [1, 1, 0, 0],
             [0, 1, 0, 0]]

        W = [[0, 0, 4, 0],
             [0, 0, 1, 2],
             [4, 1, 0, 0],
             [0, 2, 0, 0]]

        self.assertEqual(self.M.matrix, M)
        self.assertEqual(self.M.edge_weight, W)

    def test_delete_edge(self):
        self.M.delete_edge('B', 'D')

        M = [[0, 1, 0, 0, 0],
             [1, 0, 0, 0, 0],
             [0, 0, 0, 1, 1],
             [0, 1, 1, 0, 0],
             [0, 0, 1, 0, 0]]

        self.assertEqual(self.M.matrix, M)

    def test_neighbours(self):
        results = self.M.neighbours(3)

        self.assertEqual(results, [1, 2])


class TestMinimumSpanningTree(unittest.TestCase):

    def setUp(self):
        self.MST = MinimumSpanningTree()
        vertexes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

        for v in vertexes:
            self.MST.insert_vertex(v)

        edges = [('A', 'B', 7), ('A', 'D', 5), ('B', 'C', 8), ('B', 'D', 9), ('B', 'E', 7)
                 , ('C', 'E', 5), ('D', 'E', 15), ('D', 'F', 6), ('E', 'F', 8), ('E', 'G', 9),
                 ('F', 'G', 11)]

        for v1, v2, cost in edges:
            self.MST.insert_edge(v1, v2, cost)
            self.MST.insert_edge(v2, v1, cost)

    def test_prime_algorithm(self):
        result_edges, total_cost = self.MST.prime_algorithm('A')
        R = [('A', 'D', 5), ('D', 'F', 6), ('A', 'B', 7), ('B', 'E', 7), ('E', 'C', 5), ('E', 'G', 9)]

        self.assertEqual(result_edges, R)
        self.assertEqual(total_cost, 39)

    def test_kruskal_algorithm(self):
        result_edges, total_cost = self.MST.kruskal_algorithm()
        R = [('A', 'D', 5), ('C', 'E', 5), ('D', 'F', 6), ('A', 'B', 7), ('B', 'E', 7), ('E', 'G', 9)]

        self.assertEqual(result_edges, R)
        self.assertEqual(total_cost, 39)


class TestUnionFindStructure(unittest.TestCase):

    def setUp(self):
        self.set = UnionFind()

        for _ in range(5):
            self.set.add_vertex()

        self.set.union(0, 4)
        self.set.union(1, 2)

    def test_find(self):
        self.assertEqual(4, self.set.find(4))

    def test_same_component(self):
        self.assertTrue(self.set.same_components(0, 4))
        self.assertFalse(self.set.same_components(0, 1))


if __name__ == '__main__':
    unittest.main()