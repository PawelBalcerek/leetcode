from typing import DefaultDict


class Solution:
    def group_anagrams(self, strs: list[str]) -> list[list[str]]:
        res = DefaultDict(list)
        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord("a")] += 1
            res[tuple(count)].append(string)
        return [v for _, v in res.items()]
