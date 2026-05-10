class Solution:
    def happy_number(self, n: int) -> bool:
        s = {n}
        while n != 1:
            output = 0
            while n > 0:
                output += (n % 10) ** 2
                n //= 10
            n = output

            if n in s:
                return False

            s.add(n)
        return True
