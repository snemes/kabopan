#Kabopan - Readable Algorithms. Public Domain, 2007-2009
"""
Tiny Encryption Algorithm Tea, XTEA
"""
from kbp.crypt.cipher import Feistel
from kbp.types import DWORD, DWORDS

class tea_u():
    """utility class for tea"""
    phi = (1 + 5**(1./2)) /2 #: golden ratio
    constant = DWORD((1 << 32) / phi)

assert tea_u.constant == 0x9e3779b9

class tea(Feistel):
    """
    Tiny Encryption Algorithm
    """
    def __init__(self, rounds):
        Feistel.__init__(self)
        self.in_f = lambda x, y: x + y
        self.out_f = lambda x, y : x - y
        self.rounds = rounds
        self.cycles = self.rounds / 2   # 2 feistel rounds per cycle
        self.middle = 32 / 8    # message is processed in 64 bits blocks, split in 2 equal halves


    def F(self, R, key, *extra):
        i1, i2, delta = extra
        return ((R << 4) + key[i1]) ^ (R + delta) ^ ((R >> 5) + key[i2])


    def round_parameters(self, backward):
        if not backward:
            delta = 0
            for i in xrange(self.cycles):
                delta += tea_u.constant
                yield self.F, [0, 1, delta]
                yield self.F, [2, 3, delta]
        else:
            delta = self.cycles * tea_u.constant
            for i in xrange(self.cycles):
                yield self.F, [2, 3, delta]
                yield self.F, [0, 1, delta]
                delta -= tea_u.constant

class xtea(tea):
    """
    XTEA is based on L{tea}
    
     - different round function
     - delta is modified between the 2 rounds of each cycle
    """
    def F(self, R, key, *extra):
        delta, shift = extra
        return (((R << 4) ^ (R >> 5)) + R) ^ (delta + key[(delta >> shift) & 3])


    def round_parameters(self, backward):
        if not backward:
            delta = 0
            for i in xrange(self.cycles):
                yield self.F, [delta, 0]
                delta += tea_u.constant
                yield self.F, [delta, 11]
        else:
            delta = self.cycles * tea_u.constant
            for i in xrange(self.cycles):
                yield self.F, [delta, 11]
                delta -= tea_u.constant
                yield self.F, [delta, 0]


if __name__ == "__main__":
    print [str(i) for i in tea(64).crypt("\x00" * 8, DWORDS([0,0,0,0]))]
    print [str(i) for i in tea(64).decrypt("\x41\xea\x3a\x0a\x94\xba\xa9\x40", DWORDS([0,0,0,0]))]
    print
    #assert tea().crypt("\x00" * 8, DWORDS([0,0,0,0])) == DWORDS([0x41ea3a0a, 0x94baa940])
    #assert tea().decrypt("\x41\xea\x3a\x0a\x94\xba\xa9\x40", DWORDS([0,0,0,0])) == [0,0]
    print [str(i) for i in xtea(64).crypt("\x00" * 8, DWORDS([0,0,0,0]))]
    #XTEA  ['\xdee9d4d8', '\xf7131ed9']
    print [str(i) for i in xtea(64).decrypt("\xDE\xE9\xD4\xD8\xF7\x13\x1E\xD9" , DWORDS([0,0,0,0]))]
