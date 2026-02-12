class Solution:
    def container_with_most_water(self, heights: list[int]) -> int:
        l, r = 0, len(heights) - 1
        result = 0
        while l < r:
            current_area = (r - l) * min(heights[l], heights[r])
            if current_area > result:
                result = current_area
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return result
