class Solution:
    def next_permutation(self, nums: list[int]):
        p = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                p = i
                break

        if p == -1:
            self.reverse(nums, 0)
            return

        s = -1
        for i in range(len(nums) - 1, p, -1):
            if nums[i] > nums[p]:
                s = i
                break

        nums[p], nums[s] = nums[s], nums[p]

        self.reverse(nums, p + 1)

    def reverse(self, nums: list[int], l: int):
        r = len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
