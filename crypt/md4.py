#MD4 - Message Digest 4
#Cryptographic hash
#The MD4 Message-Digest Algorithm
#Ron Rivest, 1992
#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python


import struct
from math import sqrt
from _misc import *
from _int import *
import Hash


class md4(Hash.merkledamgaard):
    def __init__(self):
        Hash.merkledamgaard.__init__(self)
        self.block_length = 512
        self.padding_size_encoding_length = 64
        self.hv_size = 32
        hex = "0123456789ABCDEF"
        IVhex = hex + hex[::-1]
        self.IVs = DWORDS(struct.unpack("<4L", hex2bin(IVhex)))
        self.pad_bit_7 = True

        self.functions = [self.f, self.g, self.h]

        self.constants = [hsqrt(i) for i in [0, 2, 3]]

        self.shifts = [
            [3, 7, 11, 19],
            [3, 5,  9, 13],
            [3, 9, 11, 15]]


    def f(self, b, c, d):
        return (b & c) | ((~b) & d)

    def g(self, b, c, d):
        return (b & c) | (b & d) | (c & d)

    def h(self, b, c, d):
        return (b ^ c ^ d)

    def r(self, i):
        return [
            i,
            ((i * 4) + (i / 4)) % 16 ,          # 0, 4, 8, 12, 1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15
            [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15][i] ]


    def pad(self, message):
        return pad_0_1_size(message, self.block_length, self.padding_size_encoding_length, self.padding_big_endianness, self.pad_bit_7)


    def compress(self, block, words):
        return words


    def rounds(self, words):
        bhv = list(self.ihvs) # block hash values
        for round_ in range(3):  # rounds
            F, constant = self.functions[round_], self.constants[round_]    # round-dependant parameters
            for i in range(16): # iterations per round

                #iteration-dependant parameters
                [a, b, c, d] = [((j - i) % 4) for j in range(4)]
                s = self.shifts[round_][i % 4]
                k = self.r(i)[round_]

                bhv[a] = (bhv[a] + F(bhv[b], bhv[c], bhv[d]) + words[k] + constant).rol(s)
        return bhv

    def sum_combine(self, bhvs):
        self.ihvs = [sum(i) for i in zip(self.ihvs, bhvs)]

    def combine(self, *args):
        self.sum_combine(*args)

    def process_block(self, block):
        #compression
        words = self.as_words(block)
        words = self.compress(block, words)
        #rounds
        bhvs = self.rounds(words)
        #integration
        self.combine(bhvs)


if __name__ == "__main__":
    import test.md4_test
