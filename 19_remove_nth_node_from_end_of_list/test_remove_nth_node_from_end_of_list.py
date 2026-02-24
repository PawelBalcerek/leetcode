import unittest
from typing import List, Optional
from remove_nth_node_from_end_of_list import ListNode, Solution


def list_to_linked_list(vals: List[int]) -> Optional[ListNode]:
    if not vals:
        return None
    head = ListNode(vals[0])
    curr = head
    for val in vals[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    vals = []
    curr = head
    while curr:
        vals.append(curr.val)
        curr = curr.next
    return vals


class TestRemoveNthNode(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        head = list_to_linked_list([1, 2, 3, 4, 5])
        n = 2
        result = self.solution.remove_nth_node_from_end_of_list(head, n)
        self.assertEqual(linked_list_to_list(result), [1, 2, 3, 5])

    def test_example2(self):
        head = list_to_linked_list([1])
        n = 1
        result = self.solution.remove_nth_node_from_end_of_list(head, n)
        self.assertEqual(linked_list_to_list(result), [])

    def test_example3(self):
        head = list_to_linked_list([1, 2])
        n = 1
        result = self.solution.remove_nth_node_from_end_of_list(head, n)
        self.assertEqual(linked_list_to_list(result), [1])

    def test_remove_head(self):
        head = list_to_linked_list([1, 2, 3])
        n = 3
        result = self.solution.remove_nth_node_from_end_of_list(head, n)
        self.assertEqual(linked_list_to_list(result), [2, 3])

    def test_remove_tail(self):
        head = list_to_linked_list([1, 2, 3])
        n = 1
        result = self.solution.remove_nth_node_from_end_of_list(head, n)
        self.assertEqual(linked_list_to_list(result), [1, 2])

    def test_sz_constraints(self):
        # Min sz = 1, n = 1 (already covered by example 2)
        # Max sz = 30
        vals = list(range(30))
        head = list_to_linked_list(vals)
        n = 15
        result = self.solution.remove_nth_node_from_end_of_list(head, n)
        expected = vals[:15] + vals[16:]
        self.assertEqual(linked_list_to_list(result), expected)


if __name__ == "__main__":
    unittest.main()
