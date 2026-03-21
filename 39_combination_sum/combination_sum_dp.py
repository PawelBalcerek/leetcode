class Solution:
    def combination_sum_dp(self, candidates: list[int], target: int) -> list[int]:
        dp = [[] for _ in range(0, target + 1)]
        dp[0] = [[]]

        for c in candidates:
            for i in range(c, target + 1):
                for combination in dp[i - c]:
                    dp[i].append(combination + [c])

        return dp[target]

