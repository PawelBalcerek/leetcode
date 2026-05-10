import unittest
from reverse_bits import Solution

class TestReverseBits(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        n = 43261596
        expected = 964176192
        self.assertEqual(self.solution.reverse_bits(n), expected)

    def test_example_2(self):
        n = 2147483644
        expected = 1073741822
        self.assertEqual(self.solution.reverse_bits(n), expected)

    def test_zero(self):
        n = 0
        expected = 0
        self.assertEqual(self.solution.reverse_bits(n), expected)

    def test_max_even(self):
        n = 2147483646
        self.assertEqual(self.solution.reverse_bits(n), 2147483646)

    def test_two(self):
        n = 2
        expected = 1073741824
        self.assertEqual(self.solution.reverse_bits(n), expected)

if __name__ == '__main__':
    unittest.main()
