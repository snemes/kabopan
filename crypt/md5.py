#MD5 - Message Digest 5
#Cryptographic hash
#The MD5 Message-Digest Algorithm
#Ron Rivest, 1992
#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python

from math import sin
from md4 import *

# based on MD4. modified G, extra round and function I, different round operation and parameters.

class md5(md4):
    def __init__(self):
        md4.__init__(self)
        self.functions = [self.f, self.g, self.h, self.i]
    
        self.shifts = [
            [7, 12, 17, 22],
            [5,  9, 14, 20],
            [4, 11, 16, 23],
            [6, 10, 15, 21]]
    
        self.g_coefficients = [[1,0], [5, 1], [3, 5], [7,0]]

    def g(self, b, c, d):
        return (b & d) | (c & (~d))

    def i(self, b, c, d):
        return c ^ (b | (~d))

    def K(self, i):
        return DWORD(abs(sin(i + 1)) * (2**32))

    def rounds(self, words):
        [a,b,c,d] = list(self.ihvs)
        for round_ in range(4): 
            function = self.functions[round_]
            g_multiplier, g_increment = self.g_coefficients[round_]

            for i in range(16):
                shift = self.shifts[round_][i % 4]
                k = self.K(i + round_ * 16)
                g = (g_multiplier * i + g_increment) % 16

                [a,b,c,d] = [
                    d,
                    (a + function(b, c, d) + words[g] + k).rol(shift) + b,
                    b,
                    c]
        return [a, b, c, d]


if __name__ == "__main__":
    import test.md5_test
