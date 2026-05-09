import unittest
from typing import List, Optional
from subtree_of_another_tree import TreeNode, Solution

def build_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while queue and i < len(nodes):
        node = queue.pop(0)
        if i < len(nodes) and nodes[i] is not None:
            node.left = TreeNode(nodes[i])
            queue.append(node.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            node.right = TreeNode(nodes[i])
            queue.append(node.right)
        i += 1
    return root

class TestSubtreeOfAnotherTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        root = build_tree([3, 4, 5, 1, 2])
        sub_root = build_tree([4, 1, 2])
        self.assertTrue(self.solution.subtree_of_another_tree(root, sub_root))

    def test_example_2(self):
        root = build_tree([3, 4, 5, 1, 2, None, None, None, None, 0])
        sub_root = build_tree([4, 1, 2])
        self.assertFalse(self.solution.subtree_of_another_tree(root, sub_root))

    def test_identical_trees(self):
        root = build_tree([1, 2, 3])
        sub_root = build_tree([1, 2, 3])
        self.assertTrue(self.solution.subtree_of_another_tree(root, sub_root))

    def test_subroot_is_leaf(self):
        root = build_tree([3, 4, 5, 1, 2])
        sub_root = build_tree([1])
        self.assertTrue(self.solution.subtree_of_another_tree(root, sub_root))

    def test_subroot_not_present(self):
        root = build_tree([3, 4, 5, 1, 2])
        sub_root = build_tree([6])
        self.assertFalse(self.solution.subtree_of_another_tree(root, sub_root))

    def test_complex_not_subtree(self):
        root = build_tree([1, 1])
        sub_root = build_tree([1])
        self.assertTrue(self.solution.subtree_of_another_tree(root, sub_root))

    def test_deep_subtree(self):
        root = build_tree([1, 2, 3, 4, 5, 6, 7, 8])
        sub_root = build_tree([4, 8])
        self.assertTrue(self.solution.subtree_of_another_tree(root, sub_root))

if __name__ == "__main__":
    unittest.main()
