class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def insert(self, word):
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_word = True


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        result = []
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        rows, cols = len(board), len(board[0])

        def backtracking(r: int, c: int, parent: TrieNode, word: str):
            char = board[r][c]
            board[r][c] = "#"

            child = parent.children[char]
            word += char
            if child.is_word:
                result.append(word)
                child.is_word = False

            for x, y in directions:
                n_r, n_c = r + x, c + y
                if (
                    n_r in range(rows)
                    and n_c in range(cols)
                    and board[n_r][n_c] in child.children
                ):
                    backtracking(n_r, n_c, child, word)

            board[r][c] = char

            if not child.children:
                del parent.children[char]

        root = TrieNode()
        for word in words:
            root.insert(word)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    backtracking(r, c, root, "")

        return result
