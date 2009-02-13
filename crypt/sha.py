#Secure Hash Standard - SHS - SHA-0
#RFC 3174
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python

from md4 import *
from _int import DWORD

class sha_():
    constants = [hsqrt(i) for i in [2, 3, 5, 10]]
    f, g, h = md4_.f, md4_.h, md4_.g
    functions = [md4_.f, g, h, g]

    @staticmethod
    def round_f(a, b, c, d, e, f, rol1, rol2, words, words_index, k):
        return [
           a.rol(rol1) + f(b, c, d) + e + k + words[words_index],
            a,
            b.rol(rol2),
            c,
            d]
    IVs = list(md4_.IVs) + [DWORD(0xC0D0E0F0 | 0x03020100)]

class sha0(md4):
    def __init__(self):
        md4.__init__(self)
        self.IVs = sha_.IVs
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
            f = sha_.functions[round_]
            k = sha_.constants[round_]
            for i in range(20):
                [a, b, c, d, e] = sha_.round_f(a, b, c, d, e, f, 5, 30, words, i + 20 * round_, k)
        return [a, b, c, d, e]


class sha1(sha0):

    def compress(self, block, words):
        words.extend(0 for i in xrange(80 - 16))
        for i in range(16, 80):
            words[i] = words[i - 3] ^ words[i - 8] ^ words[i - 14] ^ words[i - 16]
            # a rotation was added between sha0 and sha1
            words[i] = words[i].rol(1)
        return words

if __name__ == "__main__":
    import test.sha_test
