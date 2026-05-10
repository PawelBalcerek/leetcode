import unittest
from happy_number import Solution

class TestHappyNumber(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertTrue(self.solution.happy_number(100))

    def test_example_2(self):
        self.assertFalse(self.solution.happy_number(101))

    def test_n_is_1(self):
        self.assertTrue(self.solution.happy_number(1))

    def test_n_is_7(self):
        self.assertTrue(self.solution.happy_number(7))

    def test_n_is_1000(self):
        self.assertTrue(self.solution.happy_number(1000))

    def test_n_is_2(self):
        self.assertFalse(self.solution.happy_number(2))

if __name__ == '__main__':
    unittest.main()
