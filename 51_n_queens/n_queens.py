class Solution:
    def n_queens(self, n: int) -> list[list[str]]:
        columns = set()
        positive_diagonals = set()  # (r + c)
        negative_diagonals = set()  # (r - c)
        result = []
        board = [["."] * n for _ in range(n)]

        def backtracking(r: int):
            if r == n:
                result.append(["".join(row) for row in board])
                return

            for c in range(n):
                if (
                    c in columns
                    or (r + c) in positive_diagonals
                    or (r - c) in negative_diagonals
                ):
                    continue

                columns.add(c)
                positive_diagonals.add(r + c)
                negative_diagonals.add(r - c)
                board[r][c] = "Q"

                backtracking(r + 1)

                board[r][c] = "."
                negative_diagonals.remove(r - c)
                positive_diagonals.remove(r + c)
                columns.remove(c)

        backtracking(0)

        return result
