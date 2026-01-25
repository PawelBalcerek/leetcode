import unittest

from median_of_two_sorted_array import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_even_total_length(self):
        self.assertEqual(self.solution.findMedianSortedArrays([1, 3], [2, 4]), 2.5)

    def test_odd_total_length(self):
        self.assertEqual(self.solution.findMedianSortedArrays([1, 3], [2]), 2.0)

    def test_one_empty_array(self):
        self.assertEqual(self.solution.findMedianSortedArrays([], [1]), 1.0)
        self.assertEqual(self.solution.findMedianSortedArrays([2], []), 2.0)
        self.assertEqual(self.solution.findMedianSortedArrays([], [1, 2, 3, 4]), 2.5)

    def test_different_sizes(self):
        self.assertEqual(
            self.solution.findMedianSortedArrays([1, 2], [3, 4, 5, 6]), 3.5
        )
        self.assertEqual(self.solution.findMedianSortedArrays([1, 2, 3], [4, 5]), 3.0)

    def test_all_smaller(self):
        self.assertEqual(self.solution.findMedianSortedArrays([1, 2], [3, 4]), 2.5)

    def test_all_larger(self):
        self.assertEqual(self.solution.findMedianSortedArrays([3, 4], [1, 2]), 2.5)

    def test_single_elements(self):
        self.assertEqual(self.solution.findMedianSortedArrays([1], [2]), 1.5)


if __name__ == "__main__":
    unittest.main()
