class Solution:
    def graph_valid_tree(self, n: int, edges: list[list[int]]) -> bool:
        if n != len(edges) + 1:
            return False

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        def dfs(u: int):
            visited.add(u)
            for v in adj[u]:
                if v not in visited:
                    dfs(v)

        dfs(0)

        return len(visited) == n
