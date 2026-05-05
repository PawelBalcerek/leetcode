class Solution:
    def largest_rectangle_in_histogram(self, heights: list[int]) -> int:
        s = []
        result = 0

        for r, h in enumerate(heights):
            l = r
            while s and s[-1][1] > h:
                s_l, s_h = s.pop()
                result = max(result, (r - s_l) * s_h)
                l = s_l
            s.append((l, h))

        for s_l, s_h in s:
            result = max(result, (len(heights) - s_l) * s_h)

        return result
