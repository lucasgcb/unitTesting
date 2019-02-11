## Using the unittest runner:
## >Put tests as methods inside of classes
## >Use a special series of assertion methods in the unittest,
## >they are called unittest.TestCase
## Converting previous test, test2.py, to the runner:

import unittest

class TestSum(unittest.TestCase):

    def test_sum(self):
        """
        This is the sum unit test for lists.
        it runs an assertEqual statement.
        Return an AssertError + string message if false.

        format:

        assert bool, string
        """

        self.assertEqual(sum([1,2,3]),6, "Should be 6")

    def test_sum_tuple(self):
        """
        This is the sum unit test for tuples.
        it runs an assertEqual statement.
        Return an AssertError + string message if false.

        format:

        assert bool, string
        """
        self.assertEqual(sum([1,2,2]), 6, "Should be 6")

## Now we check if it is the source file is the main one being run, 
## we can check this because the interpreter would assign the 
## __main__ string to the global __name__ variable like such.
##
## If it was running off an imported module, 
## it will have its filename minus the file extension.

if __name__ == "__main__": 
    unittest.main()
    print("Everything passed")
