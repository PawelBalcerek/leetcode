from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maximum_depth_of_binary_tree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(
            self.maximum_depth_of_binary_tree(root.left),
            self.maximum_depth_of_binary_tree(root.right),
        )

    def maximum_depth_of_binary_tree_queue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        level = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return level

    def maximum_depth_of_binary_tree_stack(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 1)]
        result = 0
        while stack:
            node, depth = stack.pop()
            if node:
                result = max(result, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
        return result
