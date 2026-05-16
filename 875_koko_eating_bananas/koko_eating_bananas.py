import math 

class Solution:
    def koko_eating_bananas(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)
        result = r

        while l <= r:
            m = (l + r) // 2
            eating_hours = 0
            for bananas in piles:
                eating_hours += math.ceil(bananas / m)
            if eating_hours <= h:
                result = min(result, m)
                r = m - 1
            else:
                l = m + 1

        return result
