import unittest

from generate_parentheses_dfs import Solution


class TestGenerateParenthesesDFS(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_n_1(self):
        expected = ["()"]
        result = self.solution.generate_parentheses_dfs(1)
        self.assertCountEqual(result, expected)

    def test_n_2(self):
        expected = ["(())", "()()"]
        result = self.solution.generate_parentheses_dfs(2)
        self.assertCountEqual(result, expected)

    def test_n_3(self):
        expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        result = self.solution.generate_parentheses_dfs(3)
        self.assertCountEqual(result, expected)

    def test_n_0(self):
        # Constraints say 1 <= n <= 8, but let's see how it handles 0
        expected = [""]
        result = self.solution.generate_parentheses_dfs(0)
        self.assertCountEqual(result, expected)

    def test_output_length(self):
        # Catalan numbers: C_n = (1 / (n+1)) * (2n choose n)
        # C_1 = 1
        # C_2 = 2
        # C_3 = 5
        # C_4 = 14
        self.assertEqual(len(self.solution.generate_parentheses_dfs(4)), 14)


if __name__ == "__main__":
    unittest.main()
