import unittest
from climbing_stairs import Solution

class TestClimbingStairs(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_n_1(self):
        self.assertEqual(self.solution.climbing_stairs(1), 1)

    def test_n_2(self):
        self.assertEqual(self.solution.climbing_stairs(2), 2)

    def test_n_3(self):
        self.assertEqual(self.solution.climbing_stairs(3), 3)

    def test_n_4(self):
        self.assertEqual(self.solution.climbing_stairs(4), 5)

    def test_n_5(self):
        self.assertEqual(self.solution.climbing_stairs(5), 8)

    def test_n_45(self):
        self.assertEqual(self.solution.climbing_stairs(45), 1836311903)

if __name__ == '__main__':
    unittest.main()
