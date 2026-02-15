class Solution:
    def merge_sort(self, arr, l, r):
        if l >= r:
            return arr
        m = (l + r) // 2
        self.merge_sort(arr, l, m)
        self.merge_sort(arr, m + 1, r)
        self.merge(arr, l, m, r)
        return arr

    def merge(self, arr, l, m, r):
        left_part, right_part = arr[l : m + 1], arr[m + 1 : r + 1]

        i, j, k = l, 0, 0

        while j < len(left_part) and k < len(right_part):
            if left_part[j] <= right_part[k]:
                arr[i] = left_part[j]
                j += 1
            else:
                arr[i] = right_part[k]
                k += 1
            i += 1

        while j < len(left_part):
            arr[i] = left_part[j]
            j += 1
            i += 1

        while k < len(right_part):
            arr[i] = right_part[k]
            k += 1
            i += 1
