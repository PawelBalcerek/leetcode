class Solution:
    def remove_duplicates_from_sorted_array(self, nums: list[int]) -> int:
        if not nums:
            return 0
        l, r = 0, 1
        while r < len(nums):
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]
            r += 1
        return l + 1
