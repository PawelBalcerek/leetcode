import heapq

class Solution:
    def last_stone_weight(self, stones: list[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            s1, s2 = heapq.heappop_max(stones), heapq.heappop_max(stones) if stones else 0
            if s1 != s2:
                heapq.heappush_max(stones, s1 - s2)
        return stones[0] if stones else 0
