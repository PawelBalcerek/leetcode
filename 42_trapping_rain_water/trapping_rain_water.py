class Solution:
    def trapping_rain_water(self, h: list[int]) -> int:
        l, r = 0, len(h) - 1
        max_left, max_right = h[l], h[r]
        result = 0
        while l <= r:
            if max_left <= max_right:
                part_result = max_left - h[l]
                result += part_result if part_result > 0 else 0
                max_left = max(max_left, h[l])
                l += 1
            else:
                part_result = max_right - h[r]
                result += part_result if part_result > 0 else 0
                max_right = max(max_right, h[r])
                r -= 1
        return result
