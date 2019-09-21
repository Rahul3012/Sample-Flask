'''
This test file check whether find_Capital return valid and correct output not
'''
import unittest
import json
from country import find_Capital

'''Variable to store requested result '''
expected=''

''' class TestResult of test cases '''
class TestResult(unittest.TestCase):
    ''' Test Valid capital resturns or not '''
    def testCorrectOutput(self):
        expected=find_Capital("India")
        self.assertEqual(expected,"New Delhi")

    ''' check for null outputs means capital is not found '''
    def testNoneOutput(self):
        expected=find_Capital("United")
        self.assertIsNone(expected,msg=None)

if __name__ == '__main__':
    unittest.main()
