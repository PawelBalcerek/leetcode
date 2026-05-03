import unittest
from evaluate_reverse_polish_notation import Solution

class TestEvaluateReversePolishNotation(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        tokens = ["2", "1", "+", "3", "*"]
        expected = 9
        self.assertEqual(self.solution.evaluate_reverse_polish_notation(tokens), expected)

    def test_example_2(self):
        tokens = ["4", "13", "5", "/", "+"]
        expected = 6
        self.assertEqual(self.solution.evaluate_reverse_polish_notation(tokens), expected)

    def test_example_3(self):
        tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        expected = 22
        self.assertEqual(self.solution.evaluate_reverse_polish_notation(tokens), expected)

    def test_single_operand(self):
        tokens = ["18"]
        expected = 18
        self.assertEqual(self.solution.evaluate_reverse_polish_notation(tokens), expected)

    def test_negative_result(self):
        tokens = ["3", "-4", "+"]
        expected = -1
        self.assertEqual(self.solution.evaluate_reverse_polish_notation(tokens), expected)

    def test_truncation_toward_zero(self):
        tokens = ["6", "-132", "/"]
        expected = 0
        self.assertEqual(self.solution.evaluate_reverse_polish_notation(tokens), expected)
        
        tokens = ["1", "2", "/"]
        expected = 0
        self.assertEqual(self.solution.evaluate_reverse_polish_notation(tokens), expected)

        tokens = ["-1", "2", "/"]
        expected = 0
        self.assertEqual(self.solution.evaluate_reverse_polish_notation(tokens), expected)

if __name__ == "__main__":
    unittest.main()
