
from md4 import *

from _misc import *
from _int import *

class has160(md4):
    def __init__(self):
        md4.__init__(self)
        self.IVs += [DWORD(0xC0D0E0F0 | 0x03020100)]
        self.functions = [self.f, self.g, self.h, self.g]
        self.constants = [hsqrt(i) for i in [0, 2, 3, 5]]
        self.extensions = [
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]],
            [[3, 6, 9, 12], [15, 2, 5, 8], [11, 14, 1, 4], [7, 10, 13, 0]],
            [[12, 5, 14, 7], [0, 9, 2, 11], [4, 13, 6, 15], [8, 1, 10, 3]],
            [[7, 2, 13, 8], [3, 14, 9, 4], [15, 10, 5, 0], [11, 6, 1, 12]]]

        # indexes are like extensions (flattened), with 18, 19, 16, 17 inserted every 4 value
        self.indexes = [ sum(([[18, 19, 16, 17][i]] + j 
            for i, j in enumerate(lists)), []) 
                for lists in self.extensions]
    def f(*args):
        return md4.f(*args)
    def g(*args):
        return md4.h(*args)

    def h(self, b, c, d):   # same as md5.i
        return c ^ (b | (~d))


    def rounds(self, words):
        words.extend((0 for i in xrange(20-16)))
        a, b, c, d, e = list(self.ihvs)
        for r in range(4):
            f = self.functions[r]
            k = self.constants[r]
            b_rot = [10, 17, 25, 30][r]

            for i in range(4):
                w = QWORD(0)
                for j in xrange(4):
                    w ^= words[self.extensions[r][i][j]]
                words[16 + i] = w

            for i in range(20):
                index = self.indexes[r][i]
                a_rot = [5, 11, 7, 15, 6, 13, 8, 14, 7, 12, 9, 11, 8, 15, 6, 12, 9, 14, 5, 13][i]
                
                a,b,c,d,e = [
                    a.rol(a_rot) + f(b, c, d) + e + k + words[index],
                    a,
                    b.rol(b_rot),
                    c,
                    d]
        return [a, b, c, d, e]

if __name__ == "__main__":
    import test.has160_test