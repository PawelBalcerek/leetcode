class Solution:
    def two_sum_pointers(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            current_result = numbers[l] + numbers[r]
            if current_result == target:
                return [l + 1, r + 1]
            elif current_result > target:
                r -= 1
            else:
                l += 1
        return []
