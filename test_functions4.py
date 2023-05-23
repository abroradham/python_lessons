import unittest

from functions4 import fibonaccidami

class FibonacciTest(unittest.TestCase):
    def TestCases_True(self):
        self.assertEqual(fibonaccidami(21), 'g is a Fibonacci number.') 

unittest.main()