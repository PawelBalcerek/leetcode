import unittest
from valid_palindrome import Solution

class TestValidPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertTrue(self.solution.valid_palindrome("A man, a plan, a canal: Panama"))

    def test_example_2(self):
        self.assertFalse(self.solution.valid_palindrome("race a car"))

    def test_example_3(self):
        self.assertTrue(self.solution.valid_palindrome(" "))

    def test_empty_string(self):
        self.assertTrue(self.solution.valid_palindrome(""))

    def test_numeric_palindrome(self):
        self.assertTrue(self.solution.valid_palindrome("12321"))

    def test_alphanumeric_palindrome(self):
        self.assertTrue(self.solution.valid_palindrome("a1b2b1a"))

    def test_not_a_palindrome(self):
        self.assertFalse(self.solution.valid_palindrome("hello"))

if __name__ == "__main__":
    unittest.main()
