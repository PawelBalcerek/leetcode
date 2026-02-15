import unittest
from merge_sort import Solution

class TestMergeSort(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        arr = []
        self.assertEqual(self.solution.merge_sort(arr, 0, -1), [])

    def test_single_element(self):
        arr = [1]
        self.assertEqual(self.solution.merge_sort(arr, 0, 0), [1])

    def test_sorted_list(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.merge_sort(arr, 0, len(arr) - 1), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(self.solution.merge_sort(arr, 0, len(arr) - 1), [1, 2, 3, 4, 5])

    def test_duplicate_elements(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        expected = sorted(arr)
        self.assertEqual(self.solution.merge_sort(arr, 0, len(arr) - 1), expected)

    def test_general_case(self):
        arr = [38, 27, 43, 3, 9, 82, 10]
        expected = [3, 9, 10, 27, 38, 43, 82]
        self.assertEqual(self.solution.merge_sort(arr, 0, len(arr) - 1), expected)

if __name__ == '__main__':
    unittest.main()
