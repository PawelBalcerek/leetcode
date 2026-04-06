import unittest
from longest_consecutive_sequence import Solution

class TestLongestConsecutiveSequence(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [100, 4, 200, 1, 3, 2]
        self.assertEqual(self.solution.longest_consecutive_sequence(nums), 4)

    def test_example_2(self):
        nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
        self.assertEqual(self.solution.longest_consecutive_sequence(nums), 9)

    def test_example_3(self):
        nums = [1, 0, 1, 2]
        self.assertEqual(self.solution.longest_consecutive_sequence(nums), 3)

    def test_empty_list(self):
        nums = []
        self.assertEqual(self.solution.longest_consecutive_sequence(nums), 0)

    def test_single_element(self):
        nums = [10]
        self.assertEqual(self.solution.longest_consecutive_sequence(nums), 1)

    def test_all_same_elements(self):
        nums = [5, 5, 5, 5]
        self.assertEqual(self.solution.longest_consecutive_sequence(nums), 1)

    def test_no_consecutive(self):
        nums = [10, 30, 20, 40]
        self.assertEqual(self.solution.longest_consecutive_sequence(nums), 1)

    def test_negative_numbers(self):
        nums = [-1, -2, -3, 0, 1]
        self.assertEqual(self.solution.longest_consecutive_sequence(nums), 5)

    def test_large_gap(self):
        nums = [-10**9, 10**9]
        self.assertEqual(self.solution.longest_consecutive_sequence(nums), 1)

if __name__ == '__main__':
    unittest.main()
