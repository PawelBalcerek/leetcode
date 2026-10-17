import unittest
from iterative_course_schedule import Solution as IterativeSolution
from recursive_course_schedule import Solution as RecursiveSolution


class TestCourseSchedule(unittest.TestCase):
    def setUp(self):
        self.solutions = [IterativeSolution(), RecursiveSolution()]

    def assert_all_solutions(self, num_courses: int, prerequisites: list[list[int]], expected: bool):
        for solution in self.solutions:
            with self.subTest(solution=solution.__class__.__module__):
                self.assertEqual(solution.course_schedule(num_courses, prerequisites), expected)

    def test_example_1(self):
        self.assert_all_solutions(2, [[1, 0]], True)

    def test_example_2(self):
        self.assert_all_solutions(2, [[1, 0], [0, 1]], False)

    def test_single_course_no_prerequisites(self):
        self.assert_all_solutions(1, [], True)

    def test_multiple_courses_no_prerequisites(self):
        self.assert_all_solutions(5, [], True)

    def test_self_loop(self):
        self.assert_all_solutions(1, [[0, 0]], False)

    def test_linear_chain(self):
        self.assert_all_solutions(4, [[1, 0], [2, 1], [3, 2]], True)

    def test_cycle_of_three(self):
        self.assert_all_solutions(3, [[1, 0], [2, 1], [0, 2]], False)

    def test_diamond_dependency(self):
        self.assert_all_solutions(4, [[1, 0], [2, 0], [3, 1], [3, 2]], True)

    def test_disconnected_components_valid(self):
        self.assert_all_solutions(6, [[1, 0], [3, 2], [5, 4]], True)

    def test_disconnected_components_with_cycle(self):
        self.assert_all_solutions(6, [[1, 0], [3, 2], [2, 3], [5, 4]], False)

    def test_star_graph_one_prerequisite_for_many(self):
        self.assert_all_solutions(5, [[1, 0], [2, 0], [3, 0], [4, 0]], True)

    def test_star_graph_many_prerequisites_for_one(self):
        self.assert_all_solutions(5, [[0, 1], [0, 2], [0, 3], [0, 4]], True)

    def test_cycle_not_involving_all_nodes(self):
        self.assert_all_solutions(5, [[1, 0], [2, 1], [3, 2], [1, 3], [4, 0]], False)

    def test_complex_dag(self):
        prerequisites = [
            [1, 0], [2, 0], [3, 1], [3, 2],
            [4, 2], [5, 3], [5, 4]
        ]
        self.assert_all_solutions(6, prerequisites, True)


if __name__ == "__main__":
    unittest.main()
