from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time complexity: O(n)
# Space complexity: O(k)
class Solution:
    def reverse_nodes_in_k_groups_w_stack(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        dummy = ListNode()
        worker = dummy
        stack = []
        while head:
            stack.append(head)
            head = head.next
            if len(stack) == k:
                for _ in range(k):
                    node = stack.pop()
                    node.next = None
                    worker.next = node
                    worker = worker.next
                worker.next = head
        return dummy.next
