from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swap_nodes_in_pairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        worker = dummy = ListNode()
        left, right = head, head.next
        while left and right:
            worker.next = right
            left.next = right.next
            right.next = left
            worker = left
            left = left.next
            right = left.next if left else None
        return dummy.next
