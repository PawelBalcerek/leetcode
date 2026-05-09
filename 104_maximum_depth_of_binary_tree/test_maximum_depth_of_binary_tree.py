import unittest
from typing import List, Optional
from maximum_depth_of_binary_tree import TreeNode, Solution

def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

class TestMaximumDepthOfBinaryTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.methods = [
            self.solution.maximum_depth_of_binary_tree,
            self.solution.maximum_depth_of_binary_tree_queue,
            self.solution.maximum_depth_of_binary_tree_stack
        ]

    def test_empty_tree(self):
        for method in self.methods:
            with self.subTest(method=method.__name__):
                self.assertEqual(method(None), 0)

    def test_single_node(self):
        for method in self.methods:
            with self.subTest(method=method.__name__):
                root = TreeNode(1)
                self.assertEqual(method(root), 1)

    def test_example_1(self):
        root = build_tree([3, 9, 20, None, None, 15, 7])
        for method in self.methods:
            with self.subTest(method=method.__name__):
                self.assertEqual(method(root), 3)

    def test_example_2(self):
        root = build_tree([1, None, 2])
        for method in self.methods:
            with self.subTest(method=method.__name__):
                self.assertEqual(method(root), 2)

    def test_unbalanced_tree(self):
        root = build_tree([1, 2, None, 3, None, 4])
        for method in self.methods:
            with self.subTest(method=method.__name__):
                self.assertEqual(method(root), 4)

    def test_full_binary_tree(self):
        root = build_tree([1, 2, 3, 4, 5, 6, 7])
        for method in self.methods:
            with self.subTest(method=method.__name__):
                self.assertEqual(method(root), 3)

if __name__ == '__main__':
    unittest.main()
