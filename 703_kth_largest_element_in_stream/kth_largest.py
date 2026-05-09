import heapq

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.min_heap = list(nums)
        self.k = k
        heapq.heapify(self.min_heap)
        self.__heappop()

    def add(self, val: int):
        heapq.heappush(self.min_heap, val)
        self.__heappop()
        return self.min_heap[0]

    def __heappop(self):
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

