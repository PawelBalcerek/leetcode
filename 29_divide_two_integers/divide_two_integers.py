class Solution:
    MAX_INT = 2**31 - 1
    MIN_INT = -(2**31)

    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 1:
            return dividend

        if divisor == -1:
            return self.MAX_INT if dividend == self.MIN_INT else -dividend

        is_negative = (dividend < 0) ^ (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0

        while dividend >= divisor:
            shifted_divisor = divisor
            multiplier = 1

            while dividend >= (shifted_divisor << 1):
                shifted_divisor <<= 1
                multiplier <<= 1

            dividend -= shifted_divisor

            if is_negative and result > self.MAX_INT + 1 - multiplier:
                return self.MIN_INT
            elif result > self.MAX_INT - multiplier:
                return self.MAX_INT

            result += multiplier

        return -result if is_negative else result
