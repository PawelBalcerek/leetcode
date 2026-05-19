from typing import Optional


class Node:
    def __init__(
        self, x: int, next: Optional["Node"] = None, random: Optional["Node"] = None
    ):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copy_list_with_random_pointer(self, head: Optional[Node]) -> Optional[Node]:
        original_to_copy: dict[Optional[Node], Optional[Node]] = {None: None}

        worker = head
        while worker:
            copy = Node(worker.val)
            original_to_copy[worker] = copy
            worker = worker.next

        worker = head
        while worker:
            copy = original_to_copy[worker]
            if not copy:
                continue
            copy.next = original_to_copy[worker.next]
            copy.random = original_to_copy[worker.random]
            worker = worker.next

        return original_to_copy[head]
