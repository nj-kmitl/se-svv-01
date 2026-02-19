import pytest

from src.binsearch import binary_search

def test_binary_search_basic():
    sample_list = [10,20,30,40,50]
    assert binary_search(sample_list, 10) == 0
