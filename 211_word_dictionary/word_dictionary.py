from typing import Optional

EOW_CHAR = "\0"


class Solution:
    def __init__(self) -> None:
        self.trie = {}

    def add(self, word: str) -> None:
        current = self.trie
        for char in word:
            if char not in current:
                current[char] = {}
            current = current[char]
        current[EOW_CHAR] = None

    def search(self, word: str) -> bool:
        def backtracking(current: Optional[dict], i: int) -> bool:
            if not current:
                return False

            if i >= len(word):
                return EOW_CHAR in current

            if word[i] == ".":
                for char in current:
                    if char == EOW_CHAR:
                        continue
                    if backtracking(current[char], i + 1):
                        return True
                return False

            return word[i] in current and backtracking(current[word[i]], i + 1)

        return backtracking(self.trie, 0)
