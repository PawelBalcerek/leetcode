from collections import deque


class Solution:
    def sliding_window_maximum(self, nums: list[int], k: int) -> list[int]:
        deq = deque()
        res = []
        l = r = 0
        while r < len(nums):
            while deq and nums[deq[-1]] < nums[r]:
                deq.pop()
            deq.append(r)
            if l > deq[0]:
                deq.popleft()
            r += 1
            if r >= k:
                res.append(nums[deq[0]])
                l += 1
        return res
