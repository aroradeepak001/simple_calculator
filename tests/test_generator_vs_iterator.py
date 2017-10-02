
import Calculator
from Calculator.get_primes_using_generator_iterator import *
import unittest

class comparisonTest(unittest.TestCase):

    def test_prime(self):
            Output_normal = get_primes_normal(range(10000))
            Output_generator= get_primes_generator(range(10000))
            assert Output_normal[0]==Output_generator.next()


    def test_normal(self):
            assert get_primes_generator(range(1000000)) is not None






