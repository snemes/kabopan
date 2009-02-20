#Kabopan - Readable Algorithms. Public Domain, 2009
"""
Secure Hash Standard - SHS - SHA-0
RFC 3174
"""
from md4 import md4, md4_u
from kbp._misc import hsqrt
from kbp._int import DWORD

class sha_u():
    """utility class for sha"""
    constants = [hsqrt(i) for i in [2, 3, 5, 10]]
    f, g, h = md4_u.f, md4_u.h, md4_u.g
    functions = [f, g, h, g]
    IVs = list(md4_u.IVs) + [DWORD(0xC0D0E0F0 | 0x03020100)]

    @staticmethod
    def round_f(a, b, c, d, e, f, rol1, rol2, words, words_index, k):
        return [
           a.rol(rol1) + f(b, c, d) + e + k + words[words_index],
            a,
            b.rol(rol2),
            c,
            d]


class sha0(md4):
    """
    sha-0 is based on md4. 

    changes:
     - size padding, block splitting and merging are big endian.
     - it extends the words from 16 to 80 by combining.
     - it adds an extra round, and uses the same function and constant for each round
     - 4 rounds of 20 iterations
     - the round-specific function are md4.f, md4.h, md5.i, md4.h respectively
    """
    def __init__(self):
        md4.__init__(self)
        self.IVs = sha_u.IVs
        self.output_big_endianness = self.block_big_endianness = self.padding_big_endianness = True
        # function names are swapped


    def compress(self, block, words):
        words.extend(DWORD(0) for i in xrange(80 - 16))
        for i in range(16, 80):
            words[i] = words[i - 3] ^ words[i - 8] ^ words[i - 14] ^ words[i - 16]
        return words

    def rounds(self, words):
        [a, b, c, d, e] = list(self.ihvs)
        for round_ in range(4):
            f = sha_u.functions[round_]
            k = sha_u.constants[round_]
            for i in range(20):
                [a, b, c, d, e] = sha_u.round_f(a, b, c, d, e, f, 5, 30, words, i + 20 * round_, k)
        return [a, b, c, d, e]


class sha1(sha0):
    """
    sha-1 is a revision of sha-0.

    a 1-bit left rotation is added during word compression
    """
    def compress(self, block, words):
        words.extend(0 for i in xrange(80 - 16))
        for i in range(16, 80):
            words[i] = words[i - 3] ^ words[i - 8] ^ words[i - 14] ^ words[i - 16]
            # a rotation was added between sha0 and sha1
            words[i] = words[i].rol(1)
        return words

if __name__ == "__main__":
    import kbp.test.sha_test
