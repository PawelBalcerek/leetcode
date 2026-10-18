import unittest

from iterative_graph_valid_tree import Solution as IterativeSolution
from recursive_graph_valid_tree import Solution as RecursiveSolution


class TestGraphValidTree(unittest.TestCase):
    def setUp(self):
        self.solutions = [
            IterativeSolution(),
            RecursiveSolution(),
        ]

    def assert_valid_tree(self, n: int, edges: list[list[int]], expected: bool):
        for solution in self.solutions:
            with self.subTest(solution=solution.__class__.__module__):
                self.assertEqual(solution.graph_valid_tree(n, edges), expected)

    def test_example_1(self):
        self.assert_valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]], True)

    def test_example_2(self):
        self.assert_valid_tree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], False)

    def test_single_node(self):
        self.assert_valid_tree(1, [], True)

    def test_two_nodes_connected(self):
        self.assert_valid_tree(2, [[0, 1]], True)

    def test_two_nodes_disconnected(self):
        self.assert_valid_tree(2, [], False)

    def test_disconnected_components_with_cycle_and_n_minus_1_edges(self):
        self.assert_valid_tree(4, [[0, 1], [1, 2], [2, 0]], False)

    def test_disconnected_components_with_isolated_node_0(self):
        self.assert_valid_tree(4, [[1, 2], [2, 3], [3, 1]], False)

    def test_too_few_edges(self):
        self.assert_valid_tree(4, [[0, 1], [1, 2]], False)

    def test_too_many_edges(self):
        self.assert_valid_tree(3, [[0, 1], [1, 2], [0, 2]], False)

    def test_line_graph(self):
        self.assert_valid_tree(5, [[0, 1], [1, 2], [2, 3], [3, 4]], True)

    def test_star_graph(self):
        self.assert_valid_tree(5, [[0, 1], [0, 2], [0, 3], [0, 4]], True)

    def test_two_separate_trees(self):
        self.assert_valid_tree(4, [[0, 1], [2, 3]], False)

    def test_large_star_tree(self):
        n = 2000
        edges = [[0, i] for i in range(1, n)]
        self.assert_valid_tree(n, edges, True)

    def test_large_disconnected_with_cycle(self):
        n = 500
        edges = [[i, i + 1] for i in range(n - 2)] + [[0, n - 2]]
        self.assert_valid_tree(n, edges, False)


if __name__ == "__main__":
    unittest.main()
