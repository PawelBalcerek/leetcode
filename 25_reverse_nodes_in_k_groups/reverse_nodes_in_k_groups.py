from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_nodes_in_k_groups(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        before_group = dummy

        while before_group.next:
            kth = self.get_kth(before_group, k)
            if not kth:
                break

            after_group = kth.next
            prev, curr = after_group, before_group.next

            while curr != after_group:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = before_group.next
            before_group.next = kth
            before_group = tmp

        return dummy.next

    def get_kth(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        while head and k > 0:
            head = head.next
            k -= 1
        return head
