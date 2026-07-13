import unittest

from subset_ii import Solution


class TestSubsetII(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def _assert_subsets(self, nums, expected):
        result = self.solution.subset_ii(nums)
        sorted_result = sorted([sorted(s) for s in result])
        sorted_expected = sorted([sorted(s) for s in expected])
        self.assertEqual(sorted_result, sorted_expected)

    def test_example_1(self):
        self._assert_subsets([1, 2, 2], [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]])

    def test_example_2(self):
        self._assert_subsets([0], [[], [0]])

    def test_single_element(self):
        self._assert_subsets([5], [[], [5]])

    def test_all_duplicates(self):
        self._assert_subsets([1, 1, 1], [[], [1], [1, 1], [1, 1, 1]])

    def test_no_duplicates(self):
        self._assert_subsets(
            [1, 2, 3],
            [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]],
        )

    def test_two_identical_elements(self):
        self._assert_subsets([3, 3], [[], [3], [3, 3]])

    def test_unsorted_input(self):
        self._assert_subsets(
            [3, 1, 2], [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
        )

    def test_negative_numbers(self):
        self._assert_subsets(
            [-1, -1, 2], [[], [-1], [-1, -1], [2], [-1, 2], [-1, -1, 2]]
        )

    def test_mixed_negative_and_positive(self):
        self._assert_subsets(
            [-10, 10],
            [[], [-10], [10], [-10, 10]],
        )

    def test_empty_subset_always_present(self):
        result = self.solution.subset_ii([1, 2, 2])
        self.assertIn([], result)

    def test_no_duplicate_subsets(self):
        result = self.solution.subset_ii([1, 2, 2])
        sorted_result = [sorted(s) for s in result]
        self.assertEqual(len(sorted_result), len(set(tuple(s) for s in sorted_result)))

    def test_max_length_all_same(self):
        nums = [1] * 10
        result = self.solution.subset_ii(nums)
        self.assertEqual(len(result), 11)

    def test_max_length_all_unique(self):
        nums = list(range(-5, 5))
        result = self.solution.subset_ii(nums)
        self.assertEqual(len(result), 2**10)

    def test_zeros(self):
        self._assert_subsets([0, 0], [[], [0], [0, 0]])


if __name__ == "__main__":
    unittest.main()
