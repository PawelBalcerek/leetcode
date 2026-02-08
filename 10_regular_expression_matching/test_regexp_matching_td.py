import unittest
from regexp_matching_td import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertFalse(self.solution.regexp_matching_td("aa", "a"))

    def test_example_2(self):
        self.assertTrue(self.solution.regexp_matching_td("aa", "a*"))

    def test_example_3(self):
        self.assertTrue(self.solution.regexp_matching_td("ab", ".*"))

    def test_complex_match_1(self):
        self.assertTrue(self.solution.regexp_matching_td("aab", "c*a*b"))

    def test_complex_match_2(self):
        self.assertFalse(self.solution.regexp_matching_td("mississippi", "mis*is*p*."))

    def test_empty_string(self):
        self.assertTrue(self.solution.regexp_matching_td("", "a*"))
        self.assertTrue(self.solution.regexp_matching_td("", ".*"))
        self.assertFalse(self.solution.regexp_matching_td("", "a"))

    def test_dot_matching(self):
        self.assertTrue(self.solution.regexp_matching_td("ab", ".b"))
        self.assertTrue(self.solution.regexp_matching_td("ab", "a."))
        self.assertFalse(self.solution.regexp_matching_td("ab", "..c"))

    def test_star_matching(self):
        self.assertTrue(self.solution.regexp_matching_td("a", "ab*"))
        self.assertTrue(self.solution.regexp_matching_td("aaa", "a*"))
        self.assertTrue(self.solution.regexp_matching_td("aaa", "ab*a*c*"))

    def test_overlap_star(self):
        self.assertTrue(self.solution.regexp_matching_td("bbbba", ".*a*a"))

    def test_complex_multi_star(self):
        self.assertTrue(
            self.solution.regexp_matching_td(
                "aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c*b"
            )
        )


if __name__ == "__main__":
    unittest.main()
