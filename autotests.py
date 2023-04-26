import pytest


def my_max(*args):
    max_arg = args[0]
    for arg in args:
        if arg > max_arg:
            max_arg = arg

    return max_arg


def test_my_max():
    assert my_max(2) == 2
    assert my_max(2, -3) == 3
    assert my_max(2, -3, 4) == 4
    assert my_max(2, -3, 5, 0) == 5
    assert my_max(-2, -3, -5, -10) == -2
    assert my_max(-2.5, 3.2, -5.45, 10.123) == 10.123
