import unittest
import context

# pylint: disable=import-error
import mysumpack #This works due to context module import

##PyTest free alternative

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test if it can sum a list of integers
        """
        data = [1,2,3]
        result = mysumpack.sums.sumFunction(data)
        self.assertEqual(result,6, "Should be 6")

##Check if this is the file being run
if __name__ == '__main__':
    unittest.main()