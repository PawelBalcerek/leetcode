class Solution:
    def generate_parentheses_dfs(self, n: int) -> list[str]:
        stack = []
        result = []

        def dfs(o_n: int, c_n: int):
            if o_n == c_n == n:
                result.append("".join(stack))

            if o_n < n:
                stack.append("(")  # make a choice
                dfs(o_n + 1, c_n)  # explore (go deeper)
                stack.pop()  # undo the choice (backtrack)

            if c_n < o_n:
                stack.append(")")  # make a choice
                dfs(o_n, c_n + 1)  # explore (go deeper)
                stack.pop()  # undo the choice (backtrack)

        dfs(0, 0)

        return result
