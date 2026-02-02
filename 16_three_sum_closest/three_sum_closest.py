class Solution:
    def three_sum_closest(self, nums: list[int], target: int) -> int:
        nums.sort()
        result_sum = (2**32) - 1
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                current_sum = nums[i] + nums[l] + nums[r]
                if current_sum == target:
                    return current_sum
                elif current_sum > target:
                    r -= 1
                else:
                    l += 1
                if abs(target - current_sum) < abs(target - result_sum):
                    result_sum = current_sum
        return result_sum
