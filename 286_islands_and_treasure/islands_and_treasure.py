from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        rows, cols = len(grid), len(grid[0])

        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        level = 1
        while queue:
            for _ in range(len(queue)):
                popped_r, popped_c = queue.popleft()
                for x, y in directions:
                    n_r, n_c = popped_r + x, popped_c + y
                    if 0 <= n_r < rows and 0 <= n_c < cols and level < grid[n_r][n_c]:
                        grid[n_r][n_c] = level
                        queue.append((n_r, n_c))
            level += 1
