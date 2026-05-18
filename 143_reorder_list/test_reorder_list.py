import unittest
from typing import List, Optional
from reorder_list import ListNode, Solution

def array_to_list(arr: List[int]) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for i in range(1, len(arr)):
        curr.next = ListNode(arr[i])
        curr = curr.next
    return head

def list_to_array(head: Optional[ListNode]) -> List[int]:
    arr = []
    curr = head
    while curr:
        arr.append(curr.val)
        curr = curr.next
    return arr

class TestReorderList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        head = array_to_list([1, 2, 3, 4])
        self.solution.reorder_list(head)
        self.assertEqual(list_to_array(head), [1, 4, 2, 3])

    def test_example_2(self):
        head = array_to_list([1, 2, 3, 4, 5])
        self.solution.reorder_list(head)
        self.assertEqual(list_to_array(head), [1, 5, 2, 4, 3])

    def test_empty_list(self):
        head = array_to_list([])
        self.solution.reorder_list(head)
        self.assertEqual(list_to_array(head), [])

    def test_single_node(self):
        head = array_to_list([1])
        self.solution.reorder_list(head)
        self.assertEqual(list_to_array(head), [1])

    def test_two_nodes(self):
        head = array_to_list([1, 2])
        self.solution.reorder_list(head)
        self.assertEqual(list_to_array(head), [1, 2])

    def test_three_nodes(self):
        head = array_to_list([1, 2, 3])
        self.solution.reorder_list(head)
        self.assertEqual(list_to_array(head), [1, 3, 2])

    def test_large_even(self):
        head = array_to_list([1, 2, 3, 4, 5, 6])
        self.solution.reorder_list(head)
        self.assertEqual(list_to_array(head), [1, 6, 2, 5, 3, 4])

    def test_large_odd(self):
        head = array_to_list([1, 2, 3, 4, 5, 6, 7])
        self.solution.reorder_list(head)
        self.assertEqual(list_to_array(head), [1, 7, 2, 6, 3, 5, 4])

if __name__ == '__main__':
    unittest.main()
