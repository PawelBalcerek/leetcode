import heapq

class Solution:
    def kth_largest_element_in_an_array(self, nums: list[int], k: int) -> int:
        heapq.heapify_max(nums)
        for _ in range(k - 1):
            heapq.heappop_max(nums)
        return nums[0]

