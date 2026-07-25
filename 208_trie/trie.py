EOF_CHAR = "\0"

class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        current = self.trie
        for char in word:
            if char not in current:
                current[char] = {}
            current = current[char]
        current[EOF_CHAR] = None

    def search(self, word: str) -> bool:
        current = self.trie
        for char in word:
            if char not in current:
                return False
            current = current[char]
        return EOF_CHAR in current

    def starts_with(self, prefix: str) -> bool:
        current = self.trie
        for char in prefix:
            if char not in current:
                return False
            current = current[char]
        return True

