import unittest
from binary_tree_right_side_view import Solution, TreeNode


class TestBinaryTreeRightSideView(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(4)
        self.assertEqual(self.solution.binary_tree_right_side_view(root), [1, 3, 4])

    def test_example_2(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.left.left = TreeNode(5)
        self.assertEqual(self.solution.binary_tree_right_side_view(root), [1, 3, 4, 5])

    def test_example_3(self):
        root = TreeNode(1)
        root.right = TreeNode(3)
        self.assertEqual(self.solution.binary_tree_right_side_view(root), [1, 3])

    def test_empty_tree(self):
        self.assertEqual(self.solution.binary_tree_right_side_view(None), [])

    def test_single_node(self):
        root = TreeNode(42)
        self.assertEqual(self.solution.binary_tree_right_side_view(root), [42])

    def test_left_skewed_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        self.assertEqual(self.solution.binary_tree_right_side_view(root), [1, 2, 3, 4])

    def test_right_skewed_tree(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        root.right.right.right = TreeNode(4)
        self.assertEqual(self.solution.binary_tree_right_side_view(root), [1, 2, 3, 4])

    def test_complete_binary_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        self.assertEqual(self.solution.binary_tree_right_side_view(root), [1, 3, 7])

    def test_negative_values(self):
        root = TreeNode(-1)
        root.left = TreeNode(-2)
        root.right = TreeNode(-3)
        self.assertEqual(self.solution.binary_tree_right_side_view(root), [-1, -3])

    def test_zero_values(self):
        root = TreeNode(0)
        root.left = TreeNode(0)
        root.right = TreeNode(0)
        self.assertEqual(self.solution.binary_tree_right_side_view(root), [0, 0])

    def test_left_subtree_deeper_than_right(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        self.assertEqual(self.solution.binary_tree_right_side_view(root), [1, 3, 4])

    def test_right_subtree_deeper_than_left(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.right = TreeNode(4)
        self.assertEqual(self.solution.binary_tree_right_side_view(root), [1, 3, 4])

    def test_boundary_value_100(self):
        root = TreeNode(100)
        root.left = TreeNode(-100)
        self.assertEqual(self.solution.binary_tree_right_side_view(root), [100, -100])


if __name__ == "__main__":
    unittest.main()
