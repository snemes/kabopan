#Secure Hash Standard - SHS - SHA-0
#RFC 3174
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python

from md4 import *
from _int import DWORD

class sha0(md4):
    def __init__(self):
        md4.__init__(self)
        self.IVs += [DWORD(0xC0D0E0F0 | 0x03020100)]
        self.constants = [hsqrt(i) for i in [2, 3, 5, 10]]
        self.output_big_endianness = self.block_big_endianness = self.padding_big_endianness = True
        # function names are swapped
        self.g, self.h = self.h, self.g
        self.functions = [self.f, self.g, self.h, self.g]


    def compress(self, block, words):
        words.extend(DWORD(0) for i in xrange(80 - 16))
        for i in range(16, 80):
            words[i] = words[i - 3] ^ words[i - 8] ^ words[i - 14] ^ words[i - 16]
        return words

    def rounds(self, words):
        [a, b, c, d, e] = list(self.ihvs)
        for round_ in range(4):
            f = self.functions[round_]
            k = self.constants[round_]
            for i in range(20):
                [a, b, c, d, e] = [
                   a.rol(5) + f(b, c, d) + e + k + words[i + 20 * round_],
                    a,
                    b.rol(30),
                    c,
                    d]
        return [a, b, c, d, e]

if __name__ == "__main__":
    import test.sha0_test
