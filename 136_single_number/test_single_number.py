import unittest
from single_number import Solution

class TestSingleNumber(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.single_number([2, 2, 1]), 1)

    def test_example2(self):
        self.assertEqual(self.solution.single_number([4, 1, 2, 1, 2]), 4)

    def test_example3(self):
        self.assertEqual(self.solution.single_number([1]), 1)

    def test_negative_numbers(self):
        self.assertEqual(self.solution.single_number([-1, -1, -2]), -2)

    def test_large_array(self):
        nums = list(range(1000)) * 2 + [10000]
        self.assertEqual(self.solution.single_number(nums), 10000)

if __name__ == '__main__':
    unittest.main()
