class Solution:
    def daily_temperatures(self, temperatures: list[int]) -> list[int]:
        s = []
        result = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while s and temperatures[s[-1]] < t:
                index = s.pop()
                result[index] = i - index
            s.append(i)
        return result

