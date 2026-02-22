class Solution:
    def max_heapify(self, a: list[int], n: int, i: int):
        l = 2 * i + 1
        r = 2 * i + 2
        largest = i
        if l < n and a[l] > a[i]:
            largest = l
        if r < n and a[r] > a[largest]:
            largest = r
        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            self.max_heapify(a, n, largest)

    def build_max_heap(self, a: list[int], n: int):
        for i in range(n // 2 - 1, -1, -1):
            self.max_heapify(a, n, i)

    def heap_sort(self, a: list[int]):
        n = len(a)
        self.build_max_heap(a, n)
        for i in range(n - 1, 0, -1):
            a[0], a[i] = a[i], a[0]
            n -= 1
            self.max_heapify(a, n, 0)
        return a
