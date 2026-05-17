import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.calculator import find_max, add, subtract


def test_find_max_basic():
    assert find_max([1, 5, 3]) == 5


def test_find_max_negative():
    assert find_max([-1, -5, -3]) == -1


def test_find_max_single():
    assert find_max([42]) == 42


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 4) == 6
