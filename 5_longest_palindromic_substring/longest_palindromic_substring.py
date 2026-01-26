class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = s[0]
        for i, char in enumerate(s):
            l, r = i - 1, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(longest):
                    longest = s[l : r + 1]
                l -= 1
                r += 1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(longest):
                    longest = s[l : r + 1]
                l -= 1
                r += 1
        return longest
