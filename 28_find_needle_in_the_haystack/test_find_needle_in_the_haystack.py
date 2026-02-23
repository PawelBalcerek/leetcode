import unittest
from find_needle_in_the_haystack import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.find_needle_in_the_haystack("sadbutsad", "sad"), 0)

    def test_example_2(self):
        self.assertEqual(self.solution.find_needle_in_the_haystack("leetcode", "leeto"), -1)

    def test_match_at_end(self):
        self.assertEqual(self.solution.find_needle_in_the_haystack("hello", "ll"), 2)

    def test_match_at_very_end(self):
        self.assertEqual(self.solution.find_needle_in_the_haystack("abc", "c"), 2)

    def test_needle_longer_than_haystack(self):
        self.assertEqual(self.solution.find_needle_in_the_haystack("aaa", "aaaa"), -1)

    def test_same_needle_and_haystack(self):
        self.assertEqual(self.solution.find_needle_in_the_haystack("a", "a"), 0)

    def test_multiple_occurrences(self):
        self.assertEqual(self.solution.find_needle_in_the_haystack("mississippi", "issi"), 1)

    def test_no_match_single_char(self):
        self.assertEqual(self.solution.find_needle_in_the_haystack("abc", "d"), -1)

if __name__ == "__main__":
    unittest.main()
