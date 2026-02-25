import unittest

from substring_with_concatenation_of_all_words import Solution


class TestSubstringWithConcatenationOfAllWords(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s = "barfoothefoobarman"
        words = ["foo", "bar"]
        expected = [0, 9]
        result = self.solution.substring_with_concatenation_of_all_words(s, words)
        self.assertEqual(sorted(result), sorted(expected))

    def test_example_2(self):
        s = "wordgoodgoodgoodbestword"
        words = ["word", "good", "best", "word"]
        expected = []
        result = self.solution.substring_with_concatenation_of_all_words(s, words)
        self.assertEqual(sorted(result), sorted(expected))

    def test_example_3(self):
        s = "barfoofoobarthefoobarman"
        words = ["bar", "foo", "the"]
        expected = [6, 9, 12]
        result = self.solution.substring_with_concatenation_of_all_words(s, words)
        self.assertEqual(sorted(result), sorted(expected))

    def test_no_matches(self):
        s = "abcdef"
        words = ["gh", "ij"]
        expected = []
        result = self.solution.substring_with_concatenation_of_all_words(s, words)
        self.assertEqual(sorted(result), sorted(expected))

    def test_all_same_words(self):
        s = "aaaaaaaaaaaa"
        words = ["aa", "aa", "aa"]
        expected = [0, 1, 2, 3, 4, 5, 6]
        result = self.solution.substring_with_concatenation_of_all_words(s, words)
        self.assertEqual(sorted(result), sorted(expected))

    def test_single_word(self):
        s = "word"
        words = ["word"]
        expected = [0]
        result = self.solution.substring_with_concatenation_of_all_words(s, words)
        self.assertEqual(result, expected)

    def test_s_shorter_than_words(self):
        s = "abc"
        words = ["abcd", "efgh"]
        expected = []
        result = self.solution.substring_with_concatenation_of_all_words(s, words)
        self.assertEqual(result, expected)

    def test_complex_overlapping(self):
        s = "wordgoodgoodgoodbestword"
        words = ["word", "good", "best", "good"]
        expected = [8]
        result = self.solution.substring_with_concatenation_of_all_words(s, words)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
