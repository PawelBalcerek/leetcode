import unittest

from n_queens import Solution


class TestNQueens(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def _normalize(self, boards):
        return sorted(sorted(board) for board in boards)

    def test_n1(self):
        result = self.solution.n_queens(1)
        self.assertEqual(result, [["Q"]])

    def test_n2_no_solution(self):
        result = self.solution.n_queens(2)
        self.assertEqual(result, [])

    def test_n3_no_solution(self):
        result = self.solution.n_queens(3)
        self.assertEqual(result, [])

    def test_n4_count(self):
        result = self.solution.n_queens(4)
        self.assertEqual(len(result), 2)

    def test_n4_solutions(self):
        result = self.solution.n_queens(4)
        expected = [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]
        self.assertEqual(self._normalize(result), self._normalize(expected))

    def test_n5_count(self):
        result = self.solution.n_queens(5)
        self.assertEqual(len(result), 10)

    def test_n6_count(self):
        result = self.solution.n_queens(6)
        self.assertEqual(len(result), 4)

    def test_n7_count(self):
        result = self.solution.n_queens(7)
        self.assertEqual(len(result), 40)

    def test_n8_count(self):
        result = self.solution.n_queens(8)
        self.assertEqual(len(result), 92)

    def test_n9_count(self):
        result = self.solution.n_queens(9)
        self.assertEqual(len(result), 352)

    def test_board_dimensions(self):
        for n in range(1, 6):
            with self.subTest(n=n):
                result = self.solution.n_queens(n)
                for board in result:
                    self.assertEqual(len(board), n)
                    for row in board:
                        self.assertEqual(len(row), n)

    def test_each_row_has_exactly_one_queen(self):
        for n in range(1, 6):
            with self.subTest(n=n):
                result = self.solution.n_queens(n)
                for board in result:
                    for row in board:
                        self.assertEqual(row.count("Q"), 1)

    def test_each_column_has_exactly_one_queen(self):
        for n in range(1, 6):
            with self.subTest(n=n):
                result = self.solution.n_queens(n)
                for board in result:
                    for col in range(n):
                        queens_in_col = sum(1 for row in board if row[col] == "Q")
                        self.assertEqual(queens_in_col, 1)

    def test_no_diagonal_attacks(self):
        for n in range(1, 6):
            with self.subTest(n=n):
                result = self.solution.n_queens(n)
                for board in result:
                    queen_positions = [(r, board[r].index("Q")) for r in range(n)]
                    for i in range(len(queen_positions)):
                        for j in range(i + 1, len(queen_positions)):
                            r1, c1 = queen_positions[i]
                            r2, c2 = queen_positions[j]
                            self.assertNotEqual(abs(r1 - r2), abs(c1 - c2))

    def test_board_contains_only_valid_characters(self):
        result = self.solution.n_queens(4)
        for board in result:
            for row in board:
                for ch in row:
                    self.assertIn(ch, ("Q", "."))

    def test_no_duplicate_solutions(self):
        for n in range(1, 7):
            with self.subTest(n=n):
                result = self.solution.n_queens(n)
                unique = [list(b) for b in set(tuple(b) for b in result)]
                self.assertEqual(len(result), len(unique))


if __name__ == "__main__":
    unittest.main()
