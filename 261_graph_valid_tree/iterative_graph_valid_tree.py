class Solution:
    def graph_valid_tree(self, n: int, edges: list[list[int]]) -> bool:
        if n != len(edges) + 1:
            return False

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = {0}
        stack = [0]
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if v not in visited:
                    stack.append(v)
                    visited.add(v)

        return len(visited) == n
