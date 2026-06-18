from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binary_tree_maximum_path_sum(self, root: TreeNode) -> int:
        self.result = -(2**31)

        def maximum_path_sum(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            l = max(0, maximum_path_sum(node.left))
            r = max(0, maximum_path_sum(node.right))
            self.result = max(self.result, node.val + l + r)
            return node.val + max(l, r)

        maximum_path_sum(root)
        return self.result
