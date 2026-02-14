import unittest

from generate_parentheses_bfs import Solution


class TestGenerateParenthesesBFS(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_n_1(self):
        expected = ["()"]
        result = self.solution.generate_parentheses_bfs(1)
        self.assertCountEqual(result, expected)

    def test_n_2(self):
        expected = ["(())", "()()"]
        result = self.solution.generate_parentheses_bfs(2)
        self.assertCountEqual(result, expected)

    def test_n_3(self):
        expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        result = self.solution.generate_parentheses_bfs(3)
        self.assertCountEqual(result, expected)

    def test_n_0(self):
        expected = []
        result = self.solution.generate_parentheses_bfs(0)
        self.assertEqual(result, expected)

    def test_output_length(self):
        # Catalan numbers: C_4 = 14
        self.assertEqual(len(self.solution.generate_parentheses_bfs(4)), 14)


if __name__ == "__main__":
    unittest.main()
