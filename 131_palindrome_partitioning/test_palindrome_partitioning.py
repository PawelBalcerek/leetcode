import unittest

from palindrome_partitioning import Solution


class TestPalindromePartitioning(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def sorted_result(self, result):
        return sorted([sorted(partition) for partition in result])

    def test_example_aab(self):
        result = self.solution.palindrome_partitioning("aab")
        self.assertEqual(
            sorted(map(sorted, result)),
            sorted(map(sorted, [["a", "a", "b"], ["aa", "b"]])),
        )

    def test_example_single_char(self):
        result = self.solution.palindrome_partitioning("a")
        self.assertEqual(result, [["a"]])

    def test_all_same_characters(self):
        result = self.solution.palindrome_partitioning("aaa")
        expected = [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]]
        self.assertEqual(sorted(result), sorted(expected))

    def test_two_different_chars(self):
        result = self.solution.palindrome_partitioning("ab")
        expected = [["a", "b"]]
        self.assertEqual(result, expected)

    def test_palindrome_string(self):
        result = self.solution.palindrome_partitioning("aba")
        expected = [["a", "b", "a"], ["aba"]]
        self.assertEqual(sorted(result), sorted(expected))

    def test_longer_palindrome(self):
        result = self.solution.palindrome_partitioning("abba")
        expected = [["a", "b", "b", "a"], ["a", "bb", "a"], ["abba"]]
        self.assertEqual(sorted(result), sorted(expected))

    def test_no_internal_palindromes(self):
        result = self.solution.palindrome_partitioning("abcd")
        expected = [["a", "b", "c", "d"]]
        self.assertEqual(result, expected)

    def test_returns_list_of_lists(self):
        result = self.solution.palindrome_partitioning("a")
        self.assertIsInstance(result, list)
        self.assertIsInstance(result[0], list)

    def test_all_partitions_are_palindromes(self):
        for s in ["aab", "aba", "abba", "racecar", "aaa"]:
            result = self.solution.palindrome_partitioning(s)
            for partition in result:
                for part in partition:
                    self.assertEqual(part, part[::-1])

    def test_partitions_reconstruct_original(self):
        for s in ["aab", "aba", "abba", "racecar", "abc"]:
            result = self.solution.palindrome_partitioning(s)
            for partition in result:
                self.assertEqual("".join(partition), s)

    def test_is_palindrome_true(self):
        self.assertTrue(self.solution.is_palindrome("racecar", 0, 6))
        self.assertTrue(self.solution.is_palindrome("abba", 0, 3))
        self.assertTrue(self.solution.is_palindrome("a", 0, 0))

    def test_is_palindrome_false(self):
        self.assertFalse(self.solution.is_palindrome("ab", 0, 1))
        self.assertFalse(self.solution.is_palindrome("abc", 0, 2))

    def test_is_palindrome_single_char(self):
        self.assertTrue(self.solution.is_palindrome("x", 0, 0))

    def test_racecar(self):
        result = self.solution.palindrome_partitioning("racecar")
        self.assertIn(["racecar"], result)
        self.assertIn(["r", "a", "c", "e", "c", "a", "r"], result)

    def test_result_count_aab(self):
        result = self.solution.palindrome_partitioning("aab")
        self.assertEqual(len(result), 2)


if __name__ == "__main__":
    unittest.main()
