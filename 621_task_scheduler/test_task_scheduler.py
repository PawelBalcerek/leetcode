import unittest

from task_scheduler import Solution


class TestTaskScheduler(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.task_scheduler(["A", "A", "A", "B", "B", "B"], 2), 8)

    def test_example_2(self):
        self.assertEqual(self.solution.task_scheduler(["A", "C", "A", "B", "D", "B"], 1), 6)

    def test_example_3(self):
        self.assertEqual(self.solution.task_scheduler(["A", "A", "A", "B", "B", "B"], 3), 10)

    def test_single_task(self):
        self.assertEqual(self.solution.task_scheduler(["A"], 0), 1)

    def test_single_task_with_cooldown(self):
        self.assertEqual(self.solution.task_scheduler(["A"], 5), 1)

    def test_zero_cooldown(self):
        self.assertEqual(self.solution.task_scheduler(["A", "A", "A", "B", "B", "B"], 0), 6)

    def test_all_same_tasks(self):
        self.assertEqual(self.solution.task_scheduler(["A", "A", "A", "A"], 2), 10)

    def test_all_unique_tasks(self):
        self.assertEqual(self.solution.task_scheduler(["A", "B", "C", "D", "E", "F"], 2), 6)

    def test_cooldown_larger_than_task_types(self):
        self.assertEqual(self.solution.task_scheduler(["A", "A", "B", "B"], 3), 6)

    def test_many_task_types_small_cooldown(self):
        self.assertEqual(self.solution.task_scheduler(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"], 1), 10)

    def test_two_tasks_cooldown_one(self):
        self.assertEqual(self.solution.task_scheduler(["A", "A", "B", "B"], 1), 4)

    def test_large_cooldown_single_type(self):
        self.assertEqual(self.solution.task_scheduler(["A", "A"], 100), 102)

    def test_uneven_task_distribution(self):
        self.assertEqual(self.solution.task_scheduler(["A", "A", "A", "B"], 2), 7)

    def test_many_same_tasks_cooldown_one(self):
        self.assertEqual(self.solution.task_scheduler(["A", "A", "A", "A", "A", "A"], 1), 11)

    def test_three_types_cooldown_two(self):
        self.assertEqual(self.solution.task_scheduler(["A", "A", "A", "B", "B", "B", "C", "C", "C"], 2), 9)

    def test_cooldown_equals_task_count_minus_one(self):
        self.assertEqual(self.solution.task_scheduler(["A", "A", "A"], 2), 7)


if __name__ == "__main__":
    unittest.main()
