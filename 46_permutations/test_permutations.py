import unittest
from permutations import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.methods = [
            self.solution.permutations_recursive,
            self.solution.permutations_iterative,
            self.solution.permutations_backtracking
        ]

    def test_empty_list(self):
        for method in self.methods:
            with self.subTest(method=method.__name__):
                self.assertEqual(method([]), [[]])

    def test_single_element(self):
        for method in self.methods:
            with self.subTest(method=method.__name__):
                self.assertEqual(method([1]), [[1]])

    def test_two_elements(self):
        expected = [[1, 2], [2, 1]]
        for method in self.methods:
            with self.subTest(method=method.__name__):
                result = method([1, 2])
                self.assertCountEqual(result, expected)

    def test_three_elements(self):
        expected = [
            [1, 2, 3], [2, 1, 3], [2, 3, 1],
            [1, 3, 2], [3, 1, 2], [3, 2, 1]
        ]
        for method in self.methods:
            with self.subTest(method=method.__name__):
                result = method([1, 2, 3])
                self.assertCountEqual(result, expected)

    def test_four_elements(self):
        for method in self.methods:
            with self.subTest(method=method.__name__):
                result = method([1, 2, 3, 4])
                self.assertEqual(len(result), 24)

    def test_duplicate_elements(self):
        expected = [[1, 1], [1, 1]]
        for method in self.methods:
            with self.subTest(method=method.__name__):
                result = method([1, 1])
                self.assertCountEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
