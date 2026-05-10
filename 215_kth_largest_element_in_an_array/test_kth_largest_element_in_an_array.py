import unittest
from kth_largest_element_in_an_array import Solution

class TestKthLargestElement(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [3, 2, 1, 5, 6, 4]
        k = 2
        self.assertEqual(self.solution.kth_largest_element_in_an_array(nums, k), 5)

    def test_example_2(self):
        nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        k = 4
        self.assertEqual(self.solution.kth_largest_element_in_an_array(nums, k), 4)

    def test_k_is_1(self):
        nums = [3, 2, 1, 5, 6, 4]
        k = 1
        self.assertEqual(self.solution.kth_largest_element_in_an_array(nums, k), 6)

    def test_k_is_len(self):
        nums = [3, 2, 1, 5, 6, 4]
        k = 6
        self.assertEqual(self.solution.kth_largest_element_in_an_array(nums, k), 1)

    def test_single_element(self):
        nums = [1]
        k = 1
        self.assertEqual(self.solution.kth_largest_element_in_an_array(nums, k), 1)

    def test_duplicates(self):
        nums = [2, 2, 2, 2]
        k = 2
        self.assertEqual(self.solution.kth_largest_element_in_an_array(nums, k), 2)

    def test_negative_numbers(self):
        nums = [-1, -5, 0, 2, -10]
        k = 3
        self.assertEqual(self.solution.kth_largest_element_in_an_array(nums, k), -1)

if __name__ == '__main__':
    unittest.main()
