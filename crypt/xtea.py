import cipher
from _int import *
import tea

class xtea(cipher.Feistel, tea.tea):
    def __init__(self, rounds):
        cipher.Feistel.__init__(self)
        tea.tea.__init__(self, rounds)

    def F(self, R, key, *extra):
        delta, shift = extra
        return (((R << 4) ^ (R >> 5)) + R) ^ (delta + key[(delta >> shift)& 3])


    def round_parameters(self, backward):
        if not backward:
            delta = 0
            for i in xrange(self.cycles):
                yield self.F, [delta, 0]
                delta += self.constant
                yield self.F, [delta, 11]
        else:
            delta = self.constant * self.cycles
            for i in xrange(self.cycles):
                yield self.F, [delta, 11]
                delta -= self.constant
                yield self.F, [delta, 0]


print [str(i) for i in xtea(64).crypt("\x00" * 8, DWORDS([0,0,0,0]))]
#XTEA  ['\xdee9d4d8', '\xf7131ed9']
print [str(i) for i in xtea(64).decrypt("\xDE\xE9\xD4\xD8\xF7\x13\x1E\xD9" , DWORDS([0,0,0,0]))]
