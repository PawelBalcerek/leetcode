import unittest

from word_search import Solution


class TestWordSearch(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1_abcced(self):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        self.assertTrue(self.solution.word_search(board, "ABCCED"))

    def test_example2_see(self):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        self.assertTrue(self.solution.word_search(board, "SEE"))

    def test_example3_abcb_not_found(self):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        self.assertFalse(self.solution.word_search(board, "ABCB"))

    def test_single_cell_match(self):
        board = [["A"]]
        self.assertTrue(self.solution.word_search(board, "A"))

    def test_single_cell_no_match(self):
        board = [["A"]]
        self.assertFalse(self.solution.word_search(board, "B"))

    def test_single_row_found(self):
        board = [["A", "B", "C", "D"]]
        self.assertTrue(self.solution.word_search(board, "ABCD"))

    def test_single_row_reverse(self):
        board = [["A", "B", "C", "D"]]
        self.assertTrue(self.solution.word_search(board, "DCBA"))

    def test_single_column_found(self):
        board = [["A"], ["B"], ["C"], ["D"]]
        self.assertTrue(self.solution.word_search(board, "ABCD"))

    def test_single_column_reverse(self):
        board = [["A"], ["B"], ["C"], ["D"]]
        self.assertTrue(self.solution.word_search(board, "DCBA"))

    def test_cannot_reuse_cell(self):
        board = [["A", "B"]]
        self.assertFalse(self.solution.word_search(board, "ABA"))

    def test_same_letter_grid_reuse(self):
        board = [["A", "A"], ["A", "A"]]
        self.assertTrue(self.solution.word_search(board, "AAAA"))

    def test_same_letter_grid_too_long(self):
        board = [["A", "A"], ["A", "A"]]
        self.assertFalse(self.solution.word_search(board, "AAAAA"))

    def test_snake_path(self):
        board = [["A", "B", "C"], ["F", "E", "D"]]
        self.assertTrue(self.solution.word_search(board, "ABCDEF"))

    def test_l_shaped_path(self):
        board = [["A", "B"], ["D", "C"]]
        self.assertTrue(self.solution.word_search(board, "ABCD"))

    def test_word_not_in_board(self):
        board = [["A", "B"], ["C", "D"]]
        self.assertFalse(self.solution.word_search(board, "XYZ"))

    def test_word_longer_than_board(self):
        board = [["A", "B"], ["C", "D"]]
        self.assertFalse(self.solution.word_search(board, "ABCDE"))

    def test_single_char_word_found(self):
        board = [["X", "Y"], ["Z", "W"]]
        self.assertTrue(self.solution.word_search(board, "W"))

    def test_single_char_word_not_found(self):
        board = [["X", "Y"], ["Z", "W"]]
        self.assertFalse(self.solution.word_search(board, "A"))

    def test_backtracking_required(self):
        board = [
            ["A", "B", "C", "E"],
            ["S", "F", "E", "S"],
            ["A", "D", "E", "E"],
        ]
        self.assertTrue(self.solution.word_search(board, "ABCESEEEFS"))

    def test_start_not_at_top_left(self):
        board = [["X", "Y"], ["A", "B"]]
        self.assertTrue(self.solution.word_search(board, "AB"))

    def test_full_traversal_large_grid(self):
        board = [
            ["A", "B", "C"],
            ["D", "E", "F"],
            ["G", "H", "I"],
        ]
        self.assertTrue(self.solution.word_search(board, "ABE"))
        self.assertFalse(self.solution.word_search(board, "ABI"))

    def test_diagonal_not_adjacent(self):
        board = [["A", "B"], ["C", "D"]]
        self.assertFalse(self.solution.word_search(board, "AD"))


if __name__ == "__main__":
    unittest.main()
