import unittest

from lru_cache import LRUCache


class TestLRUCache(unittest.TestCase):
    def test_example_1(self):
        lRUCache = LRUCache(2)
        lRUCache.put(1, 1)
        lRUCache.put(2, 2)
        self.assertEqual(lRUCache.get(1), 1)
        lRUCache.put(3, 3)
        self.assertEqual(lRUCache.get(2), -1)
        lRUCache.put(4, 4)
        self.assertEqual(lRUCache.get(1), -1)
        self.assertEqual(lRUCache.get(3), 3)
        self.assertEqual(lRUCache.get(4), 4)

    def test_capacity_1(self):
        cache = LRUCache(1)
        cache.put(1, 1)
        self.assertEqual(cache.get(1), 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(2), 2)

    def test_update_existing_key(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(1, 10)
        self.assertEqual(cache.get(1), 10)
        cache.put(3, 3)
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(1), 10)
        self.assertEqual(cache.get(3), 3)

    def test_get_non_existent(self):
        cache = LRUCache(2)
        self.assertEqual(cache.get(1), -1)

    def test_put_at_capacity(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(3, 3)
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(2), 2)
        self.assertEqual(cache.get(3), 3)

    def test_complex_access(self):
        cache = LRUCache(3)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(3, 3)
        cache.get(1)
        cache.put(4, 4)
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(3), 3)
        cache.put(5, 5)
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)
        self.assertEqual(cache.get(5), 5)


if __name__ == "__main__":
    unittest.main()
