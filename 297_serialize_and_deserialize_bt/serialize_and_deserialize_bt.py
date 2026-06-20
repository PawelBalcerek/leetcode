from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"
        return (
            str(root.val)
            + ","
            + self.serialize(root.left)
            + ","
            + self.serialize(root.right)
        )

    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.i = 0

        def dfs_deserialize():
            if vals[self.i] == "N":
                self.i += 1
                return None
            curr = TreeNode(int(vals[self.i]))
            self.i += 1
            curr.left = dfs_deserialize()
            curr.right = dfs_deserialize()
            return curr

        return dfs_deserialize()
