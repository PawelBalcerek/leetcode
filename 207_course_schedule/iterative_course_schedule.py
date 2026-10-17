class Solution:
    def course_schedule(self, num_courses: int, prerequisites: list[list[int]]) -> bool:
        adj = [[] for _ in range(num_courses)]
        in_degrees = [0] * num_courses
        for c, p in prerequisites:
            adj[p].append(c)
            in_degrees[c] += 1

        s = [c for c in range(num_courses) if in_degrees[c] == 0]
        completed = 0
        while s:
            c = s.pop()
            completed += 1
            for n_c in adj[c]:
                in_degrees[n_c] -= 1
                if in_degrees[n_c] == 0:
                    s.append(n_c)

        return completed == num_courses
