from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binary_tree_level_order_traversal(
        self, root: Optional[TreeNode]
    ) -> list[list[int]]:
        if not root:
            return []

        queue = deque([root])
        results = []
        while queue:
            level_len = len(queue)
            level = []
            for _ in range(level_len):
                curr = queue.popleft()
                if curr:
                    level.append(curr.val)
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
            if level:
                results.append(level)
        return results
