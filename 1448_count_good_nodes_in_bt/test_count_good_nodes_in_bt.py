import unittest

from count_good_nodes_in_bt import Solution, TreeNode


class TestCountGoodNodesInBT(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.left.left = TreeNode(3)
        root.right.left = TreeNode(1)
        root.right.right = TreeNode(5)
        self.assertEqual(self.solution.count_good_nodes_in_bt(root), 4)

    def test_example_2(self):
        root = TreeNode(3)
        root.left = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(2)
        self.assertEqual(self.solution.count_good_nodes_in_bt(root), 3)

    def test_example_3_single_node(self):
        root = TreeNode(1)
        self.assertEqual(self.solution.count_good_nodes_in_bt(root), 1)

    def test_all_nodes_same_value(self):
        root = TreeNode(5)
        root.left = TreeNode(5)
        root.right = TreeNode(5)
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(5)
        self.assertEqual(self.solution.count_good_nodes_in_bt(root), 5)

    def test_strictly_increasing_left_spine(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        self.assertEqual(self.solution.count_good_nodes_in_bt(root), 4)

    def test_strictly_decreasing_left_spine(self):
        root = TreeNode(4)
        root.left = TreeNode(3)
        root.left.left = TreeNode(2)
        root.left.left.left = TreeNode(1)
        self.assertEqual(self.solution.count_good_nodes_in_bt(root), 1)

    def test_negative_values(self):
        root = TreeNode(-2)
        root.left = TreeNode(-3)
        root.right = TreeNode(-1)
        self.assertEqual(self.solution.count_good_nodes_in_bt(root), 2)

    def test_all_negative_same(self):
        root = TreeNode(-5)
        root.left = TreeNode(-5)
        root.right = TreeNode(-5)
        self.assertEqual(self.solution.count_good_nodes_in_bt(root), 3)

    def test_left_only_tree(self):
        root = TreeNode(2)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(1)
        self.assertEqual(self.solution.count_good_nodes_in_bt(root), 3)

    def test_right_only_tree(self):
        root = TreeNode(1)
        root.right = TreeNode(3)
        root.right.right = TreeNode(2)
        root.right.right.right = TreeNode(4)
        self.assertEqual(self.solution.count_good_nodes_in_bt(root), 3)

    def test_root_is_max(self):
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(8)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(7)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(9)
        self.assertEqual(self.solution.count_good_nodes_in_bt(root), 1)

    def test_complete_tree_mixed(self):
        root = TreeNode(3)
        root.left = TreeNode(4)
        root.right = TreeNode(2)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(2)
        root.right.right = TreeNode(6)
        self.assertEqual(self.solution.count_good_nodes_in_bt(root), 5)

    def test_boundary_values(self):
        root = TreeNode(-10_000)
        root.left = TreeNode(10_000)
        root.right = TreeNode(-10_000)
        self.assertEqual(self.solution.count_good_nodes_in_bt(root), 3)


if __name__ == "__main__":
    unittest.main()
