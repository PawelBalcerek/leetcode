import unittest
from typing import List, Optional
from reverse_linked_list_iterative import ListNode, Solution

def list_to_linked_list(arr: List[int]) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result

class TestReverseLinkedListIterative(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        head = list_to_linked_list([])
        reversed_head = self.solution.reverse_linked_list_iterative(head)
        self.assertEqual(linked_list_to_list(reversed_head), [])

    def test_single_node(self):
        head = list_to_linked_list([1])
        reversed_head = self.solution.reverse_linked_list_iterative(head)
        self.assertEqual(linked_list_to_list(reversed_head), [1])

    def test_multiple_nodes(self):
        head = list_to_linked_list([1, 2, 3, 4, 5])
        reversed_head = self.solution.reverse_linked_list_iterative(head)
        self.assertEqual(linked_list_to_list(reversed_head), [5, 4, 3, 2, 1])

    def test_two_nodes(self):
        head = list_to_linked_list([1, 2])
        reversed_head = self.solution.reverse_linked_list_iterative(head)
        self.assertEqual(linked_list_to_list(reversed_head), [2, 1])

if __name__ == "__main__":
    unittest.main()
