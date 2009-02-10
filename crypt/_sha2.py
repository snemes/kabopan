#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python

from _misc import nroot, frac, generate_primes
from _int import Int
primes = generate_primes(409)

def nroot_primes(start, end, root, precision):
    """returns the 'precision' bits representation of fractional parts of 'root'-root of the prime numbers, from the 'start'th to the 'end'th"""
    return list(Int(frac(nroot(i, root)) * 2 ** precision, precision) for i in primes[start:end])
