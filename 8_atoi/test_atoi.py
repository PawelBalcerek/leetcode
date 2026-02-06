import unittest
from atoi import Solution

class TestAtoi(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.atoi("42"), 42)

    def test_example2(self):
        self.assertEqual(self.solution.atoi("   -042"), -42)

    def test_example3(self):
        self.assertEqual(self.solution.atoi("1337c0d3"), 1337)

    def test_example4(self):
        self.assertEqual(self.solution.atoi("0-1"), 0)

    def test_example5(self):
        self.assertEqual(self.solution.atoi("words and 987"), 0)

    def test_leading_whitespace(self):
        self.assertEqual(self.solution.atoi("   42"), 42)

    def test_plus_sign(self):
        self.assertEqual(self.solution.atoi("+42"), 42)

    def test_minus_sign(self):
        self.assertEqual(self.solution.atoi("-42"), -42)

    def test_overflow(self):
        self.assertEqual(self.solution.atoi("2147483647"), 2147483647)
        self.assertEqual(self.solution.atoi("2147483648"), 2147483647)
        self.assertEqual(self.solution.atoi("91283472332"), 2147483647)

    def test_underflow(self):
        self.assertEqual(self.solution.atoi("-2147483648"), -2147483648)
        self.assertEqual(self.solution.atoi("-2147483649"), -2147483648)
        self.assertEqual(self.solution.atoi("-91283472332"), -2147483648)

    def test_empty_string(self):
        self.assertEqual(self.solution.atoi(""), 0)

    def test_only_whitespace(self):
        self.assertEqual(self.solution.atoi("   "), 0)

    def test_invalid_first_char(self):
        self.assertEqual(self.solution.atoi("a42"), 0)

    def test_multiple_signs(self):
        self.assertEqual(self.solution.atoi("+-12"), 0)
        self.assertEqual(self.solution.atoi("-+12"), 0)
        self.assertEqual(self.solution.atoi("--12"), 0)
        self.assertEqual(self.solution.atoi("++12"), 0)

    def test_decimal_point(self):
        self.assertEqual(self.solution.atoi("3.14159"), 3)

    def test_leading_zeros(self):
        self.assertEqual(self.solution.atoi("00000-42a123"), 0)
        self.assertEqual(self.solution.atoi("  0000000000012345678"), 12345678)

if __name__ == '__main__':
    unittest.main()
