from functools import cache

class Solution:
    @cache
    def climbing_stairs(self, n: int) -> int:
        if n < 0:
            return 0
        if n == 0:
            return 1
        return self.climbing_stairs(n - 1) + self.climbing_stairs(n - 2)

