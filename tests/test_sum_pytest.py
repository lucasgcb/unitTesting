import unittest
import context

# pylint: disable=import-error
from mysumpack import sumFunction #This works due to context module import

def test_list_int():
    """
    Test if it can sum a list of integers
    """
    data = [1,2,3]
    result = sumFunction(data)
    assert result == 5, "Should be 5"

def test_sum_tuple():
    data = (1,2,3)
    result = sumFunction(data)
    assert result == 6, "Should be 6"
