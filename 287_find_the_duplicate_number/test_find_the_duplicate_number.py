import unittest
from find_the_duplicate_number import Solution

class TestFindTheDuplicateNumber(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 3, 4, 2, 2]
        self.assertEqual(self.solution.find_the_duplicate_number(nums), 2)

    def test_example_2(self):
        nums = [3, 1, 3, 4, 2]
        self.assertEqual(self.solution.find_the_duplicate_number(nums), 3)

    def test_example_3(self):
        nums = [3, 3, 3, 3, 3]
        self.assertEqual(self.solution.find_the_duplicate_number(nums), 3)

    def test_minimal_array(self):
        nums = [1, 1]
        self.assertEqual(self.solution.find_the_duplicate_number(nums), 1)

    def test_duplicate_at_boundaries(self):
        nums = [1, 2, 3, 4, 4]
        self.assertEqual(self.solution.find_the_duplicate_number(nums), 4)

    def test_multiple_occurrences(self):
        nums = [2, 2, 2, 2]
        self.assertEqual(self.solution.find_the_duplicate_number(nums), 2)

    def test_larger_range(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 5]
        self.assertEqual(self.solution.find_the_duplicate_number(nums), 5)

if __name__ == '__main__':
    unittest.main()
