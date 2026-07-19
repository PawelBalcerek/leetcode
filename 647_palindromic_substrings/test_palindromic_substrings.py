import unittest
from palindromic_substrings import Solution


class TestPalindromicSubstrings(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_all_unique_characters(self):
        self.assertEqual(self.solution.palindromic_substrings("abc"), 3)

    def test_all_same_characters(self):
        self.assertEqual(self.solution.palindromic_substrings("aaa"), 6)

    def test_single_character(self):
        self.assertEqual(self.solution.palindromic_substrings("a"), 1)

    def test_two_same_characters(self):
        self.assertEqual(self.solution.palindromic_substrings("aa"), 3)

    def test_two_different_characters(self):
        self.assertEqual(self.solution.palindromic_substrings("ab"), 2)

    def test_palindrome_string(self):
        self.assertEqual(self.solution.palindromic_substrings("racecar"), 10)

    def test_mixed_palindromes(self):
        self.assertEqual(self.solution.palindromic_substrings("aab"), 4)

    def test_longer_string(self):
        self.assertEqual(self.solution.palindromic_substrings("abcba"), 7)

    def test_repeated_pattern(self):
        self.assertEqual(self.solution.palindromic_substrings("abab"), 6)

    def test_four_same_characters(self):
        self.assertEqual(self.solution.palindromic_substrings("aaaa"), 10)


if __name__ == "__main__":
    unittest.main()
