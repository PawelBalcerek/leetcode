import unittest
from typing import List, Optional
from reverse_nodes_in_k_groups_w_stack import ListNode, Solution

def list_to_linked_list(arr: List[int]) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

class TestReverseNodesInKGroups(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        head = list_to_linked_list([1, 2, 3, 4, 5])
        k = 2
        result = self.solution.reverse_nodes_in_k_groups_w_stack(head, k)
        self.assertEqual(linked_list_to_list(result), [2, 1, 4, 3, 5])

    def test_example_2(self):
        head = list_to_linked_list([1, 2, 3, 4, 5])
        k = 3
        result = self.solution.reverse_nodes_in_k_groups_w_stack(head, k)
        self.assertEqual(linked_list_to_list(result), [3, 2, 1, 4, 5])

    def test_k_equals_one(self):
        head = list_to_linked_list([1, 2, 3])
        k = 1
        result = self.solution.reverse_nodes_in_k_groups_w_stack(head, k)
        self.assertEqual(linked_list_to_list(result), [1, 2, 3])

    def test_k_equals_n(self):
        head = list_to_linked_list([1, 2, 3, 4])
        k = 4
        result = self.solution.reverse_nodes_in_k_groups_w_stack(head, k)
        self.assertEqual(linked_list_to_list(result), [4, 3, 2, 1])

    def test_n_multiple_of_k(self):
        head = list_to_linked_list([1, 2, 3, 4, 5, 6])
        k = 2
        result = self.solution.reverse_nodes_in_k_groups_w_stack(head, k)
        self.assertEqual(linked_list_to_list(result), [2, 1, 4, 3, 6, 5])

    def test_empty_list(self):
        head = list_to_linked_list([])
        k = 3
        result = self.solution.reverse_nodes_in_k_groups_w_stack(head, k)
        self.assertEqual(linked_list_to_list(result), [])

if __name__ == "__main__":
    unittest.main()
