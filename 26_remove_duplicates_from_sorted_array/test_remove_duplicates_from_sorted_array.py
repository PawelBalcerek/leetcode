import unittest
from remove_duplicates_from_sorted_array import Solution

class TestRemoveDuplicatesFromSortedArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def check_result(self, nums, expected_nums):
        k = self.solution.remove_duplicates_from_sorted_array(nums)
        self.assertEqual(k, len(expected_nums))
        for i in range(k):
            self.assertEqual(nums[i], expected_nums[i])

    def test_example_1(self):
        nums = [1, 1, 2]
        expected_nums = [1, 2]
        self.check_result(nums, expected_nums)

    def test_example_2(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        expected_nums = [0, 1, 2, 3, 4]
        self.check_result(nums, expected_nums)

    def test_single_element(self):
        nums = [1]
        expected_nums = [1]
        self.check_result(nums, expected_nums)

    def test_no_duplicates(self):
        nums = [1, 2, 3]
        expected_nums = [1, 2, 3]
        self.check_result(nums, expected_nums)

    def test_all_duplicates(self):
        nums = [1, 1, 1, 1]
        expected_nums = [1]
        self.check_result(nums, expected_nums)

    def test_empty_array(self):
        nums = []
        expected_nums = []
        self.check_result(nums, expected_nums)

if __name__ == "__main__":
    unittest.main()
