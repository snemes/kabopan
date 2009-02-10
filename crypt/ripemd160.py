#RIPEMD
#RIPEMD-128/160/256/320
#RACE Integrity Primitives Evaluation Message Digest
#Hans Dobbertin, Antoon Bosselaers and Bart Preneel, 1960
#http://homes.esat.kuleuven.be/~bosselae/ripemd160.html
#
#RIPEMD-160, a strengthened version of RIPEMD, 1996
#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python

import _misc as misc
from md5 import *

class ripemd160(md5):
    def __init__(self):
        md5.__init__(self)
        self.IVs += [DWORD(0xC0D0E0F0 | 0x03020100)]
        self.ks = [misc.hsqrt(i) for i in [0, 2 ,3 , 5, 7]]
        self.Ks = [misc.hcbrt(i) for i in [2 ,3 , 5, 7, 0]]

        self.ss = [
            [11, 14, 15, 12, 5, 8, 7, 9, 11, 13, 14, 15, 6, 7, 9, 8],
            [7, 6, 8, 13, 11, 9, 7, 15, 7, 12, 15, 9, 11, 7, 13, 12],
            [11, 13, 6, 7, 14, 9, 13, 15, 14, 8, 13, 6, 5, 12, 7, 5],
            [11, 12, 14, 15, 14, 15, 9, 8, 9, 14, 5, 6, 8, 6, 5, 12],
            [9, 15, 5, 11, 6, 8, 13, 12, 5, 12, 13, 14, 11, 8, 5, 6]]

        self.Ss = [
            [ 8,  9,  9, 11, 13, 15, 15,  5,  7,  7,  8, 11, 14, 14, 12,  6],
            [ 9, 13, 15,  7, 12,  8,  9, 11,  7,  7, 12,  7,  6, 15, 13, 11],
            [ 9,  7, 15, 11,  8,  6,  6, 14, 12, 13,  5, 14, 13, 13,  7,  5],
            [15,  5,  8, 11, 14, 14,  6, 14,  6,  9, 12,  9, 12,  5, 15,  8],
            [ 8,  5, 12,  9, 12,  5, 14,  6,  8, 13,  6,  5, 15, 13, 11, 11]]

        self.fs = [self.f1, self.f2, self.f3, self.f4, self.f5]
        self.Fs = list(reversed(self.fs))

    def ro(self,i):
        return  [7, 4, 13, 1, 10, 6, 15, 3, 12, 0, 9, 5, 2, 14, 11, 8][i]

    def pi(self,i):
        return (9 * i + 5) % 16

    def rs(self, i):
        return [i, self.ro(i), self.ro(self.ro(i)), self.ro(self.ro(self.ro(i))), self.ro(self.ro(self.ro(self.ro(i))))]

    def Rs(self,i):
        return self.rs(self.pi(i))


    def f1(*args): return md5.h(*args) # b ^ c ^ d , exor
    def f2(*args): return md5.f(*args) # (b & c) | ((~b) & d) , mux
    def f3(self, b, c, d): return (b | ~c) ^ d
    def f4(*args): return md5.g(*args) #(b & d) | (c & (~d)), mux
    def f5(self, b, c, d): return b ^ (c | ~d)    # similar to md5.i


    def T_(self, a, b, c, d, f, w, k, s, e):
        return (a + f(b, c, d) + w + k).rol(s) + e

    def round_f(self, a, b, c, d, e, f, w, k, s):
        """permutation on a, b, c, d, e + transformation on b and d"""
        return e, self.T_(a, b, c, d, f, w, k, s, e), b, c.rol(10), d


    def rounds(self, words):
        a, b, c, d, e = A, B, C, D, E = list(self.ihvs)
        for round in range(5):
            f, F, k, K = [j[round] for j in self.fs, self.Fs, self.ks, self.Ks] # round-dependant parameters
            for i in range(16):
                #iteration-dependant parameters
                s, S, r, R = self.ss[round][i], self.Ss[round][i], self.rs(i)[round], self.Rs(i)[round]
                a, b, c, d, e = self.round_f(a,b,c,d,e,f, words[r], k, s)
                A, B, C, D, E = self.round_f(A,B,C,D,E,F, words[R], K, S)    # the same
        return a, b, c, d, e, A, B, C, D, E


    def combine(self, bhvs):
        a, b, c, d, e, A, B, C, D, E = bhvs
        h0, h1, h2, h3, h4 = self.ihvs
        self.ihvs = h1 + c + D, h2 + d + E, h3 + e + A, h4 + a + B, h0 + b + C


if __name__ == "__main__":
    import test.ripemd160_test