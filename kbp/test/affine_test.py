#Kabopan - Readable Algorithms. Public Domain, 2007-2009
"""
Affine substitution cipher
"""

from kbp.coder.affine import encode, decode, inverse, coprimes
from kbp._misc import ALPHABET
assert inverse(17, 26) == 23

assert coprimes(18) == [1, 5, 7, 11, 13, 17]

assert encode(ALPHABET, ALPHABET, multiplier=17, increment=5) == "FWNEVMDULCTKBSJARIZQHYPGXO"

assert decode("FWNEVMDULCTKBSJARIZQHYPGXO", ALPHABET, multiplier=17, increment=5) == \
    ALPHABET
