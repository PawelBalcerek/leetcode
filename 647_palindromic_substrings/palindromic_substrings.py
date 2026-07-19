class Solution:
    def palindromic_substrings(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            result += self.count_palindromes(s, i, i)
            result += self.count_palindromes(s, i, i + 1)
        return result

    def count_palindromes(self, s: str, l: int, r: int) -> int:
        result = 0
        while 0 <= l and r < len(s) and s[l] == s[r]:
            result += 1
            l -= 1
            r += 1
        return result
