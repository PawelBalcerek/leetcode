class Solution:
    def zigzag_conversion(self, s: str, num_rows: int) -> str:
        if num_rows == 1 or num_rows >= len(s):
            return s
        result = [""] * num_rows
        current_row = 0
        step = 1
        for char in s:
            result[current_row] += char
            if current_row == num_rows - 1:
                step = -1
            elif current_row == 0:
                step = 1
            current_row += step
        return "".join(result)
