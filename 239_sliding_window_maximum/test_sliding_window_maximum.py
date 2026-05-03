import unittest
from sliding_window_maximum import Solution

class TestSlidingWindowMaximum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        expected = [3, 3, 5, 5, 6, 7]
        self.assertEqual(self.solution.sliding_window_maximum(nums, k), expected)

    def test_example_2(self):
        nums = [1]
        k = 1
        expected = [1]
        self.assertEqual(self.solution.sliding_window_maximum(nums, k), expected)

    def test_window_size_equals_array_length(self):
        nums = [1, 2, 3, 4, 5]
        k = 5
        expected = [5]
        self.assertEqual(self.solution.sliding_window_maximum(nums, k), expected)

    def test_decreasing_elements(self):
        nums = [5, 4, 3, 2, 1]
        k = 2
        expected = [5, 4, 3, 2]
        self.assertEqual(self.solution.sliding_window_maximum(nums, k), expected)

    def test_increasing_elements(self):
        nums = [1, 2, 3, 4, 5]
        k = 3
        expected = [3, 4, 5]
        self.assertEqual(self.solution.sliding_window_maximum(nums, k), expected)

    def test_negative_numbers(self):
        nums = [-7, -8, 7, 5, 7, 1, 6, 0]
        k = 4
        expected = [7, 7, 7, 7, 7]
        self.assertEqual(self.solution.sliding_window_maximum(nums, k), expected)

    def test_all_same_elements(self):
        nums = [2, 2, 2, 2]
        k = 2
        expected = [2, 2, 2]
        self.assertEqual(self.solution.sliding_window_maximum(nums, k), expected)

if __name__ == '__main__':
    unittest.main()
