import unittest

from word_search_ii import Solution


class TestFindWords(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        board = [
            ["o", "a", "a", "n"],
            ["e", "t", "a", "e"],
            ["i", "h", "k", "r"],
            ["i", "f", "l", "v"],
        ]
        words = ["oath", "pea", "eat", "rain"]
        result = self.solution.findWords(board, words)
        self.assertCountEqual(result, ["eat", "oath"])

    def test_example_2(self):
        board = [["a", "b"], ["c", "d"]]
        words = ["abcb"]
        result = self.solution.findWords(board, words)
        self.assertCountEqual(result, [])

    def test_single_cell_match(self):
        board = [["a"]]
        words = ["a"]
        result = self.solution.findWords(board, words)
        self.assertCountEqual(result, ["a"])

    def test_single_cell_no_match(self):
        board = [["a"]]
        words = ["b"]
        result = self.solution.findWords(board, words)
        self.assertCountEqual(result, [])

    def test_no_words_found(self):
        board = [["a", "b"], ["c", "d"]]
        words = ["xyz", "mnop"]
        result = self.solution.findWords(board, words)
        self.assertCountEqual(result, [])

    def test_all_words_found(self):
        board = [["a", "b"], ["c", "d"]]
        words = ["ab", "abc", "abcd", "abdc"]
        result = self.solution.findWords(board, words)
        self.assertCountEqual(result, ["ab", "abdc"])

    def test_word_longer_than_board_cells(self):
        board = [["a", "b"], ["c", "d"]]
        words = ["abcde"]
        result = self.solution.findWords(board, words)
        self.assertCountEqual(result, [])

    def test_same_letter_cannot_be_reused(self):
        board = [["a", "b"], ["c", "d"]]
        words = ["aba"]
        result = self.solution.findWords(board, words)
        self.assertCountEqual(result, [])

    def test_diagonal_not_adjacent(self):
        board = [["a", "b"], ["c", "d"]]
        words = ["ad", "bc"]
        result = self.solution.findWords(board, words)
        self.assertCountEqual(result, [])

    def test_single_row(self):
        board = [["a", "b", "c", "d"]]
        words = ["abcd", "dcba", "ab", "cd"]
        result = self.solution.findWords(board, words)
        self.assertCountEqual(result, ["abcd", "dcba", "ab", "cd"])

    def test_single_column(self):
        board = [["a"], ["b"], ["c"], ["d"]]
        words = ["abcd", "dcba", "ab"]
        result = self.solution.findWords(board, words)
        self.assertCountEqual(result, ["abcd", "dcba", "ab"])

    def test_overlapping_paths(self):
        board = [["a", "b"], ["a", "b"]]
        words = ["aab", "aba", "abb"]
        result = self.solution.findWords(board, words)
        self.assertCountEqual(result, ["aab", "abb"])

    def test_duplicate_letters_board(self):
        board = [["a", "a", "a"], ["a", "a", "a"], ["a", "a", "a"]]
        words = ["aaaaaaaaa", "aaaaaaaaaa", "a", "aa"]
        result = self.solution.findWords(board, words)
        self.assertCountEqual(result, ["aaaaaaaaa", "a", "aa"])

    def test_prefix_and_full_word(self):
        board = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
        words = ["ab", "abc", "abcf", "abcfi", "abcfih"]
        result = self.solution.findWords(board, words)
        self.assertCountEqual(result, ["ab", "abc", "abcf", "abcfi", "abcfih"])

    def test_board_not_mutated(self):
        board = [
            ["o", "a", "a", "n"],
            ["e", "t", "a", "e"],
            ["i", "h", "k", "r"],
            ["i", "f", "l", "v"],
        ]
        original = [row[:] for row in board]
        self.solution.findWords(board, ["oath", "eat"])
        self.assertEqual(board, original)

    def test_large_word_list_with_few_matches(self):
        board = [["a", "b"], ["c", "d"]]
        words = [chr(ord("e") + i) for i in range(22)] + ["ab", "cd"]
        result = self.solution.findWords(board, words)
        self.assertCountEqual(result, ["ab", "cd"])

    def test_snake_path(self):
        board = [
            ["a", "b", "c"],
            ["f", "e", "d"],
            ["g", "h", "i"],
        ]
        words = ["abcdefghi"]
        result = self.solution.findWords(board, words)
        self.assertCountEqual(result, ["abcdefghi"])


if __name__ == "__main__":
    unittest.main()
