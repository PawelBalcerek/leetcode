import unittest

from integer_to_roman import Solution


class TestIntegerToRoman(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_units(self):
        self.assertEqual(self.solution.integer_to_roman(1), "I")
        self.assertEqual(self.solution.integer_to_roman(5), "V")
        self.assertEqual(self.solution.integer_to_roman(10), "X")
        self.assertEqual(self.solution.integer_to_roman(50), "L")
        self.assertEqual(self.solution.integer_to_roman(100), "C")
        self.assertEqual(self.solution.integer_to_roman(500), "D")
        self.assertEqual(self.solution.integer_to_roman(1000), "M")

    def test_subtraction_cases(self):
        self.assertEqual(self.solution.integer_to_roman(4), "IV")
        self.assertEqual(self.solution.integer_to_roman(9), "IX")
        self.assertEqual(self.solution.integer_to_roman(40), "XL")
        self.assertEqual(self.solution.integer_to_roman(90), "XC")
        self.assertEqual(self.solution.integer_to_roman(400), "CD")
        self.assertEqual(self.solution.integer_to_roman(900), "CM")

    def test_complex_cases(self):
        self.assertEqual(self.solution.integer_to_roman(3), "III")
        self.assertEqual(self.solution.integer_to_roman(58), "LVIII")
        self.assertEqual(self.solution.integer_to_roman(1994), "MCMXCIV")
        self.assertEqual(self.solution.integer_to_roman(3999), "MMMCMXCIX")


if __name__ == "__main__":
    unittest.main()
