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
    def construct_binary_tree(
        self, preorder: list[int], inorder: list[int]
    ) -> Optional[TreeNode]:
        inorder_index = {val: idx for idx, val in enumerate(inorder)}

        def build_tree(
            preorder_l: int, preorder_r: int, inorder_l: int, inorder_r: int
        ) -> Optional[TreeNode]:
            if preorder_l > preorder_r:
                return None
            root = TreeNode(preorder[preorder_l])
            partition_index = inorder_index[root.val]
            l_size = partition_index - inorder_l
            root.left = build_tree(
                preorder_l + 1, preorder_l + l_size, inorder_l, partition_index - 1
            )
            root.right = build_tree(
                preorder_l + l_size + 1, preorder_r, partition_index + 1, inorder_r
            )
            return root

        return build_tree(0, len(preorder) - 1, 0, len(inorder) - 1)
