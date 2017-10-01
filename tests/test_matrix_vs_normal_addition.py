
import Calculator
from Calculator.addition_matrices_using_numpy import *
import unittest

class comparisonTest(unittest.TestCase):
    def test_addition_normal(self):
            assert addition_of_normal_lists(range(1000000),range(1000000)) is not None

    def test_addition_numpy(self):
            assert addition_using_numpy(range(1000000),range(1000000)) is not None

    def test_addition_for_loop(self):
            assert addition_using_for_loops(range(1000000),range(1000000)) is not None


