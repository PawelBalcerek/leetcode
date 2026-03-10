import pytest

from search_in_rotated_sorted_array import Solution


@pytest.fixture
def solution():
    return Solution()


# Examples from problem statement
def test_example1(solution):
    assert solution.search_in_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 0) == 4


def test_example2(solution):
    assert solution.search_in_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 3) == -1


def test_example3(solution):
    assert solution.search_in_rotated_sorted_array([1], 0) == -1


# Single element
def test_single_element_found(solution):
    assert solution.search_in_rotated_sorted_array([5], 5) == 0


def test_single_element_not_found(solution):
    assert solution.search_in_rotated_sorted_array([5], 3) == -1


# No rotation (sorted array)
def test_no_rotation_target_found(solution):
    assert solution.search_in_rotated_sorted_array([1, 2, 3, 4, 5], 3) == 2


def test_no_rotation_target_not_found(solution):
    assert solution.search_in_rotated_sorted_array([1, 2, 3, 4, 5], 6) == -1


# Rotation variants
def test_rotated_target_in_left_half(solution):
    assert solution.search_in_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 6) == 2


def test_rotated_target_in_right_half(solution):
    assert solution.search_in_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 1) == 5


def test_rotated_target_at_pivot(solution):
    assert solution.search_in_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 4) == 0


def test_rotated_target_at_last(solution):
    assert solution.search_in_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 2) == 6


# Boundary values
def test_target_at_first_index(solution):
    assert solution.search_in_rotated_sorted_array([3, 4, 5, 1, 2], 3) == 0


def test_target_at_last_index(solution):
    assert solution.search_in_rotated_sorted_array([3, 4, 5, 1, 2], 2) == 4


def test_target_below_min(solution):
    assert solution.search_in_rotated_sorted_array([3, 4, 5, 1, 2], 0) == -1


def test_target_above_max(solution):
    assert solution.search_in_rotated_sorted_array([3, 4, 5, 1, 2], 6) == -1


# Negative numbers
def test_negative_numbers_found(solution):
    assert solution.search_in_rotated_sorted_array([-3, -1, 0, 2, -5], -1) == 1


def test_negative_numbers_not_found(solution):
    assert solution.search_in_rotated_sorted_array([-3, -1, 0, 2, -5], -4) == -1


# Two elements
def test_two_elements_found_first(solution):
    assert solution.search_in_rotated_sorted_array([2, 1], 2) == 0


def test_two_elements_found_second(solution):
    assert solution.search_in_rotated_sorted_array([2, 1], 1) == 1


def test_two_elements_not_found(solution):
    assert solution.search_in_rotated_sorted_array([2, 1], 3) == -1
