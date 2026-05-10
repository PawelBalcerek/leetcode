class Solution:
    def missing_number(self, nums: list[int]) -> int:
        result = len(nums)
        for i, num in enumerate(nums):
            result ^= i ^ num
        return result
