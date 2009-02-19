#Kabopan - Readable Algorithms. Public Domain, 2009
from kbp.coder.affine import *

assert inverse(17,26) == 23

assert encode(ALPHABET, ALPHABET, multiplier=17, increment=5) == "FWNEVMDULCTKBSJARIZQHYPGXO"

assert decode("FWNEVMDULCTKBSJARIZQHYPGXO", ALPHABET, multiplier=17, increment=5) == \
    ALPHABET
    
if __name__ == "__main__":
    import kbp.test.affine_test
