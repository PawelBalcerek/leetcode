import unittest
from car_fleet import Solution

class TestCarFleet(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        target = 12
        position = [10, 8, 0, 5, 3]
        speed = [2, 4, 1, 1, 3]
        self.assertEqual(self.solution.car_fleet(target, position, speed), 3)

    def test_example2(self):
        target = 10
        position = [3]
        speed = [3]
        self.assertEqual(self.solution.car_fleet(target, position, speed), 1)

    def test_example3(self):
        target = 100
        position = [0, 2, 4]
        speed = [4, 2, 1]
        self.assertEqual(self.solution.car_fleet(target, position, speed), 1)

    def test_all_separate(self):
        target = 10
        position = [0, 2, 4]
        speed = [1, 1, 1]
        self.assertEqual(self.solution.car_fleet(target, position, speed), 3)

    def test_all_one_fleet(self):
        target = 10
        position = [0, 4, 2]
        speed = [10, 2, 5]
        self.assertEqual(self.solution.car_fleet(target, position, speed), 1)

    def test_meet_at_target(self):
        target = 10
        position = [0, 5]
        speed = [2, 1]
        self.assertEqual(self.solution.car_fleet(target, position, speed), 1)

if __name__ == '__main__':
    unittest.main()
