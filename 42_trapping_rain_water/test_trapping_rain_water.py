import unittest
from trapping_rain_water import Solution

class TestTrappingRainWater(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        self.assertEqual(self.sol.trapping_rain_water(height), 6)

    def test_example_2(self):
        height = [4, 2, 0, 3, 2, 5]
        self.assertEqual(self.sol.trapping_rain_water(height), 9)

    def test_single_element(self):
        height = [1]
        self.assertEqual(self.sol.trapping_rain_water(height), 0)

    def test_two_elements(self):
        height = [1, 2]
        self.assertEqual(self.sol.trapping_rain_water(height), 0)

    def test_no_trap_ascending(self):
        height = [1, 2, 3, 4, 5]
        self.assertEqual(self.sol.trapping_rain_water(height), 0)

    def test_no_trap_descending(self):
        height = [5, 4, 3, 2, 1]
        self.assertEqual(self.sol.trapping_rain_water(height), 0)

    def test_flat(self):
        height = [2, 2, 2, 2]
        self.assertEqual(self.sol.trapping_rain_water(height), 0)

    def test_simple_trap(self):
        height = [3, 0, 3]
        self.assertEqual(self.sol.trapping_rain_water(height), 3)

    def test_large_trap(self):
        height = [100000, 0, 100000]
        self.assertEqual(self.sol.trapping_rain_water(height), 100000)

    def test_multiple_traps(self):
        height = [3, 0, 2, 0, 4]
        self.assertEqual(self.sol.trapping_rain_water(height), 7)

if __name__ == "__main__":
    unittest.main()
