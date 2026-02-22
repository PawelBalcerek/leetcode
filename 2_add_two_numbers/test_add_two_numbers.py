import unittest
from typing import List, Optional
from add_two_numbers import ListNode, Solution

class TestAddTwoNumbers(unittest.TestCase):
    def list_to_linked_list(self, nums: List[int]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        for num in nums:
            curr.next = ListNode(num)
            curr = curr.next
        return dummy.next

    def linked_list_to_list(self, head: Optional[ListNode]) -> List[int]:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res

    def test_standard_addition(self):
        sol = Solution()
        l1 = self.list_to_linked_list([2, 4, 3])
        l2 = self.list_to_linked_list([5, 6, 4])
        result = sol.add_two_numbers(l1, l2)
        self.assertEqual(self.linked_list_to_list(result), [7, 0, 8])

    def test_zeros(self):
        sol = Solution()
        l1 = self.list_to_linked_list([0])
        l2 = self.list_to_linked_list([0])
        result = sol.add_two_numbers(l1, l2)
        self.assertEqual(self.linked_list_to_list(result), [0])

    def test_different_lengths(self):
        sol = Solution()
        l1 = self.list_to_linked_list([9, 9, 9, 9, 9, 9, 9])
        l2 = self.list_to_linked_list([9, 9, 9, 9])
        result = sol.add_two_numbers(l1, l2)
        self.assertEqual(self.linked_list_to_list(result), [8, 9, 9, 9, 0, 0, 0, 1])

    def test_single_carry(self):
        sol = Solution()
        l1 = self.list_to_linked_list([5])
        l2 = self.list_to_linked_list([5])
        result = sol.add_two_numbers(l1, l2)
        self.assertEqual(self.linked_list_to_list(result), [0, 1])

    def test_carry_at_end_different_length(self):
        sol = Solution()
        l1 = self.list_to_linked_list([9, 9])
        l2 = self.list_to_linked_list([1])
        result = sol.add_two_numbers(l1, l2)
        self.assertEqual(self.linked_list_to_list(result), [0, 0, 1])

    def test_large_numbers(self):
        sol = Solution()
        num1 = [1] + [0] * 30 + [1]
        num2 = [5, 6, 4]
        l1 = self.list_to_linked_list(num1)
        l2 = self.list_to_linked_list(num2)
        result = sol.add_two_numbers(l1, l2)
        expected = [6, 6, 4] + [0] * 28 + [1]
        self.assertEqual(self.linked_list_to_list(result), expected)

if __name__ == '__main__':
    unittest.main()
