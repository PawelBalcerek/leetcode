class Solution:
    def count_and_say_iterative(self, n: int) -> str:
        result = "1"
        for _ in range(n - 1):
            new_result = []
            count = 1

            for i in range(1, len(result)):
                if result[i - 1] == result[i]:
                    count += 1
                else:
                    new_result.extend([str(count), result[i - 1]])
                    count = 1
            new_result.extend([str(count), result[-1]])
            result = "".join(new_result)
        return result

    def count_and_say_recursive(self, n: int) -> str:
        if n == 1:
            return "1"

        prev_result = self.count_and_say_recursive(n - 1)

        new_result = []
        count = 1

        for i in range(1, len(prev_result)):
            if prev_result[i - 1] == prev_result[i]:
                count += 1
            else:
                new_result.extend([str(count), prev_result[i - 1]])
                count = 1

        new_result.extend([str(count), prev_result[-1]])

        return "".join(new_result)
