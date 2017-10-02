import math
def get_primes_normal(input_list):
    return (element for element in input_list if is_prime(element))


def get_primes_generator(input_list):
    while True:
        if is_prime(input_list):
            yield input_list
        input_list += 1


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


print(get_primes_generator(range(1000)))