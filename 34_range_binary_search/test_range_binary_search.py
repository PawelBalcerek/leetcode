import pytest
from range_binary_search import Solution


@pytest.fixture
def solution():
    return Solution()


def test_target_with_multiple_occurrences(solution):
    assert solution.range_binary_search([5, 7, 7, 8, 8, 10], 8) == [3, 4]


def test_target_not_found(solution):
    assert solution.range_binary_search([5, 7, 7, 8, 8, 10], 6) == [-1, -1]


def test_empty_array(solution):
    assert solution.range_binary_search([], 0) == [-1, -1]


def test_single_occurrence(solution):
    assert solution.range_binary_search([5, 7, 7, 8, 8, 10], 10) == [5, 5]


def test_all_elements_are_target(solution):
    assert solution.range_binary_search([3, 3, 3, 3], 3) == [0, 3]


def test_single_element_matches(solution):
    assert solution.range_binary_search([5], 5) == [0, 0]


def test_single_element_no_match(solution):
    assert solution.range_binary_search([5], 3) == [-1, -1]


def test_target_at_start(solution):
    assert solution.range_binary_search([1, 1, 2, 3], 1) == [0, 1]


def test_target_at_end(solution):
    assert solution.range_binary_search([1, 2, 3, 3], 3) == [2, 3]


def test_negative_target(solution):
    assert solution.range_binary_search([-5, -3, -3, 0, 1], -3) == [1, 2]


def test_target_below_min(solution):
    assert solution.range_binary_search([1, 2, 3], -1) == [-1, -1]


def test_target_above_max(solution):
    assert solution.range_binary_search([1, 2, 3], 100) == [-1, -1]
