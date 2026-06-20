import unittest
from serialize_and_deserialize_bt import TreeNode, Solution


def trees_equal(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    return a.val == b.val and trees_equal(a.left, b.left) and trees_equal(a.right, b.right)


class TestSerializeAndDeserialize(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_one(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
        data = self.sol.serialize(root)
        result = self.sol.deserialize(data)
        self.assertTrue(trees_equal(root, result))

    def test_empty_tree(self):
        data = self.sol.serialize(None)
        result = self.sol.deserialize(data)
        self.assertIsNone(result)

    def test_single_node(self):
        root = TreeNode(42)
        data = self.sol.serialize(root)
        result = self.sol.deserialize(data)
        self.assertTrue(trees_equal(root, result))

    def test_left_skewed(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
        data = self.sol.serialize(root)
        result = self.sol.deserialize(data)
        self.assertTrue(trees_equal(root, result))

    def test_right_skewed(self):
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
        data = self.sol.serialize(root)
        result = self.sol.deserialize(data)
        self.assertTrue(trees_equal(root, result))

    def test_negative_values(self):
        root = TreeNode(-1, TreeNode(-500), TreeNode(-1000))
        data = self.sol.serialize(root)
        result = self.sol.deserialize(data)
        self.assertTrue(trees_equal(root, result))

    def test_mixed_values(self):
        root = TreeNode(0, TreeNode(-1000), TreeNode(1000))
        data = self.sol.serialize(root)
        result = self.sol.deserialize(data)
        self.assertTrue(trees_equal(root, result))

    def test_serialize_returns_string(self):
        root = TreeNode(1)
        data = self.sol.serialize(root)
        self.assertIsInstance(data, str)

    def test_serialize_empty_returns_string(self):
        data = self.sol.serialize(None)
        self.assertIsInstance(data, str)

    def test_deserialize_returns_none_or_treenode(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        data = self.sol.serialize(root)
        result = self.sol.deserialize(data)
        self.assertIsInstance(result, TreeNode)

    def test_roundtrip_preserves_structure(self):
        root = TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(4)), TreeNode(8, TreeNode(7), TreeNode(9)))
        data = self.sol.serialize(root)
        result = self.sol.deserialize(data)
        self.assertTrue(trees_equal(root, result))

    def test_duplicate_values(self):
        root = TreeNode(1, TreeNode(1, TreeNode(1)), TreeNode(1))
        data = self.sol.serialize(root)
        result = self.sol.deserialize(data)
        self.assertTrue(trees_equal(root, result))

    def test_large_values_at_boundary(self):
        root = TreeNode(-1000, TreeNode(1000), TreeNode(-1000, None, TreeNode(1000)))
        data = self.sol.serialize(root)
        result = self.sol.deserialize(data)
        self.assertTrue(trees_equal(root, result))

    def test_double_roundtrip(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
        data1 = self.sol.serialize(root)
        tree1 = self.sol.deserialize(data1)
        data2 = self.sol.serialize(tree1)
        tree2 = self.sol.deserialize(data2)
        self.assertEqual(data1, data2)
        self.assertTrue(trees_equal(root, tree2))


if __name__ == "__main__":
    unittest.main()
