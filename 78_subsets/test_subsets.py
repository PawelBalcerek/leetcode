import unittest

from subsets import Solution


class TestSubsets(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_three_elements(self):
        result = self.solution.subsets([1, 2, 3])
        expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        self.assertEqual(sorted(map(sorted, result)), sorted(map(sorted, expected)))

    def test_single_element(self):
        result = self.solution.subsets([0])
        expected = [[], [0]]
        self.assertEqual(sorted(map(sorted, result)), sorted(map(sorted, expected)))

    def test_two_elements(self):
        result = self.solution.subsets([1, 2])
        expected = [[], [1], [2], [1, 2]]
        self.assertEqual(sorted(map(sorted, result)), sorted(map(sorted, expected)))

    def test_single_negative(self):
        result = self.solution.subsets([-5])
        expected = [[], [-5]]
        self.assertEqual(sorted(map(sorted, result)), sorted(map(sorted, expected)))

    def test_negative_and_positive(self):
        result = self.solution.subsets([-1, 0, 1])
        expected = [[], [-1], [0], [1], [-1, 0], [-1, 1], [0, 1], [-1, 0, 1]]
        self.assertEqual(sorted(map(sorted, result)), sorted(map(sorted, expected)))

    def test_correct_count(self):
        result = self.solution.subsets([1, 2, 3, 4])
        self.assertEqual(len(result), 16)

    def test_no_duplicate_subsets(self):
        result = self.solution.subsets([1, 2, 3])
        as_tuples = [tuple(sorted(s)) for s in result]
        self.assertEqual(len(as_tuples), len(set(as_tuples)))

    def test_empty_subset_always_present(self):
        result = self.solution.subsets([5, 10])
        self.assertIn([], result)

    def test_full_set_always_present(self):
        result = self.solution.subsets([5, 10])
        self.assertTrue(any(sorted(s) == [5, 10] for s in result))

    def test_max_length(self):
        nums = list(range(-5, 5))
        result = self.solution.subsets(nums)
        self.assertEqual(len(result), 1024)


if __name__ == "__main__":
    unittest.main()
