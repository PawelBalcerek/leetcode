class Solution:
    def permutation_in_string(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False

        s1_c = [0] * 26
        s2_c = [0] * 26

        for i in range(n):
            s1_c[ord(s1[i]) - ord('a')] += 1 
            s2_c[ord(s2[i]) - ord('a')] += 1 

        matches = 0
        for i in range(26):
            matches += 1 if s1_c[i] == s2_c[i] else 0

        for i in range(n, m):
            if matches == 26:
                return True

            r = ord(s2[i]) - ord('a')
            s2_c[r] += 1
            if s2_c[r] == s1_c[r]:
                matches += 1
            elif s2_c[r] == s1_c[r] + 1:
                matches -= 1

            l = ord(s2[i - n]) - ord('a')
            s2_c[l] -= 1
            if s2_c[l] == s1_c[l]:
                matches += 1
            elif s2_c[l] == s1_c[l] - 1:
                matches -= 1

        return matches == 26
