import unittest
from binary_search import Solution

class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_found_middle(self):
        self.assertEqual(self.sol.binary_search([1, 2, 3, 4, 5], 3), 2)

    def test_found_start(self):
        self.assertEqual(self.sol.binary_search([1, 2, 3, 4, 5], 1), 0)

    def test_found_end(self):
        self.assertEqual(self.sol.binary_search([1, 2, 3, 4, 5], 5), 4)

    def test_not_found(self):
        self.assertIsNone(self.sol.binary_search([1, 2, 3, 4, 5], 6))
        self.assertIsNone(self.sol.binary_search([1, 2, 3, 4, 5], 0))

    def test_empty_list(self):
        self.assertIsNone(self.sol.binary_search([], 3))

    def test_single_element_found(self):
        self.assertEqual(self.sol.binary_search([3], 3), 0)

    def test_single_element_not_found(self):
        self.assertIsNone(self.sol.binary_search([3], 1))

if __name__ == "__main__":
    unittest.main()
