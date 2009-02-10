#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python

from ripemd160 import *
import _misc as m

"""
Ripemd-128 is a cut version of Ripemd-160.
one round less, with 2 small changes in the functions and constants.
also, the Rol10 on the last hash value of ripemd-160 is not included.
"""
class ripemd128(ripemd160):
    def __init__(self):
        ripemd160.__init__(self)
        # same as ripemd160, without the last elements
        self.IVs, self.ss, self.Ss, self.fs, self.ks, self.Ks = [
            l[:4] for l in [
                self.IVs, self.ss, self.Ss, self.fs, self.ks, self.Ks]]

        #exception
        self.Fs = list(reversed(self.fs)) # Fs is still the mirror of fs
        self.Ks[3] = 0               # 7^1/3 is replaced by 0


    def rs(self, i):
        return ripemd160.rs(self, i)[:4]


    def Rs(self, i):
        return ripemd160.Rs(self, i)[:4]

    def T_(self, a, b, c, d, f, w, k, s):
        return (a + f(b, c, d) + w + k).rol(s)

    def round_f(self, a, b, c, d, f, w, k, s):
        """permutation on a, b, c, d + transformation on b and d"""
        return d, self.T_(a, b, c, d, f, w, k, s), b, c # no rotation on C for rmd128


    def rounds(self, words):
        a, b, c, d = A, B, C, D = list(self.ihvs)
        for round in range(4):
            f, F , k, K = [j[round] for j in self.fs, self.Fs, self.ks, self.Ks] #round-dependant parameters
            for i in range(16):
                # iteration dependant parameters
                s, S, r, R = self.ss[round][i], self.Ss[round][i], self.rs(i)[round], self.Rs(i)[round]
    
                a, b, c, d = self.round_f(a, b, c, d, f, words[r], k, s)
                A, B, C, D = self.round_f(A, B, C, D, F, words[R], K, S)
        return a, b, c, d, A, B, C, D

    def combine(self, bhvs):
        a, b, c, d,A, B, C, D = bhvs
        h0, h1, h2, h3 = self.ihvs
        self.ihvs = h1 + c + D, h2 + d + A, h3 + a + B, h0 + b + C


if __name__ == "__main__":
    import test.ripemd128_test
