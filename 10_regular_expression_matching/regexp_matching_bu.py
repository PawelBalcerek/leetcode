class Solution:
    def regexp_matching_bu(self, s: str, p: str) -> bool:
        a = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        a[len(s)][len(p)] = True
        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                matches = i < len(s) and (s[i] == p[j] or p[j] == ".")
                if j + 1 < len(p) and p[j + 1] == "*":
                    a[i][j] = (matches and a[i + 1][j]) or a[i][j + 2]
                else:
                    a[i][j] = matches and a[i + 1][j + 1]
        return a[0][0]
