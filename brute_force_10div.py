"""Brute force solver for Ten Divisibilities problem.

Works in base 10, tried a couple of other and found no solutions.
Not sure they actually exist.
"""

import time
t0 = time.time()
from itertools import permutations

base = 10
digits = range(1,base)

def cand(d):
    """
    Return the sum of the listo of digits where the position is a power of the base.
    Example in base 10: l=[1,2,3]->1e0+2e1+3e2.
    """
    return sum([dd*base**di for di, dd in enumerate(d)])

for perm_digits in permutations(digits):
    if not any([cand(perm_digits[(base-1-factor):]) % factor
                for factor in range(1,base)]):
        print(cand(perm_digits))
        # If you are interested in one solution only (and in base 10 there is only 1)
        # break

t1 = time.time()
print("Found in %.2fs (%.2fmin)" % (t1-t0, (t1-t0)/60))
