import unittest

from trie import Trie


class TestTrieExample(unittest.TestCase):
    def test_example_from_problem(self):
        trie = Trie()
        trie.insert("apple")
        self.assertTrue(trie.search("apple"))
        self.assertFalse(trie.search("app"))
        self.assertTrue(trie.starts_with("app"))
        trie.insert("app")
        self.assertTrue(trie.search("app"))


class TestTrieInsert(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_insert_single_word(self):
        self.trie.insert("hello")
        self.assertTrue(self.trie.search("hello"))

    def test_insert_returns_none(self):
        result = self.trie.insert("word")
        self.assertIsNone(result)

    def test_insert_same_word_twice(self):
        self.trie.insert("hello")
        self.trie.insert("hello")
        self.assertTrue(self.trie.search("hello"))

    def test_insert_single_char(self):
        self.trie.insert("a")
        self.assertTrue(self.trie.search("a"))

    def test_insert_prefix_then_full_word(self):
        self.trie.insert("app")
        self.trie.insert("apple")
        self.assertTrue(self.trie.search("app"))
        self.assertTrue(self.trie.search("apple"))

    def test_insert_full_word_then_prefix(self):
        self.trie.insert("apple")
        self.trie.insert("app")
        self.assertTrue(self.trie.search("apple"))
        self.assertTrue(self.trie.search("app"))

    def test_insert_multiple_words_sharing_prefix(self):
        self.trie.insert("apple")
        self.trie.insert("application")
        self.trie.insert("apply")
        self.assertTrue(self.trie.search("apple"))
        self.assertTrue(self.trie.search("application"))
        self.assertTrue(self.trie.search("apply"))

    def test_insert_words_no_common_prefix(self):
        self.trie.insert("cat")
        self.trie.insert("dog")
        self.assertTrue(self.trie.search("cat"))
        self.assertTrue(self.trie.search("dog"))


class TestTrieSearch(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_search_missing_word_returns_false(self):
        self.assertFalse(self.trie.search("anything"))

    def test_search_prefix_not_inserted_as_word(self):
        self.trie.insert("apple")
        self.assertFalse(self.trie.search("app"))

    def test_search_extension_of_inserted_word(self):
        self.trie.insert("app")
        self.assertFalse(self.trie.search("apple"))

    def test_search_empty_trie(self):
        self.assertFalse(self.trie.search("a"))

    def test_search_returns_bool(self):
        self.trie.insert("hi")
        result = self.trie.search("hi")
        self.assertIsInstance(result, bool)

    def test_search_after_inserting_many_words(self):
        words = ["the", "their", "there", "these", "they"]
        for word in words:
            self.trie.insert(word)
        for word in words:
            self.assertTrue(self.trie.search(word))

    def test_search_word_not_in_set_but_shares_prefix(self):
        self.trie.insert("there")
        self.assertFalse(self.trie.search("the"))
        self.assertFalse(self.trie.search("their"))


class TestTrieStartsWith(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_starts_with_empty_trie(self):
        self.assertFalse(self.trie.starts_with("a"))

    def test_starts_with_full_word_as_prefix(self):
        self.trie.insert("apple")
        self.assertTrue(self.trie.starts_with("apple"))

    def test_starts_with_strict_prefix(self):
        self.trie.insert("apple")
        self.assertTrue(self.trie.starts_with("app"))
        self.assertTrue(self.trie.starts_with("ap"))
        self.assertTrue(self.trie.starts_with("a"))

    def test_starts_with_non_matching_prefix(self):
        self.trie.insert("apple")
        self.assertFalse(self.trie.starts_with("b"))
        self.assertFalse(self.trie.starts_with("banana"))

    def test_starts_with_returns_bool(self):
        self.trie.insert("hello")
        result = self.trie.starts_with("hel")
        self.assertIsInstance(result, bool)

    def test_starts_with_single_char(self):
        self.trie.insert("z")
        self.assertTrue(self.trie.starts_with("z"))

    def test_starts_with_longer_than_any_word(self):
        self.trie.insert("hi")
        self.assertFalse(self.trie.starts_with("hiking"))

    def test_starts_with_after_multiple_inserts(self):
        self.trie.insert("apple")
        self.trie.insert("application")
        self.assertTrue(self.trie.starts_with("appl"))
        self.assertTrue(self.trie.starts_with("appli"))
        self.assertFalse(self.trie.starts_with("applix"))


class TestTrieMixedOperations(unittest.TestCase):
    def test_interleaved_insert_and_search(self):
        trie = Trie()
        self.assertFalse(trie.search("a"))
        trie.insert("a")
        self.assertTrue(trie.search("a"))
        self.assertTrue(trie.starts_with("a"))
        trie.insert("ab")
        self.assertTrue(trie.search("a"))
        self.assertTrue(trie.search("ab"))
        self.assertFalse(trie.search("abc"))

    def test_large_alphabet_coverage(self):
        trie = Trie()
        words = [chr(ord("a") + i) for i in range(26)]
        for word in words:
            trie.insert(word)
        for word in words:
            self.assertTrue(trie.search(word))
            self.assertTrue(trie.starts_with(word))

    def test_long_word(self):
        trie = Trie()
        word = "a" * 2000
        trie.insert(word)
        self.assertTrue(trie.search(word))
        self.assertTrue(trie.starts_with(word[:1000]))
        self.assertFalse(trie.search(word[:1999]))


if __name__ == "__main__":
    unittest.main()
