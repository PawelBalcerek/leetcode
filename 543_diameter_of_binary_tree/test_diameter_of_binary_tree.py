import unittest
from typing import List, Optional
from diameter_of_binary_tree import TreeNode, Solution

class TestDiameterOfBinaryTree(unittest.TestCase):
    def build_tree(self, nodes: List[Optional[int]]) -> Optional[TreeNode]:
        if not nodes:
            return None
        
        root = TreeNode(nodes[0])
        queue = [root]
        i = 1
        while i < len(nodes):
            current = queue.pop(0)
            
            if i < len(nodes) and nodes[i] is not None:
                current.left = TreeNode(nodes[i])
                queue.append(current.left)
            i += 1
            
            if i < len(nodes) and nodes[i] is not None:
                current.right = TreeNode(nodes[i])
                queue.append(current.right)
            i += 1
            
        return root

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        root = self.build_tree([1, 2, 3, 4, 5])
        self.assertEqual(self.solution.diameter_of_binary_tree(root), 3)

    def test_example_2(self):
        root = self.build_tree([1, 2])
        self.assertEqual(self.solution.diameter_of_binary_tree(root), 1)

    def test_single_node(self):
        root = self.build_tree([1])
        self.assertEqual(self.solution.diameter_of_binary_tree(root), 0)

    def test_none_root(self):
        self.assertEqual(self.solution.diameter_of_binary_tree(None), 0)

    def test_skewed_left(self):
        root = self.build_tree([1, 2, None, 3, None, 4])
        self.assertEqual(self.solution.diameter_of_binary_tree(root), 3)

    def test_skewed_right(self):
        root = self.build_tree([1, None, 2, None, 3, None, 4])
        self.assertEqual(self.solution.diameter_of_binary_tree(root), 3)

    def test_long_diameter_not_through_root(self):
        root = self.build_tree([1, 2, 3, 4, 5, None, None, 6, None, None, 7, 8, None, None, 9])
        self.assertEqual(self.solution.diameter_of_binary_tree(root), 6)

if __name__ == '__main__':
    unittest.main()
