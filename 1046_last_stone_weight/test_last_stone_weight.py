import unittest
from last_stone_weight import Solution

class TestLastStoneWeight(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        stones = [2, 7, 4, 1, 8, 1]
        self.assertEqual(self.solution.last_stone_weight(stones), 1)

    def test_example_2(self):
        stones = [1]
        self.assertEqual(self.solution.last_stone_weight(stones), 1)

    def test_all_destroyed(self):
        stones = [2, 2]
        self.assertEqual(self.solution.last_stone_weight(stones), 0)

    def test_different_weights(self):
        stones = [2, 4]
        self.assertEqual(self.solution.last_stone_weight(stones), 2)

    def test_multiple_identical_stones(self):
        stones = [1, 1, 1, 1]
        self.assertEqual(self.solution.last_stone_weight(stones), 0)

    def test_large_stones(self):
        stones = [1000, 1000, 500]
        self.assertEqual(self.solution.last_stone_weight(stones), 500)

    def test_constraints_min(self):
        stones = [1000]
        self.assertEqual(self.solution.last_stone_weight(stones), 1000)

if __name__ == '__main__':
    unittest.main()
