from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def linked_list_cycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while slow and fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
