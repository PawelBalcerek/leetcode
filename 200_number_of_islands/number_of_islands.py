from collections import deque


class Solution:
    def num_of_islands(self, grid: list[list[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        result = 0

        def bfs(r, c):
            queue = deque([(r, c)])
            visited.add((r, c))
            while queue:
                c_r, c_c = queue.popleft()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for x, y in directions:
                    n_r, n_c = c_r + x, c_c + y
                    if (
                        n_r in range(rows)
                        and n_c in range(cols)
                        and (n_r, n_c) not in visited
                        and grid[n_r][n_c] == "1"
                    ):
                        queue.append((n_r, n_c))
                        visited.add((n_r, n_c))

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == "1":
                    bfs(r, c)
                    result += 1

        return result
