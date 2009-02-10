#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python

from ripemd160 import *
import _misc as m

"""Ripemd-320 is base Ripemd-160,
but instead of combining both sets of intermediate hash values at the end of each round,
it stores them separately, with an extra swap.
thus, it doesn't increase security over Ripemd-160, but just extends
the size of the hash."""


class ripemd320(ripemd160):
    def __init__(self):
        ripemd160.__init__(self)
        #initialization vectors are extended by nibble-mirroring
        self.IVs += [m.nibbleswap(i, 4) for i in self.IVs]
        #ripemd320 uses standard sum combining, unlike ripemd160
        self.combine = self.sum_combine

    def rounds(self, words):
        a, b, c, d, e, A, B, C, D, E = self.ihvs
        # ripemd standard round...
        for round in range(5):
            f, F, k, K = [j[round] for j in self.fs, self.Fs, self.ks, self.Ks] # round-dependant parameters
            for i in range(16):
                #iteration-dependant parameters
                s, S, r, R = self.ss[round][i], self.Ss[round][i], self.rs(i)[round], self.Rs(i)[round]
                a, b, c, d, e = self.round_f(a,b,c,d,e,f, words[r], k, s)
                A, B, C, D, E = self.round_f(A,B,C,D,E,F, words[R], K, S)    # the same
            # ...with an extra swap at the end of each round
            if round == 0L:
                b, B = B, b
            elif round == 1:
                d, D = D, d
            elif round == 2:
                a, A = A, a
            elif round == 3:
                c, C = C, c
            elif round == 4:
                e, E = E, e

        return a, b, c, d, e, A, B, C, D, E

if __name__ == "__main__":
    import test.ripemd320_test
