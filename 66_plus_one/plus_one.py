class Solution:
    def plus_one(self, digits: list[int]) -> list[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            carry, digits[i] = divmod(digits[i] + carry, 10)
        if carry == 1:
            digits.insert(0, carry)
        return digits
