import unittest
from top_k_frequent_elements import Solution

class TestTopKFrequentElements(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        expected = {1, 2}
        result = set(self.solution.top_k_frequent_elements(nums, k))
        self.assertEqual(result, expected)

    def test_example2(self):
        nums = [1]
        k = 1
        expected = {1}
        result = set(self.solution.top_k_frequent_elements(nums, k))
        self.assertEqual(result, expected)

    def test_example3(self):
        nums = [1, 2, 1, 2, 1, 2, 3, 1, 3, 2]
        k = 2
        expected = {1, 2}
        result = set(self.solution.top_k_frequent_elements(nums, k))
        self.assertEqual(result, expected)

    def test_negative_numbers(self):
        nums = [-1, -1, -2, -2, -2, 0]
        k = 2
        expected = {-1, -2}
        result = set(self.solution.top_k_frequent_elements(nums, k))
        self.assertEqual(result, expected)

    def test_large_k(self):
        nums = [1, 2, 3, 4, 5]
        k = 5
        expected = {1, 2, 3, 4, 5}
        result = set(self.solution.top_k_frequent_elements(nums, k))
        self.assertEqual(result, expected)

    def test_repeated_elements_with_same_freq(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 1
        expected = {1}
        result = set(self.solution.top_k_frequent_elements(nums, k))
        self.assertEqual(result, expected)

    def test_tight_bucket_size(self):
        nums = [1, 1, 1, 1, 1, 2, 3]
        k = 3
        expected = {1, 2, 3}
        result = set(self.solution.top_k_frequent_elements(nums, k))
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
