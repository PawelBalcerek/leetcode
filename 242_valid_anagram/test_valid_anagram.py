import unittest
from .is_anagram import Solution

class TestIsAnagram(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_is_anagram_true(self):
        self.assertTrue(self.solution.is_anagram("racecar", "carrace"))

    def test_is_anagram_false(self):
        self.assertFalse(self.solution.is_anagram("jar", "jam"))

    def test_is_anagram_different_lengths(self):
        self.assertFalse(self.solution.is_anagram("a", "ab"))

    def test_is_anagram_same_chars_different_counts(self):
        self.assertFalse(self.solution.is_anagram("aa", "a"))

    def test_is_anagram_empty_strings(self):
        self.assertTrue(self.solution.is_anagram("", ""))

if __name__ == "__main__":
    unittest.main()
