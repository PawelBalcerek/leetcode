class Solution:
    ARABIC_TO_ROMAN = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }

    def integer_to_roman(self, num: int) -> str:
        result = ""
        for arabic in self.ARABIC_TO_ROMAN:
            while num >= arabic:
                num -= arabic
                result += self.ARABIC_TO_ROMAN[arabic]
        return result
