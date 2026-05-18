from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorder_list(self, head: Optional[ListNode]) -> None:
        if not head:
            return head

        s, f = head, head.next
        while s and f and f.next:
            s = s.next
            f = f.next.next

        r, curr = None, s.next if s else None
        while curr:
            tmp = curr.next
            curr.next = r
            r = curr
            curr = tmp

        if s:
            s.next = None

        l = head
        while l and r:
            tmp_l, tmp_r = l.next, r.next
            l.next = r
            r.next = tmp_l
            l = tmp_l
            r = tmp_r

