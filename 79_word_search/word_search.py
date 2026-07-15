class Solution:
    def word_search(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()

        def backtracking(i: int, r: int, c: int) -> bool:
            if i >= len(word):
                return True

            if (
                r not in range(rows)
                or c not in range(cols)
                or (r, c) in path
                or board[r][c] != word[i]
            ):
                return False

            path.add((r, c))
            result = (
                backtracking(i + 1, r + 1, c)
                or backtracking(i + 1, r - 1, c)
                or backtracking(i + 1, r, c + 1)
                or backtracking(i + 1, r, c - 1)
            )
            path.remove((r, c))

            return result

        for r in range(rows):
            for c in range(cols):
                if backtracking(0, r, c):
                    return True

        return False
