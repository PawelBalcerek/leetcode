import unittest

from binary_tree_level_order_traversal import Solution, TreeNode


class TestBinaryTreeLevelOrderTraversal(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        self.assertEqual(
            self.solution.binary_tree_level_order_traversal(root),
            [[3], [9, 20], [15, 7]],
        )

    def test_example_2(self):
        root = TreeNode(1)
        self.assertEqual(
            self.solution.binary_tree_level_order_traversal(root),
            [[1]],
        )

    def test_example_3(self):
        self.assertEqual(
            self.solution.binary_tree_level_order_traversal(None),
            [],
        )

    def test_left_skewed_tree(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
        self.assertEqual(
            self.solution.binary_tree_level_order_traversal(root),
            [[1], [2], [3], [4]],
        )

    def test_right_skewed_tree(self):
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
        self.assertEqual(
            self.solution.binary_tree_level_order_traversal(root),
            [[1], [2], [3], [4]],
        )

    def test_complete_binary_tree(self):
        root = TreeNode(
            1,
            TreeNode(2, TreeNode(4), TreeNode(5)),
            TreeNode(3, TreeNode(6), TreeNode(7)),
        )
        self.assertEqual(
            self.solution.binary_tree_level_order_traversal(root),
            [[1], [2, 3], [4, 5, 6, 7]],
        )

    def test_negative_values(self):
        root = TreeNode(-1, TreeNode(-2), TreeNode(-3))
        self.assertEqual(
            self.solution.binary_tree_level_order_traversal(root),
            [[-1], [-2, -3]],
        )

    def test_mixed_values(self):
        root = TreeNode(0, TreeNode(-1000), TreeNode(1000))
        self.assertEqual(
            self.solution.binary_tree_level_order_traversal(root),
            [[0], [-1000, 1000]],
        )

    def test_unbalanced_tree(self):
        root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
        self.assertEqual(
            self.solution.binary_tree_level_order_traversal(root),
            [[1], [2, 3], [4]],
        )

    def test_single_left_child(self):
        root = TreeNode(1, TreeNode(2))
        self.assertEqual(
            self.solution.binary_tree_level_order_traversal(root),
            [[1], [2]],
        )

    def test_single_right_child(self):
        root = TreeNode(1, None, TreeNode(2))
        self.assertEqual(
            self.solution.binary_tree_level_order_traversal(root),
            [[1], [2]],
        )


if __name__ == "__main__":
    unittest.main()
