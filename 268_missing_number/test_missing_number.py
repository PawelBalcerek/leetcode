import unittest
from missing_number import Solution

class TestMissingNumber(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        nums = [3, 0, 1]
        self.assertEqual(self.solution.missing_number(nums), 2)

    def test_example2(self):
        nums = [0, 1]
        self.assertEqual(self.solution.missing_number(nums), 2)

    def test_example3(self):
        nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
        self.assertEqual(self.solution.missing_number(nums), 8)

    def test_single_element_zero(self):
        nums = [0]
        self.assertEqual(self.solution.missing_number(nums), 1)

    def test_single_element_one(self):
        nums = [1]
        self.assertEqual(self.solution.missing_number(nums), 0)

    def test_empty_list(self):
        nums = []
        self.assertEqual(self.solution.missing_number(nums), 0)

if __name__ == '__main__':
    unittest.main()
