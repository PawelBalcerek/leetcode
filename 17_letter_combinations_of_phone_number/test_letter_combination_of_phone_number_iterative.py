import unittest
from letter_combination_of_phone_number_iterative import Solution

class TestLetterCombinationsIterative(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        digits = "23"
        expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        self.assertCountEqual(self.solution.letter_combinations_of_phone_number_iterative(digits), expected)

    def test_example_2(self):
        digits = "2"
        expected = ["a", "b", "c"]
        self.assertCountEqual(self.solution.letter_combinations_of_phone_number_iterative(digits), expected)

    def test_empty_string(self):
        digits = ""
        expected = []
        self.assertCountEqual(self.solution.letter_combinations_of_phone_number_iterative(digits), expected)

    def test_four_letter_mapping(self):
        digits = "7"
        expected = ["p", "q", "r", "s"]
        self.assertCountEqual(self.solution.letter_combinations_of_phone_number_iterative(digits), expected)

    def test_duplicate_digits(self):
        digits = "22"
        expected = ["aa", "ab", "ac", "ba", "bb", "bc", "ca", "cb", "cc"]
        self.assertCountEqual(self.solution.letter_combinations_of_phone_number_iterative(digits), expected)

if __name__ == "__main__":
    unittest.main()
