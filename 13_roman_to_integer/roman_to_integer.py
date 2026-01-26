class Solution:
    ROMAN_TO_ARABIC = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1,
    }

    def romanToInt(self, s: str) -> int:
        result = 0
        i = 0
        while i < len(s):
            curr, next = s[i], s[i + 1] if i + 1 < len(s) else ""
            if curr + next in self.ROMAN_TO_ARABIC:
                result += self.ROMAN_TO_ARABIC[curr + next]
                i += 2
            else:
                result += self.ROMAN_TO_ARABIC[curr]
                i += 1
        return result
