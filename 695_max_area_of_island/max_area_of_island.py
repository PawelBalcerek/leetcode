class Solution:
    def max_area_of_island(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        result = 0

        def dfs(r, c):
            if (
                r not in range(rows)
                or c not in range(cols)
                or grid[r][c] == 0
                or (r, c) in visited
            ):
                return 0

            visited.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == 1:
                    result = max(result, dfs(r, c))

        return result
