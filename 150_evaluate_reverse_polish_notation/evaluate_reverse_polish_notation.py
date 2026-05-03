class Solution:
    def evaluate_reverse_polish_notation(self, tokens: list[str]) -> int:
        s = []
        for t in tokens:
            if t == "+":
                s.append(s.pop() + s.pop())
            elif t == "-":
                second, first = s.pop(), s.pop()
                s.append(first - second)
            elif t == "*":
                s.append(s.pop() * s.pop())
            elif t == "/":
                second, first = s.pop(), s.pop()
                s.append(int(first / second))
            else:
                s.append(int(t))
        return s.pop()
