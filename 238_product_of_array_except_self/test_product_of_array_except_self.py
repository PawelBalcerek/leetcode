import unittest
from product_of_array_except_self import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        nums = [1, 2, 3, 4]
        expected = [24, 12, 8, 6]
        self.assertEqual(self.solution.product_of_array_except_self(nums), expected)

    def test_example2(self):
        nums = [-1, 1, 0, -3, 3]
        expected = [0, 0, 9, 0, 0]
        self.assertEqual(self.solution.product_of_array_except_self(nums), expected)

    def test_minimum_length(self):
        nums = [1, 2]
        expected = [2, 1]
        self.assertEqual(self.solution.product_of_array_except_self(nums), expected)

    def test_all_zeros(self):
        nums = [0, 0, 0]
        expected = [0, 0, 0]
        self.assertEqual(self.solution.product_of_array_except_self(nums), expected)

    def test_negative_numbers(self):
        nums = [-1, -1, -1]
        expected = [1, 1, 1]
        self.assertEqual(self.solution.product_of_array_except_self(nums), expected)

    def test_large_numbers_in_range(self):
        nums = [10, 20, 30]
        expected = [600, 300, 200]
        self.assertEqual(self.solution.product_of_array_except_self(nums), expected)

if __name__ == '__main__':
    unittest.main()
