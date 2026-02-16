import unittest
from longest_substring_without_repeating_characters import Solution

class TestLongestSubstringWithoutRepeatingCharacters(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.longest_substring_without_repeating_characters("abcabcbb"), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.longest_substring_without_repeating_characters("bbbbb"), 1)

    def test_example_3(self):
        self.assertEqual(self.solution.longest_substring_without_repeating_characters("pwwkew"), 3)

    def test_empty_string(self):
        self.assertEqual(self.solution.longest_substring_without_repeating_characters(""), 0)

    def test_all_unique_characters(self):
        self.assertEqual(self.solution.longest_substring_without_repeating_characters("abcdef"), 6)

    def test_single_character(self):
        self.assertEqual(self.solution.longest_substring_without_repeating_characters("a"), 1)

    def test_with_spaces_and_symbols(self):
        self.assertEqual(self.solution.longest_substring_without_repeating_characters("a b c!@#"), 6)

    def test_long_string_unique(self):
        s = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;':",./<>? """
        self.assertEqual(self.solution.longest_substring_without_repeating_characters(s), len(s))

if __name__ == "__main__":
    unittest.main()
