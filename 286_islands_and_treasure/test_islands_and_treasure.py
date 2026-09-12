import unittest

from islands_and_treasure import Solution

INF = 2147483647


class TestIslandsAndTreasure(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        grid = [
            [INF, -1, 0, INF],
            [INF, INF, INF, -1],
            [INF, -1, INF, -1],
            [0, -1, INF, INF],
        ]
        expected = [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]
        self.solution.islandsAndTreasure(grid)
        self.assertEqual(grid, expected)

    def test_example_2(self):
        grid = [[0, -1], [INF, INF]]
        expected = [[0, -1], [1, 2]]
        self.solution.islandsAndTreasure(grid)
        self.assertEqual(grid, expected)

    def test_unreachable_land(self):
        grid = [[INF, -1, 0], [-1, -1, -1], [INF, INF, INF]]
        expected = [[INF, -1, 0], [-1, -1, -1], [INF, INF, INF]]
        self.solution.islandsAndTreasure(grid)
        self.assertEqual(grid, expected)

    def test_no_treasure(self):
        grid = [[INF, INF], [INF, -1]]
        expected = [[INF, INF], [INF, -1]]
        self.solution.islandsAndTreasure(grid)
        self.assertEqual(grid, expected)

    def test_only_treasure(self):
        grid = [[0, 0], [0, 0]]
        expected = [[0, 0], [0, 0]]
        self.solution.islandsAndTreasure(grid)
        self.assertEqual(grid, expected)

    def test_only_water(self):
        grid = [[-1, -1], [-1, -1]]
        expected = [[-1, -1], [-1, -1]]
        self.solution.islandsAndTreasure(grid)
        self.assertEqual(grid, expected)

    def test_single_cell_treasure(self):
        grid = [[0]]
        expected = [[0]]
        self.solution.islandsAndTreasure(grid)
        self.assertEqual(grid, expected)

    def test_single_cell_water(self):
        grid = [[-1]]
        expected = [[-1]]
        self.solution.islandsAndTreasure(grid)
        self.assertEqual(grid, expected)

    def test_single_cell_land(self):
        grid = [[INF]]
        expected = [[INF]]
        self.solution.islandsAndTreasure(grid)
        self.assertEqual(grid, expected)

    def test_single_row(self):
        grid = [[0, INF, -1, INF, 0]]
        expected = [[0, 1, -1, 1, 0]]
        self.solution.islandsAndTreasure(grid)
        self.assertEqual(grid, expected)

    def test_single_column(self):
        grid = [[0], [INF], [INF], [-1], [INF]]
        expected = [[0], [1], [2], [-1], [INF]]
        self.solution.islandsAndTreasure(grid)
        self.assertEqual(grid, expected)

    def test_multiple_treasures(self):
        grid = [[0, INF, 0], [INF, INF, INF], [0, INF, 0]]
        expected = [[0, 1, 0], [1, 2, 1], [0, 1, 0]]
        self.solution.islandsAndTreasure(grid)
        self.assertEqual(grid, expected)


if __name__ == "__main__":
    unittest.main()
