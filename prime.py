import math

def is_prime(n):
    if n in [0,1,2]:
        return True

    if n % 2 == 0:
        return False

    for i in xrange(3, int(math.ceil(math.sqrt(n)) + 1), 2):
        if n % i == 0:
            return False

    return True
