class Solution:
    def range_binary_search(self, nums: list[int], target: int) -> list[int]:
        def biased_binary_search(left_biased: bool) -> int:
            l, r = 0, len(nums) - 1
            result = -1
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    result = m
                    if left_biased:
                        r = m - 1
                    else:
                        l = m + 1
                elif nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            return result

        return [biased_binary_search(True), biased_binary_search(False)]
