class Solution:
    def longest_repeating_character_replacement(self, s: str, k: int) -> int:
        m = {}
        l = 0
        max_freq = 0
        result = 0

        for r, char in enumerate(s):
            m[char] = m.get(char, 0) + 1
            max_freq = max(max_freq, m[char])
            while r - l + 1 - max_freq > k:
                m[s[l]] -= 1
                l += 1
            result = max(result, r - l + 1)

        return result
