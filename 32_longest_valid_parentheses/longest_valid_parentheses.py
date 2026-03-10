class Solution:
    def longest_valid_parentheses(self, s: str) -> int:
        stack = [-1]
        result = 0

        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            else:
                stack.pop()

                if not stack:
                    stack.append(i)
                else:
                    result = max(result, i - stack[-1])

        return result
