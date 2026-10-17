class Solution:
    def course_schedule(self, num_courses: int, prerequisites: list[list[int]]) -> bool:
        adj = [[] for _ in range(num_courses)]
        for c, p in prerequisites:
            adj[c].append(p)
        state = [0] * num_courses

        def dfs(c: int) -> bool:
            if state[c] == 1:
                return False
            if state[c] == 2:
                return True
            state[c] = 1
            if all(dfs(p) for p in adj[c]):
                state[c] = 2
                return True
            return False

        return all(dfs(c) for c in range(num_courses))
