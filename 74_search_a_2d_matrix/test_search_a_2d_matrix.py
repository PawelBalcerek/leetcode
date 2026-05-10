import unittest
from search_a_2d_matrix import Solution

class TestSearch2DMatrix(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        target = 3
        self.assertTrue(self.solution.search_a_2d_matrix(matrix, target))

    def test_example2(self):
        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        target = 13
        self.assertFalse(self.solution.search_a_2d_matrix(matrix, target))

    def test_single_element_found(self):
        matrix = [[1]]
        target = 1
        self.assertTrue(self.solution.search_a_2d_matrix(matrix, target))

    def test_single_element_not_found(self):
        matrix = [[1]]
        target = 2
        self.assertFalse(self.solution.search_a_2d_matrix(matrix, target))

    def test_target_at_beginning(self):
        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        target = 1
        self.assertTrue(self.solution.search_a_2d_matrix(matrix, target))

    def test_target_at_end(self):
        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        target = 60
        self.assertTrue(self.solution.search_a_2d_matrix(matrix, target))

    def test_target_too_small(self):
        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        target = 0
        self.assertFalse(self.solution.search_a_2d_matrix(matrix, target))

    def test_target_too_large(self):
        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        target = 61
        self.assertFalse(self.solution.search_a_2d_matrix(matrix, target))

    def test_target_between_rows(self):
        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        target = 8
        self.assertFalse(self.solution.search_a_2d_matrix(matrix, target))

    def test_one_row(self):
        matrix = [[1,3,5,7]]
        target = 3
        self.assertTrue(self.solution.search_a_2d_matrix(matrix, target))
        target = 4
        self.assertFalse(self.solution.search_a_2d_matrix(matrix, target))

    def test_one_column(self):
        matrix = [[1],[10],[23]]
        target = 10
        self.assertTrue(self.solution.search_a_2d_matrix(matrix, target))
        target = 11
        self.assertFalse(self.solution.search_a_2d_matrix(matrix, target))

if __name__ == '__main__':
    unittest.main()
