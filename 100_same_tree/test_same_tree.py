import unittest

from same_tree import Solution, TreeNode


class TestSameTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_both_none(self):
        self.assertTrue(self.solution.same_tree(None, None))

    def test_one_none(self):
        p = TreeNode(1)
        self.assertFalse(self.solution.same_tree(p, None))
        self.assertFalse(self.solution.same_tree(None, p))

    def test_example_1(self):
        p = TreeNode(1, TreeNode(2), TreeNode(3))
        q = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertTrue(self.solution.same_tree(p, q))

    def test_example_2(self):
        p = TreeNode(1, TreeNode(2))
        q = TreeNode(1, None, TreeNode(2))
        self.assertFalse(self.solution.same_tree(p, q))

    def test_example_3(self):
        p = TreeNode(1, TreeNode(2), TreeNode(1))
        q = TreeNode(1, TreeNode(1), TreeNode(2))
        self.assertFalse(self.solution.same_tree(p, q))

    def test_single_node_equal(self):
        p = TreeNode(5)
        q = TreeNode(5)
        self.assertTrue(self.solution.same_tree(p, q))

    def test_single_node_unequal(self):
        p = TreeNode(5)
        q = TreeNode(10)
        self.assertFalse(self.solution.same_tree(p, q))

    def test_complex_tree_false(self):
        p = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
        q = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(6)), TreeNode(3))
        self.assertFalse(self.solution.same_tree(p, q))


if __name__ == "__main__":
    unittest.main()
