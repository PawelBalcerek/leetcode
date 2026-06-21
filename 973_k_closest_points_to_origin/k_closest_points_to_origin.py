from heapq import heapify, heappop
from math import sqrt


class Solution:
    def k_closest_points_to_origin(
        self, points: list[list[int]], k: int
    ) -> list[list[int]]:
        heap = []
        for x, y in points:
            d = sqrt((x - 0) ** 2 + (y - 0) ** 2)
            heap.append([d, x, y])
        heapify(heap)
        result = []
        while k:
            _, x, y = heappop(heap)
            result.append([x, y])
            k -= 1
        return result
