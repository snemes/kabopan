#Kabopan - Readable Algorithms. Public Domain, 2007-2009
"""
Secure Hash Algorithm 2 - SHA-2
sha-512, sha-384, sha-256, sha-224
"""

from kbp.crypt.md4 import Md4
from kbp.types import dwords, Utility, Int
from kbp._misc import nroot, frac, generate_primes
from kbp._pickle import get_variables, save_variables

primes = generate_primes(409)

def nroot_primes(start, end, root, precision):
    """returns the 'precision' bits representation of fractional parts of 'root'-root of the prime numbers, from the 'start'th to the 'end'th"""
    return list(Int(frac(nroot(i, root)) * 2 ** precision, precision) for i in primes[start:end])

class Sha512_u(Utility):
    """utility class for sha-512"""
    pickled = get_variables("sha512", ["IVs", "K"])
    if pickled is None:

        # 64bits representation of fractional parts of square root of the 8th first primes
        IVs = nroot_primes(0, 8, 2, 64)
        # 64bits representation of fractional parts of cube root of the 80th first primes
        K = nroot_primes(0, 80, 3, 64)

        save_variables("sha512", {"IVs": IVs, "K":K})
    else:
        IVs, K = pickled["IVs"], pickled["K"]


class Sha512(Md4):
    """
    sha-512 is based on md4

    ...
    """
    def __init__(self):
        Md4.__init__(self)
        self.block_length = 1024
        self.nb_rounds = 80
        self.hv_size = 64
        self.padding_size_encoding_length = 128
        self.output_big_endianness = self.block_big_endianness = self.padding_big_endianness = True
        self.IVs = Sha512_u.IVs
        self.K = Sha512_u.K


    def f1(self, x):
        return x.ror(28) ^ x.ror(34) ^ x.ror(39)
    def f2(self, x):
        return x.ror(14) ^ x.ror(18) ^ x.ror(41)

    def f3(self, x):
        return x.ror( 1) ^ x.ror( 8) ^ (x >> 7)
    def f4(self, x):
        return x.ror(19) ^ x.ror(61) ^ (x >> 6)

    def maj(self, x, y, z):
        return (x & y) ^ (x & z) ^ (y & z)
    def ch(self, x, y, z):
        return (x & y) ^ ((~x) & z)

    def compress(self, block, words):
        words.extend(0 for i in xrange(self.nb_rounds - 16))
        for i in range(16, self.nb_rounds):
            words[i] = words[i - 16] + self.f3(words[i - 15]) + words[i - 7] + self.f4(words[i - 2])
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

class Sha384_u(Utility):
    """utility class for sha-384"""
    pickled = get_variables("sha384", ["IVs"])
    if pickled is None:

        # 64bits representation of fractional parts of square root of the 8th to 16th first primes
        IVs = nroot_primes(8, 16, 2, 64)

        save_variables("sha384", {"IVs": IVs})
    else:
        IVs = pickled["IVs"]

class Sha384(Sha512):
    """
    sha-384 is based on sha-512

     - different (but similarly computed) initialisation vectors,
     - the digest is truncated to 384 bits
    """
    def __init__(self):
        Sha512.__init__(self)
        self.IVs = Sha384_u.IVs

    def digest(self):
        return Sha512.digest(self)[:384 / 8]


class Sha256_u(Utility):
    """utility class for sha-256"""
    #highest 4 bytes of sha512 IVs and K
    IVs = [i[:32 / 8] for i in  Sha512_u.IVs]
    K = [i[:32 / 8] for i in Sha512_u.K[:64]]

class Sha256(Sha512):
    """
    sha-256 is based on sha-512

    it's sha-512 with IHVs on 32 bits instead of 64:
     - the initialisations vectors and the constants K are the highest 32bits of their sha-512 counterparts.
     - it's using 64 rounds instead of 80, thus:
      - the F1-4 functions need different constants
     - the message length is is encoded on 64 bits instead of 128, during the padding
    """
    def __init__(self):
        Sha512.__init__(self)
        self.nb_rounds = 64
        self.block_length = 512
        self.hv_size = 32
        self.padding_size_encoding_length = 64
        self.K = Sha256_u.K
        self.IVs = Sha256_u.IVs


    def f1(self, x):
        return x.ror( 2) ^ x.ror(13) ^ x.ror(22)
    def f2(self, x):
        return x.ror( 6) ^ x.ror(11) ^ x.ror(25)
    def f3(self, x):
        return x.ror( 7) ^ x.ror(18) ^ (x >>  3)
    def f4(self, x):
        return x.ror(17) ^ x.ror(19) ^ (x >> 10)

class Sha224_u(Utility):
    """utility class for sha-224"""
    pickled = get_variables("sha224", ["IVs"])
    if pickled is None:
        # lowest 32 bits of sha384 IVs
        IVs = dwords(Sha384_u.IVs)

        save_variables("sha224", {"IVs": IVs})
    else:
        IVs = pickled["IVs"]


class Sha224(Sha256):
    """
    sha-224 is based on sha-256

     - different IVs (Dword of sha-384's)
     - the digest is truncated to 224 bits
    """
    def __init__(self):
        Sha256.__init__(self)
        self.IVs = Sha224_u.IVs

    def digest(self):
        return Sha256.digest(self)[:224 / 8]

if __name__ == "__main__":
    import kbp.test.sha2_test
