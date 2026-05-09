from collections import deque
from typing import Optional


class BTNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invert_binary_tree(self, root: Optional[BTNode]) -> Optional[BTNode]:
        if not root:
            return root
        queue = deque([root])
        while queue:
            parent = queue.popleft()
            left, right = parent.left, parent.right
            parent.left, parent.right = parent.right, parent.left
            if left and (left.left or left.right):
                queue.append(left)
            if right and (right.left or right.right):
                queue.append(right)
        return root

    def invert_binary_tree_r(self, root: Optional[BTNode]) -> Optional[BTNode]:
        if not root:
            return root
        root.left, root.right = (
            self.invert_binary_tree_r(root.right),
            self.invert_binary_tree_r(root.left),
        )
        return root
