import unittest
from typing import List, Optional
from collections import deque
from invert_binary_tree import BTNode, Solution

def build_tree(vals: List[Optional[int]]) -> Optional[BTNode]:
    if not vals:
        return None
    root = BTNode(vals[0])
    queue = deque([root])
    i = 1
    while queue and i < len(vals):
        node = queue.popleft()
        if i < len(vals) and vals[i] is not None:
            node.left = BTNode(vals[i])
            queue.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = BTNode(vals[i])
            queue.append(node.right)
        i += 1
    return root

def tree_to_list(root: Optional[BTNode]) -> List[Optional[int]]:
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result

class TestInvertBinaryTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.test_cases = [
            ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1], "Example 1"),
            ([2, 1, 3], [2, 3, 1], "Example 2"),
            ([], [], "Example 3"),
            ([1], [1], "Single Node"),
            ([1, 2, None, 3], [1, None, 2, None, 3], "Unbalanced Tree"),
            ([1, 2, 3, 4], [1, 3, 2, None, None, None, 4], "Complex Tree"),
        ]

    def _run_all_cases(self, invert_func):
        for root_vals, expected_vals, name in self.test_cases:
            with self.subTest(case=name):
                root = build_tree(root_vals)
                inverted_root = invert_func(root)
                self.assertEqual(tree_to_list(inverted_root), expected_vals)

    def test_iterative(self):
        self._run_all_cases(self.solution.invert_binary_tree)

    def test_recursive(self):
        self._run_all_cases(self.solution.invert_binary_tree_r)

if __name__ == "__main__":
    unittest.main()
