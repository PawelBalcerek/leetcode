import unittest
from minimum_window_substring import Solution

class TestMinimumWindowSubstring(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s = "ADOBECODEBANC"
        t = "ABC"
        expected = "BANC"
        self.assertEqual(self.solution.minimum_window_substring(s, t), expected)

    def test_example_2(self):
        s = "a"
        t = "a"
        expected = "a"
        self.assertEqual(self.solution.minimum_window_substring(s, t), expected)

    def test_example_3(self):
        s = "a"
        t = "aa"
        expected = ""
        self.assertEqual(self.solution.minimum_window_substring(s, t), expected)

    def test_no_match(self):
        s = "abcdef"
        t = "gh"
        expected = ""
        self.assertEqual(self.solution.minimum_window_substring(s, t), expected)

    def test_duplicate_chars_in_t(self):
        s = "abbbbbcdd"
        t = "abcd"
        expected = "abbbbbcd"
        self.assertEqual(self.solution.minimum_window_substring(s, t), expected)

    def test_all_chars_match(self):
        s = "aa"
        t = "aa"
        expected = "aa"
        self.assertEqual(self.solution.minimum_window_substring(s, t), expected)

    def test_t_longer_than_s(self):
        s = "abc"
        t = "abcd"
        expected = ""
        self.assertEqual(self.solution.minimum_window_substring(s, t), expected)

    def test_multiple_potential_windows(self):
        s = "caae"
        t = "cae"
        expected = "caae"
        self.assertEqual(self.solution.minimum_window_substring(s, t), expected)
        
        s2 = "ADOBECODEBANC"
        t2 = "ABC"
        self.assertEqual(self.solution.minimum_window_substring(s2, t2), "BANC")

    def test_case_sensitivity(self):
        s = "aAbB"
        t = "aB"
        expected = "aAbB"
        self.assertEqual(self.solution.minimum_window_substring(s, t), expected)

if __name__ == "__main__":
    unittest.main()
