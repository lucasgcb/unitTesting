import unittest
import context

# pylint: disable=import-error
from mydivpack import divFunction #This works due to context module import
def test_div_int():
    """
    #Test if it can div a list of integers
    """
    data = [1,2,3]
    result = divFunction(data)
    assert result == 1.5, "Should be 1.5"

def test_div_tuple():
    data = (1,2,3)
    result = divFunction(data)
    assert result == 1.5, "Should be 1.5"