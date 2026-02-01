class Solution:
    def two_sum_binary_search(self, numbers: list[int], target: int) -> list[int]:
        i = 0

        def binary_search(l: int, real_target: int) -> int:
            r = len(numbers) - 1
            while l <= r:
                mid = (l + r) // 2
                if numbers[mid] == real_target:
                    return mid
                elif numbers[mid] > real_target:
                    r = mid - 1
                else:
                    l = mid + 1
            return i

        while i < len(numbers):
            number = numbers[i]
            real_target = target - number
            seeked = binary_search(i + 1, real_target)
            if i != seeked:
                return [i + 1, seeked + 1]
            i += 1

        return []
