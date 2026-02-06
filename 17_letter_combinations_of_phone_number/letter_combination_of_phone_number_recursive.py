class Solution:
    LETTERS = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def letter_combinations_of_phone_number_recursive(self, digits: str) -> list[str]:
        if len(digits) == 0:
            return []

        results = []

        def backtrack(i, result):
            if len(result) == len(digits):
                results.append(result)
                return
            for c in self.LETTERS[digits[i]]:
                backtrack(i + 1, result + c)

        backtrack(0, "")

        return results
