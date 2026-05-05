import unittest
from largest_rectangle_in_histogram import Solution

class TestLargestRectangleInHistogram(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.largest_rectangle_in_histogram([2, 1, 5, 6, 2, 3]), 10)

    def test_example_2(self):
        self.assertEqual(self.solution.largest_rectangle_in_histogram([2, 4]), 4)

    def test_single_element(self):
        self.assertEqual(self.solution.largest_rectangle_in_histogram([5]), 5)

    def test_all_same_heights(self):
        self.assertEqual(self.solution.largest_rectangle_in_histogram([2, 2, 2, 2]), 8)

    def test_increasing_heights(self):
        self.assertEqual(self.solution.largest_rectangle_in_histogram([1, 2, 3, 4, 5]), 9)

    def test_decreasing_heights(self):
        self.assertEqual(self.solution.largest_rectangle_in_histogram([5, 4, 3, 2, 1]), 9)

    def test_with_zero_heights(self):
        self.assertEqual(self.solution.largest_rectangle_in_histogram([2, 0, 2]), 2)

    def test_large_rectangle_at_end(self):
        self.assertEqual(self.solution.largest_rectangle_in_histogram([1, 2, 3, 4, 5, 10, 10]), 20)

    def test_large_rectangle_at_beginning(self):
        self.assertEqual(self.solution.largest_rectangle_in_histogram([10, 10, 5, 4, 3, 2, 1]), 20)

    def test_empty_list(self):
        self.assertEqual(self.solution.largest_rectangle_in_histogram([]), 0)

if __name__ == '__main__':
    unittest.main()
