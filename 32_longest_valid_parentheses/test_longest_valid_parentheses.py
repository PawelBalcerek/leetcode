import pytest
from longest_valid_parentheses import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example1(solution):
    assert solution.longest_valid_parentheses("(()") == 2


def test_example2(solution):
    assert solution.longest_valid_parentheses(")()())") == 4


def test_example3_empty(solution):
    assert solution.longest_valid_parentheses("") == 0


def test_no_valid_parentheses(solution):
    assert solution.longest_valid_parentheses("((((") == 0


def test_all_closing(solution):
    assert solution.longest_valid_parentheses("))))") == 0


def test_single_pair(solution):
    assert solution.longest_valid_parentheses("()") == 2


def test_nested(solution):
    assert solution.longest_valid_parentheses("(())") == 4


def test_multiple_groups(solution):
    assert solution.longest_valid_parentheses("()()") == 4


def test_longer_sequence(solution):
    assert solution.longest_valid_parentheses("()(()") == 2


def test_complex(solution):
    assert solution.longest_valid_parentheses("()(())") == 6


def test_leading_invalid(solution):
    assert solution.longest_valid_parentheses("))()") == 2


def test_surrounded_by_invalid(solution):
    assert solution.longest_valid_parentheses("))(()()))(") == 6
