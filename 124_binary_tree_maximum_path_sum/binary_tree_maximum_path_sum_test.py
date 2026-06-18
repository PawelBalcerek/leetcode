import unittest

from binary_tree_maximum_path_sum import Solution, TreeNode


class TestBinaryTreeMaximumPathSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertEqual(self.solution.binary_tree_maximum_path_sum(root), 6)

    def test_example2(self):
        root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        self.assertEqual(self.solution.binary_tree_maximum_path_sum(root), 42)

    def test_single_node_positive(self):
        root = TreeNode(5)
        self.assertEqual(self.solution.binary_tree_maximum_path_sum(root), 5)

    def test_single_node_negative(self):
        root = TreeNode(-3)
        self.assertEqual(self.solution.binary_tree_maximum_path_sum(root), -3)

    def test_single_node_zero(self):
        root = TreeNode(0)
        self.assertEqual(self.solution.binary_tree_maximum_path_sum(root), 0)

    def test_all_negative(self):
        root = TreeNode(-1, TreeNode(-2), TreeNode(-3))
        self.assertEqual(self.solution.binary_tree_maximum_path_sum(root), -1)

    def test_left_skewed(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3)))
        self.assertEqual(self.solution.binary_tree_maximum_path_sum(root), 6)

    def test_right_skewed(self):
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        self.assertEqual(self.solution.binary_tree_maximum_path_sum(root), 6)

    def test_path_not_through_root(self):
        root = TreeNode(-100, TreeNode(50, TreeNode(40), TreeNode(60)))
        self.assertEqual(self.solution.binary_tree_maximum_path_sum(root), 150)

    def test_negative_root_with_positive_subtrees(self):
        root = TreeNode(-1, TreeNode(5), TreeNode(4))
        self.assertEqual(self.solution.binary_tree_maximum_path_sum(root), 8)

    def test_large_values(self):
        root = TreeNode(1000, TreeNode(1000), TreeNode(1000))
        self.assertEqual(self.solution.binary_tree_maximum_path_sum(root), 3000)

    def test_min_values(self):
        root = TreeNode(-1000, TreeNode(-1000), TreeNode(-1000))
        self.assertEqual(self.solution.binary_tree_maximum_path_sum(root), -1000)

    def test_mixed_deep_tree(self):
        root = TreeNode(
            1,
            TreeNode(2, TreeNode(4), TreeNode(5)),
            TreeNode(3, TreeNode(6), TreeNode(7)),
        )
        self.assertEqual(self.solution.binary_tree_maximum_path_sum(root), 18)

    def test_best_path_in_left_subtree(self):
        root = TreeNode(
            -5,
            TreeNode(10, TreeNode(8), TreeNode(9)),
            TreeNode(-3),
        )
        self.assertEqual(self.solution.binary_tree_maximum_path_sum(root), 27)

    def test_best_path_in_right_subtree(self):
        root = TreeNode(
            -5,
            TreeNode(-3),
            TreeNode(10, TreeNode(8), TreeNode(9)),
        )
        self.assertEqual(self.solution.binary_tree_maximum_path_sum(root), 27)

    def test_zigzag_path(self):
        root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
        self.assertEqual(self.solution.binary_tree_maximum_path_sum(root), 6)

    def test_negative_children_better_alone(self):
        root = TreeNode(10, TreeNode(-20), TreeNode(-30))
        self.assertEqual(self.solution.binary_tree_maximum_path_sum(root), 10)

    def test_two_nodes(self):
        root = TreeNode(1, TreeNode(2))
        self.assertEqual(self.solution.binary_tree_maximum_path_sum(root), 3)

    def test_two_nodes_negative_child(self):
        root = TreeNode(5, TreeNode(-10))
        self.assertEqual(self.solution.binary_tree_maximum_path_sum(root), 5)


if __name__ == "__main__":
    unittest.main()
