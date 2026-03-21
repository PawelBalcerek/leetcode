import unittest
from combination_sum import Solution

class TestCombinationSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def normalize(self, results):
        """Sorts both inner lists and the outer list to allow for comparison."""
        return sorted([sorted(res) for res in results])

    def test_example_1(self):
        candidates = [2, 3, 6, 7]
        target = 7
        expected = self.normalize([[2, 2, 3], [7]])
        actual = self.normalize(self.solution.combination_sum(candidates, target))
        self.assertEqual(actual, expected)

    def test_example_2(self):
        candidates = [2, 3, 5]
        target = 8
        expected = self.normalize([[2, 2, 2, 2], [2, 3, 3], [3, 5]])
        actual = self.normalize(self.solution.combination_sum(candidates, target))
        self.assertEqual(actual, expected)

    def test_example_3(self):
        candidates = [2]
        target = 1
        expected = []
        actual = self.solution.combination_sum(candidates, target)
        self.assertEqual(actual, expected)

    def test_no_possible_combinations(self):
        candidates = [3, 5]
        target = 2
        expected = []
        actual = self.solution.combination_sum(candidates, target)
        self.assertEqual(actual, expected)

    def test_single_candidate_multiple_times(self):
        candidates = [2]
        target = 6
        expected = [[2, 2, 2]]
        actual = self.normalize(self.solution.combination_sum(candidates, target))
        self.assertEqual(actual, expected)

    def test_target_is_candidate(self):
        candidates = [2, 4, 6]
        target = 6
        expected = self.normalize([[2, 2, 2], [2, 4], [6]])
        actual = self.normalize(self.solution.combination_sum(candidates, target))
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
