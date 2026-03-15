import unittest
from count_and_say import Solution

class TestCountAndSay(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_iterative_n1(self):
        self.assertEqual(self.solution.count_and_say_iterative(1), "1")

    def test_recursive_n1(self):
        self.assertEqual(self.solution.count_and_say_recursive(1), "1")

    def test_iterative_n2(self):
        self.assertEqual(self.solution.count_and_say_iterative(2), "11")

    def test_recursive_n2(self):
        self.assertEqual(self.solution.count_and_say_recursive(2), "11")

    def test_iterative_n3(self):
        self.assertEqual(self.solution.count_and_say_iterative(3), "21")

    def test_recursive_n3(self):
        self.assertEqual(self.solution.count_and_say_recursive(3), "21")

    def test_iterative_n4(self):
        self.assertEqual(self.solution.count_and_say_iterative(4), "1211")

    def test_recursive_n4(self):
        self.assertEqual(self.solution.count_and_say_recursive(4), "1211")

    def test_iterative_n5(self):
        self.assertEqual(self.solution.count_and_say_iterative(5), "111221")

    def test_recursive_n5(self):
        self.assertEqual(self.solution.count_and_say_recursive(5), "111221")

    def test_comparison_n10(self):
        res_iterative = self.solution.count_and_say_iterative(10)
        res_recursive = self.solution.count_and_say_recursive(10)
        self.assertEqual(res_iterative, res_recursive)

    def test_comparison_n30(self):
        res_iterative = self.solution.count_and_say_iterative(30)
        res_recursive = self.solution.count_and_say_recursive(30)
        self.assertEqual(res_iterative, res_recursive)

if __name__ == '__main__':
    unittest.main()
