#Secure Hash Algorithm 2 - SHA-2, SHA256
#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python


from md4 import *
from _sha2 import nroot_primes

import _pickle as p

class sha512(md4):
    def __init__(self):
        md4.__init__(self)
        self.block_length = 1024
        self.nb_rounds = 80
        self.hv_size = 64
        self.padding_size_encoding_length = 128
        self.output_big_endianness = self.block_big_endianness = self.padding_big_endianness = True

        pickled = p.get_variables("sha512", ["IVs", "K"])
        if pickled is None:
            # 64bits representation of fractional parts of square root of the 8th first primes
            self.IVs = nroot_primes(0, 8, 2, 64) 
            # 64bits representation of fractional parts of cube root of the 80th first primes
            self.K = nroot_primes(0, 80, 3, 64)
            p.save_variables("sha512", {"IVs": self.IVs,"K":self.K})
        else:
            self.IVs, self.K = pickled["IVs"], pickled["K"]


    def rxrxr(self, x, i1, i2, i3):
        """rol ^ rol ^ rol """
        return x.ror(i1) ^ x.ror(i2) ^ x.ror(i3)
    def rxrxs(self, x, i1, i2, i3):
        """rol ^ rol ^ shift """
        return x.ror(i1) ^ x.ror(i2) ^ (x >> i3)

    def f1(self, x):
        return self.rxrxr(x, 28, 34, 39)
    def f2(self, x):
        return self.rxrxr(x, 14, 18, 41)

    def f3(self, x):
        return self.rxrxs(x,  1,  8, 7)
    def f4(self, x):
        return self.rxrxs(x, 19, 61, 6)

    def maj(self, x, y, z):
        return ((x & y) ^ (x & z) ^ (y & z))
    def ch(self, x, y, z):
        return (x & y) ^ ((~x) & z)

    def compress(self, block, words):
        words.extend(0 for i in xrange(self.nb_rounds - 16))
        for i in range(16, self.nb_rounds):
            words[i] = words[i-16] + self.f3(words[i-15]) + words[i-7] + self.f4(words[i-2])
        return words
    
    def rounds(self, words):
        a,b,c,d,e,f,g,h = list(self.ihvs)
        for i in range(self.nb_rounds):
            t1 = h + self.f2(e) + self.ch(e, f, g) + self.K[i] + words[i]
            a,b,c,d,e,f,g,h = [
                t1 + self.f1(a) + self.maj(a, b, c),
                a, b, c, 
                d + t1,
                e, f, g
                ]
        return [a, b, c, d, e, f, g, h]


if __name__ == "__main__":
    import test.sha512_test
