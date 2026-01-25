class Solution:
    def findMedianSortedArrays(self, a: list[int], b: list[int]) -> float:
        if len(a) > len(b):
            return self.findMedianSortedArrays(b, a)
        size = len(a) + len(b)
        half_size = size // 2
        l, r = 0, len(a) - 1
        while True:
            mid_a = (l + r) // 2
            mid_b = half_size - mid_a - 2
            left_max_a = a[mid_a] if mid_a >= 0 else float("-inf")
            left_max_b = b[mid_b] if mid_b >= 0 else float("-inf")
            right_min_a = a[mid_a + 1] if mid_a + 1 < len(a) else float("inf")
            right_min_b = b[mid_b + 1] if mid_b + 1 < len(b) else float("inf")
            if left_max_a <= right_min_b and left_max_b <= right_min_a:
                if size % 2:
                    return min(right_min_a, right_min_b)
                else:
                    return (
                        max(left_max_a, left_max_b) + min(right_min_a, right_min_b)
                    ) / 2
            elif left_max_a > right_min_b:
                r = mid_a - 1
            else:
                l = mid_a + 1
