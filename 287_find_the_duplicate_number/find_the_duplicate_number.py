class Solution:
    def find_the_duplicate_number(self, nums: list[int]) -> int:
        s = f = 0
        while True:
            s = nums[s]
            f = nums[nums[f]]
            if s == f:
                break

        s2 = 0
        while True:
            s = nums[s]
            s2 = nums[s2]
            if s == s2:
                return s

