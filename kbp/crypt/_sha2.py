#
#Kabopan - Readable Algorithms. Public Domain, 2009

from kbp._misc import nroot, frac, generate_primes
from kbp.types import Int
primes = generate_primes(409)

def nroot_primes(start, end, root, precision):
    """returns the 'precision' bits representation of fractional parts of 'root'-root of the prime numbers, from the 'start'th to the 'end'th"""
    return list(Int(frac(nroot(i, root)) * 2 ** precision, precision) for i in primes[start:end])
