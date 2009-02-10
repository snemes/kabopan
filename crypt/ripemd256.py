#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python
from ripemd128 import *
import _misc as m

"""Ripemd-256 is base Ripemd-128,
but instead of combining both sets of intermediate hash values at the end of each round,
it stores them separately, with an extra swap.
thus, it doesn't increase security over Ripemd-128, but just extends
the size of the hash."""

class ripemd256(ripemd128):
    def __init__(self):
        ripemd128.__init__(self)
        #initialization vectors are extended by nibble-mirroring
        self.IVs += [m.nibbleswap(i, 4) for i in self.IVs]
        #ripemd256 uses standard sum combining, unlike ripemd128
        self.combine = self.sum_combine

    def rounds(self, words):
        a, b, c, d, A, B, C, D,= self.ihvs
        # ripemd standard round...
        for round in range(4):
            f, F, k, K = [j[round] for j in self.fs, self.Fs, self.ks, self.Ks] # round-dependant parameters
            for i in range(16):
                #iteration-dependant parameters
                s, S, r, R = self.ss[round][i], self.Ss[round][i], self.rs(i)[round], self.Rs(i)[round]
                a, b, c, d, = self.round_f(a,b,c,d,f, words[r], k, s)
                A, B, C, D, = self.round_f(A,B,C,D,F, words[R], K, S)    # the same
            # ...with an extra swap at the end of each round
            if round == 0:
                a, A = A, a
            elif round == 1:
                b, B = B, b
            elif round == 2:
               c, C = C, c
            elif round == 3:
                d, D = D, d
        return a, b, c, d, A, B, C, D

if __name__ == "__main__":
    import test.ripemd256_test
