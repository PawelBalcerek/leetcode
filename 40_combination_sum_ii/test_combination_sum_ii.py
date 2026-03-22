import unittest
from combination_sum_ii import Solution

class TestCombinationSumII(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def assertEqualIgnoreOrder(self, actual, expected):
        # Sort each inner list and then the outer list for stable comparison
        actual_sorted = sorted([sorted(x) for x in actual])
        expected_sorted = sorted([sorted(x) for x in expected])
        self.assertEqual(actual_sorted, expected_sorted)

    def test_example_1(self):
        candidates = [10, 1, 2, 7, 6, 1, 5]
        target = 8
        expected = [
            [1, 1, 6],
            [1, 2, 5],
            [1, 7],
            [2, 6]
        ]
        self.assertEqualIgnoreOrder(self.solution.combination_sum_ii(candidates, target), expected)

    def test_example_2(self):
        candidates = [2, 5, 2, 1, 2]
        target = 5
        expected = [
            [1, 2, 2],
            [5]
        ]
        self.assertEqualIgnoreOrder(self.solution.combination_sum_ii(candidates, target), expected)

    def test_single_candidate_match(self):
        candidates = [2]
        target = 2
        expected = [[2]]
        self.assertEqualIgnoreOrder(self.solution.combination_sum_ii(candidates, target), expected)

    def test_single_candidate_no_match(self):
        candidates = [2]
        target = 3
        expected = []
        self.assertEqualIgnoreOrder(self.solution.combination_sum_ii(candidates, target), expected)

    def test_duplicate_candidates(self):
        candidates = [1, 1, 1]
        target = 2
        expected = [[1, 1]]
        self.assertEqualIgnoreOrder(self.solution.combination_sum_ii(candidates, target), expected)

    def test_no_solution(self):
        candidates = [2, 3, 5]
        target = 1
        expected = []
        self.assertEqualIgnoreOrder(self.solution.combination_sum_ii(candidates, target), expected)

    def test_large_target(self):
        candidates = [1, 1, 1, 1]
        target = 5
        expected = []
        self.assertEqualIgnoreOrder(self.solution.combination_sum_ii(candidates, target), expected)

if __name__ == '__main__':
    unittest.main()
