#Secure Hash Algorithm 2 - SHA-2, SHA256
#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python


from sha256 import *
from _int import Int, DWORDS
from _sha2 import nroot_primes
import _pickle as p

class sha224(sha256):
    def __init__(self):
        sha256.__init__(self)
        pickled = p.get_variables("sha224", ["IVs"])
        if pickled is None:
            self.IVs = DWORDS(nroot_primes(8, 16, 2, 64)) #:Lowest 32 bits of sha384 IVs
            p.save_variables("sha256", {"IVs": self.IVs})
        else:
            self.IVs = pickled["IVs"]

    def digest(self):
        return sha256.digest(self)[:28]


if __name__ == "__main__":
    import test.sha224_test
