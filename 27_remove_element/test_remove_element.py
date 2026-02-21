import unittest
from remove_element import Solution


class TestRemoveElement(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def check_result(self, nums, val, expected_nums):
        """
        Helper method to verify the result according to the problem's custom judge.
        """
        k = self.solution.remove_element(nums, val)
        self.assertEqual(k, len(expected_nums))

        # Sort the first k elements of nums to compare with expected_nums
        actual_nums = sorted(nums[:k])
        self.assertEqual(actual_nums, sorted(expected_nums))

    def test_example_1(self):
        nums = [3, 2, 2, 3]
        val = 3
        expected_nums = [2, 2]
        self.check_result(nums, val, expected_nums)

    def test_example_2(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        expected_nums = [0, 1, 4, 0, 3]
        self.check_result(nums, val, expected_nums)

    def test_empty_nums(self):
        nums = []
        val = 0
        expected_nums = []
        self.check_result(nums, val, expected_nums)

    def test_all_val(self):
        nums = [1, 1, 1]
        val = 1
        expected_nums = []
        self.check_result(nums, val, expected_nums)

    def test_no_val(self):
        nums = [1, 2, 3]
        val = 4
        expected_nums = [1, 2, 3]
        self.check_result(nums, val, expected_nums)

    def test_single_element_val(self):
        nums = [1]
        val = 1
        expected_nums = []
        self.check_result(nums, val, expected_nums)

    def test_single_element_not_val(self):
        nums = [1]
        val = 2
        expected_nums = [1]
        self.check_result(nums, val, expected_nums)


if __name__ == "__main__":
    unittest.main()
