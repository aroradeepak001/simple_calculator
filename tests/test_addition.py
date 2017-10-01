
import Calculator
from Calculator.Addition import AddTwoNumbers
import unittest

class AStarSearchTest(unittest.TestCase):
    def test_addition(self):
            assert AddTwoNumbers(3,4) == 7


