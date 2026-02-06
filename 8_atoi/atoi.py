class Solution:
    def atoi(self, s: str) -> int:
        s = s.lstrip()
        result = 0
        sign = 1
        limit = (2**31) // 10
        for i, char in enumerate(s):
            if i == 0 and char == "+":
                continue
            if i == 0 and char == "-":
                sign = -1
                continue
            if not char.isnumeric():
                break
            to_add = int(char)
            if result > limit or (result == limit and to_add >= [7, 8][sign < 0]):
                return sign * (limit * 10 + [7, 8][sign < 0])
            result *= 10
            result += to_add
        return sign * result
