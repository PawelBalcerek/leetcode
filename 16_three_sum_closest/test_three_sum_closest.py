import unittest
from three_sum_closest import Solution

class TestThreeSumClosest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [-1, 2, 1, -4]
        target = 1
        expected = 2
        self.assertEqual(self.solution.three_sum_closest(nums, target), expected)

    def test_example_2(self):
        nums = [0, 0, 0]
        target = 1
        expected = 0
        self.assertEqual(self.solution.three_sum_closest(nums, target), expected)

    def test_all_negative(self):
        nums = [-5, -4, -3, -2, -1]
        target = -10
        expected = -10 # (-5 + -4 + -1) or (-5 + -3 + -2) or (-4 + -3 + -2)? Wait: -5-4-1 = -10. Correct.
        self.assertEqual(self.solution.three_sum_closest(nums, target), expected)

    def test_large_target(self):
        nums = [1, 1, 1, 0]
        target = 100
        expected = 3
        self.assertEqual(self.solution.three_sum_closest(nums, target), expected)

    def test_small_target(self):
        nums = [1, 1, 1, 0]
        target = -100
        expected = 2 # 0 + 1 + 1
        self.assertEqual(self.solution.three_sum_closest(nums, target), expected)

    def test_minimum_length(self):
        nums = [1, 2, 3]
        target = 10
        expected = 6
        self.assertEqual(self.solution.three_sum_closest(nums, target), expected)

    def test_duplicate_elements(self):
        nums = [1, 1, 1, 1]
        target = 0
        expected = 3
        self.assertEqual(self.solution.three_sum_closest(nums, target), expected)

    def test_extreme_values(self):
        nums = [-1000, -1000, -1000, 1000, 1000, 1000]
        target = 10000
        expected = 3000
        self.assertEqual(self.solution.three_sum_closest(nums, target), expected)
        
        target = -10000
        expected = -3000
        self.assertEqual(self.solution.three_sum_closest(nums, target), expected)

if __name__ == "__main__":
    unittest.main()
