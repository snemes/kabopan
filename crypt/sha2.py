#Secure Hash Algorithm 2 - SHA-2, SHA256
#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python


from md4 import *
from _sha2 import nroot_primes

import _pickle as p

class sha512_():
    pickled = p.get_variables("sha512", ["IVs", "K"])
    if pickled is None:

        # 64bits representation of fractional parts of square root of the 8th first primes
        IVs = nroot_primes(0, 8, 2, 64)
        # 64bits representation of fractional parts of cube root of the 80th first primes
        K = nroot_primes(0, 80, 3, 64)

        p.save_variables("sha512", {"IVs": IVs,"K":K})
    else:
        IVs, K = pickled["IVs"], pickled["K"]


class sha512(md4):
    def __init__(self):
        md4.__init__(self)
        self.block_length = 1024
        self.nb_rounds = 80
        self.hv_size = 64
        self.padding_size_encoding_length = 128
        self.output_big_endianness = self.block_big_endianness = self.padding_big_endianness = True
        self.IVs = sha512_.IVs
        self.K = sha512_.K

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
        a, b, c, d, e, f, g, h = list(self.ihvs)
        for i in range(self.nb_rounds):
            t1 = h + self.f2(e) + self.ch(e, f, g) + self.K[i] + words[i]
            a, b, c, d, e, f, g, h = [
                t1 + self.f1(a) + self.maj(a, b, c),
                a, b, c,
                d + t1,
                e, f, g
                ]
        return [a, b, c, d, e, f, g, h]

class sha384_():
    pickled = p.get_variables("sha384", ["IVs"])
    if pickled is None:

        IVs = nroot_primes(8, 16, 2, 64)

        p.save_variables("sha384", {"IVs": IVs})
    else:
        IVs = pickled["IVs"]

class sha384(sha512):
    def __init__(self):
        sha512.__init__(self)
        self.IVs = sha384_.IVs

    def digest(self):
        return sha512.digest(self)[:48]


class sha256_():
    #highest 4 bytes of sha512 IVs and K
    IVs = [i[:4] for i in  sha512_.IVs]
    K = [i[:4] for i in sha512_.K[:64]]

class sha256(sha512):
    def __init__(self):
        sha512.__init__(self)
        self.nb_rounds = 64
        self.block_length = 512
        self.hv_size = 32
        self.padding_size_encoding_length = 64
        self.K = sha256_.K
        self.IVs = sha256_.IVs


    def f1(self, x):
        return self.rxrxr(x,  2, 13, 22)
    def f2(self, x):
        return self.rxrxr(x,  6, 11, 25)

    def f3(self, x):
        return self.rxrxs(x,  7, 18,  3)
    def f4(self, x):
        return self.rxrxs(x, 17, 19, 10)

class sha224_():
    pickled = p.get_variables("sha224", ["IVs"])
    if pickled is None:

        IVs = DWORDS(sha384_.IVs)

        p.save_variables("sha256", {"IVs": IVs})
    else:
        IVs = pickled["IVs"]

class sha224(sha256):
    def __init__(self):
        sha256.__init__(self)
        self.IVs = sha224_.IVs

    def digest(self):
        return sha256.digest(self)[:28]

if __name__ == "__main__":
    import test.sha2_test
