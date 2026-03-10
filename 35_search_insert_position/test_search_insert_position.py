import pytest
from search_insert_position import Solution


@pytest.fixture
def solution():
    return Solution()


# Target found in array
def test_target_found_middle(solution):
    assert solution.search_insert_position([1, 3, 5, 6], 5) == 2

def test_target_found_first(solution):
    assert solution.search_insert_position([1, 3, 5, 6], 1) == 0

def test_target_found_last(solution):
    assert solution.search_insert_position([1, 3, 5, 6], 6) == 3

def test_target_found_single_element(solution):
    assert solution.search_insert_position([5], 5) == 0


# Target not found — insert position
def test_insert_between_elements(solution):
    assert solution.search_insert_position([1, 3, 5, 6], 2) == 1

def test_insert_at_end(solution):
    assert solution.search_insert_position([1, 3, 5, 6], 7) == 4

def test_insert_at_beginning(solution):
    assert solution.search_insert_position([1, 3, 5, 6], 0) == 0

def test_insert_single_element_before(solution):
    assert solution.search_insert_position([5], 3) == 0

def test_insert_single_element_after(solution):
    assert solution.search_insert_position([5], 7) == 1


# Negative numbers
def test_negative_numbers_target_found(solution):
    assert solution.search_insert_position([-10, -5, 0, 3], -5) == 1

def test_negative_numbers_insert(solution):
    assert solution.search_insert_position([-10, -5, 0, 3], -7) == 1

def test_all_negative_insert_at_end(solution):
    assert solution.search_insert_position([-5, -3, -1], 0) == 3


# Boundary values per constraints
def test_min_constraint_value(solution):
    assert solution.search_insert_position([-10000, 0, 10000], -10000) == 0

def test_max_constraint_value(solution):
    assert solution.search_insert_position([-10000, 0, 10000], 10000) == 2

def test_target_beyond_max_constraint(solution):
    assert solution.search_insert_position([-10000, 0, 9999], 10000) == 3
