import unittest
from permutation_in_string import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        s1 = "ab"
        s2 = "eidbaooo"
        self.assertTrue(self.solution.permutation_in_string(s1, s2))

    def test_example2(self):
        s1 = "ab"
        s2 = "eidboaoo"
        self.assertFalse(self.solution.permutation_in_string(s1, s2))

    def test_s1_longer_than_s2(self):
        s1 = "abcd"
        s2 = "abc"
        self.assertFalse(self.solution.permutation_in_string(s1, s2))

    def test_exact_match(self):
        s1 = "abc"
        s2 = "abc"
        self.assertTrue(self.solution.permutation_in_string(s1, s2))

    def test_permutation_at_start(self):
        s1 = "abc"
        s2 = "cbaquiet"
        self.assertTrue(self.solution.permutation_in_string(s1, s2))

    def test_permutation_at_end(self):
        s1 = "abc"
        s2 = "quietcba"
        self.assertTrue(self.solution.permutation_in_string(s1, s2))

    def test_single_character_match(self):
        s1 = "a"
        s2 = "bca"
        self.assertTrue(self.solution.permutation_in_string(s1, s2))

    def test_single_character_no_match(self):
        s1 = "a"
        s2 = "bcd"
        self.assertFalse(self.solution.permutation_in_string(s1, s2))

    def test_all_same_characters(self):
        s1 = "aaa"
        s2 = "aaaaa"
        self.assertTrue(self.solution.permutation_in_string(s1, s2))

    def test_all_different_characters(self):
        s1 = "abc"
        s2 = "defgh"
        self.assertFalse(self.solution.permutation_in_string(s1, s2))

    def test_permutation_in_middle(self):
        s1 = "abc"
        s2 = "deabcgh"
        self.assertTrue(self.solution.permutation_in_string(s1, s2))

if __name__ == "__main__":
    unittest.main()
