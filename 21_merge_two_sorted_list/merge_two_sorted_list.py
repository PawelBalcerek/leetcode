from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_two_sorted_list(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        merged = ListNode()
        worker = merged
        while l1 and l2:
            if l1.val <= l2.val:
                worker.next = l1
                l1 = l1.next
            else:
                worker.next = l2
                l2 = l2.next
            worker = worker.next
        if l1:
            worker.next = l1
        else:
            worker.next = l2
        return merged.next
