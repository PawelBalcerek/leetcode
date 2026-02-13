import unittest
from typing import List, Optional
from merge_two_sorted_list import ListNode, Solution

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

class TestMergeTwoSortedList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        l1 = list_to_linked_list([1, 2, 4])
        l2 = list_to_linked_list([1, 3, 4])
        result = self.solution.merge_two_sorted_list(l1, l2)
        self.assertEqual(linked_list_to_list(result), [1, 1, 2, 3, 4, 4])

    def test_example2(self):
        l1 = list_to_linked_list([])
        l2 = list_to_linked_list([])
        result = self.solution.merge_two_sorted_list(l1, l2)
        self.assertEqual(linked_list_to_list(result), [])

    def test_example3(self):
        l1 = list_to_linked_list([])
        l2 = list_to_linked_list([0])
        result = self.solution.merge_two_sorted_list(l1, l2)
        self.assertEqual(linked_list_to_list(result), [0])

    def test_one_empty(self):
        l1 = list_to_linked_list([1, 2, 3])
        l2 = list_to_linked_list([])
        result = self.solution.merge_two_sorted_list(l1, l2)
        self.assertEqual(linked_list_to_list(result), [1, 2, 3])

    def test_different_lengths(self):
        l1 = list_to_linked_list([1])
        l2 = list_to_linked_list([2, 3, 4])
        result = self.solution.merge_two_sorted_list(l1, l2)
        self.assertEqual(linked_list_to_list(result), [1, 2, 3, 4])

if __name__ == "__main__":
    unittest.main()
