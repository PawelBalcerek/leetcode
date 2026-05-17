import unittest
from time_based_key_value_store import TimeBasedKeyValueStore

class TestTimeBasedKeyValueStore(unittest.TestCase):
    def setUp(self):
        self.time_map = TimeBasedKeyValueStore()

    def test_example_1(self):
        self.time_map.set("foo", "bar", 1)
        self.assertEqual(self.time_map.get("foo", 1), "bar")
        self.assertEqual(self.time_map.get("foo", 3), "bar")
        self.time_map.set("foo", "bar2", 4)
        self.assertEqual(self.time_map.get("foo", 4), "bar2")
        self.assertEqual(self.time_map.get("foo", 5), "bar2")

    def test_get_non_existent_key(self):
        self.assertEqual(self.time_map.get("non_existent", 1), "")

    def test_get_before_first_timestamp(self):
        self.time_map.set("foo", "bar", 10)
        self.assertEqual(self.time_map.get("foo", 5), "")

    def test_get_exact_timestamp(self):
        self.time_map.set("foo", "v1", 10)
        self.time_map.set("foo", "v2", 20)
        self.assertEqual(self.time_map.get("foo", 10), "v1")
        self.assertEqual(self.time_map.get("foo", 20), "v2")

    def test_get_between_timestamps(self):
        self.time_map.set("foo", "v1", 10)
        self.time_map.set("foo", "v2", 20)
        self.assertEqual(self.time_map.get("foo", 15), "v1")

    def test_multiple_keys(self):
        self.time_map.set("k1", "v1", 1)
        self.time_map.set("k2", "v2", 2)
        self.assertEqual(self.time_map.get("k1", 2), "v1")
        self.assertEqual(self.time_map.get("k2", 2), "v2")
        self.assertEqual(self.time_map.get("k1", 0), "")

if __name__ == '__main__':
    unittest.main()
