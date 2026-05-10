import unittest
from counting_bits import Solution

class TestCountingBits(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.counting_bits(2), [0, 1, 1])

    def test_example2(self):
        self.assertEqual(self.solution.counting_bits(5), [0, 1, 1, 2, 1, 2])

    def test_n_zero(self):
        self.assertEqual(self.solution.counting_bits(0), [0])

    def test_n_one(self):
        self.assertEqual(self.solution.counting_bits(1), [0, 1])

    def test_larger_n(self):
        expected = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]
        self.assertEqual(self.solution.counting_bits(15), expected)

if __name__ == "__main__":
    unittest.main()
