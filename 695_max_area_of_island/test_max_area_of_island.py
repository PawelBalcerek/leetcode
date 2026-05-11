import unittest
from max_area_of_island import Solution

class TestMaxAreaOfIsland(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        grid = [
            [0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]
        ]
        self.assertEqual(self.solution.max_area_of_island(grid), 6)

    def test_example_2(self):
        grid = [[0,0,0,0,0,0,0,0]]
        self.assertEqual(self.solution.max_area_of_island(grid), 0)

    def test_no_islands(self):
        grid = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.assertEqual(self.solution.max_area_of_island(grid), 0)

    def test_all_land(self):
        grid = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        self.assertEqual(self.solution.max_area_of_island(grid), 9)

    def test_single_cell_island(self):
        grid = [[1]]
        self.assertEqual(self.solution.max_area_of_island(grid), 1)

    def test_single_cell_water(self):
        grid = [[0]]
        self.assertEqual(self.solution.max_area_of_island(grid), 0)

    def test_diagonal_islands(self):
        grid = [
            [1, 0, 1],
            [0, 1, 0],
            [1, 0, 1]
        ]
        self.assertEqual(self.solution.max_area_of_island(grid), 1)

if __name__ == "__main__":
    unittest.main()
