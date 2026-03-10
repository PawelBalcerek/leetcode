import unittest

from valid_sudoku import Solution


class TestValidSudoku(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1_valid(self):
        board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        self.assertTrue(self.sol.valid_sudoku(board))
        self.assertTrue(self.sol.valid_sudoku_single_set(board))

    def test_example_2_invalid(self):
        board = [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        self.assertFalse(self.sol.valid_sudoku(board))
        self.assertFalse(self.sol.valid_sudoku_single_set(board))

    def test_invalid_box(self):
        board = [["."] * 9 for _ in range(9)]
        board[0][0] = "5"
        board[2][2] = "5"
        self.assertFalse(self.sol.valid_sudoku(board))
        self.assertFalse(self.sol.valid_sudoku_single_set(board))

    def test_invalid_row(self):
        board = [["."] * 9 for _ in range(9)]
        board[0][0] = "5"
        board[0][8] = "5"
        self.assertFalse(self.sol.valid_sudoku(board))
        self.assertFalse(self.sol.valid_sudoku_single_set(board))

    def test_invalid_column(self):
        board = [["."] * 9 for _ in range(9)]
        board[0][0] = "5"
        board[8][0] = "5"
        self.assertFalse(self.sol.valid_sudoku(board))
        self.assertFalse(self.sol.valid_sudoku_single_set(board))

    def test_empty_board(self):
        board = [["."] * 9 for _ in range(9)]
        self.assertTrue(self.sol.valid_sudoku(board))
        self.assertTrue(self.sol.valid_sudoku_single_set(board))

    def test_full_valid_board(self):
        board = [
            ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
            ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
            ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
            ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
            ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
            ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
            ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
            ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
            ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
        ]
        self.assertTrue(self.sol.valid_sudoku(board))
        self.assertTrue(self.sol.valid_sudoku_single_set(board))


if __name__ == "__main__":
    unittest.main()
