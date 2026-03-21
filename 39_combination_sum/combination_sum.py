class Solution:
    def combination_sum(self, candidates: list[int], target: int) -> list[list[int]]:
        if target == 1:
            return []

        results, possible_result = [], []

        def backtracking(i: int, current_target: int):
            if current_target == 0:
                results.append(possible_result[:])
                return

            if current_target < 0:
                return

            for j in range(i, len(candidates)):
                candidate = candidates[j]
                possible_result.append(candidate)
                backtracking(j, current_target - candidate)
                possible_result.pop()

        backtracking(0, target)

        return results
