import unittest
from typing import Optional

from clone_graph import Node, Solution


def build_graph(adj_list: list[list[int]]) -> Optional[Node]:
    if not adj_list:
        return None
    nodes = {i + 1: Node(i + 1) for i in range(len(adj_list))}
    for i, neighbors in enumerate(adj_list):
        nodes[i + 1].neighbors = [nodes[n] for n in neighbors]
    return nodes[1]


def graph_to_adj_list(node: Optional[Node]) -> list[list[int]]:
    if node is None:
        return []
    visited = {}
    queue = [node]
    visited[node.val] = node
    while queue:
        curr = queue.pop(0)
        for n in curr.neighbors:
            if n.val not in visited:
                visited[n.val] = n
                queue.append(n)
    result = []
    for val in sorted(visited):
        result.append(sorted(n.val for n in visited[val].neighbors))
    return result


def collect_nodes(node: Optional[Node]) -> dict:
    if node is None:
        return {}
    visited = {}
    queue = [node]
    visited[node.val] = node
    while queue:
        curr = queue.pop(0)
        for n in curr.neighbors:
            if n.val not in visited:
                visited[n.val] = n
                queue.append(n)
    return visited


class TestCloneGraph(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_graph(self):
        result = self.solution.clone_graph(None)
        self.assertIsNone(result)

    def test_single_node_no_neighbors(self):
        node = Node(1)
        result = self.solution.clone_graph(node)
        self.assertIsNotNone(result)
        assert result is not None
        self.assertIsNot(result, node)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.neighbors, [])

    def test_four_nodes_cycle(self):
        adj_list = [[2, 4], [1, 3], [2, 4], [1, 3]]
        node = build_graph(adj_list)
        result = self.solution.clone_graph(node)
        self.assertEqual(graph_to_adj_list(result), [[2, 4], [1, 3], [2, 4], [1, 3]])

    def test_two_nodes_connected(self):
        adj_list = [[2], [1]]
        node = build_graph(adj_list)
        result = self.solution.clone_graph(node)
        self.assertEqual(graph_to_adj_list(result), [[2], [1]])

    def test_deep_copy_no_shared_references(self):
        adj_list = [[2, 4], [1, 3], [2, 4], [1, 3]]
        node = build_graph(adj_list)
        original_nodes = collect_nodes(node)
        result = self.solution.clone_graph(node)
        cloned_nodes = collect_nodes(result)
        self.assertEqual(len(original_nodes), len(cloned_nodes))
        for val in original_nodes:
            self.assertIn(val, cloned_nodes)
            self.assertIsNot(original_nodes[val], cloned_nodes[val])

    def test_cloned_values_match(self):
        adj_list = [[2, 4], [1, 3], [2, 4], [1, 3]]
        node = build_graph(adj_list)
        result = self.solution.clone_graph(node)
        original_nodes = collect_nodes(node)
        cloned_nodes = collect_nodes(result)
        for val in original_nodes:
            self.assertEqual(original_nodes[val].val, cloned_nodes[val].val)

    def test_cloned_neighbor_structure(self):
        adj_list = [[2, 4], [1, 3], [2, 4], [1, 3]]
        node = build_graph(adj_list)
        result = self.solution.clone_graph(node)
        original_nodes = collect_nodes(node)
        cloned_nodes = collect_nodes(result)
        for val in original_nodes:
            orig_neighbor_vals = sorted(n.val for n in original_nodes[val].neighbors)
            clone_neighbor_vals = sorted(n.val for n in cloned_nodes[val].neighbors)
            self.assertEqual(orig_neighbor_vals, clone_neighbor_vals)

    def test_cloned_neighbors_are_cloned_objects(self):
        adj_list = [[2, 3], [1, 3], [1, 2]]
        node = build_graph(adj_list)
        original_nodes = collect_nodes(node)
        result = self.solution.clone_graph(node)
        cloned_nodes = collect_nodes(result)
        for val in cloned_nodes:
            for neighbor in cloned_nodes[val].neighbors:
                self.assertNotIn(id(neighbor), {id(n) for n in original_nodes.values()})

    def test_triangle_graph(self):
        adj_list = [[2, 3], [1, 3], [1, 2]]
        node = build_graph(adj_list)
        result = self.solution.clone_graph(node)
        self.assertEqual(graph_to_adj_list(result), [[2, 3], [1, 3], [1, 2]])

    def test_star_graph(self):
        adj_list = [[2, 3, 4, 5], [1], [1], [1], [1]]
        node = build_graph(adj_list)
        result = self.solution.clone_graph(node)
        self.assertEqual(graph_to_adj_list(result), [[2, 3, 4, 5], [1], [1], [1], [1]])

    def test_linear_chain(self):
        adj_list = [[2], [1, 3], [2, 4], [3]]
        node = build_graph(adj_list)
        result = self.solution.clone_graph(node)
        self.assertEqual(graph_to_adj_list(result), [[2], [1, 3], [2, 4], [3]])

    def test_complete_graph_five_nodes(self):
        adj_list = [
            [2, 3, 4, 5],
            [1, 3, 4, 5],
            [1, 2, 4, 5],
            [1, 2, 3, 5],
            [1, 2, 3, 4],
        ]
        node = build_graph(adj_list)
        result = self.solution.clone_graph(node)
        self.assertEqual(
            graph_to_adj_list(result),
            [
                [2, 3, 4, 5],
                [1, 3, 4, 5],
                [1, 2, 4, 5],
                [1, 2, 3, 5],
                [1, 2, 3, 4],
            ],
        )

    def test_mutating_original_does_not_affect_clone(self):
        adj_list = [[2], [1]]
        node = build_graph(adj_list)
        assert node is not None
        result = self.solution.clone_graph(node)
        assert result is not None
        node.val = 99
        node.neighbors = []
        self.assertEqual(result.val, 1)
        self.assertEqual(len(result.neighbors), 1)
        self.assertEqual(result.neighbors[0].val, 2)

    def test_return_node_val_equals_input_node_val(self):
        adj_list = [[2, 3], [1], [1]]
        node = build_graph(adj_list)
        assert node is not None
        result = self.solution.clone_graph(node)
        assert result is not None
        self.assertEqual(result.val, node.val)


if __name__ == "__main__":
    unittest.main()
