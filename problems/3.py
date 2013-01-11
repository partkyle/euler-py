from math import sqrt, ceil
import itertools
from prime import is_prime

def factors(n, skip_one=False):
    start = 2 if skip_one else 1
    return [(i, n / i)
            for i in xrange(start, int(ceil(sqrt(n))) + 1)
            if n % i == 0]

print max([n for n in set(itertools.chain(*list(factors(600851475143, True)))) if is_prime(n)])
