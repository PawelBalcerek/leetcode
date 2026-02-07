import unittest

from four_sum import Solution as IterativeSolution
from four_sum_recursive import Solution as RecursiveSolution


class TestFourSum(unittest.TestCase):
    def setUp(self):
        self.iterative_solution = IterativeSolution()
        self.recursive_solution = RecursiveSolution()

    def assert_nested_lists_equal(self, actual, expected):
        actual_sorted = sorted([sorted(x) for x in actual])
        expected_sorted = sorted([sorted(x) for x in expected])
        self.assertEqual(actual_sorted, expected_sorted)

    def run_on_both(self, nums, target, expected):
        # Test Iterative
        self.assert_nested_lists_equal(
            self.iterative_solution.four_sum(nums, target), expected
        )
        # Test Recursive
        self.assert_nested_lists_equal(
            self.recursive_solution.four_sum_recursive(nums, target), expected
        )

    def test_example1(self):
        nums = [1, 0, -1, 0, -2, 2]
        target = 0
        expected = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
        self.run_on_both(nums, target, expected)

    def test_example2(self):
        nums = [2, 2, 2, 2, 2]
        target = 8
        expected = [[2, 2, 2, 2]]
        self.run_on_both(nums, target, expected)

    def test_empty_array(self):
        nums = []
        target = 0
        expected = []
        self.run_on_both(nums, target, expected)

    def test_small_array(self):
        nums = [1, 2, 3]
        target = 6
        expected = []
        self.run_on_both(nums, target, expected)

    def test_no_solution(self):
        nums = [1, 2, 3, 4]
        target = 11
        expected = []
        self.run_on_both(nums, target, expected)

    def test_all_zeros(self):
        nums = [0, 0, 0, 0]
        target = 0
        expected = [[0, 0, 0, 0]]
        self.run_on_both(nums, target, expected)

    def test_large_numbers(self):
        nums = [10**9, 10**9, 10**9, 10**9]
        target = 4 * 10**9
        expected = [[10**9, 10**9, 10**9, 10**9]]
        self.run_on_both(nums, target, expected)

    def test_negative_numbers(self):
        nums = [-1, -2, -3, -4, -5]
        target = -10
        expected = [[-4, -3, -2, -1]]
        self.run_on_both(nums, target, expected)


if __name__ == "__main__":
    unittest.main()

