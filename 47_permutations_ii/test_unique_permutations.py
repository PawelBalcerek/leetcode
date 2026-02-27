import unittest
from unique_permutations import Solution

class TestUniquePermutations(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        self.assertEqual(self.solution.unique_permutations([]), [[]])

    def test_single_element(self):
        self.assertEqual(self.solution.unique_permutations([1]), [[1]])

    def test_two_different_elements(self):
        result = self.solution.unique_permutations([1, 2])
        expected = [[1, 2], [2, 1]]
        self.assertCountEqual(result, expected)

    def test_two_identical_elements(self):
        result = self.solution.unique_permutations([1, 1])
        expected = [[1, 1]]
        self.assertEqual(result, expected)

    def test_three_elements_with_duplicates(self):
        result = self.solution.unique_permutations([1, 1, 2])
        expected = [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
        self.assertCountEqual(result, expected)

    def test_multiple_duplicates(self):
        result = self.solution.unique_permutations([1, 2, 1, 2])
        expected = [
            [1, 1, 2, 2], [1, 2, 1, 2], [1, 2, 2, 1],
            [2, 1, 1, 2], [2, 1, 2, 1], [2, 2, 1, 1]
        ]
        self.assertCountEqual(result, expected)

    def test_all_identical_elements(self):
        result = self.solution.unique_permutations([1, 1, 1])
        expected = [[1, 1, 1]]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
