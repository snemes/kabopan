import cipher
from _int import *
class tea(cipher.Feistel):
    def __init__(self, rounds):
        cipher.Feistel.__init__(self)
        self.in_f = lambda x, y: x + y
        self.out_f = lambda x, y : x - y
        self.rounds = rounds
        self.cycles = self.rounds / 2   # 2 feistel rounds per cycle
        self.middle = 32 / 8    # message is processed in 64 bits blocks, split in 2 equal halves


        phi = (1 + 5**(1./2)) /2 #: golden ratio
        self.constant = DWORD((1 << 32) / phi)
        assert self.constant == 0x9e3779b9


    def F(self, R, key, *extra):
        i1, i2, delta = extra
        return ((R << 4) + key[i1]) ^ (R + delta) ^ ((R >> 5) + key[i2])


    def round_parameters(self, backward):
        if not backward:
            delta = 0
            for i in xrange(self.cycles):
                delta += self.constant
                yield self.F, [0, 1, delta]
                yield self.F, [2, 3, delta]
        else:
            delta = self.constant * self.cycles  
            for i in xrange(self.cycles):
                yield self.F, [2, 3, delta]
                yield self.F, [0, 1, delta]
                delta -= self.constant

print [str(i) for i in tea(64).crypt("\x00" * 8, DWORDS([0,0,0,0]))]
print [str(i) for i in tea(64).decrypt("\x41\xea\x3a\x0a\x94\xba\xa9\x40", DWORDS([0,0,0,0]))]
print
#assert tea().crypt("\x00" * 8, DWORDS([0,0,0,0])) == DWORDS([0x41ea3a0a, 0x94baa940])
#assert tea().decrypt("\x41\xea\x3a\x0a\x94\xba\xa9\x40", DWORDS([0,0,0,0])) == [0,0]
