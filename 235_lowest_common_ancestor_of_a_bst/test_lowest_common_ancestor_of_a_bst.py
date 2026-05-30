import unittest
from typing import List, Optional

from lowest_common_ancestor_of_a_bst import Solution, TreeNode


def build_bst(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue: List[TreeNode] = [root]
    i = 1
    while i < len(values):
        node = queue.pop(0)
        if i < len(values):
            val = values[i]
            if val is not None:
                node.left = TreeNode(val)
                queue.append(node.left)
        i += 1
        if i < len(values):
            val = values[i]
            if val is not None:
                node.right = TreeNode(val)
                queue.append(node.right)
        i += 1
    return root


def find_node(root: Optional[TreeNode], val: int) -> TreeNode:
    if root is None:
        raise ValueError(f"Node with value {val} not found")

    if val == root.val:
        return root

    if val < root.val:
        return find_node(root.left, val)

    return find_node(root.right, val)


def assert_build_bst(values: List[Optional[int]]) -> TreeNode:
    root = build_bst(values)
    assert root is not None
    return root


class TestLowestCommonAncestorOfABST(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example1_lca_is_root(self) -> None:
        root = assert_build_bst([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
        p = find_node(root, 2)
        q = find_node(root, 8)
        result = self.solution.lowest_common_ancestor_of_a_bst(root, p, q)
        assert result is not None
        self.assertEqual(result.val, 6)

    def test_example2_one_node_is_ancestor(self) -> None:
        root = assert_build_bst([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
        p = find_node(root, 2)
        q = find_node(root, 4)
        result = self.solution.lowest_common_ancestor_of_a_bst(root, p, q)
        assert result is not None
        self.assertEqual(result.val, 2)

    def test_example3_two_node_tree(self) -> None:
        root = assert_build_bst([2, 1])
        p = find_node(root, 2)
        q = find_node(root, 1)
        result = self.solution.lowest_common_ancestor_of_a_bst(root, p, q)
        assert result is not None
        self.assertEqual(result.val, 2)

    def test_reversed_order_p_greater_than_q(self) -> None:
        root = assert_build_bst([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
        p = find_node(root, 8)
        q = find_node(root, 2)
        result = self.solution.lowest_common_ancestor_of_a_bst(root, p, q)
        assert result is not None
        self.assertEqual(result.val, 6)

    def test_both_nodes_in_left_subtree(self) -> None:
        root = assert_build_bst([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
        p = find_node(root, 0)
        q = find_node(root, 5)
        result = self.solution.lowest_common_ancestor_of_a_bst(root, p, q)
        assert result is not None
        self.assertEqual(result.val, 2)

    def test_both_nodes_in_right_subtree(self) -> None:
        root = assert_build_bst([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
        p = find_node(root, 7)
        q = find_node(root, 9)
        result = self.solution.lowest_common_ancestor_of_a_bst(root, p, q)
        assert result is not None
        self.assertEqual(result.val, 8)

    def test_deep_leaf_nodes(self) -> None:
        root = assert_build_bst([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
        p = find_node(root, 3)
        q = find_node(root, 5)
        result = self.solution.lowest_common_ancestor_of_a_bst(root, p, q)
        assert result is not None
        self.assertEqual(result.val, 4)

    def test_parent_child_right(self) -> None:
        root = assert_build_bst([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
        p = find_node(root, 8)
        q = find_node(root, 9)
        result = self.solution.lowest_common_ancestor_of_a_bst(root, p, q)
        assert result is not None
        self.assertEqual(result.val, 8)

    def test_parent_child_left(self) -> None:
        root = assert_build_bst([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
        p = find_node(root, 2)
        q = find_node(root, 0)
        result = self.solution.lowest_common_ancestor_of_a_bst(root, p, q)
        assert result is not None
        self.assertEqual(result.val, 2)

    def test_left_skewed_tree(self) -> None:
        n5 = TreeNode(5)
        n4 = TreeNode(4)
        n3 = TreeNode(3)
        n2 = TreeNode(2)
        n1 = TreeNode(1)
        n5.left = n4
        n4.left = n3
        n3.left = n2
        n2.left = n1
        p = find_node(n5, 1)
        q = find_node(n5, 3)
        result = self.solution.lowest_common_ancestor_of_a_bst(n5, p, q)
        assert result is not None
        self.assertEqual(result.val, 3)

    def test_right_skewed_tree(self) -> None:
        n1 = TreeNode(1)
        n2 = TreeNode(2)
        n3 = TreeNode(3)
        n4 = TreeNode(4)
        n5 = TreeNode(5)
        n1.right = n2
        n2.right = n3
        n3.right = n4
        n4.right = n5
        p = find_node(n1, 2)
        q = find_node(n1, 4)
        result = self.solution.lowest_common_ancestor_of_a_bst(n1, p, q)
        assert result is not None
        self.assertEqual(result.val, 2)

    def test_negative_values(self) -> None:
        root = assert_build_bst([0, -5, 5, -10, -3, 3, 10])
        p = find_node(root, -10)
        q = find_node(root, -3)
        result = self.solution.lowest_common_ancestor_of_a_bst(root, p, q)
        assert result is not None
        self.assertEqual(result.val, -5)

    def test_deepest_nodes_opposite_sides(self) -> None:
        root = assert_build_bst([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
        p = find_node(root, 0)
        q = find_node(root, 9)
        result = self.solution.lowest_common_ancestor_of_a_bst(root, p, q)
        assert result is not None
        self.assertEqual(result.val, 6)


if __name__ == "__main__":
    unittest.main()
