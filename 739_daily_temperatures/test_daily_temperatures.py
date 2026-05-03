import unittest
from daily_temperatures import Solution

class TestDailyTemperatures(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
        expected = [1, 1, 4, 2, 1, 1, 0, 0]
        self.assertEqual(self.solution.daily_temperatures(temperatures), expected)

    def test_example_2(self):
        temperatures = [30, 40, 50, 60]
        expected = [1, 1, 1, 0]
        self.assertEqual(self.solution.daily_temperatures(temperatures), expected)

    def test_example_3(self):
        temperatures = [30, 60, 90]
        expected = [1, 1, 0]
        self.assertEqual(self.solution.daily_temperatures(temperatures), expected)

    def test_single_temperature(self):
        temperatures = [30]
        expected = [0]
        self.assertEqual(self.solution.daily_temperatures(temperatures), expected)

    def test_decreasing_temperatures(self):
        temperatures = [90, 80, 70, 60]
        expected = [0, 0, 0, 0]
        self.assertEqual(self.solution.daily_temperatures(temperatures), expected)

    def test_increasing_temperatures(self):
        temperatures = [60, 70, 80, 90]
        expected = [1, 1, 1, 0]
        self.assertEqual(self.solution.daily_temperatures(temperatures), expected)

    def test_same_temperatures(self):
        temperatures = [70, 70, 70, 70]
        expected = [0, 0, 0, 0]
        self.assertEqual(self.solution.daily_temperatures(temperatures), expected)

if __name__ == '__main__':
    unittest.main()
