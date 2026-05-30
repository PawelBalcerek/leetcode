from typing import Optional


class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


class Solution:
    def lowest_common_ancestor_of_a_bst(
        self, root: Optional[TreeNode], p: TreeNode, q: TreeNode
    ) -> Optional[TreeNode]:
        if not root:
            return None

        if q.val < p.val:
            return self.lowest_common_ancestor_of_a_bst(root, q, p)

        if q.val < root.val:
            return self.lowest_common_ancestor_of_a_bst(root.left, p, q)
        elif root.val < p.val:
            return self.lowest_common_ancestor_of_a_bst(root.right, p, q)
        else:
            return root
