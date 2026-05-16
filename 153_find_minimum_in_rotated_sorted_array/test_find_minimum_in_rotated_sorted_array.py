import unittest
from find_minimum_in_rotated_sorted_array import Solution

class TestFindMinimumInRotatedSortedArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.find_minimum_in_rotated_sorted_array([3, 4, 5, 1, 2]), 1)

    def test_example2(self):
        self.assertEqual(self.solution.find_minimum_in_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2]), 0)

    def test_example3(self):
        self.assertEqual(self.solution.find_minimum_in_rotated_sorted_array([11, 13, 15, 17]), 11)

    def test_single_element(self):
        self.assertEqual(self.solution.find_minimum_in_rotated_sorted_array([1]), 1)

    def test_two_elements_sorted(self):
        self.assertEqual(self.solution.find_minimum_in_rotated_sorted_array([1, 2]), 1)

    def test_two_elements_rotated(self):
        self.assertEqual(self.solution.find_minimum_in_rotated_sorted_array([2, 1]), 1)

    def test_not_rotated(self):
        self.assertEqual(self.solution.find_minimum_in_rotated_sorted_array([1, 2, 3, 4, 5]), 1)

    def test_rotated_once(self):
        self.assertEqual(self.solution.find_minimum_in_rotated_sorted_array([5, 1, 2, 3, 4]), 1)

    def test_large_array(self):
        nums = list(range(-5000, 5001))
        rotated_nums = nums[3000:] + nums[:3000]
        self.assertEqual(self.solution.find_minimum_in_rotated_sorted_array(rotated_nums), -5000)

if __name__ == "__main__":
    unittest.main()
