import unittest

from next_permutation import Solution


class TestNextPermutation(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        nums = [1, 2, 3]
        self.solution.next_permutation(nums)
        self.assertEqual(nums, [1, 3, 2])

    def test_example2(self):
        nums = [3, 2, 1]
        self.solution.next_permutation(nums)
        self.assertEqual(nums, [1, 2, 3])

    def test_example3(self):
        nums = [1, 1, 5]
        self.solution.next_permutation(nums)
        self.assertEqual(nums, [1, 5, 1])

    def test_single_element(self):
        nums = [1]
        self.solution.next_permutation(nums)
        self.assertEqual(nums, [1])

    def test_two_elements_ascending(self):
        nums = [1, 2]
        self.solution.next_permutation(nums)
        self.assertEqual(nums, [2, 1])

    def test_two_elements_descending(self):
        nums = [2, 1]
        self.solution.next_permutation(nums)
        self.assertEqual(nums, [1, 2])

    def test_all_same_elements(self):
        nums = [1, 1, 1]
        self.solution.next_permutation(nums)
        self.assertEqual(nums, [1, 1, 1])

    def test_longer_sequence(self):
        nums = [1, 2, 3, 6, 5, 4]
        self.solution.next_permutation(nums)
        self.assertEqual(nums, [1, 2, 4, 3, 5, 6])


if __name__ == "__main__":
    unittest.main()
