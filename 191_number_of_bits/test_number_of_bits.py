import unittest
from number_of_bits import Solution

class TestNumberOfBits(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.number_of_bits(11), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.number_of_bits(128), 1)

    def test_example_3(self):
        self.assertEqual(self.solution.number_of_bits(2147483645), 30)

    def test_minimum_constraint(self):
        self.assertEqual(self.solution.number_of_bits(1), 1)

    def test_maximum_constraint(self):
        n = (1 << 31) - 1
        self.assertEqual(self.solution.number_of_bits(n), 31)

if __name__ == '__main__':
    unittest.main()
