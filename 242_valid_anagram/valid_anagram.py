class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        m = {}

        for i in range(len(s)):
            m[s[i]] = m[s[i]] + 1 if s[i] in m else 1
            m[t[i]] = m[t[i]] - 1 if t[i] in m else -1

        return all(v == 0 for _, v in m.items())
