class Solution:
    def subset_ii(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        results, result = [], []

        def backtracking(i: int):
            if i >= len(nums):
                results.append(result[:])
                return

            result.append(nums[i])
            backtracking(i + 1)
            result.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            backtracking(i + 1)

        backtracking(0)

        return results
