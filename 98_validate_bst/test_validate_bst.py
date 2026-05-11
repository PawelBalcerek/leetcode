import unittest

from validate_bst import Solution, TreeNode


class TestValidateBST(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(2, TreeNode(1), TreeNode(3))
        self.assertTrue(self.solution.validate_bst(root))

    def test_example_2(self):
        root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
        self.assertFalse(self.solution.validate_bst(root))

    def test_empty_tree(self):
        self.assertTrue(self.solution.validate_bst(None))

    def test_single_node(self):
        root = TreeNode(1)
        self.assertTrue(self.solution.validate_bst(root))

    def test_invalid_right_child(self):
        root = TreeNode(10, TreeNode(5), TreeNode(15, TreeNode(6), TreeNode(20)))
        self.assertFalse(self.solution.validate_bst(root))

    def test_duplicates(self):
        root = TreeNode(2, TreeNode(2), TreeNode(2))
        self.assertFalse(self.solution.validate_bst(root))

    def test_large_values(self):
        val_min = -(2**31)
        val_max = 2**31 - 1
        root = TreeNode(0, TreeNode(val_min), TreeNode(val_max))
        self.assertTrue(self.solution.validate_bst(root))

    def test_strictly_greater_failure(self):
        root = TreeNode(2, TreeNode(1), TreeNode(2))
        self.assertFalse(self.solution.validate_bst(root))


if __name__ == "__main__":
    unittest.main()
