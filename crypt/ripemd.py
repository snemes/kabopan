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
from sha import sha_
from md4 import *

class ripemd160_():

    ks = [misc.hsqrt(i) for i in [0, 2 ,3 , 5, 7]]
    Ks = [misc.hcbrt(i) for i in [2 ,3 , 5, 7, 0]]

    ss = [
        [11, 14, 15, 12, 5, 8, 7, 9, 11, 13, 14, 15, 6, 7, 9, 8],
        [7, 6, 8, 13, 11, 9, 7, 15, 7, 12, 15, 9, 11, 7, 13, 12],
        [11, 13, 6, 7, 14, 9, 13, 15, 14, 8, 13, 6, 5, 12, 7, 5],
        [11, 12, 14, 15, 14, 15, 9, 8, 9, 14, 5, 6, 8, 6, 5, 12],
        [9, 15, 5, 11, 6, 8, 13, 12, 5, 12, 13, 14, 11, 8, 5, 6]]

    Ss = [
        [ 8,  9,  9, 11, 13, 15, 15,  5,  7,  7,  8, 11, 14, 14, 12,  6],
        [ 9, 13, 15,  7, 12,  8,  9, 11,  7,  7, 12,  7,  6, 15, 13, 11],
        [ 9,  7, 15, 11,  8,  6,  6, 14, 12, 13,  5, 14, 13, 13,  7,  5],
        [15,  5,  8, 11, 14, 14,  6, 14,  6,  9, 12,  9, 12,  5, 15,  8],
        [ 8,  5, 12,  9, 12,  5, 14,  6,  8, 13,  6,  5, 15, 13, 11, 11]]

    ro = [7, 4, 13, 1, 10, 6, 15, 3, 12, 0, 9, 5, 2, 14, 11, 8]

    def pi(i):
        return (9 * i + 5) % 16

    rs = [
        [i, ro[i], ro[ro[i]], ro[ro[ro[i]]], ro[ro[ro[ro[i]]]]]
        for i in xrange(16)]

    Rs = [
        rs[pi(i)]
        for i in xrange(16)]


    @staticmethod
    def f1(*args): return md4_.h(*args) # b ^ c ^ d , exor
    @staticmethod
    def f2(*args): return md4_.f(*args) # (b & c) | ((~b) & d) , mux
    @staticmethod
    def f3(b, c, d): return (b | ~c) ^ d
    @staticmethod
    def f4(*args): return md5_.g(*args) #(b & d) | (c & (~d)), mux
    @staticmethod
    def f5(b, c, d): return b ^ (c | ~d)    # similar to md5.i

    @staticmethod
    def T_(a, b, c, d, f, w, k, s, e):
        return (a + f(b, c, d) + w + k).rol(s) + e

    @staticmethod
    def round_f(a, b, c, d, e, f, w, k, s):
        """permutation on a, b, c, d, e + transformation on b and d"""
        return e, ripemd160_.T_(a, b, c, d, f, w, k, s, e), b, c.rol(10), d


class ripemd160(md5):
    def __init__(self):
        md5.__init__(self)
        self.IVs = sha_.IVs



    def rounds(self, words):
        a, b, c, d, e = A, B, C, D, E = list(self.ihvs)
        for round in range(5):
            f = [ripemd160_.f1, ripemd160_.f2, ripemd160_.f3, ripemd160_.f4, ripemd160_.f5][round]
            F = [ripemd160_.f5, ripemd160_.f4, ripemd160_.f3, ripemd160_.f2, ripemd160_.f1][round]
            k, K = [j[round] for j in ripemd160_.ks, ripemd160_.Ks] # round-dependant parameters
            for i in range(16):
                #iteration-dependant parameters
                s, S, r, R = ripemd160_.ss[round][i], ripemd160_.Ss[round][i], ripemd160_.rs[i][round], ripemd160_.Rs[i][round]
                a, b, c, d, e = ripemd160_.round_f(a,b,c,d,e,f, words[r], k, s)
                A, B, C, D, E = ripemd160_.round_f(A,B,C,D,E,F, words[R], K, S)    # the same
        return a, b, c, d, e, A, B, C, D, E


    def combine(self, bhvs):
        a, b, c, d, e, A, B, C, D, E = bhvs
        h0, h1, h2, h3, h4 = self.ihvs
        self.ihvs = h1 + c + D, h2 + d + E, h3 + e + A, h4 + a + B, h0 + b + C


class ripemd320_():
    #initialization vectors are extended by nibble-mirroring
    IVs = list(sha_.IVs) + [misc.nibbleswap(i, 4) for i in sha_.IVs]


class ripemd320(ripemd160):
    """
    Ripemd-320 is base Ripemd-160,
    but instead of combining both sets of intermediate hash values at the end of each round,
    it stores them separately, with an extra swap.
    thus, it doesn't increase security over Ripemd-160, but just extends
    the size of the hash.
    """
    def __init__(self):
        ripemd160.__init__(self)
        self.IVs = ripemd320_.IVs

    def combine(self, bhvs):
        #ripemd320 uses standard sum combining, unlike ripemd160
        self.ihvs = [sum(i) for i in zip(self.ihvs, bhvs)]

    def rounds(self, words):
        a, b, c, d, e, A, B, C, D, E = self.ihvs
        # ripemd standard round...
        for round in range(5):
            f = [ripemd160_.f1, ripemd160_.f2, ripemd160_.f3, ripemd160_.f4, ripemd160_.f5][round]
            F = [ripemd160_.f5, ripemd160_.f4, ripemd160_.f3, ripemd160_.f2, ripemd160_.f1][round]
            k, K = [j[round] for j in ripemd160_.ks, ripemd160_.Ks] # round-dependant parameters
            for i in range(16):
                #iteration-dependant parameters
                s, S, r, R = ripemd160_.ss[round][i], ripemd160_.Ss[round][i], ripemd160_.rs[i][round], ripemd160_.Rs[i][round]
                a, b, c, d, e = ripemd160_.round_f(a,b,c,d,e,f, words[r], k, s)
                A, B, C, D, E = ripemd160_.round_f(A,B,C,D,E,F, words[R], K, S)    # the same
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

class ripemd128_():
    # 4 rounds instead of 5
    # same as ripemd160, without the last elements, and f5 not beeing used
    IVs, ss, Ss, ks, Ks = [
        l[:4] for l in [
            md4_.IVs, ripemd160_.ss, ripemd160_.Ss, ripemd160_.ks, ripemd160_.Ks]]
    rs = [ripemd160_.rs[i][:4] for i in range(16)]
    Rs = [ripemd160_.Rs[i][:4] for i in range(16)]

    #excepted
    Ks[3] = 0               # 7^1/3 is replaced by 0

    @staticmethod
    def T_(a, b, c, d, f, w, k, s):
        return (a + f(b, c, d) + w + k).rol(s)

    @staticmethod
    def round_f(a, b, c, d, f, w, k, s):
        """permutation on a, b, c, d + transformation on b and d"""
        return d, ripemd128_.T_(a, b, c, d, f, w, k, s), b, c # no rotation on C for rmd128


class ripemd128(ripemd160):
    """
    Ripemd-128 is a cut version of Ripemd-160.
    one round less, with 2 small changes in the functions and constants.
    also, the Rol10 on the last hash value of ripemd-160 is not included.
    """
    def __init__(self):
        ripemd160.__init__(self)
        self.IVs = ripemd128_.IVs


    def rounds(self, words):
        a, b, c, d = A, B, C, D = list(self.ihvs)
        for round in range(4):
            f = [ripemd160_.f1, ripemd160_.f2, ripemd160_.f3, ripemd160_.f4][round]
            F = [ripemd160_.f4, ripemd160_.f3, ripemd160_.f2, ripemd160_.f1][round]
            k, K = [j[round] for j in ripemd128_.ks, ripemd128_.Ks] #round-dependant parameters
            for i in range(16):
                # iteration dependant parameters
                s, S, r, R = ripemd128_.ss[round][i], ripemd128_.Ss[round][i], ripemd128_.rs[i][round], ripemd128_.Rs[i][round]

                a, b, c, d = ripemd128_.round_f(a, b, c, d, f, words[r], k, s)
                A, B, C, D = ripemd128_.round_f(A, B, C, D, F, words[R], K, S)
        return a, b, c, d, A, B, C, D

    def combine(self, bhvs):
        a, b, c, d,A, B, C, D = bhvs
        h0, h1, h2, h3 = self.ihvs
        self.ihvs = h1 + c + D, h2 + d + A, h3 + a + B, h0 + b + C


class ripemd256_():
    #initialization vectors are extended by nibble-mirroring
    IVs = list(ripemd128_.IVs) + [misc.nibbleswap(i, 4) for i in ripemd128_.IVs]

class ripemd256(ripemd128):
    """
    Ripemd-256 is base Ripemd-128,
    but instead of combining both sets of intermediate hash values at the end of each round,
    it stores them separately, with an extra swap.
    thus, it doesn't increase security over Ripemd-128, but just extends
    the size of the hash.
    """
    def __init__(self):
        ripemd128.__init__(self)
        self.IVs = ripemd256_.IVs


    def combine(self, bhvs):
        #ripemd256 uses standard sum combining, unlike ripemd128
        self.ihvs = [sum(i) for i in zip(self.ihvs, bhvs)]

    def rounds(self, words):
        a, b, c, d, A, B, C, D,= self.ihvs
        # ripemd standard round...
        for round in range(4):
            f = [ripemd160_.f1, ripemd160_.f2, ripemd160_.f3, ripemd160_.f4][round]
            F = [ripemd160_.f4, ripemd160_.f3, ripemd160_.f2, ripemd160_.f1][round]
            k, K = [j[round] for j in ripemd128_.ks, ripemd128_.Ks] #round-dependant parameters
            for i in range(16):
                #iteration-dependant parameters
                s, S, r, R = ripemd128_.ss[round][i], ripemd128_.Ss[round][i], ripemd128_.rs[i][round], ripemd128_.Rs[i][round]
                a, b, c, d, = ripemd128_.round_f(a,b,c,d,f, words[r], k, s)
                A, B, C, D, = ripemd128_.round_f(A,B,C,D,F, words[R], K, S)    # the same
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
    import test.ripemd_test