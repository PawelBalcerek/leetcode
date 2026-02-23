class Solution:
    def find_needle_in_the_haystack(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                l, r = 0, len(needle) - 1
                while l <= r:
                    if haystack[i + l] != needle[l] or haystack[i + r] != needle[r]:
                        break
                    l += 1
                    r -= 1
                if l > r:
                    return i
        return -1
