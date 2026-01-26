import unittest
from roman_to_integer import Solution

class TestRomanToInteger(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_symbols(self):
        self.assertEqual(self.solution.romanToInt("I"), 1)
        self.assertEqual(self.solution.romanToInt("V"), 5)
        self.assertEqual(self.solution.romanToInt("X"), 10)
        self.assertEqual(self.solution.romanToInt("L"), 50)
        self.assertEqual(self.solution.romanToInt("C"), 100)
        self.assertEqual(self.solution.romanToInt("D"), 500)
        self.assertEqual(self.solution.romanToInt("M"), 1000)

    def test_additive_combinations(self):
        self.assertEqual(self.solution.romanToInt("III"), 3)
        self.assertEqual(self.solution.romanToInt("LVIII"), 58)
        self.assertEqual(self.solution.romanToInt("MDC"), 1600)

    def test_subtractive_combinations(self):
        self.assertEqual(self.solution.romanToInt("IV"), 4)
        self.assertEqual(self.solution.romanToInt("IX"), 9)
        self.assertEqual(self.solution.romanToInt("XL"), 40)
        self.assertEqual(self.solution.romanToInt("XC"), 90)
        self.assertEqual(self.solution.romanToInt("CD"), 400)
        self.assertEqual(self.solution.romanToInt("CM"), 900)

    def test_complex_cases(self):
        self.assertEqual(self.solution.romanToInt("MCMXCIV"), 1994)
        self.assertEqual(self.solution.romanToInt("MMMCMXCIX"), 3999)

    def test_empty_string(self):
        self.assertEqual(self.solution.romanToInt(""), 0)

if __name__ == '__main__':
    unittest.main()
