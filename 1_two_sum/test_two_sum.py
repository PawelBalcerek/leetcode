import unittest

from two_sum import Solution


class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_standard_case(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        self.assertEqual(self.solution.two_sum(nums, target), expected)

    def test_indices_not_at_start(self):
        nums = [3, 2, 4]
        target = 6
        expected = [1, 2]
        self.assertEqual(self.solution.two_sum(nums, target), expected)

    def test_same_elements(self):
        nums = [3, 3]
        target = 6
        expected = [0, 1]
        self.assertEqual(self.solution.two_sum(nums, target), expected)

    def test_no_solution(self):
        nums = [1, 2, 3]
        target = 7
        expected = []
        self.assertEqual(self.solution.two_sum(nums, target), expected)


if __name__ == "__main__":
    unittest.main()
