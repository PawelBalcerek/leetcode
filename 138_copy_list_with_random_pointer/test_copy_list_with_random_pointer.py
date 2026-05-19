import unittest
from copy_list_with_random_pointer import Node, Solution


class TestCopyListWithRandomPointer(unittest.TestCase):
    def from_list(self, data):
        if not data:
            return None
        nodes = [Node(val) for val, _ in data]
        for i, (_, random_idx) in enumerate(data):
            if i < len(nodes) - 1:
                nodes[i].next = nodes[i + 1]
            if random_idx is not None:
                nodes[i].random = nodes[random_idx]
        return nodes[0]

    def to_list(self, head):
        if not head:
            return []
        nodes = []
        curr = head
        node_to_idx = {}
        idx = 0
        while curr:
            nodes.append(curr)
            node_to_idx[curr] = idx
            curr = curr.next
            idx += 1

        res = []
        for node in nodes:
            random_idx = node_to_idx.get(node.random) if node.random else None
            res.append([node.val, random_idx])
        return res

    def is_deep_copy(self, original, copy):
        if not original and not copy:
            return True
        if not original or not copy:
            return False

        orig_nodes = []
        curr = original
        while curr:
            orig_nodes.append(curr)
            curr = curr.next

        copy_nodes = []
        curr = copy
        while curr:
            copy_nodes.append(curr)
            curr = curr.next

        if len(orig_nodes) != len(copy_nodes):
            return False

        for o, c in zip(orig_nodes, copy_nodes):
            if o is c:
                return False
            if o.val != c.val:
                return False
            if c.random and c.random in orig_nodes:
                return False
        return True

    def test_example_1(self):
        data = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
        head = self.from_list(data)
        solution = Solution()
        copy = solution.copy_list_with_random_pointer(head)

        self.assertEqual(self.to_list(copy), data)
        self.assertTrue(self.is_deep_copy(head, copy))

    def test_example_2(self):
        data = [[1, 1], [2, 1]]
        head = self.from_list(data)
        solution = Solution()
        copy = solution.copy_list_with_random_pointer(head)

        self.assertEqual(self.to_list(copy), data)
        self.assertTrue(self.is_deep_copy(head, copy))

    def test_example_3(self):
        data = [[3, None], [3, 0], [3, None]]
        head = self.from_list(data)
        solution = Solution()
        copy = solution.copy_list_with_random_pointer(head)

        self.assertEqual(self.to_list(copy), data)
        self.assertTrue(self.is_deep_copy(head, copy))

    def test_empty_list(self):
        head = None
        solution = Solution()
        copy = solution.copy_list_with_random_pointer(head)

        self.assertIsNone(copy)

    def test_single_node(self):
        data = [[1, 0]]
        head = self.from_list(data)
        solution = Solution()
        copy = solution.copy_list_with_random_pointer(head)

        self.assertEqual(self.to_list(copy), data)
        self.assertTrue(self.is_deep_copy(head, copy))

    def test_no_random_pointers(self):
        data = [[1, None], [2, None], [3, None]]
        head = self.from_list(data)
        solution = Solution()
        copy = solution.copy_list_with_random_pointer(head)

        self.assertEqual(self.to_list(copy), data)
        self.assertTrue(self.is_deep_copy(head, copy))


if __name__ == "__main__":
    unittest.main()
