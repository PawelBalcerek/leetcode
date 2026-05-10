import unittest
from plus_one import Solution

class TestPlusOne(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.plus_one([1, 2, 3]), [1, 2, 4])

    def test_example2(self):
        self.assertEqual(self.solution.plus_one([4, 3, 2, 1]), [4, 3, 2, 2])

    def test_example3(self):
        self.assertEqual(self.solution.plus_one([9]), [1, 0])

    def test_single_zero(self):
        self.assertEqual(self.solution.plus_one([0]), [1])

    def test_carry_middle(self):
        self.assertEqual(self.solution.plus_one([1, 9, 9]), [2, 0, 0])

    def test_all_nines(self):
        self.assertEqual(self.solution.plus_one([9, 9, 9]), [1, 0, 0, 0])

    def test_large_number(self):
        digits = [9] * 100
        expected = [1] + [0] * 100
        self.assertEqual(self.solution.plus_one(digits), expected)

if __name__ == "__main__":
    unittest.main()
