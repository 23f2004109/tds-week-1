import pytest
from streak import longest_positive_streak

def test_empty_list():
    assert longest_positive_streak([]) == 0

def test_no_positive_numbers():
    assert longest_positive_streak([-1, -2, 0, -5]) == 0

def test_single_streak():
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_multiple_streaks_longest_first():
    assert longest_positive_streak([1, 2, 3, -1, 1, 2]) == 3

def test_multiple_streaks_longest_last():
    assert longest_positive_streak([1, 2, -1, 1, 2, 3]) == 3

def test_streaks_with_zeros():
    assert longest_positive_streak([1, 2, 0, 1, 2, 3]) == 3

def test_all_ones():
    assert longest_positive_streak([1, 1, 1]) == 3

def test_example_from_prompt():
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3
