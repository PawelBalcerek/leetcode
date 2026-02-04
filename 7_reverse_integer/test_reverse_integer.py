import unittest
from reverse_integer import Solution

class TestReverseInteger(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_positive_integer(self):
        self.assertEqual(self.solution.reverse_integer(123), 321)

    def test_negative_integer(self):
        self.assertEqual(self.solution.reverse_integer(-123), -321)

    def test_trailing_zero(self):
        self.assertEqual(self.solution.reverse_integer(120), 21)

    def test_zero(self):
        self.assertEqual(self.solution.reverse_integer(0), 0)

    def test_max_int(self):
        # 2147483647 reversed is 7463847412, which overflows
        self.assertEqual(self.solution.reverse_integer(2147483647), 0)

    def test_min_int(self):
        # -2147483648 reversed is -8463847412, which overflows
        self.assertEqual(self.solution.reverse_integer(-2147483648), 0)

    def test_overflow_positive(self):
        self.assertEqual(self.solution.reverse_integer(1534236469), 0)

    def test_overflow_negative(self):
        self.assertEqual(self.solution.reverse_integer(-2147483648), 0)

    def test_large_but_no_overflow(self):
        # 1147483641 reversed is 1463847411, which is within range
        self.assertEqual(self.solution.reverse_integer(1147483641), 1463847411)

if __name__ == "__main__":
    unittest.main()
