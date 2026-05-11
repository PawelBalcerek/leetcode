from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def validate_bst(self, root: Optional[TreeNode]) -> bool:
        def is_valid(
            node: Optional[TreeNode], left_boundary: float, right_boundary: float
        ):
            if not node:
                return True
            if not (left_boundary < node.val < right_boundary):
                return False
            return is_valid(node.left, left_boundary, node.val) and is_valid(
                node.right, node.val, right_boundary
            )

        return is_valid(root, float("-inf"), float("inf"))
