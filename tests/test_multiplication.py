
import Calculator
from Calculator.Multiplication import multiplyTwoNumbers
import unittest

class MultiplicationTest(unittest.TestCase):
    def test_two_multiplication(self):
            assert multiplyTwoNumbers(3,4) == 12


