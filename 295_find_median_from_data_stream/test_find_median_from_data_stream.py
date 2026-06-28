import unittest

from find_median_from_data_stream import Solution


class TestMedianFinder(unittest.TestCase):
    def setUp(self):
        self.mf = Solution()

    def test_example(self):
        self.mf.add(1)
        self.mf.add(2)
        self.assertAlmostEqual(self.mf.median(), 1.5)
        self.mf.add(3)
        self.assertAlmostEqual(self.mf.median(), 2.0)

    def test_single_element(self):
        self.mf.add(42)
        self.assertAlmostEqual(self.mf.median(), 42.0)

    def test_two_elements(self):
        self.mf.add(1)
        self.mf.add(3)
        self.assertAlmostEqual(self.mf.median(), 2.0)

    def test_odd_count(self):
        for n in [5, 3, 8, 1, 9]:
            self.mf.add(n)
        self.assertAlmostEqual(self.mf.median(), 5.0)

    def test_even_count(self):
        for n in [5, 3, 8, 1]:
            self.mf.add(n)
        self.assertAlmostEqual(self.mf.median(), 4.0)

    def test_duplicates(self):
        for n in [5, 5, 5, 5]:
            self.mf.add(n)
        self.assertAlmostEqual(self.mf.median(), 5.0)

    def test_negative_numbers(self):
        for n in [-3, -1, -5]:
            self.mf.add(n)
        self.assertAlmostEqual(self.mf.median(), -3.0)

    def test_mixed_sign_numbers(self):
        self.mf.add(-1)
        self.mf.add(1)
        self.assertAlmostEqual(self.mf.median(), 0.0)

    def test_sorted_ascending(self):
        for n in [1, 2, 3, 4, 5]:
            self.mf.add(n)
        self.assertAlmostEqual(self.mf.median(), 3.0)

    def test_sorted_descending(self):
        for n in [5, 4, 3, 2, 1]:
            self.mf.add(n)
        self.assertAlmostEqual(self.mf.median(), 3.0)

    def test_median_after_each_add(self):
        self.mf.add(6)
        self.assertAlmostEqual(self.mf.median(), 6.0)
        self.mf.add(10)
        self.assertAlmostEqual(self.mf.median(), 8.0)
        self.mf.add(2)
        self.assertAlmostEqual(self.mf.median(), 6.0)
        self.mf.add(6)
        self.assertAlmostEqual(self.mf.median(), 6.0)
        self.mf.add(5)
        self.assertAlmostEqual(self.mf.median(), 6.0)
        self.mf.add(0)
        self.assertAlmostEqual(self.mf.median(), 5.5)

    def test_large_values(self):
        self.mf.add(-100000)
        self.mf.add(100000)
        self.assertAlmostEqual(self.mf.median(), 0.0)

    def test_zeros(self):
        for _ in range(4):
            self.mf.add(0)
        self.assertAlmostEqual(self.mf.median(), 0.0)

    def test_all_same_negative(self):
        for _ in range(3):
            self.mf.add(-7)
        self.assertAlmostEqual(self.mf.median(), -7.0)

    def test_many_elements(self):
        for n in range(1, 101):
            self.mf.add(n)
        self.assertAlmostEqual(self.mf.median(), 50.5)


if __name__ == "__main__":
    unittest.main()
