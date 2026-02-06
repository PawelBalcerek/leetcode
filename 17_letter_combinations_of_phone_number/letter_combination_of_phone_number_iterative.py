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

    def letter_combinations_of_phone_number_iterative(self, digits: str) -> list[str]:
        if not digits:
            return []
        results = [""]
        for digit in digits:
            new_results = []
            for combination in results:
                for letter in self.LETTERS[digit]:
                    new_results.append(combination + letter)
            results = new_results
        return results
