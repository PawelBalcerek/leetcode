from heapq import heappop, heappop_max, heappush, heappush_max


class Solution:
    def __init__(self) -> None:
        self.left = []
        self.right = []

    def add(self, num: int) -> None:
        heappush_max(self.left, num)
        heappush(self.right, heappop_max(self.left))
        if len(self.left) < len(self.right):
            heappush_max(self.left, heappop(self.right))

    def median(self) -> float:
        if len(self.right) < len(self.left):
            return self.left[0]
        return (self.left[0] + self.right[0]) / 2
