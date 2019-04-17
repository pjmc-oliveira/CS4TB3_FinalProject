# Python test set -- part 1, grammar.
# This just tests whether the parser accepts them all.

# NOTE: When you run this test as a script from the command line, you
# get warnings about certain hex/oct constants.  Since those are
# issued by the parser, you can't suppress them by adding a
# filterwarnings() call to this module.  Therefore, to shut up the
# regression test, the filterwarnings() call has been added to
# regrtest.py.

from test.support import run_unittest, check_syntax_error
import unittest
import sys
# testing import *
from sys import *

    #until_stmt: 'until' test ':' suite ['else' ':' suite]
class UntilTests(unittest.TestCase):

    def testFalseUntilStatment(self):
        x = 0 
        until x == 2:
            x += 1 
        self.assertEqual(x, 2)

    def testTrueUntilStatment(self):
        x = 2 
        until x == 2:
            x += 1 
        self.assertEqual(x, 2)

#unless_stmt: 'unless' test ':' suite ['else' ':' suite]
class UnlessTests(unittest.TestCase):

    def testFalseUnlessTests(self):
        x = 2
        unless x == 2:
            x -= 1
        else:
            x += 1
        
        self.assertEqual(x, 3)

    def testTrueUnlessTests(self):
        x = 2
        unless x == 0:
            x -= 1
        else:
            x += 1
        
        self.assertEqual(x, 1)
        
        
# incr_stmt: '++'
class IncrementTests(unittest.TestCase):


    def testIncrementTests(self):
        x = 1
        x++

        self.assertEqual(x, 2)

    def testNegativeIncrementTests(self):
        x = -2
        x++

        self.assertEqual(x, -1)
    
    
    def testFloatInrementTests(self):
        x = 1.0
        x++

        self.assertEqual(x, 2.0)

    def testPositiveFloatIncrementTests(self):
        x = -1.0
        x++
        x++

        self.assertEqual(x, 1.0)

#decr_stmt: '--'
class DecrementTests(unittest.TestCase):


    def testDecrementTests(self):
        x = 1
        x--

        self.assertEqual(x, 0)


    def testNegativeDecrementTests(self):
        x = 0
        x--

        self.assertEqual(x, -1)
    
    
    def testFloatDecrementTests(self):
        x = 1.0
        x--

        self.assertEqual(x, 0.0)

    def testNegativeFloatDecrementTests(self):
        x = 0.0
        x--

        self.assertEqual(x, -1.0)


def test_main():
    run_unittest(UntilTests, UnlessTests, IncrementTests, DecrementTests)

if __name__ == '__main__':
    test_main()