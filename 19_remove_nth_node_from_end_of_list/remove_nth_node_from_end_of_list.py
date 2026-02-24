from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def remove_nth_node_from_end_of_list(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        l = dummy
        r = head

        while n > 0 and r:
            r = r.next
            n -= 1

        while r and l:
            r = r.next
            l = l.next

        if l and l.next:
            l.next = l.next.next

        return dummy.next
