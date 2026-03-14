import unittest
import copy
from sudoku_solver import Solution

class TestSudokuSolver(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.board = [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]
        self.expected = [
            ["5","3","4","6","7","8","9","1","2"],
            ["6","7","2","1","9","5","3","4","8"],
            ["1","9","8","3","4","2","5","6","7"],
            ["8","5","9","7","6","1","4","2","3"],
            ["4","2","6","8","5","3","7","9","1"],
            ["7","1","3","9","2","4","8","5","6"],
            ["9","6","1","5","3","7","2","8","4"],
            ["2","8","7","4","1","9","6","3","5"],
            ["3","4","5","2","8","6","1","7","9"]
        ]

    def test_sudoku_solver(self):
        board = copy.deepcopy(self.board)
        self.solution.sudoku_solver(board)
        self.assertEqual(board, self.expected)

    def test_sudoku_solver_bitwise(self):
        board = copy.deepcopy(self.board)
        self.solution.sudoku_solver_bitwise(board)
        self.assertEqual(board, self.expected)

    def is_valid_sudoku(self, board):
        for i in range(9):
            row = [board[i][j] for j in range(9) if board[i][j] != '.']
            col = [board[j][i] for j in range(9) if board[j][i] != '.']
            if len(set(row)) != len(row) or len(set(col)) != len(col):
                return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = []
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        if board[r][c] != '.':
                            box.append(board[r][c])
                if len(set(box)) != len(box):
                    return False
        return True

    def test_already_solved(self):
        board = copy.deepcopy(self.expected)
        # Test standard solver
        board_std = copy.deepcopy(board)
        self.solution.sudoku_solver(board_std)
        self.assertEqual(board_std, self.expected)
        # Test bitwise solver
        board_bit = copy.deepcopy(board)
        self.solution.sudoku_solver_bitwise(board_bit)
        self.assertEqual(board_bit, self.expected)

    def test_rule_validation(self):
        board = copy.deepcopy(self.board)
        self.solution.sudoku_solver(board)
        self.assertTrue(self.is_valid_sudoku(board))
        # Ensure no empty cells
        for row in board:
            self.assertNotIn(".", row)


if __name__ == '__main__':
    unittest.main()
