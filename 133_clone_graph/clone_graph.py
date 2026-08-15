from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def clone_graph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return None

        copies = {node: Node(node.val)}
        queue = [node]

        for curr in queue:
            for n in curr.neighbors:
                if n not in copies:
                    copies[n] = Node(n.val)
                    queue.append(n)
                copies[curr].neighbors.append(copies[n])

        return copies[node]
