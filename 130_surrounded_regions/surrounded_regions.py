class Solution:
    def surrounded_regions(self, board: list[list[str]]):
        rows, cols = len(board), len(board[0])
        border_cells = (
            [(r, 0) for r in range(rows)]
            + [(r, cols - 1) for r in range(rows)]
            + [(0, c) for c in range(cols)]
            + [(rows - 1, c) for c in range(cols)]
        )

        stack = []
        for r, c in border_cells:
            if board[r][c] == "O":
                board[r][c] = "S"
                stack.append((r, c))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while stack:
            p_r, p_c = stack.pop()
            for x, y in directions:
                n_r, n_c = p_r + x, p_c + y
                if 0 <= n_r < rows and 0 <= n_c < cols and board[n_r][n_c] == "O":
                    board[n_r][n_c] = "S"
                    stack.append((n_r, n_c))

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"
