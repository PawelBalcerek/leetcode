from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def count_good_nodes_in_bt(self, root: TreeNode) -> int:
        def dfs(curr: Optional[TreeNode], m: int) -> int:
            if not curr:
                return 0
            return (
                (1 if m <= curr.val else 0)
                + dfs(curr.left, max(m, curr.val))
                + dfs(curr.right, max(m, curr.val))
            )

        return dfs(root, root.val)
