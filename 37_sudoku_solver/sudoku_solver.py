class Solution:
    def sudoku_solver(self, board: list[list[str]]) -> None:
        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        boxes = [[False] * 9 for _ in range(9)]
        to_solve = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    to_solve.append((r, c))
                else:
                    val = int(board[r][c]) - 1
                    rows[r][val] = True
                    cols[c][val] = True
                    boxes[(r // 3) * 3 + (c // 3)][val] = True

        def solve(i: int) -> bool:
            if i == len(to_solve):
                return True

            r, c = to_solve[i]
            box_idx = (r // 3) * 3 + (c // 3)

            for guess in range(9):
                if (
                    not rows[r][guess]
                    and not cols[c][guess]
                    and not boxes[box_idx][guess]
                ):
                    board[r][c] = str(guess + 1)
                    rows[r][guess] = True
                    cols[c][guess] = True
                    boxes[box_idx][guess] = True

                    if solve(i + 1):
                        return True

                    board[r][c] = "."
                    rows[r][guess] = False
                    cols[c][guess] = False
                    boxes[box_idx][guess] = False

            return False
        
        solve(0)

    def sudoku_solver_bitwise(self, board: list[list[str]]):
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        to_solve = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    to_solve.append((r, c))
                else:
                    val = int(board[r][c]) - 1
                    mask = 1 << val

                    rows[r] |= mask
                    cols[c] |= mask
                    boxes[(r // 3) * 3 + (c // 3)] |= mask

        def solve(i):
            if i == len(to_solve):
                return True

            r, c = to_solve[i]
            box_idx = (r // 3) * 3 + (c // 3)

            for val in range(9):
                mask = 1 << val

                if (
                    not (rows[r] & mask)
                    and not (cols[c] & mask)
                    and not (boxes[box_idx] & mask)
                ):
                    board[r][c] = str(val + 1)
                    rows[r] |= mask
                    cols[c] |= mask
                    boxes[box_idx] |= mask

                    if solve(i + 1):
                        return True

                    board[r][c] = "."
                    rows[r] &= ~mask
                    cols[c] &= ~mask
                    boxes[box_idx] &= ~mask

            return False

        solve(0)
