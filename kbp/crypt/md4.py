#Kabopan - Readable Algorithms. Public Domain, 2007-2009
"""
MD4 - Message Digest 4

Cryptographic hash 
The MD4 Message-Digest Algorithm
Ron Rivest, 1992
"""


import struct
from math import sin
from kbp._misc import hsqrt, hex2bin, pad_0_1_size
from kbp.types import dwords, Utility
import kbp.crypt.Hash as Hash

class Md4_u(Utility):
    """utility class for L{MD4<Md4>} cryptographic hash"""
    constants = [hsqrt(i) for i in [0, 2, 3]]

    shifts = [
            [3, 7, 11, 19],
            [3, 5,  9, 13],
            [3, 9, 11, 15]]

    r = [
            [
            i,
            ((i * 4) + (i / 4)) % 16 ,          # 0, 4, 8, 12, 1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15
            [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15][i] ]
        for i in range(16)]

    @staticmethod
    def f(b, c, d):
        return (b & c) | ((~b) & d)

    @staticmethod
    def g(b, c, d):
        return (b & c) | (b & d) | (c & d)

    @staticmethod
    def h(b, c, d):
        return (b ^ c ^ d)

    hex = "0123456789ABCDEF"
    IVhex = hex + hex[::-1]
    IVs = dwords(struct.unpack("<4L", hex2bin(IVhex)))


class Md4(Hash.Merkledamgaard):
    """
    MD4 is based on the L{Merkle-Damgaard<Merkledamgaard>} model.
    
    padding is done by adding a 1 bit, then a number of 0, then size of the original messages (in bits) is encoded.
    
    so at least, one bit + the size are padded.
    """
    def __init__(self):
        Hash.Merkledamgaard.__init__(self)
        self.block_length = 512
        self.padding_size_encoding_length = 64
        self.hv_size = 32
        self.IVs = Md4_u.IVs
        self.pad_bit_7 = True

    def compress(self, block, words):
        return words

    def pad(self, message):
        return pad_0_1_size(message, self.block_length, self.padding_size_encoding_length, self.padding_big_endianness, self.pad_bit_7)


    def rounds(self, words):
        bhv = list(self.ihvs) # block hash values
        for round_ in range(3):  # rounds
            F = [Md4_u.f, Md4_u.g, Md4_u.h][round_]
            constant = Md4_u.constants[round_]
            for iteration in range(16): # iterations per round
                #iteration-dependant parameters
                [a, b, c, d] = [((j - iteration) % 4) for j in range(4)]
                s = Md4_u.shifts[round_][iteration % 4]
                k = Md4_u.r[iteration][round_]
                bhv[a] = (bhv[a] + F(bhv[b], bhv[c], bhv[d]) + words[k] + constant).rol(s)
        return bhv

    def combine(self, bhvs):
        self.ihvs = [sum(i) for i in zip(self.ihvs, bhvs)]

    def process_block(self, block):
        #compression
        words = self.as_words(block)
        words = self.compress(block, words)
        #rounds
        bhvs = self.rounds(words)
        #integration
        self.combine(bhvs)

class Md5_u(Utility):
    """utility class for MD5 cryptographic hash"""
    g_coefficients = [[1, 0], [5, 1], [3, 5], [7, 0]]
    K = dwords([abs(sin(index + 1)) * (2**32) for index in range(16 * 4)])
    shifts = [
        [7, 12, 17, 22],
        [5,  9, 14, 20],
        [4, 11, 16, 23],
        [6, 10, 15, 21]]

    @staticmethod
    def g(b, c, d):
        return (b & d) | (c & (~d))

    @staticmethod
    def i(b, c, d):
        return c ^ (b | (~d))


class Md5(Md4):
    """
    MD5 is based on MD4
    
    modified G
    extra round with its function I
    different round operation and parameters.
    """

    def rounds(self, words):
        [a, b, c, d] = list(self.ihvs)
        for round_ in range(4):
            function = [Md4_u.f, Md5_u.g, Md4_u.h, Md5_u.i][round_]
            for iteration in range(16):
                shift = Md5_u.shifts[round_][iteration % 4]
                k = Md5_u.K[iteration + round_ * 16]
                mul, add = Md5_u.g_coefficients[round_]
                g = (mul * iteration + add) % 16
                [a, b, c, d] = [
                 d,
                 (a + function(b, c, d) + words[g] + k).rol(shift) + b,
                 b,
                 c]
        return [a, b, c, d]

if __name__ == "__main__":
    import kbp.test.md4_test
