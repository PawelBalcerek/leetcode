class Solution:
    def three_sum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                current_sum = num + nums[l] + nums[r]
                if current_sum > 0:
                    r -= 1
                elif current_sum < 0:
                    l += 1
                else:
                    result.append([num, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return result
