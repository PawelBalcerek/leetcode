from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swap_nodes_in_pairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        l, r = dummy, dummy.next
        while l and r and r.next:
            l.next = r.next
            r.next = r.next.next
            l.next.next = r
            l = r
            r = r.next
        return dummy.next
