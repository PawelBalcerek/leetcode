import unittest

from rotting_oranges import Solution


class TestRottingOranges(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
        self.assertEqual(self.solution.rotting_oranges(grid), 4)

    def test_example_2(self):
        grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
        self.assertEqual(self.solution.rotting_oranges(grid), -1)

    def test_example_3(self):
        grid = [[0, 2]]
        self.assertEqual(self.solution.rotting_oranges(grid), 0)

    def test_single_cell_empty(self):
        grid = [[0]]
        self.assertEqual(self.solution.rotting_oranges(grid), 0)

    def test_single_cell_fresh(self):
        grid = [[1]]
        self.assertEqual(self.solution.rotting_oranges(grid), -1)

    def test_single_cell_rotten(self):
        grid = [[2]]
        self.assertEqual(self.solution.rotting_oranges(grid), 0)

    def test_all_empty(self):
        grid = [[0, 0], [0, 0]]
        self.assertEqual(self.solution.rotting_oranges(grid), 0)

    def test_all_fresh(self):
        grid = [[1, 1], [1, 1]]
        self.assertEqual(self.solution.rotting_oranges(grid), -1)

    def test_all_rotten(self):
        grid = [[2, 2], [2, 2]]
        self.assertEqual(self.solution.rotting_oranges(grid), 0)

    def test_single_row_reachable(self):
        grid = [[2, 1, 1, 1, 1]]
        self.assertEqual(self.solution.rotting_oranges(grid), 4)

    def test_single_row_rotten_in_middle(self):
        grid = [[1, 2, 1]]
        self.assertEqual(self.solution.rotting_oranges(grid), 1)

    def test_single_row_blocked(self):
        grid = [[1, 0, 2]]
        self.assertEqual(self.solution.rotting_oranges(grid), -1)

    def test_single_column_reachable(self):
        grid = [[2], [1], [1]]
        self.assertEqual(self.solution.rotting_oranges(grid), 2)

    def test_single_column_blocked(self):
        grid = [[1], [0], [2]]
        self.assertEqual(self.solution.rotting_oranges(grid), -1)

    def test_multiple_rotten_sources(self):
        grid = [[2, 1, 1], [1, 1, 1], [0, 1, 2]]
        self.assertEqual(self.solution.rotting_oranges(grid), 2)

    def test_disconnected_fresh_oranges(self):
        grid = [[2, 1, 0, 1]]
        self.assertEqual(self.solution.rotting_oranges(grid), -1)


if __name__ == "__main__":
    unittest.main()
