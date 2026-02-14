class Solution:
    def generate_parentheses_bfs(self, n: int) -> list[str]:
        if n == 0:
            return []

        curr_level = [("(", 1, 0)]

        for _ in range(2 * n - 1):
            next_level = []
            for s, o_n, c_n in curr_level:
                if o_n < n:
                    next_level.append((s + "(", o_n + 1, c_n))

                if c_n < o_n:
                    next_level.append((s + ")", o_n, c_n + 1))
            curr_level = next_level

        return [state[0] for state in curr_level]
