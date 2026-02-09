import unittest
from valid_parentheses import Solution


class TestValidParentheses(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertTrue(self.solution.valid_parentheses("()"))

    def test_example2(self):
        self.assertTrue(self.solution.valid_parentheses("()[]{}"))

    def test_example3(self):
        self.assertFalse(self.solution.valid_parentheses("(]"))

    def test_example4(self):
        self.assertTrue(self.solution.valid_parentheses("([])"))

    def test_example5(self):
        self.assertFalse(self.solution.valid_parentheses("([)]"))

    def test_single_open(self):
        self.assertFalse(self.solution.valid_parentheses("("))

    def test_single_close(self):
        self.assertFalse(self.solution.valid_parentheses(")"))

    def test_mismatched_types(self):
        self.assertFalse(self.solution.valid_parentheses("(]"))

    def test_empty_stack_on_close(self):
        self.assertFalse(self.solution.valid_parentheses("]"))

    def test_complex_valid(self):
        self.assertTrue(self.solution.valid_parentheses("{[()]}"))

    def test_complex_invalid(self):
        self.assertFalse(self.solution.valid_parentheses("{[(])}"))


if __name__ == "__main__":
    unittest.main()
