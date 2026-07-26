import unittest

from word_dictionary import Solution


class TestWordDictionary(unittest.TestCase):
    def setUp(self):
        self.wd = Solution()

    def test_example_from_problem(self):
        self.wd.add("bad")
        self.wd.add("dad")
        self.wd.add("mad")
        self.assertFalse(self.wd.search("pad"))
        self.assertTrue(self.wd.search("bad"))
        self.assertTrue(self.wd.search(".ad"))
        self.assertTrue(self.wd.search("b.."))

    def test_search_empty_dictionary(self):
        self.assertFalse(self.wd.search("a"))
        self.assertFalse(self.wd.search("."))

    def test_search_exact_match(self):
        self.wd.add("hello")
        self.assertTrue(self.wd.search("hello"))

    def test_search_no_match(self):
        self.wd.add("hello")
        self.assertFalse(self.wd.search("world"))

    def test_single_dot_matches_any_letter(self):
        self.wd.add("cat")
        self.assertTrue(self.wd.search("c.t"))
        self.assertTrue(self.wd.search(".at"))
        self.assertTrue(self.wd.search("ca."))

    def test_two_dots(self):
        self.wd.add("abc")
        self.assertTrue(self.wd.search("a.."))
        self.assertTrue(self.wd.search(".b."))
        self.assertTrue(self.wd.search("..c"))

    def test_all_dots_match_word(self):
        self.wd.add("ab")
        self.assertTrue(self.wd.search(".."))

    def test_dot_does_not_match_end_of_word(self):
        self.wd.add("ab")
        self.assertFalse(self.wd.search("ab."))

    def test_dot_pattern_longer_than_any_word(self):
        self.wd.add("hi")
        self.assertFalse(self.wd.search("..."))

    def test_dot_pattern_shorter_than_stored_word(self):
        self.wd.add("abc")
        self.assertFalse(self.wd.search("."))

    def test_search_prefix_not_match(self):
        self.wd.add("abc")
        self.assertFalse(self.wd.search("ab"))

    def test_search_does_not_match_extension(self):
        self.wd.add("ab")
        self.assertFalse(self.wd.search("abc"))

    def test_multiple_words_same_length(self):
        self.wd.add("bat")
        self.wd.add("cat")
        self.wd.add("hat")
        self.assertTrue(self.wd.search("bat"))
        self.assertTrue(self.wd.search("cat"))
        self.assertTrue(self.wd.search("hat"))
        self.assertFalse(self.wd.search("mat"))
        self.assertTrue(self.wd.search(".at"))

    def test_multiple_words_different_lengths(self):
        self.wd.add("a")
        self.wd.add("ab")
        self.wd.add("abc")
        self.assertTrue(self.wd.search("a"))
        self.assertTrue(self.wd.search("ab"))
        self.assertTrue(self.wd.search("abc"))
        self.assertFalse(self.wd.search("abcd"))

    def test_dot_among_multiple_candidates(self):
        self.wd.add("bad")
        self.wd.add("bed")
        self.wd.add("bid")
        self.assertTrue(self.wd.search("b.d"))
        self.assertFalse(self.wd.search("b.x"))

    def test_duplicate_add(self):
        self.wd.add("word")
        self.wd.add("word")
        self.assertTrue(self.wd.search("word"))

    def test_single_character_word(self):
        self.wd.add("a")
        self.assertTrue(self.wd.search("a"))
        self.assertTrue(self.wd.search("."))
        self.assertFalse(self.wd.search("b"))

    def test_dot_does_not_match_eow_sentinel(self):
        self.wd.add("a")
        self.wd.add("ab")
        self.assertTrue(self.wd.search("."))
        self.assertTrue(self.wd.search(".."))
        self.assertFalse(self.wd.search("..."))

    def test_word_length_25(self):
        long_word = "a" * 25
        self.wd.add(long_word)
        self.assertTrue(self.wd.search(long_word))
        pattern = "." * 25
        self.assertTrue(self.wd.search(pattern))
        self.assertFalse(self.wd.search("." * 24))


if __name__ == "__main__":
    unittest.main()
