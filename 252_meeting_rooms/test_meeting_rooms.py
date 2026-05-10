import unittest
from meeting_rooms import Interval, Solution

class TestMeetingRooms(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        intervals = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
        self.assertFalse(self.solution.meeting_rooms(intervals))

    def test_example_2(self):
        intervals = [Interval(5, 8), Interval(9, 15)]
        self.assertTrue(self.solution.meeting_rooms(intervals))

    def test_empty_intervals(self):
        intervals = []
        self.assertTrue(self.solution.meeting_rooms(intervals))

    def test_single_interval(self):
        intervals = [Interval(5, 10)]
        self.assertTrue(self.solution.meeting_rooms(intervals))

    def test_adjacent_intervals(self):
        intervals = [Interval(0, 8), Interval(8, 10)]
        self.assertTrue(self.solution.meeting_rooms(intervals))

    def test_overlapping_intervals_at_boundary(self):
        intervals = [Interval(0, 10), Interval(9, 15)]
        self.assertFalse(self.solution.meeting_rooms(intervals))

    def test_unsorted_intervals_no_conflict(self):
        intervals = [Interval(15, 20), Interval(5, 10), Interval(0, 5)]
        self.assertTrue(self.solution.meeting_rooms(intervals))

    def test_unsorted_intervals_with_conflict(self):
        intervals = [Interval(15, 20), Interval(5, 15), Interval(0, 10)]
        self.assertFalse(self.solution.meeting_rooms(intervals))

if __name__ == "__main__":
    unittest.main()
