#Secure Hash Algorithm 2 - SHA-2, SHA256
# FIPS PUB 180-2
#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python

from sha512 import *

class sha256(sha512):
    def __init__(self):
        sha512.__init__(self)
        self.nb_rounds = 64
        self.block_length = 512
        self.hv_size = 32
        self.padding_size_encoding_length = 64

        self.IVs = DWORDS([i >> 32 for i in  self.IVs])
        self.K = DWORDS([i >> 32 for i in self.K[:64]])

    def f1(self, x):
        return self.rxrxr(x,  2, 13, 22)
    def f2(self, x):
        return self.rxrxr(x,  6, 11, 25)

    def f3(self, x):
        return self.rxrxs(x,  7, 18,  3)
    def f4(self, x):
        return self.rxrxs(x, 17, 19, 10)

if __name__ == "__main__":
    import test.sha256_test
