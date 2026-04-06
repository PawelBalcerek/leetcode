class Solution:
    def longest_consecutive_sequence(self, nums: list[int]) -> int:
        s = set(nums)
        result = 0
        for num in s:
            if num - 1 not in s:
                d = 0
                while num + d in s:
                    d += 1
                result = max(d, result)
        return result
