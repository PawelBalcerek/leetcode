import copy
import random
import unittest

from pacific_atlantic_water_flow import Solution


def brute_force(heights):
    rows, cols = len(heights), len(heights[0])
    result = []
    for sr in range(rows):
        for sc in range(cols):
            pacific = atlantic = False
            seen = {(sr, sc)}
            stack = [(sr, sc)]
            while stack:
                r, c = stack.pop()
                if r == 0 or c == 0:
                    pacific = True
                if r == rows - 1 or c == cols - 1:
                    atlantic = True
                for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and (nr, nc) not in seen
                        and heights[nr][nc] <= heights[r][c]
                    ):
                        seen.add((nr, nc))
                        stack.append((nr, nc))
            if pacific and atlantic:
                result.append([sr, sc])
    return result


class TestPacificAtlanticWaterFlow(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def run_case(self, heights):
        return sorted(self.solution.pacific_atlantic_water_flow(heights))

    def all_cells(self, rows, cols):
        return [[r, c] for r in range(rows) for c in range(cols)]

    def test_example_one(self):
        heights = [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4],
        ]
        expected = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
        self.assertEqual(self.run_case(heights), expected)

    def test_example_two(self):
        self.assertEqual(self.run_case([[1]]), [[0, 0]])

    def test_single_cell_zero(self):
        self.assertEqual(self.run_case([[0]]), [[0, 0]])

    def test_single_row(self):
        heights = [[5, 1, 9, 2, 7]]
        self.assertEqual(self.run_case(heights), self.all_cells(1, 5))

    def test_single_column(self):
        heights = [[3], [8], [1], [6]]
        self.assertEqual(self.run_case(heights), self.all_cells(4, 1))

    def test_all_equal_heights(self):
        heights = [[7] * 4 for _ in range(3)]
        self.assertEqual(self.run_case(heights), self.all_cells(3, 4))

    def test_all_zero_heights(self):
        heights = [[0] * 3 for _ in range(3)]
        self.assertEqual(self.run_case(heights), self.all_cells(3, 3))

    def test_increasing_towards_bottom_right(self):
        heights = [[1, 2], [3, 4]]
        self.assertEqual(self.run_case(heights), [[0, 1], [1, 0], [1, 1]])

    def test_decreasing_towards_bottom_right(self):
        heights = [[4, 3], [2, 1]]
        self.assertEqual(self.run_case(heights), [[0, 0], [0, 1], [1, 0]])

    def test_center_peak(self):
        heights = [[1, 1, 1], [1, 5, 1], [1, 1, 1]]
        self.assertEqual(self.run_case(heights), self.all_cells(3, 3))

    def test_center_valley(self):
        heights = [[5, 5, 5], [5, 1, 5], [5, 5, 5]]
        expected = [cell for cell in self.all_cells(3, 3) if cell != [1, 1]]
        self.assertEqual(self.run_case(heights), expected)

    def test_strictly_increasing_rows(self):
        heights = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [[0, 2], [1, 2], [2, 0], [2, 1], [2, 2]]
        self.assertEqual(self.run_case(heights), expected)

    def test_wall_blocks_atlantic(self):
        heights = [[1, 1, 9], [1, 1, 9], [9, 9, 9]]
        expected = [[0, 2], [1, 2], [2, 0], [2, 1], [2, 2]]
        self.assertEqual(self.run_case(heights), expected)

    def test_max_heights(self):
        heights = [[100000, 0], [0, 100000]]
        expected = [[0, 0], [0, 1], [1, 0], [1, 1]]
        self.assertEqual(self.run_case(heights), expected)

    def test_result_format_and_no_duplicates(self):
        heights = [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4],
        ]
        result = self.solution.pacific_atlantic_water_flow(heights)
        self.assertIsInstance(result, list)
        for cell in result:
            self.assertIsInstance(cell, list)
            self.assertEqual(len(cell), 2)
        self.assertEqual(len(result), len({tuple(cell) for cell in result}))

    def test_input_not_mutated(self):
        heights = [[3, 1, 4], [1, 5, 9], [2, 6, 5]]
        original = copy.deepcopy(heights)
        self.solution.pacific_atlantic_water_flow(heights)
        self.assertEqual(heights, original)

    def test_random_against_brute_force(self):
        rng = random.Random(417)
        for _ in range(200):
            rows = rng.randint(1, 8)
            cols = rng.randint(1, 8)
            max_height = rng.choice([1, 3, 10, 100000])
            heights = [
                [rng.randint(0, max_height) for _ in range(cols)] for _ in range(rows)
            ]
            self.assertEqual(self.run_case(heights), sorted(brute_force(heights)))

    def test_large_uniform_grid(self):
        heights = [[1] * 200 for _ in range(200)]
        self.assertEqual(len(self.solution.pacific_atlantic_water_flow(heights)), 40000)

    def test_large_increasing_grid(self):
        heights = [[r + c for c in range(200)] for r in range(200)]
        result = self.run_case(heights)
        expected = sorted(
            [[r, 199] for r in range(200)] + [[199, c] for c in range(199)]
        )
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
