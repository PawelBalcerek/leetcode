class Solution:
    def min_cost_climbing_stairs(self, cost: list[int]) -> int:
        for i in range(len(cost) - 2, -1, -1):
            min_cost = min(cost[i + 1], cost[i + 2] if i + 2 < len(cost) else 0)
            cost[i] += min_cost
        return min(cost[0], cost[1])
