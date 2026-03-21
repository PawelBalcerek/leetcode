class Solution:
    def combination_sum(self, candidates: list[int], target: int) -> list[list[int]]:
        if target == 1:
            return []

        results, possible_result = [], []

        def backtracking(i: int, current_target: int):
            if current_target == 0:
                results.append(possible_result[:])
                return

            if current_target < 0 or i >= len(candidates):
                return

            candidate = candidates[i]
            possible_result.append(candidate)
            backtracking(i, current_target - candidate)
            possible_result.pop()
            backtracking(i + 1, current_target)

        backtracking(0, target)

        return results
