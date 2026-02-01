import unittest

from two_sum_pointers import Solution


class TestTwoSumPointers(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        numbers = [2, 7, 11, 15]
        target = 9
        expected = [1, 2]
        self.assertEqual(self.solution.two_sum_pointers(numbers, target), expected)

    def test_example_2(self):
        numbers = [2, 3, 4]
        target = 6
        expected = [1, 3]
        self.assertEqual(self.solution.two_sum_pointers(numbers, target), expected)

    def test_example_3(self):
        numbers = [-1, 0]
        target = -1
        expected = [1, 2]
        self.assertEqual(self.solution.two_sum_pointers(numbers, target), expected)

    def test_first_element_not_in_solution(self):
        numbers = [1, 3, 4, 5]
        target = 9  # 4 + 5 = 9, indices 3 and 4
        expected = [3, 4]
        self.assertEqual(self.solution.two_sum_pointers(numbers, target), expected)

    def test_no_solution(self):
        # Although problem guarantees exactly one solution, good to handle graceful failure or empty list
        numbers = [1, 2, 3]
        target = 10
        expected = []
        self.assertEqual(self.solution.two_sum_pointers(numbers, target), expected)


if __name__ == "__main__":
    unittest.main()
