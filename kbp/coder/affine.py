#Kabopan - Readable Algorithms. Public Domain, 2007-2009
"""
Affine substitution cipher
"""

from kbp._subst import substitute
from kbp._misc import gcd

def inverse(number, modulo):
    for i in range(modulo):
        if (i * number) % modulo == 1:
            return i
    return None


def encode(plaintext, alphabet, increment, multiplier,):
    assert gcd(multiplier, len(alphabet)) == 1 # multiplier and length have to be co-primes
    ciphertext = substitute(plaintext, alphabet, lambda x: x * multiplier + increment)
    return ciphertext


def decode(ciphertext, alphabet, increment, multiplier):
    modulo = len(alphabet)
    assert gcd(multiplier, modulo) == 1 # multiplier and length have to be co-primes
    multiplier_inverse = inverse(multiplier, modulo)    # TODO
    plaintext = substitute(ciphertext, alphabet, lambda x: multiplier_inverse * (x - increment))
    return plaintext


if __name__ == "__main__":
    import kbp.test.affine_test
