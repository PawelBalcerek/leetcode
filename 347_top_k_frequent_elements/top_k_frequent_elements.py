class Solution:
    def top_k_frequent_elements(self, nums: list[int], k: int) -> list[int]:
        n_count = {}
        for n in nums:
            n_count[n] = 1 + n_count.get(n, 0)

        freq = [[] for _ in range(len(nums) - k + 2)]
        for n, count in n_count.items():
            freq[count].append(n)

        result = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result
        return result
