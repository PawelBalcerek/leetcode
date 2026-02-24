import unittest
from divide_two_integers import Solution

class TestDivideTwoIntegers(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.divide(10, 3), 3)

    def test_example2(self):
        self.assertEqual(self.solution.divide(7, -3), -2)

    def test_dividend_zero(self):
        self.assertEqual(self.solution.divide(0, 1), 0)

    def test_divisor_one(self):
        self.assertEqual(self.solution.divide(100, 1), 100)

    def test_divisor_minus_one(self):
        self.assertEqual(self.solution.divide(100, -1), -100)

    def test_overflow_positive(self):
        # -2^31 / -1 = 2^31, but should return 2^31 - 1
        self.assertEqual(self.solution.divide(-(2**31), -1), 2**31 - 1)

    def test_min_int_divisor_one(self):
        self.assertEqual(self.solution.divide(-(2**31), 1), -(2**31))

    def test_negative_result(self):
        self.assertEqual(self.solution.divide(-10, 2), -5)
        self.assertEqual(self.solution.divide(10, -2), -5)

    def test_both_negative(self):
        self.assertEqual(self.solution.divide(-10, -2), 5)

    def test_max_int_divisor_one(self):
        self.assertEqual(self.solution.divide(2**31 - 1, 1), 2**31 - 1)

    def test_max_int_divisor_minus_one(self):
        self.assertEqual(self.solution.divide(2**31 - 1, -1), -(2**31 - 1))

    def test_min_int_divisor_minus_one(self):
        # This is the overflow case: -2^31 / -1 = 2^31, should be capped at 2^31 - 1
        self.assertEqual(self.solution.divide(-(2**31), -1), 2**31 - 1)

    def test_large_dividend(self):
        self.assertEqual(self.solution.divide(1000000, 2), 500000)

    def test_small_divisor(self):
        self.assertEqual(self.solution.divide(10, 100), 0)

if __name__ == "__main__":
    unittest.main()
