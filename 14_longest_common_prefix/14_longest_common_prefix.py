class Solution:
    def longest_common_prefix(self, strs: list[str]) -> str:
        result = ""
        for i in range(len(strs[0])):
            for string in strs:
                if i >= len(string) or string[i] != strs[0][i]:
                    return result
            result += strs[0][i]
        return result
