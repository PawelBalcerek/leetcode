import unittest

from course_schedule_ii import Solution


class TestCourseScheduleII(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def assert_valid_order(self, num_courses: int, prerequisites: list[list[int]]):
        order = self.solution.course_schedule_ii(num_courses, prerequisites)
        self.assertEqual(len(order), num_courses)
        self.assertEqual(set(order), set(range(num_courses)))
        position = {course: idx for idx, course in enumerate(order)}
        for course, prereq in prerequisites:
            self.assertLess(position[prereq], position[course])

    def assert_impossible(self, num_courses: int, prerequisites: list[list[int]]):
        self.assertEqual(
            self.solution.course_schedule_ii(num_courses, prerequisites), []
        )

    def test_example_1(self):
        self.assertEqual(self.solution.course_schedule_ii(2, [[1, 0]]), [0, 1])

    def test_example_2(self):
        prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
        self.assert_valid_order(4, prerequisites)

    def test_example_3(self):
        self.assertEqual(self.solution.course_schedule_ii(1, []), [0])

    def test_multiple_courses_no_prerequisites(self):
        self.assert_valid_order(5, [])

    def test_two_course_cycle(self):
        self.assert_impossible(2, [[1, 0], [0, 1]])

    def test_three_course_cycle(self):
        self.assert_impossible(3, [[1, 0], [2, 1], [0, 2]])

    def test_linear_chain(self):
        self.assertEqual(
            self.solution.course_schedule_ii(4, [[1, 0], [2, 1], [3, 2]]),
            [0, 1, 2, 3],
        )

    def test_reverse_labeled_linear_chain(self):
        self.assertEqual(
            self.solution.course_schedule_ii(4, [[0, 1], [1, 2], [2, 3]]),
            [3, 2, 1, 0],
        )

    def test_disconnected_components_valid(self):
        self.assert_valid_order(6, [[1, 0], [3, 2], [5, 4]])

    def test_disconnected_components_with_cycle(self):
        self.assert_impossible(6, [[1, 0], [3, 2], [2, 3], [5, 4]])

    def test_star_graph_one_prerequisite_for_many(self):
        self.assert_valid_order(5, [[1, 0], [2, 0], [3, 0], [4, 0]])

    def test_star_graph_many_prerequisites_for_one(self):
        self.assert_valid_order(5, [[0, 1], [0, 2], [0, 3], [0, 4]])

    def test_cycle_not_involving_all_nodes(self):
        self.assert_impossible(5, [[1, 0], [2, 1], [3, 2], [1, 3], [4, 0]])

    def test_complex_dag(self):
        prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [4, 2], [5, 3], [5, 4]]
        self.assert_valid_order(6, prerequisites)

    def test_isolated_courses_with_dependencies(self):
        self.assert_valid_order(5, [[2, 1], [3, 2]])


if __name__ == "__main__":
    unittest.main()
