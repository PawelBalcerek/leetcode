class Solution:
    def four_sum_recursive(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        results, quad = [], []

        def k_sum(k: int, idx: int, actual_target: int):
            if k > 2:
                for i in range(idx, len(nums) - k + 1):
                    if i > idx and nums[i] == nums[i - 1]:
                        continue
                    quad.append(nums[i])
                    k_sum(k - 1, i + 1, actual_target - nums[i])
                    quad.pop()
                return
            l, r = idx, len(nums) - 1
            while l < r:
                curr_sum = nums[l] + nums[r]
                if curr_sum == actual_target:
                    results.append(quad + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif curr_sum < actual_target:
                    l += 1
                else:
                    r -= 1

        k_sum(4, 0, target)

        return results
