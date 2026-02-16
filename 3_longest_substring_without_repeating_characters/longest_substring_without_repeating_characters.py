class Solution:
    def longest_substring_without_repeating_characters(self, s: str) -> int:
        longest = 0
        l = 0
        m = {}
        for r, char in enumerate(s):
            if char in m and l < m[char] + 1:
                l = m[char] + 1

            if (r - l + 1) > longest:
                longest = r - l + 1

            m[char] = r
        return longest
