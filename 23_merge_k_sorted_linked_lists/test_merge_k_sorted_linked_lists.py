import unittest
from typing import List, Optional
from merge_k_sorted_linked_lists import ListNode, Solution


def to_linked_list(arr: List[int]) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def from_linked_list(node: Optional[ListNode]) -> List[int]:
    result = []
    current = node
    while current:
        result.append(current.val)
        current = current.next
    return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        lists = [
            to_linked_list([1, 4, 5]),
            to_linked_list([1, 3, 4]),
            to_linked_list([2, 6]),
        ]
        merged = self.solution.merge_k_sorted_lists(lists)
        self.assertEqual(from_linked_list(merged), [1, 1, 2, 3, 4, 4, 5, 6])

    def test_example_2(self):
        lists = []
        merged = self.solution.merge_k_sorted_lists(lists)
        self.assertEqual(from_linked_list(merged), [])

    def test_example_3(self):
        lists = [to_linked_list([])]
        merged = self.solution.merge_k_sorted_lists(lists)
        self.assertEqual(from_linked_list(merged), [])

    def test_single_list(self):
        lists = [to_linked_list([1, 2, 3])]
        merged = self.solution.merge_k_sorted_lists(lists)
        self.assertEqual(from_linked_list(merged), [1, 2, 3])

    def test_all_empty_lists(self):
        lists = [to_linked_list([]), to_linked_list([]), None]
        merged = self.solution.merge_k_sorted_lists(lists)
        self.assertEqual(from_linked_list(merged), [])

    def test_mixed_empty_and_non_empty(self):
        lists = [to_linked_list([]), to_linked_list([1, 2]), None, to_linked_list([0])]
        merged = self.solution.merge_k_sorted_lists(lists)
        self.assertEqual(from_linked_list(merged), [0, 1, 2])


if __name__ == "__main__":
    unittest.main()
