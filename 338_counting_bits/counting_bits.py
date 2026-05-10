class Solution:
    def counting_bits(self, n: int) -> list[int]:
        result = [0]
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset *= 2
            result.append(1 + result[i - offset])
        return result
