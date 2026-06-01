from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binary_tree_right_side_view(self, root: Optional[TreeNode]) -> list[int]:
        result = []
        if not root:
            return result
        queue = deque([root])
        while queue:
            level_len = len(queue)
            result.append(queue[-1].val)
            for _ in range(level_len):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return result

