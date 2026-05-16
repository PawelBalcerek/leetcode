import unittest
from koko_eating_bananas import Solution

class TestKokoEatingBananas(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        piles = [3, 6, 7, 11]
        h = 8
        self.assertEqual(self.solution.koko_eating_bananas(piles, h), 4)

    def test_example_2(self):
        piles = [30, 11, 23, 4, 20]
        h = 5
        self.assertEqual(self.solution.koko_eating_bananas(piles, h), 30)

    def test_example_3(self):
        piles = [30, 11, 23, 4, 20]
        h = 6
        self.assertEqual(self.solution.koko_eating_bananas(piles, h), 23)

    def test_single_pile(self):
        piles = [10]
        h = 5
        self.assertEqual(self.solution.koko_eating_bananas(piles, h), 2)

    def test_h_equals_len_piles(self):
        piles = [3, 6, 7, 11]
        h = 4
        self.assertEqual(self.solution.koko_eating_bananas(piles, h), 11)

    def test_large_h(self):
        piles = [3, 6, 7, 11]
        h = 1000000000
        self.assertEqual(self.solution.koko_eating_bananas(piles, h), 1)

    def test_all_ones(self):
        piles = [1, 1, 1, 1]
        h = 4
        self.assertEqual(self.solution.koko_eating_bananas(piles, h), 1)

if __name__ == '__main__':
    unittest.main()
