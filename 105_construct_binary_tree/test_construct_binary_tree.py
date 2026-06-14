import unittest
from typing import Optional

from construct_binary_tree import Solution, TreeNode


def tree_to_list(root: Optional[TreeNode]) -> list:
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


class TestConstructBinaryTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        preorder = [3, 9, 20, 15, 7]
        inorder = [9, 3, 15, 20, 7]
        result = self.solution.construct_binary_tree(preorder, inorder)
        self.assertEqual(tree_to_list(result), [3, 9, 20, None, None, 15, 7])

    def test_example_2(self):
        preorder = [-1]
        inorder = [-1]
        result = self.solution.construct_binary_tree(preorder, inorder)
        self.assertEqual(tree_to_list(result), [-1])

    def test_empty(self):
        result = self.solution.construct_binary_tree([], [])
        self.assertIsNone(result)

    def test_two_nodes_left_child(self):
        preorder = [1, 2]
        inorder = [2, 1]
        result = self.solution.construct_binary_tree(preorder, inorder)
        self.assertEqual(tree_to_list(result), [1, 2])

    def test_two_nodes_right_child(self):
        preorder = [1, 2]
        inorder = [1, 2]
        result = self.solution.construct_binary_tree(preorder, inorder)
        self.assertEqual(tree_to_list(result), [1, None, 2])

    def test_left_skewed(self):
        preorder = [1, 2, 3, 4]
        inorder = [4, 3, 2, 1]
        result = self.solution.construct_binary_tree(preorder, inorder)
        self.assertEqual(tree_to_list(result), [1, 2, None, 3, None, 4])

    def test_right_skewed(self):
        preorder = [1, 2, 3, 4]
        inorder = [1, 2, 3, 4]
        result = self.solution.construct_binary_tree(preorder, inorder)
        self.assertEqual(tree_to_list(result), [1, None, 2, None, 3, None, 4])

    def test_full_binary_tree(self):
        preorder = [1, 2, 4, 5, 3, 6, 7]
        inorder = [4, 2, 5, 1, 6, 3, 7]
        result = self.solution.construct_binary_tree(preorder, inorder)
        self.assertEqual(tree_to_list(result), [1, 2, 3, 4, 5, 6, 7])

    def test_negative_values(self):
        preorder = [-10, -20, -30]
        inorder = [-30, -20, -10]
        result = self.solution.construct_binary_tree(preorder, inorder)
        self.assertEqual(tree_to_list(result), [-10, -20, None, -30])

    def test_mixed_values(self):
        preorder = [0, -1, 1]
        inorder = [-1, 0, 1]
        result = self.solution.construct_binary_tree(preorder, inorder)
        self.assertEqual(tree_to_list(result), [0, -1, 1])

    def test_root_structure(self):
        preorder = [3, 9, 20, 15, 7]
        inorder = [9, 3, 15, 20, 7]
        result = self.solution.construct_binary_tree(preorder, inorder)
        self.assertIsNotNone(result)
        self.assertEqual(result.val, 3)
        self.assertEqual(result.left.val, 9)
        self.assertEqual(result.right.val, 20)
        self.assertEqual(result.right.left.val, 15)
        self.assertEqual(result.right.right.val, 7)
        self.assertIsNone(result.left.left)
        self.assertIsNone(result.left.right)


if __name__ == "__main__":
    unittest.main()
