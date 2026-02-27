class Solution:
    def permutations_recursive(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 0:
            return [[]]

        perms = self.permutations_recursive(nums[1:])
        result = []

        for perm in perms:
            for i in range(len(perm) + 1):
                perm_copy = perm[:]
                perm_copy.insert(i, nums[0])
                result.append(perm_copy)

        return result

    def permutations_iterative(self, nums: list[int]) -> list[list[int]]:
        results = [[]]

        for num in nums:
            new_results = []
            for result in results:
                for i in range(len(result) + 1):
                    result_copy = result[:]
                    result_copy.insert(i, num)
                    new_results.append(result_copy)
            results = new_results

        return results

    def permutations_backtracking(self, nums: list[int]) -> list[list[int]]:
        results = []

        if len(nums) <= 1:
            return [nums[:]]

        for _ in range(len(nums)):
            num = nums.pop(0)
            perms = self.permutations_backtracking(nums)
            for perm in perms:
                perm.append(num)
                results.append(perm)
            nums.append(num)

        return results

        return results
