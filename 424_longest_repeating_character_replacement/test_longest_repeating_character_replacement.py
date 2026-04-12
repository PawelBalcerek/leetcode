import unittest
from longest_repeating_character_replacement import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.longest_repeating_character_replacement("ABAB", 2), 4)

    def test_example_2(self):
        self.assertEqual(self.solution.longest_repeating_character_replacement("AABABBA", 1), 4)

    def test_all_same_characters(self):
        self.assertEqual(self.solution.longest_repeating_character_replacement("AAAA", 2), 4)

    def test_all_different_characters_k_zero(self):
        self.assertEqual(self.solution.longest_repeating_character_replacement("ABCDE", 0), 1)

    def test_all_different_characters_k_large(self):
        self.assertEqual(self.solution.longest_repeating_character_replacement("ABCDE", 5), 5)

    def test_single_character(self):
        self.assertEqual(self.solution.longest_repeating_character_replacement("A", 0), 1)
        self.assertEqual(self.solution.longest_repeating_character_replacement("A", 1), 1)

    def test_empty_k_zero(self):
        self.assertEqual(self.solution.longest_repeating_character_replacement("", 0), 0)
        self.assertEqual(self.solution.longest_repeating_character_replacement("", 2), 0)

    def test_k_greater_than_length(self):
        self.assertEqual(self.solution.longest_repeating_character_replacement("AB", 10), 2)

    def test_k_zero(self):
        self.assertEqual(self.solution.longest_repeating_character_replacement("AAABBB", 0), 3)
        self.assertEqual(self.solution.longest_repeating_character_replacement("ABCDE", 0), 1)
        self.assertEqual(self.solution.longest_repeating_character_replacement("AABA", 0), 2)

    def test_long_string_with_replacements(self):
        self.assertEqual(self.solution.longest_repeating_character_replacement("BAAAB", 2), 5)
        self.assertEqual(self.solution.longest_repeating_character_replacement("AABA", 0), 2)

    def test_multiple_major_characters(self):
        self.assertEqual(self.solution.longest_repeating_character_replacement("AABCC", 1), 3)

if __name__ == "__main__":
    unittest.main()
