from functools import cache


class Solution:
    def regexp_matching_td(self, s: str, p: str) -> bool:
        @cache
        def dfs(i: int, j: int) -> bool:
            if j >= len(p):
                return i >= len(s)
            matches = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if j + 1 < len(p) and p[j + 1] == "*":
                return (matches and dfs(i + 1, j)) or dfs(i, j + 2)
            if matches:
                return dfs(i + 1, j + 1)
            return False

        return dfs(0, 0)
