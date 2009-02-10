#Tiger Hash
#Cryptographic Hash
#Ross Anderson and Eli Biham, 1996
#Tiger - A Fast New Hash Function
#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python

try:
    import psyco
    psyco.run()
except:
    pass
import _misc as m
from md4 import *
from _int import QWORD, BYTE, List

import tiger_const

class tiger(md4):
    def __init__(self):
        md4.__init__(self)
        self.hv_size = 64

        hex = "0123456789ABCDEF"
        IVhex = hex + hex[::-1]
        self.IVs = QWORDS(list(struct.unpack(">2Q", hex2bin(IVhex)))  + [0xF090A0B0C0B0E080 | 0x0006050403020107])
        self.pad_bit_7 = False

        self.S = tiger_const.Ss_test
        self.nb_pass = 3 # standard tiger uses 3 passes
        self.sboxes = self.S
        self.Sboxes = self.S[::-1]
        self.gen_const()


    def key_schedule(self, words):
          x0, x1, x2, x3, x4, x5, x6, x7 = words

          x0 -= x7 ^ 0xA5A5A5A5A5A5A5A5
          x1 ^= x0
          x2 += x1
          x3 -= x2 ^ ((~x1) << 19)
          x4 ^= x3
          x5 += x4
          x6 -= x5 ^ ((~x4) >> 23)
          x7 ^= x6

          x0 += x7
          x1 -= x0 ^ ((~x7) << 19)
          x2 ^= x1
          x3 += x2
          x4 -= x3 ^ ((~x2) >> 23)
          x5 ^= x4
          x6 += x5
          x7 -= x6 ^ 0x0123456789ABCDEF
          return x0, x1, x2, x3, x4, x5, x6, x7


    def combine(self, bhvs): #: feed forward
        a, b, c = bhvs
        aa, bb, cc = self.ihvs
        self.ihvs = a ^ aa, b - bb, c + cc


    def round_(self, bhvs, round_indexes, x, mul):
        a, b, c = round_indexes
        bhvs[c] ^= x
        c = bhvs[c]
        ta = m.xor((sbox[c[7 - index]] for sbox, index in zip(self.sboxes, [0, 2, 4, 6])), QWORD(0))
        tb = m.xor((sbox[c[7 - index]] for sbox, index in zip(self.Sboxes, [1, 3, 5, 7])), QWORD(0))
        bhvs[a] -= ta
        bhvs[b] += tb
        bhvs[b] *= mul


    def pass_(self, bhvs, pass_indexes, mul, words):
        for p in range(8):
            # same round, but with rotated indexes, and next word
            self.round_(bhvs, pass_indexes << p , words[p], mul)


    def rounds(self, words):
        bhvs = list(self.ihvs)
        indexes = List(range(3))
        for i in range(self.nb_pass):
            multiplier = [5,7][i] if 0 <= i <= 1 else 9
            self.pass_(bhvs, indexes >> i, multiplier, words)
            #print words[0]
            words = self.key_schedule(words)
        return bhvs

    def gen_const(self):
        nb_passes = 5
        seed_string = "Tiger - A Fast New Hash Function, by Ross Anderson and Eli Biham"
        words = m.as_words(seed_string, 512, 64, bigendian=False)
        self.ihvs = list(self.IVs)
        print self.ihvs[0]
        self.ihvs = self.rounds(words)
        print self.ihvs[0]
        import sys
        sys.exit()
#        print [str(i) for i in words]
        print [str(i) for i in words]
        table = [list([DWORD(0) for i in range(1024)]) for j in range(2)]
        #input: 1024 of 8 of char
        #output : 2 of 1024 of dword
        """
        for i in xrange(1024):
            for j in xrange(8):
                current_iteration = i * 8 + j
                j_ = current_iteration % 1024
                i_ = current_iteration / (1024 * 2)
                if (int(table[i_][j_] >> j) & 0xFF)  != 0:
                    print "error",  i, j, "-", current_iteration, "-", i_, j_, (int(table[i_][j_] >> j) & 0xFF)
                table[i_][j_] |= ((i & 0xFF) << j)
                    
        print table[1][0]
        abc = 2
        self.ihvs = self.IVs
        for cnt in range(nb_passes):
            for i in range(256):
                for sb in xrange(0, 1024, 256):
                    abc += 1
                    if abc == 3:
                        abc = 0
                        self.ihvs = self.rounds(words)
                    for col in xrange(8):
                        current_iteration = (sb + i) * 8 + col
                        i_ = current_iteration / (1024 * 4)
                        j_ = current_iteration % 1024
                        sb2 = sb + self.ihvs[abc][col]
                        current_iteration = sb2 * 8 + col
                        i2_ = current_iteration / (1024 * 4)
                        j2_ = current_iteration % 1024
                        temp = (table[i_][j_] >> j) & 0xFF
                        table[i_][j_], table[i2_][j2_] = table[i2_][j2_], table[i_][j_]
        """
        table_ch = [list([BYTE(0) for i in range(8)]) for j in range(1024)]
        for i in xrange(1024):
            for col in xrange(8):
                table_ch[i][col] = BYTE(i & 0xff)
        abc = 2
        self.ihvs = list(self.IVs)
        for cnt in range(nb_passes):
            for i in range(256):
                for sb in xrange(0, 1024, 256):
                    abc += 1
                    if abc == 3:
                        abc = 0
                        print self.ihvs[0]
                        self.ihvs = self.rounds(words)
                        print self.ihvs[0]
                        print

                    for col in xrange(8):
                        i1 = sb + i
                        i2 = sb + self.ihvs[abc][col]
                        table_ch[i1][col] , table_ch[i2][col] = table_ch[i2][col] , table_ch[i1][col]
        for i in xrange(2):
            for col in xrange(8):
                print table_ch[i][col],
            print
    
        import pprint
"""        for i in range(2):
            for j in range(1024):
                print str(table[i][j])
#            out_index = [2, 1024]# 32
            #in_index = [1024, 8]# 8
"""
tiger()
import sys
sys.exit()
if __name__ == "__main__":
    import test.tiger_test
