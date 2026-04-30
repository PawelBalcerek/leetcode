import unittest
from min_stack import MinStack

class TestMinStack(unittest.TestCase):
    def test_example(self):
        min_stack = MinStack()
        min_stack.push(-2)
        min_stack.push(0)
        min_stack.push(-3)
        self.assertEqual(min_stack.getMin(), -3)
        min_stack.pop()
        self.assertEqual(min_stack.top(), 0)
        self.assertEqual(min_stack.getMin(), -2)

    def test_increasing_order(self):
        min_stack = MinStack()
        min_stack.push(1)
        self.assertEqual(min_stack.getMin(), 1)
        min_stack.push(2)
        self.assertEqual(min_stack.getMin(), 1)
        min_stack.push(3)
        self.assertEqual(min_stack.getMin(), 1)
        min_stack.pop()
        self.assertEqual(min_stack.getMin(), 1)
        min_stack.pop()
        self.assertEqual(min_stack.getMin(), 1)

    def test_decreasing_order(self):
        min_stack = MinStack()
        min_stack.push(3)
        self.assertEqual(min_stack.getMin(), 3)
        min_stack.push(2)
        self.assertEqual(min_stack.getMin(), 2)
        min_stack.push(1)
        self.assertEqual(min_stack.getMin(), 1)
        min_stack.pop()
        self.assertEqual(min_stack.getMin(), 2)
        min_stack.pop()
        self.assertEqual(min_stack.getMin(), 3)

    def test_duplicate_min(self):
        min_stack = MinStack()
        min_stack.push(2)
        min_stack.push(1)
        min_stack.push(1)
        self.assertEqual(min_stack.getMin(), 1)
        min_stack.pop()
        self.assertEqual(min_stack.getMin(), 1)
        min_stack.pop()
        self.assertEqual(min_stack.getMin(), 2)

    def test_large_values(self):
        min_stack = MinStack()
        min_stack.push(2**31 - 1)
        self.assertEqual(min_stack.getMin(), 2**31 - 1)
        min_stack.push(-(2**31))
        self.assertEqual(min_stack.getMin(), -(2**31))
        self.assertEqual(min_stack.top(), -(2**31))
        min_stack.pop()
        self.assertEqual(min_stack.getMin(), 2**31 - 1)

if __name__ == "__main__":
    unittest.main()
