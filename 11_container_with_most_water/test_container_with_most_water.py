import unittest
from container_with_most_water import Solution


class TestContainerWithMostWater(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(
            self.solution.container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49
        )

    def test_example_2(self):
        self.assertEqual(self.solution.container_with_most_water([1, 1]), 1)

    def test_all_same_height(self):
        self.assertEqual(self.solution.container_with_most_water([5, 5, 5, 5]), 15)

    def test_descending_heights(self):
        self.assertEqual(self.solution.container_with_most_water([5, 4, 3, 2, 1]), 6)

    def test_ascending_heights(self):
        self.assertEqual(self.solution.container_with_most_water([1, 2, 3, 4, 5]), 6)

    def test_large_distance_small_height(self):
        self.assertEqual(self.solution.container_with_most_water([1, 2, 1]), 2)

    def test_min_elements(self):
        self.assertEqual(self.solution.container_with_most_water([1, 1]), 1)


if __name__ == "__main__":
    unittest.main()
