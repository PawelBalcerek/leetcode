import unittest
from three_sum import Solution

class TestThreeSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_case(self):
        nums = [-1, 0, 1, 2, -1, -4]
        expected = [[-1, -1, 2], [-1, 0, 1]]
        result = self.solution.three_sum(nums)
        # Sort inner lists and outer list to ensure comparison is order-independent
        # regarding the problem statement, although the implementation produces sorted output.
        self.assertCountEqual([sorted(t) for t in result], [sorted(t) for t in expected])

    def test_no_solution(self):
        nums = [0, 1, 1]
        expected = []
        result = self.solution.three_sum(nums)
        self.assertEqual(result, expected)

    def test_all_zeros(self):
        nums = [0, 0, 0]
        expected = [[0, 0, 0]]
        result = self.solution.three_sum(nums)
        self.assertEqual(result, expected)
    
    def test_all_zeros_multiple(self):
        nums = [0, 0, 0, 0]
        expected = [[0, 0, 0]]
        result = self.solution.three_sum(nums)
        self.assertEqual(result, expected)

    def test_duplicates_handling(self):
        nums = [-2, 0, 1, 1, 2]
        expected = [[-2, 0, 2], [-2, 1, 1]]
        result = self.solution.three_sum(nums)
        self.assertCountEqual([sorted(t) for t in result], [sorted(t) for t in expected])

    def test_empty_input(self):
        nums = []
        expected = []
        result = self.solution.three_sum(nums)
        self.assertEqual(result, expected)

    def test_less_than_three_elements(self):
        nums = [0, 0]
        expected = []
        result = self.solution.three_sum(nums)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
