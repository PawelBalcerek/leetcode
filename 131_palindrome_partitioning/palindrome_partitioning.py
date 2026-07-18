class Solution:
    def palindrome_partitioning(self, s: str) -> list[list[str]]:
        results, result = [], []

        def dfs(i: int):
            if i >= len(s):
                results.append(result[:])
                return

            for j in range(i, len(s)):
                if self.is_palindrome(s, i, j):
                    result.append(s[i : j + 1])
                    dfs(j + 1)
                    result.pop()

        dfs(0)
        return results

    def is_palindrome(self, s: str, l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
