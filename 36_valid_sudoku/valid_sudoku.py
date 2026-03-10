class Solution:
    def valid_sudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]
        for r, columns in enumerate(board):
            for c, value in enumerate(columns):
                if value == ".":
                    continue
                if (
                    value in rows[r]
                    or value in cols[c]
                    or value in boxes[r // 3][c // 3]
                ):
                    return False
                rows[r].add(value)
                cols[c].add(value)
                boxes[r // 3][c // 3].add(value)
        return True

    def valid_sudoku_single_set(self, board: list[list[str]]) -> bool:
        s = set()
        for r, columns in enumerate(board):
            for c, value in enumerate(columns):
                if value == ".":
                    continue

                row_id = ("row", r, value)
                col_id = ("col", c, value)
                box_id = ("box", r // 3, c // 3, value)

                if row_id in s or col_id in s or box_id in s:
                    return False

                s.update((row_id, col_id, box_id))

        return True
