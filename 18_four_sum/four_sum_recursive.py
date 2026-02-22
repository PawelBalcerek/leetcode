class Solution:
    def four_sum_recursive(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        results, possible_result = [], []

        def k_sum(i: int, k: int, curr_target: int):
            if k > 2:
                for j in range(i, len(nums) - k + 1):
                    if j > i and nums[j] == nums[j - 1]:
                        continue
                    possible_result.append(nums[j])
                    k_sum(j + 1, k - 1, curr_target - nums[j])
                    possible_result.pop()
                return

            l, r = i, len(nums) - 1

            while l < r:
                curr_sum = nums[l] + nums[r]
                if curr_sum == curr_target:
                    results.append(possible_result + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif curr_sum < curr_target:
                    l += 1
                else:
                    r -= 1

        k_sum(0, 4, target)

        return results
