import unittest
from typing import Optional, List
from balanced_binary_tree import TreeNode, Solution

class TestBalancedBinaryTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def build_tree(self, nodes: List[Optional[int]]) -> Optional[TreeNode]:
        if not nodes:
            return None
        
        root = TreeNode(nodes[0])
        queue = [root]
        i = 1
        while i < len(nodes):
            node = queue.pop(0)
            if nodes[i] is not None:
                node.left = TreeNode(nodes[i])
                queue.append(node.left)
            i += 1
            if i < len(nodes) and nodes[i] is not None:
                node.right = TreeNode(nodes[i])
                queue.append(node.right)
            i += 1
        return root

    def test_example_1(self):
        root = self.build_tree([3, 9, 20, None, None, 15, 7])
        self.assertTrue(self.solution.balanced_binary_tree(root))

    def test_example_2(self):
        root = self.build_tree([1, 2, 2, 3, 3, None, None, 4, 4])
        self.assertFalse(self.solution.balanced_binary_tree(root))

    def test_example_3(self):
        root = self.build_tree([])
        self.assertTrue(self.solution.balanced_binary_tree(root))

    def test_single_node(self):
        root = self.build_tree([1])
        self.assertTrue(self.solution.balanced_binary_tree(root))

    def test_unbalanced_right_heavy(self):
        root = self.build_tree([1, None, 2, None, 3])
        self.assertFalse(self.solution.balanced_binary_tree(root))

    def test_unbalanced_left_heavy(self):
        root = self.build_tree([1, 2, None, 3, None])
        self.assertFalse(self.solution.balanced_binary_tree(root))

if __name__ == "__main__":
    unittest.main()
