import unittest
from .contains_duplicate import Solution

class TestContainsDuplicate(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_has_duplicate_with_duplicates(self):
        self.assertTrue(self.solution.has_duplicate([1, 2, 3, 3]))

    def test_has_duplicate_without_duplicates(self):
        self.assertFalse(self.solution.has_duplicate([1, 2, 3, 4]))

    def test_has_duplicate_empty_list(self):
        self.assertFalse(self.solution.has_duplicate([]))

    def test_has_duplicate_single_element(self):
        self.assertFalse(self.solution.has_duplicate([1]))

    def test_has_duplicate_multiple_duplicates(self):
        self.assertTrue(self.solution.has_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))

if __name__ == "__main__":
    unittest.main()
