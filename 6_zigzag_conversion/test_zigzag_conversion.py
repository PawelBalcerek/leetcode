import unittest

from zigzag_conversion import Solution


class TestZigzagConversion(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s = "PAYPALISHIRING"
        num_rows = 3
        expected = "PAHNAPLSIIGYIR"
        self.assertEqual(self.solution.zigzag_conversion(s, num_rows), expected)

    def test_example_2(self):
        s = "PAYPALISHIRING"
        num_rows = 4
        expected = "PINALSIGYAHRPI"
        self.assertEqual(self.solution.zigzag_conversion(s, num_rows), expected)

    def test_example_3(self):
        s = "A"
        num_rows = 1
        expected = "A"
        self.assertEqual(self.solution.zigzag_conversion(s, num_rows), expected)

    def test_single_row(self):
        s = "ABC"
        num_rows = 1
        expected = "ABC"
        self.assertEqual(self.solution.zigzag_conversion(s, num_rows), expected)

    def test_num_rows_greater_than_length(self):
        s = "ABC"
        num_rows = 5
        expected = "ABC"
        self.assertEqual(self.solution.zigzag_conversion(s, num_rows), expected)

    def test_two_rows(self):
        s = "ABCD"
        num_rows = 2
        # A C
        # B D
        expected = "ACBD"
        self.assertEqual(self.solution.zigzag_conversion(s, num_rows), expected)


if __name__ == "__main__":
    unittest.main()
