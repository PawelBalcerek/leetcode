import unittest
from typing import List, Optional
from linked_list_cycle import ListNode, Solution

class TestLinkedListCycle(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def create_linked_list(self, values: List[int], pos: int) -> Optional[ListNode]:
        if not values:
            return None
        
        nodes = [ListNode(val) for val in values]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        
        if pos != -1:
            nodes[-1].next = nodes[pos]
        
        return nodes[0]

    def test_example_1(self):
        head = self.create_linked_list([3, 2, 0, -4], 1)
        self.assertTrue(self.solution.linked_list_cycle(head))

    def test_example_2(self):
        head = self.create_linked_list([1, 2], 0)
        self.assertTrue(self.solution.linked_list_cycle(head))

    def test_example_3(self):
        head = self.create_linked_list([1], -1)
        self.assertFalse(self.solution.linked_list_cycle(head))

    def test_empty_list(self):
        head = self.create_linked_list([], -1)
        self.assertFalse(self.solution.linked_list_cycle(head))

    def test_no_cycle_multiple_nodes(self):
        head = self.create_linked_list([1, 2, 3, 4, 5], -1)
        self.assertFalse(self.solution.linked_list_cycle(head))

    def test_cycle_at_end_to_self(self):
        head = self.create_linked_list([1, 2, 3], 2)
        self.assertTrue(self.solution.linked_list_cycle(head))

if __name__ == '__main__':
    unittest.main()
