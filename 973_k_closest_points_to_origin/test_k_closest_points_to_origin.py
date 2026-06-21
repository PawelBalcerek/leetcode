import unittest

from k_closest_points_to_origin import Solution


class TestKClosestPointsToOrigin(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        result = self.solution.k_closest_points_to_origin([[1, 3], [-2, 2]], 1)
        self.assertEqual(result, [[-2, 2]])

    def test_example_2(self):
        result = self.solution.k_closest_points_to_origin([[3, 3], [5, -1], [-2, 4]], 2)
        self.assertEqual(sorted(result), sorted([[3, 3], [-2, 4]]))

    def test_single_point(self):
        result = self.solution.k_closest_points_to_origin([[1, 1]], 1)
        self.assertEqual(result, [[1, 1]])

    def test_k_equals_length(self):
        points = [[1, 2], [3, 4], [5, 6]]
        result = self.solution.k_closest_points_to_origin(points, 3)
        self.assertEqual(sorted(result), sorted(points))

    def test_origin_point(self):
        result = self.solution.k_closest_points_to_origin([[0, 0], [1, 1]], 1)
        self.assertEqual(result, [[0, 0]])

    def test_negative_coordinates(self):
        result = self.solution.k_closest_points_to_origin(
            [[-1, -1], [-3, -3], [-2, -2]], 2
        )
        self.assertEqual(sorted(result), sorted([[-1, -1], [-2, -2]]))

    def test_same_distance(self):
        result = self.solution.k_closest_points_to_origin([[1, 0], [0, 1], [10, 10]], 2)
        self.assertEqual(sorted(result), sorted([[1, 0], [0, 1]]))

    def test_large_coordinates(self):
        result = self.solution.k_closest_points_to_origin(
            [[10000, 10000], [-10000, -10000], [1, 1]], 1
        )
        self.assertEqual(result, [[1, 1]])

    def test_mixed_positive_negative(self):
        result = self.solution.k_closest_points_to_origin([[1, -1], [-1, 1], [3, 3]], 2)
        self.assertEqual(sorted(result), sorted([[1, -1], [-1, 1]]))

    def test_points_on_axes(self):
        result = self.solution.k_closest_points_to_origin([[5, 0], [0, 3], [0, -2]], 1)
        self.assertEqual(result, [[0, -2]])


if __name__ == "__main__":
    unittest.main()
