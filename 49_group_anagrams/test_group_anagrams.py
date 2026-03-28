import unittest
from group_anagrams import Solution

class TestGroupAnagrams(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def assert_group_equal(self, actual, expected):
        def canonical(groups):
            return sorted([sorted(group) for group in groups])
        
        self.assertEqual(canonical(actual), canonical(expected))

    def test_example_1(self):
        strs = ["eat","tea","tan","ate","nat","bat"]
        expected = [["bat"],["nat","tan"],["ate","eat","tea"]]
        actual = self.sol.group_anagrams(strs)
        self.assert_group_equal(actual, expected)

    def test_example_2(self):
        strs = [""]
        expected = [[""]]
        actual = self.sol.group_anagrams(strs)
        self.assert_group_equal(actual, expected)

    def test_example_3(self):
        strs = ["a"]
        expected = [["a"]]
        actual = self.sol.group_anagrams(strs)
        self.assert_group_equal(actual, expected)

    def test_no_anagrams(self):
        strs = ["abc", "def", "ghi"]
        expected = [["abc"], ["def"], ["ghi"]]
        actual = self.sol.group_anagrams(strs)
        self.assert_group_equal(actual, expected)

    def test_all_anagrams(self):
        strs = ["abc", "bca", "cab"]
        expected = [["abc", "bca", "cab"]]
        actual = self.sol.group_anagrams(strs)
        self.assert_group_equal(actual, expected)

    def test_multiple_groups(self):
        strs = ["abc", "bca", "xyz", "zyx", "pqr"]
        expected = [["abc", "bca"], ["xyz", "zyx"], ["pqr"]]
        actual = self.sol.group_anagrams(strs)
        self.assert_group_equal(actual, expected)

    def test_mixed_length(self):
        strs = ["a", "ab", "abc", "ba", "cba"]
        expected = [["a"], ["ab", "ba"], ["abc", "cba"]]
        actual = self.sol.group_anagrams(strs)
        self.assert_group_equal(actual, expected)

    def test_empty_list(self):
        strs = []
        expected = []
        actual = self.sol.group_anagrams(strs)
        self.assert_group_equal(actual, expected)

    def test_repeated_chars(self):
        strs = ["aabb", "abab", "baba", "bbaa", "abc", "cab"]
        expected = [["aabb", "abab", "baba", "bbaa"], ["abc", "cab"]]
        actual = self.sol.group_anagrams(strs)
        self.assert_group_equal(actual, expected)

if __name__ == "__main__":
    unittest.main()
