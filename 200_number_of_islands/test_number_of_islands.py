import unittest
from number_of_islands import Solution

class TestNumberOfIslands(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        grid = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ]
        self.assertEqual(self.solution.num_of_islands(grid), 1)

    def test_example_2(self):
        grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]
        self.assertEqual(self.solution.num_of_islands(grid), 3)

    def test_only_water(self):
        grid = [
            ["0","0","0"],
            ["0","0","0"]
        ]
        self.assertEqual(self.solution.num_of_islands(grid), 0)

    def test_only_land(self):
        grid = [
            ["1","1","1"],
            ["1","1","1"]
        ]
        self.assertEqual(self.solution.num_of_islands(grid), 1)

    def test_single_cell_land(self):
        grid = [["1"]]
        self.assertEqual(self.solution.num_of_islands(grid), 1)

    def test_single_cell_water(self):
        grid = [["0"]]
        self.assertEqual(self.solution.num_of_islands(grid), 0)

    def test_diagonal_islands(self):
        grid = [
            ["1","0","1"],
            ["0","1","0"],
            ["1","0","1"]
        ]
        self.assertEqual(self.solution.num_of_islands(grid), 5)

if __name__ == "__main__":
    unittest.main()
