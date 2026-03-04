class Solution:
    def search_in_rotated_sorted_array(self, a: list[int], target: int) -> int:
        l, r = 0, len(a) - 1
        while l <= r:
            m = (l + r) // 2
            if a[m] == target:
                return m
            elif a[0] <= a[m]:
                if target < a[m] and target >= a[l]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if target > a[m] and target <= a[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1
