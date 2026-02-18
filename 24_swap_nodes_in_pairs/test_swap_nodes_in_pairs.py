import unittest
from typing import List, Optional
from swap_nodes_in_pairs import ListNode, Solution

def list_to_linked_list(arr: List[int]) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for i in range(1, len(arr)):
        curr.next = ListNode(arr[i])
        curr = curr.next
    return head

def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result

class TestSwapNodesInPairs(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        head = list_to_linked_list([1, 2, 3, 4])
        result = self.solution.swap_nodes_in_pairs(head)
        self.assertEqual(linked_list_to_list(result), [2, 1, 4, 3])

    def test_example_2_empty(self):
        head = list_to_linked_list([])
        result = self.solution.swap_nodes_in_pairs(head)
        self.assertEqual(linked_list_to_list(result), [])

    def test_example_3_single_node(self):
        head = list_to_linked_list([1])
        result = self.solution.swap_nodes_in_pairs(head)
        self.assertEqual(linked_list_to_list(result), [1])

    def test_example_4_odd_nodes(self):
        head = list_to_linked_list([1, 2, 3])
        result = self.solution.swap_nodes_in_pairs(head)
        self.assertEqual(linked_list_to_list(result), [2, 1, 3])

    def test_longer_even_list(self):
        head = list_to_linked_list([1, 2, 3, 4, 5, 6])
        result = self.solution.swap_nodes_in_pairs(head)
        self.assertEqual(linked_list_to_list(result), [2, 1, 4, 3, 6, 5])

if __name__ == "__main__":
    unittest.main()
