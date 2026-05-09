from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameter_of_binary_tree(self, root: Optional[TreeNode]) -> int:
        result = 0

        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal result 

            if not root:
                return -1

            left = dfs(root.left) + 1
            right = dfs(root.right) + 1
            result = max(result, left + right)

            return max(left, right)

        dfs(root)

        return result
