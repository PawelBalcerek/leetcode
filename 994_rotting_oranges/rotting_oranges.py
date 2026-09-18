from collections import deque


class Solution:
    def rotting_oranges(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1

        minutes = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue and fresh > 0:
            for _ in range(len(queue)):
                popped_r, popped_c = queue.popleft()
                for x, y in directions:
                    n_r, n_c = popped_r + x, popped_c + y
                    if 0 <= n_r < rows and 0 <= n_c < cols and grid[n_r][n_c] == 1:
                        grid[n_r][n_c] = 2
                        fresh -= 1
                        queue.append((n_r, n_c))
            minutes += 1

        return minutes if fresh == 0 else -1
