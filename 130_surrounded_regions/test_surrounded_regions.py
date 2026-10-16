import unittest

from surrounded_regions import Solution


class TestSurroundedRegions(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        board = [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"],
        ]
        expected = [
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "O", "X", "X"],
        ]
        result = self.solution.surrounded_regions(board)
        self.assertIsNone(result)
        self.assertEqual(board, expected)

    def test_example_2(self):
        board = [["X"]]
        expected = [["X"]]
        self.solution.surrounded_regions(board)
        self.assertEqual(board, expected)

    def test_single_cell_o(self):
        board = [["O"]]
        expected = [["O"]]
        self.solution.surrounded_regions(board)
        self.assertEqual(board, expected)

    def test_all_x(self):
        board = [
            ["X", "X", "X"],
            ["X", "X", "X"],
            ["X", "X", "X"],
        ]
        expected = [
            ["X", "X", "X"],
            ["X", "X", "X"],
            ["X", "X", "X"],
        ]
        self.solution.surrounded_regions(board)
        self.assertEqual(board, expected)

    def test_all_o(self):
        board = [
            ["O", "O", "O"],
            ["O", "O", "O"],
            ["O", "O", "O"],
        ]
        expected = [
            ["O", "O", "O"],
            ["O", "O", "O"],
            ["O", "O", "O"],
        ]
        self.solution.surrounded_regions(board)
        self.assertEqual(board, expected)

    def test_single_surrounded_cell(self):
        board = [
            ["X", "X", "X"],
            ["X", "O", "X"],
            ["X", "X", "X"],
        ]
        expected = [
            ["X", "X", "X"],
            ["X", "X", "X"],
            ["X", "X", "X"],
        ]
        self.solution.surrounded_regions(board)
        self.assertEqual(board, expected)

    def test_single_row(self):
        board = [["X", "O", "X", "O", "O", "X"]]
        expected = [["X", "O", "X", "O", "O", "X"]]
        self.solution.surrounded_regions(board)
        self.assertEqual(board, expected)

    def test_single_column(self):
        board = [["X"], ["O"], ["X"], ["O"], ["X"]]
        expected = [["X"], ["O"], ["X"], ["O"], ["X"]]
        self.solution.surrounded_regions(board)
        self.assertEqual(board, expected)

    def test_two_by_two(self):
        board = [
            ["X", "O"],
            ["O", "X"],
        ]
        expected = [
            ["X", "O"],
            ["O", "X"],
        ]
        self.solution.surrounded_regions(board)
        self.assertEqual(board, expected)

    def test_diagonal_not_connected_to_edge(self):
        board = [
            ["O", "X", "X", "O"],
            ["X", "O", "O", "X"],
            ["X", "O", "O", "X"],
            ["O", "X", "X", "O"],
        ]
        expected = [
            ["O", "X", "X", "O"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["O", "X", "X", "O"],
        ]
        self.solution.surrounded_regions(board)
        self.assertEqual(board, expected)

    def test_snake_connected_to_top_edge(self):
        board = [
            ["X", "O", "X", "X", "X"],
            ["X", "O", "O", "O", "X"],
            ["X", "X", "X", "O", "X"],
            ["X", "O", "O", "O", "X"],
            ["X", "X", "X", "X", "X"],
        ]
        expected = [
            ["X", "O", "X", "X", "X"],
            ["X", "O", "O", "O", "X"],
            ["X", "X", "X", "O", "X"],
            ["X", "O", "O", "O", "X"],
            ["X", "X", "X", "X", "X"],
        ]
        self.solution.surrounded_regions(board)
        self.assertEqual(board, expected)

    def test_multiple_regions_mixed(self):
        board = [
            ["X", "X", "X", "X", "O"],
            ["X", "O", "X", "O", "O"],
            ["X", "O", "X", "X", "X"],
            ["X", "X", "O", "O", "X"],
            ["O", "X", "X", "X", "X"],
        ]
        expected = [
            ["X", "X", "X", "X", "O"],
            ["X", "X", "X", "O", "O"],
            ["X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X"],
            ["O", "X", "X", "X", "X"],
        ]
        self.solution.surrounded_regions(board)
        self.assertEqual(board, expected)

    def test_concentric_rings(self):
        board = [
            ["O", "O", "O", "O", "O"],
            ["O", "X", "X", "X", "O"],
            ["O", "X", "O", "X", "O"],
            ["O", "X", "X", "X", "O"],
            ["O", "O", "O", "O", "O"],
        ]
        expected = [
            ["O", "O", "O", "O", "O"],
            ["O", "X", "X", "X", "O"],
            ["O", "X", "X", "X", "O"],
            ["O", "X", "X", "X", "O"],
            ["O", "O", "O", "O", "O"],
        ]
        self.solution.surrounded_regions(board)
        self.assertEqual(board, expected)


if __name__ == "__main__":
    unittest.main()
