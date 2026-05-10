class Solution:
    def reverse_bits(self, n: int) -> int:
        result = 0
        for i in range(31, -1, -1):
            result += (1 << i) if n & 1 else 0
            n >>= 1
        return result
