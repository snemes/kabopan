#MD4 - Message Digest 4 / Cryptographic hash / The MD4 Message-Digest Algorithm / Ron Rivest, 1992
#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python


import struct
from math import sin
from _misc import *
from _int import *
import Hash

class md4_():
    """constants and functions of MD4 cryptographic hash"""
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
    IVs = DWORDS(struct.unpack("<4L", hex2bin(IVhex)))


class md4(Hash.merkledamgaard):
    def __init__(self):
        Hash.merkledamgaard.__init__(self)
        self.block_length = 512
        self.padding_size_encoding_length = 64
        self.hv_size = 32
        self.IVs = md4_.IVs
        self.pad_bit_7 = True

    def compress(self, block, words):
        return words

    def pad(self, message):
        return pad_0_1_size(message, self.block_length, self.padding_size_encoding_length, self.padding_big_endianness, self.pad_bit_7)


    def rounds(self, words):
        bhv = list(self.ihvs) # block hash values
        for self.round in range(3):  # rounds
            F = [md4_.f, md4_.g, md4_.h][self.round]
            constant = md4_.constants[self.round]
            for self.iteration in range(16): # iterations per round
                #iteration-dependant parameters
                [a, b, c, d] = [((j - self.iteration) % 4) for j in range(4)]
                s = md4_.shifts[self.round][self.iteration % 4]
                k = md4_.r[self.iteration][self.round]
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

class md5_():
    """constants and functions of md5 cryptographic hash"""
    g_coefficients = [[1,0], [5, 1], [3, 5], [7,0]]
    K = DWORDS([abs(sin(i + 1)) * (2**32) for i in range(16 * 4)])
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


class md5(md4):
    """
    MD4 with:
    modified G
    extra round with its function I
    different round operation and parameters.
    """

    def rounds(self, words):
        [a,b,c,d] = list(self.ihvs)
        for self.round in range(4):
            function = [md4_.f, md5_.g, md4_.h, md5_.i][self.round]
            for self.iteration in range(16):
                shift = md5_.shifts[self.round][self.iteration % 4]
                k = md5_.K[self.iteration + self.round * 16]
                mul, add = md5_.g_coefficients[self.round]
                g = (mul * self.iteration + add) % 16
                [a,b,c,d] = [
                    d,
                    (a + function(b, c, d) + words[g] + k).rol(shift) + b,
                    b,
                    c]
        return [a, b, c, d]

if __name__ == "__main__":
    import test.md4_test
