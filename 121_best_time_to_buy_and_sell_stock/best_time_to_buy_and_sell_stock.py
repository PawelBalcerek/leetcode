class Solution:
    def best_time_to_buy_and_sell_stock(self, prices: list[int]) -> int:
        result = 0
        b = 0
        for s in range(1, len(prices)):
            if prices[s] < prices[b]:
                b = s
                continue
            result = max(result, prices[s] - prices[b])
        return result
