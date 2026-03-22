class Solution:
    def combination_sum_ii(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        results, result = [], []

        def backtracking(i: int, current_target: int):
            if current_target == 0:
                results.append(result[:])
                return

            if current_target < 0:
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j - 1] == candidates[j]:
                    continue
                candidate = candidates[j]
                result.append(candidate)
                backtracking(j + 1, current_target - candidate)
                result.pop()

        backtracking(0, target)

        return results
