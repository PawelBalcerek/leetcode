from typing import Optional


class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.left, self.right = Node(), Node()
        self.left.next, self.right.prev = self.right, self.left

    def insert_node(self, node) -> None:
        prev = self.right.prev
        if prev:
            prev.next = node
        self.right.prev = node
        node.prev, node.next = prev, self.right

    def remove_node(self, node) -> None:
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove_node(node)
        self.insert_node(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove_node(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self.insert_node(node)
        if len(self.cache) > self.capacity:
            node_to_remove = self.left.next
            if node_to_remove:
                self.remove_node(node_to_remove)
                del self.cache[node_to_remove.key]
