class Solution:
    def find_minimum_in_rotated_sorted_array(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        result = nums[0]
        while l <= r:
            m = (l + r) // 2
            if nums[l] <= nums[m]:
                result = min(result, nums[l])
                l = m + 1
            else:
                result = min(result, nums[m])
                r = m - 1
        return result
