import unittest
import importlib.util
import sys
import os

# Helper to import the module since it starts with a number
def import_module_from_path(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

current_dir = os.path.dirname(os.path.abspath(__file__))
module_path = os.path.join(current_dir, "14_longest_common_prefix.py")
solution_module = import_module_from_path("problem_14", module_path)

class TestLongestCommonPrefix(unittest.TestCase):
    def setUp(self):
        self.solution = solution_module.Solution()

    def test_common_prefix_exists(self):
        self.assertEqual(self.solution.longest_common_prefix(["flower", "flow", "flight"]), "fl")

    def test_no_common_prefix(self):
        self.assertEqual(self.solution.longest_common_prefix(["dog", "racecar", "car"]), "")

    def test_all_empty_strings(self):
        self.assertEqual(self.solution.longest_common_prefix(["", "", ""]), "")

    def test_some_empty_strings(self):
        self.assertEqual(self.solution.longest_common_prefix(["a", ""]), "")

    def test_single_string(self):
        self.assertEqual(self.solution.longest_common_prefix(["hello"]), "hello")

    def test_identical_strings(self):
        self.assertEqual(self.solution.longest_common_prefix(["test", "test", "test"]), "test")

    def test_prefix_is_entire_string(self):
        self.assertEqual(self.solution.longest_common_prefix(["ab", "abc", "abcd"]), "ab")

if __name__ == '__main__':
    unittest.main()
