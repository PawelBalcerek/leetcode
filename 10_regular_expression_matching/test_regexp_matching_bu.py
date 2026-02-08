import unittest
from regexp_matching_bu import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertFalse(self.solution.regexp_matching_bu("aa", "a"))

    def test_example_2(self):
        self.assertTrue(self.solution.regexp_matching_bu("aa", "a*"))

    def test_example_3(self):
        self.assertTrue(self.solution.regexp_matching_bu("ab", ".*"))

    def test_complex_match_1(self):
        self.assertTrue(self.solution.regexp_matching_bu("aab", "c*a*b"))

    def test_complex_match_2(self):
        self.assertFalse(self.solution.regexp_matching_bu("mississippi", "mis*is*p*."))

    def test_empty_string(self):
        self.assertTrue(self.solution.regexp_matching_bu("", "a*"))
        self.assertTrue(self.solution.regexp_matching_bu("", ".*"))
        self.assertFalse(self.solution.regexp_matching_bu("", "a"))

    def test_dot_matching(self):
        self.assertTrue(self.solution.regexp_matching_bu("ab", ".b"))
        self.assertTrue(self.solution.regexp_matching_bu("ab", "a."))
        self.assertFalse(self.solution.regexp_matching_bu("ab", "..c"))

    def test_star_matching(self):
        self.assertTrue(self.solution.regexp_matching_bu("a", "ab*"))
        self.assertTrue(self.solution.regexp_matching_bu("aaa", "a*"))
        self.assertTrue(self.solution.regexp_matching_bu("aaa", "ab*a*c*"))

    def test_overlap_star(self):
        self.assertTrue(self.solution.regexp_matching_bu("bbbba", ".*a*a"))

    def test_complex_multi_star(self):
        self.assertTrue(self.solution.regexp_matching_bu("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c*b"))

if __name__ == "__main__":
    unittest.main()
