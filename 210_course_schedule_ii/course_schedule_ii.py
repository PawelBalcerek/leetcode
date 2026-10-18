class Solution:
    def course_schedule_ii(
        self, num_courses: int, prerequisites: list[list[int]]
    ) -> list[int]:
        adj = [[] for _ in range(num_courses)]
        in_degrees = [0] * num_courses
        for c, p in prerequisites:
            adj[p].append(c)
            in_degrees[c] += 1

        s = [c for c in range(num_courses) if in_degrees[c] == 0]
        completed = []
        while s:
            c = s.pop()
            completed.append(c)
            for n_c in adj[c]:
                in_degrees[n_c] -= 1
                if in_degrees[n_c] == 0:
                    s.append(n_c)

        return completed if len(completed) == num_courses else []
