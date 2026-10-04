class Solution:
    def pacific_atlantic_water_flow(self, heights: list[list[int]]) -> list[list[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r: int, c: int, visited: set[tuple[int, int]]):
            stack = [(r, c)]
            visited.add((r, c))
            while stack:
                p_r, p_c = stack.pop()
                for x, y in directions:
                    n_r, n_c = p_r + x, p_c + y
                    if (
                        0 <= n_r < rows
                        and 0 <= n_c < cols
                        and (n_r, n_c) not in visited
                        and heights[p_r][p_c] <= heights[n_r][n_c]
                    ):
                        stack.append((n_r, n_c))
                        visited.add((n_r, n_c))

        pacific = set()
        atlantic = set()
        for r in range(rows):
            dfs(r, 0, pacific)
            dfs(r, cols - 1, atlantic)

        for c in range(cols):
            dfs(0, c, pacific)
            dfs(rows - 1, c, atlantic)

        return [[r, c] for r, c in pacific & atlantic]
