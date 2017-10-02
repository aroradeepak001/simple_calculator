import math
def get_primes_normal(input_list):
    return [element for element in input_list if is_prime(element)]


def get_primes_generator(input_list):
   for number in input_list:
        if is_prime(number):
                yield number
       


def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False


