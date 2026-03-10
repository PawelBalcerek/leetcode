import unittest
from typing import List, Optional

from reverse_nodes_in_k_groups import ListNode, Solution
from reverse_nodes_in_k_groups_w_stack import Solution as SolutionWStack


def _list_to_linked_list(arr: List[int]) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def _linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


class TestReverseNodesInKGroups(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.solution_w_stack = SolutionWStack()

    def test_example_1(self):
        self._test_all_solutions([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5])

    def test_example_2(self):
        self._test_all_solutions([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5])

    def test_k_equals_one(self):
        self._test_all_solutions([1, 2, 3], 1, [1, 2, 3])

    def test_k_equals_n(self):
        self._test_all_solutions([1, 2, 3, 4], 4, [4, 3, 2, 1])

    def test_n_multiple_of_k(self):
        self._test_all_solutions([1, 2, 3, 4, 5, 6], 2, [2, 1, 4, 3, 6, 5])

    def test_empty_list(self):
        self._test_all_solutions([], 3, [])

    def _test_all_solutions(self, arr: list[int], k: int, expected: list[int]):
        self.assertEqual(
            _linked_list_to_list(
                self.solution.reverse_nodes_in_k_groups(_list_to_linked_list(arr), k)
            ),
            expected,
        )
        self.assertEqual(
            _linked_list_to_list(
                self.solution_w_stack.reverse_nodes_in_k_groups_w_stack(
                    _list_to_linked_list(arr), k
                )
            ),
            expected,
        )


if __name__ == "__main__":
    unittest.main()
