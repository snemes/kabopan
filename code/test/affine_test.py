#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python
from code.affine import *

assert inverse(17,26) == 23

assert encode(ALPHABET, ALPHABET, multiplier=17, increment=5) == "FWNEVMDULCTKBSJARIZQHYPGXO"

assert decode("FWNEVMDULCTKBSJARIZQHYPGXO", ALPHABET, multiplier=17, increment=5) == \
    ALPHABET
    
if __name__ == "__main__":
    import affine_test
