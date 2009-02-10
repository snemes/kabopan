#Secure Hash Algorithm 2 - SHA-2, SHA256
#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python


from sha512 import *
from _int import *
from _sha2 import nroot_primes

class sha384(sha512):
    def __init__(self):
        sha512.__init__(self)
        pickled = p.get_variables("sha384", ["IVs"])
        if pickled is None:
            self.IVs = nroot_primes(8, 16, 2, 64)
            p.save_variables("sha384", {"IVs": self.IVs})
        else:
            self.IVs = pickled["IVs"]

    def digest(self):
        return sha512.digest(self)[:48]


if __name__ == "__main__":
    import test.sha384_test
