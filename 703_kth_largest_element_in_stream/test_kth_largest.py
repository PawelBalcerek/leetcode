import unittest
from kth_largest import KthLargest

class TestKthLargest(unittest.TestCase):
    def test_example_1(self):
        kthLargest = KthLargest(3, [4, 5, 8, 2])
        self.assertEqual(kthLargest.add(3), 4)
        self.assertEqual(kthLargest.add(5), 5)
        self.assertEqual(kthLargest.add(10), 5)
        self.assertEqual(kthLargest.add(9), 8)
        self.assertEqual(kthLargest.add(4), 8)

    def test_example_2(self):
        kthLargest = KthLargest(4, [7, 7, 7, 7, 8, 3])
        self.assertEqual(kthLargest.add(2), 7)
        self.assertEqual(kthLargest.add(10), 7)
        self.assertEqual(kthLargest.add(9), 7)
        self.assertEqual(kthLargest.add(9), 8)

    def test_empty_initial_nums(self):
        kthLargest = KthLargest(1, [])
        self.assertEqual(kthLargest.add(-3), -3)
        self.assertEqual(kthLargest.add(-2), -2)
        self.assertEqual(kthLargest.add(-4), -2)
        self.assertEqual(kthLargest.add(0), 0)

    def test_k_equals_length_plus_one(self):
        kthLargest = KthLargest(3, [1, 2])
        self.assertEqual(kthLargest.add(3), 1)
        self.assertEqual(kthLargest.add(4), 2)

    def test_all_same_elements(self):
        kthLargest = KthLargest(2, [5, 5, 5])
        self.assertEqual(kthLargest.add(5), 5)
        self.assertEqual(kthLargest.add(5), 5)

if __name__ == "__main__":
    unittest.main()
