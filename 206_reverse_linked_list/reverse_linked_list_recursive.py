from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_linked_list_recursive(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not head:
            return head

        newHead = head  # it handles [1]

        if head.next:
            newHead = self.reverse_linked_list_recursive(head.next)
            head.next.next = head  # head.next, point to the head

        head.next = None  # head, point to the none

        return newHead
