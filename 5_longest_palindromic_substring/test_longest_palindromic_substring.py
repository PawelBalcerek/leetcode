import unittest
from longest_palindromic_substring import Solution

class TestLongestPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s = "babad"
        # "bab" and "aba" are both valid answers
        result = self.solution.longestPalindrome(s)
        self.assertIn(result, ["bab", "aba"])

    def test_example_2(self):
        s = "cbbd"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, "bb")

    def test_single_character(self):
        s = "a"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, "a")

    def test_all_same_characters(self):
        s = "aaaa"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, "aaaa")

    def test_no_palindrome_longer_than_one(self):
        s = "abcdef"
        # Any single character is a valid palindrome of length 1.
        # The implementation initializes longest = s[0], so it should return 'a'.
        result = self.solution.longestPalindrome(s)
        self.assertEqual(len(result), 1)
        self.assertEqual(result, "a")

    def test_even_length_palindrome(self):
        s = "abba"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, "abba")

    def test_long_palindrome_in_middle(self):
        s = "abacdfgdcaba"
        # "aba" is at the start and end, but check if there's anything else?
        # Actually "abacdfgdcaba" -> nothing longer than 3 ("aba")?
        # let's try a clearer one: "xabay" -> "aba"
        s = "xabay"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, "aba")

if __name__ == '__main__':
    unittest.main()
