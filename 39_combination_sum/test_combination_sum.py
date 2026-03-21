import unittest
from combination_sum import Solution as BacktrackingSolution
from combination_sum_dp import Solution as DPSolution

class TestCombinationSum(unittest.TestCase):
    def setUp(self):
        self.backtracking_sol = BacktrackingSolution()
        self.dp_sol = DPSolution()

    def normalize(self, results):
        """Sorts both inner lists and the outer list to allow for comparison."""
        return sorted([sorted(res) for res in results])

    def _run_test(self, candidates, target, expected):
        # Test Backtracking
        with self.subTest(method="backtracking", candidates=candidates, target=target):
            actual = self.backtracking_sol.combination_sum(candidates, target)
            self.assertEqual(self.normalize(actual), self.normalize(expected))
        
        # Test DP
        with self.subTest(method="dp", candidates=candidates, target=target):
            actual = self.dp_sol.combination_sum_dp(candidates, target)
            self.assertEqual(self.normalize(actual), self.normalize(expected))

    def test_example_1(self):
        candidates = [2, 3, 6, 7]
        target = 7
        expected = [[2, 2, 3], [7]]
        self._run_test(candidates, target, expected)

    def test_example_2(self):
        candidates = [2, 3, 5]
        target = 8
        expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        self._run_test(candidates, target, expected)

    def test_example_3(self):
        candidates = [2]
        target = 1
        expected = []
        self._run_test(candidates, target, expected)

    def test_no_possible_combinations(self):
        candidates = [3, 5]
        target = 2
        expected = []
        self._run_test(candidates, target, expected)

    def test_single_candidate_multiple_times(self):
        candidates = [2]
        target = 6
        expected = [[2, 2, 2]]
        self._run_test(candidates, target, expected)

    def test_target_is_candidate(self):
        candidates = [2, 4, 6]
        target = 6
        expected = [[2, 2, 2], [2, 4], [6]]
        self._run_test(candidates, target, expected)

if __name__ == '__main__':
    unittest.main()
