import unittest
from best_time_to_buy_and_sell_stock import Solution

class TestBestTimeToBuyAndSellStock(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        prices = [7, 1, 5, 3, 6, 4]
        self.assertEqual(self.solution.best_time_to_buy_and_sell_stock(prices), 5)

    def test_example_2(self):
        prices = [7, 6, 4, 3, 1]
        self.assertEqual(self.solution.best_time_to_buy_and_sell_stock(prices), 0)

    def test_single_element(self):
        prices = [1]
        self.assertEqual(self.solution.best_time_to_buy_and_sell_stock(prices), 0)

    def test_increasing_prices(self):
        prices = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.best_time_to_buy_and_sell_stock(prices), 4)

    def test_decreasing_prices(self):
        prices = [5, 4, 3, 2, 1]
        self.assertEqual(self.solution.best_time_to_buy_and_sell_stock(prices), 0)

    def test_same_prices(self):
        prices = [3, 3, 3, 3]
        self.assertEqual(self.solution.best_time_to_buy_and_sell_stock(prices), 0)

    def test_large_profit_at_end(self):
        prices = [2, 4, 1, 7]
        self.assertEqual(self.solution.best_time_to_buy_and_sell_stock(prices), 6)

if __name__ == "__main__":
    unittest.main()
