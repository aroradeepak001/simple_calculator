
import Calculator
from Calculator.get_primes_using_generator_iterator import *
import unittest

class comparisonTest(unittest.TestCase):
    def test_normal(self):

            assert get_primes_normal(range(1000000)) is not None


    def test_normal(self):
            assert get_primes_generator(range(1000000)) is not None






