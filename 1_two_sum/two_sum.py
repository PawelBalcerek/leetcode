class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        m = {}
        for i, num in enumerate(nums):
            real_target = target - num
            if real_target in m:
                return [m[real_target], i]
            m[num] = i
        return []
