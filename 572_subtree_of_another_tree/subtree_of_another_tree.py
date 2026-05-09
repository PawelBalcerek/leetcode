from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def subtree_of_another_tree(
        self, root: Optional[TreeNode], sub_tree: Optional[TreeNode]
    ) -> bool:
        if not root and sub_tree:
            return False
        return (
            not sub_tree
            or self.same_tree(root, sub_tree)
            or self.subtree_of_another_tree(root.left if root else None, sub_tree)
            or self.subtree_of_another_tree(root.right if root else None, sub_tree)
        )

    def same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.same_tree(p.left, q.left) and self.same_tree(p.right, q.right)
