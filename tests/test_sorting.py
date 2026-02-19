import pytest

from src.sorting import insertion_sort

def test_insertion_sort_basic():
    sample_list = [20,10]
    expected_result = [10,20]
    assert insertion_sort(sample_list) == expected_result
