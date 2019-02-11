def test_sum():
    """
    This is the sum unit test for lists.
    it runs an assert statement which takes no parenthesis
    and evaluates if it is true or false. 
    > Requires debug mode. Ommit -O from start up to enter it.

    
    
    Return an AssertError + string message if false.

    format:

    assert bool, string
    """
    assert sum([1,2,3]) == 6, "Should be 6" 

def test_sum_tuple():
    """
    This is the sum unit test for tuples.
    it runs an assert statement which takes no parenthesis
    and evaluates if it is true or false. 
    > Requires debug mode. Ommit -O from start up to enter it.

    
    
    Return an AssertError + string message if false.

    format:

    assert bool, string
    """
    assert sum((1,2,2)) == 6, "Should be 6" 

## Now we check if it is the source file is the main one being run, 
## we can check this because the interpreter would assign the 
## __main__ string to the global __name__ variable like such.
##
## If it was running off an imported module, 
## it will have its filename minus the file extension.

if __name__ == "__main__": 
    test_sum()
    test_sum_tuple()
    print("Everything passed")
