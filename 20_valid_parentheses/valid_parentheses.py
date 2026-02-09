class Solution:
    CLOSED_TO_OPEN_PARENTHESE = {")": "(", "]": "[", "}": "{"}

    def valid_parentheses(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in self.CLOSED_TO_OPEN_PARENTHESE:
                if not stack or stack.pop() != self.CLOSED_TO_OPEN_PARENTHESE[char]:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0
