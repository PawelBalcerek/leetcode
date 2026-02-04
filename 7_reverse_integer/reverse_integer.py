class Solution:
    def reverse_integer(self, x: int) -> int:
        result = 0
        sign = [-1, 1][x > 0]
        limit, limit_r = divmod([2**31, 2**31 - 1][x > 0], 10)
        x = abs(x)
        while x > 0:
            x, x_r = divmod(x, 10)
            if result > limit or (result == limit and x_r > limit_r):
                return 0
            result *= 10
            result += x_r
        return sign * result
