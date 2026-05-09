import unittest
from min_cost_climbing_stairs import Solution

class TestMinCostClimbingStairs(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        cost = [10, 15, 20]
        self.assertEqual(self.solution.min_cost_climbing_stairs(cost), 15)

    def test_example_2(self):
        cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
        self.assertEqual(self.solution.min_cost_climbing_stairs(cost), 6)

    def test_minimum_length(self):
        # 2 <= cost.length <= 1000
        cost = [10, 20]
        self.assertEqual(self.solution.min_cost_climbing_stairs(cost), 10)

    def test_all_zeros(self):
        cost = [0, 0, 0, 0]
        self.assertEqual(self.solution.min_cost_climbing_stairs(cost), 0)

    def test_increasing_cost(self):
        cost = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.min_cost_climbing_stairs(cost), 6)

    def test_decreasing_cost(self):
        cost = [5, 4, 3, 2, 1]
        self.assertEqual(self.solution.min_cost_climbing_stairs(cost), 6)
    
    def test_large_costs(self):
        cost = [999, 999, 999]
        self.assertEqual(self.solution.min_cost_climbing_stairs(cost), 999)

if __name__ == '__main__':
    unittest.main()
