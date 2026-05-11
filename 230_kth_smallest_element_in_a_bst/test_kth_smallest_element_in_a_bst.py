import unittest
from typing import List, Optional
from kth_smallest_element_in_a_bst import TreeNode, Solution

def build_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    if not nodes:
        return None
    
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while i < len(nodes):
        current = queue.pop(0)
        if nodes[i] is not None:
            current.left = TreeNode(nodes[i])
            queue.append(current.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
        i += 1
    return root

class TestKthSmallest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        root = build_tree([3, 1, 4, None, 2])
        self.assertEqual(self.solution.kth_smallest_element_in_a_bst(root, 1), 1)

    def test_example_2(self):
        root = build_tree([5, 3, 6, 2, 4, None, None, 1])
        self.assertEqual(self.solution.kth_smallest_element_in_a_bst(root, 3), 3)

    def test_single_node(self):
        root = build_tree([1])
        self.assertEqual(self.solution.kth_smallest_element_in_a_bst(root, 1), 1)

    def test_right_skewed(self):
        root = build_tree([1, None, 2, None, 3])
        self.assertEqual(self.solution.kth_smallest_element_in_a_bst(root, 2), 2)
        self.assertEqual(self.solution.kth_smallest_element_in_a_bst(root, 3), 3)

    def test_left_skewed(self):
        root = build_tree([3, 2, None, 1, None])
        self.assertEqual(self.solution.kth_smallest_element_in_a_bst(root, 1), 1)
        self.assertEqual(self.solution.kth_smallest_element_in_a_bst(root, 2), 2)

    def test_large_k(self):
        bst_nodes = [5, 3, 8, 2, 4, 7, 9, 1, None, None, None, 6, None, None, 10]
        root = build_tree(bst_nodes)
        self.assertEqual(self.solution.kth_smallest_element_in_a_bst(root, 10), 10)
        self.assertEqual(self.solution.kth_smallest_element_in_a_bst(root, 5), 5)
        self.assertEqual(self.solution.kth_smallest_element_in_a_bst(root, 1), 1)

if __name__ == '__main__':
    unittest.main()
