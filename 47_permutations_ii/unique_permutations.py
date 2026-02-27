class Solution:
    def unique_permutations(self, nums: list[int]) -> list[list[int]]:
        results = []
        perm = []
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        def dfs():
            if len(perm) == len(nums):
                results.append(perm[:])
                return

            for num in counter:
                if counter[num] > 0:
                    perm.append(num)
                    counter[num] -= 1
                    dfs()
                    counter[num] += 1
                    perm.pop()

        dfs()
        return results
