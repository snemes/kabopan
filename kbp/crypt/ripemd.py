#Kabopan - Readable Algorithms. Public Domain, 2007-2009
"""
RACE Integrity Primitives Evaluation Message Digest

RIPEMD-128/160/256/320
Hans Dobbertin, Antoon Bosselaers and Bart Preneel, 1960
U{http://homes.esat.kuleuven.be/~bosselae/ripemd160.html}

RIPEMD-160, a strengthened version of RIPEMD, 1996
"""

import kbp._misc as misc
from kbp.types import Utility
from kbp.crypt.sha import Sha_u
from kbp.crypt.md4 import Md4_u, Md4, Md5_u

class Ripemd160_u(Utility):
    """utility class for RIPEMD-160 cryptographic hash"""

    ks = [misc.hsqrt(i) for i in [0, 2 , 3, 5, 7]]
    Ks = [misc.hcbrt(i) for i in [2, 3 , 5, 7, 0]]

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

    #f1 = md4.h     # exor
    #f2 = md4.f     # mux

    @staticmethod
    def f3(b, c, d):
        return (b | ~c) ^ d

    #f4 = md5.g     # mux

    @staticmethod
    def f5(b, c, d): 
        return b ^ (c | ~d)    # similar to md5.i

    @staticmethod
    def T_(a, b, c, d, f, w, k, s, e):
        return (a + f(b, c, d) + w + k).rol(s) + e

    @staticmethod
    def iteration_f(a, b, c, d, e, f, w, k, s):
        """permutation on a, b, c, d, e + transformation on b and d"""
        return e, Ripemd160_u.T_(a, b, c, d, f, w, k, s, e), b, c.rol(10), d

    @staticmethod
    def round_f(round_, a, b, c, d, e, A, B, C, D, E, words):
        functions = [Md4_u.h, Md4_u.f, Ripemd160_u.f3, Md5_u.g, Ripemd160_u.f5]
        Functions = list(reversed(functions))
        f = functions[round_]
        F = Functions[round_]
        k, K = [j[round_] for j in Ripemd160_u.ks, Ripemd160_u.Ks] # round-dependant parameters
        for i in range(16):
            #iteration-dependant parameters
            s, S, r, R = Ripemd160_u.ss[round_][i], Ripemd160_u.Ss[round_][i], Ripemd160_u.rs[i][round_], Ripemd160_u.Rs[i][round_]

            a, b, c, d, e = Ripemd160_u.iteration_f(a, b, c, d, e, f, words[r], k, s)
            A, B, C, D, E = Ripemd160_u.iteration_f(A, B, C, D, E, F, words[R], K, S)    # the same
        return a, b, c, d, e, A, B, C, D, E

class Ripemd160(Md4):
    """
    RIPEMD-160 is based on L{MD5<Md5>}
    
     - uses sha-0 IVs
     - each round computes 2 sets of IHVs in parallel which are combined in a special way
    """
    def __init__(self):
        Md4.__init__(self)
        self.IVs = Sha_u.IVs

    def rounds(self, words):
        a, b, c, d, e = A, B, C, D, E = list(self.ihvs)
        for round_ in range(5):
            a, b, c, d, e, A, B, C, D, E = Ripemd160_u.round_f(round_, a, b, c, d, e, A, B, C, D, E, words)
        return a, b, c, d, e, A, B, C, D, E


    def combine(self, bhvs):
        a, b, c, d, e, A, B, C, D, E = bhvs
        h0, h1, h2, h3, h4 = self.ihvs
        self.ihvs = h1 + c + D, h2 + d + E, h3 + e + A, h4 + a + B, h0 + b + C


class Ripemd320_u(Utility):
    """utility class for RIPEMD-320 cryptographic hash"""
    #initialization vectors are extended by nibble-mirroring
    IVs = list(Sha_u.IVs) + [misc.nibbleswap(i, 4) for i in Sha_u.IVs]


class Ripemd320(Ripemd160):
    """
    RIPEMD-320 is based on RIPEMD-160
    
     - uses doubled RIPEMD-160 IVs.
     - instead of combining both sets of intermediate hash values at the end of each round,
    it stores them separately, with an extra swap.
    thus, it doesn't increase security over Ripemd-160,
    but just extends the size of the hash.
    """
    def __init__(self):
        Ripemd160.__init__(self)
        self.IVs = Ripemd320_u.IVs

    def combine(self, bhvs):
        """RIPEMD-320 uses standard sum combining, unlike RIPEMD-160"""
        self.ihvs = [sum(i) for i in zip(self.ihvs, bhvs)]

    def rounds(self, words):
        a, b, c, d, e, A, B, C, D, E = self.ihvs
        # ripemd standard round...
        for round_ in range(5):
            a, b, c, d, e, A, B, C, D, E = Ripemd160_u.round_f(round_, a, b, c, d, e, A, B, C, D, E, words)
            # ...with an extra swap at the end of each round
            if round_ == 0L:
                b, B = B, b
            elif round_ == 1:
                d, D = D, d
            elif round_ == 2:
                a, A = A, a
            elif round_ == 3:
                c, C = C, c
            elif round_ == 4:
                e, E = E, e

        return a, b, c, d, e, A, B, C, D, E

class Ripemd128_u(Utility):
    """utility class for RIPEMD-128 cryptographic hash"""
    # 4 rounds instead of 5
    # same as RIPEMD-160, without the last elements, and f5 not beeing used
    IVs, ss, Ss, ks, Ks = [
        l[:4] for l in [
            Md4_u.IVs, Ripemd160_u.ss, Ripemd160_u.Ss, Ripemd160_u.ks, Ripemd160_u.Ks]]
    rs = [Ripemd160_u.rs[i][:4] for i in range(16)]
    Rs = [Ripemd160_u.Rs[i][:4] for i in range(16)]

    #excepted
    Ks[3] = 0               # 7^1/3 is replaced by 0

    @staticmethod
    def T_(a, b, c, d, f, w, k, s):
        return (a + f(b, c, d) + w + k).rol(s)

    @staticmethod
    def iteration_f(a, b, c, d, f, w, k, s):
        """permutation on a, b, c, d + transformation on b and d"""
        return d, Ripemd128_u.T_(a, b, c, d, f, w, k, s), b, c # no rotation on C for rmd128

    @staticmethod
    def round_f(round_, a, b, c, d, A, B, C, D, words):
        functions = [Md4_u.h, Md4_u.f, Ripemd160_u.f3, Md5_u.g]
        Functions = list(reversed(functions))
        f = functions[round_]
        F = Functions[round_]
        f = [Md4_u.h, Md4_u.f, Ripemd160_u.f3, Md5_u.g][round_]
        F = [Md5_u.g, Ripemd160_u.f3, Md4_u.f, Md4_u.h][round_]
        k, K = [j[round_] for j in Ripemd128_u.ks, Ripemd128_u.Ks] #round-dependant parameters
        for i in range(16):
            # iteration dependant parameters
            s, S, r, R = Ripemd128_u.ss[round_][i], Ripemd128_u.Ss[round_][i], Ripemd128_u.rs[i][round_], Ripemd128_u.Rs[i][round_]

            a, b, c, d = Ripemd128_u.iteration_f(a, b, c, d, f, words[r], k, s)
            A, B, C, D = Ripemd128_u.iteration_f(A, B, C, D, F, words[R], K, S)
        return a, b, c, d, A, B, C, D


class Ripemd128(Ripemd160):
    """
    RIPEMD-128 is based on RIPEMD-160.
    
     - one round less
     - 2 small changes in the functions and constants.
     - the Rol10 on the last hash value of RIPEMD-160 is not included.
    """
    def __init__(self):
        Ripemd160.__init__(self)
        self.IVs = Ripemd128_u.IVs

    def rounds(self, words):
        a, b, c, d = A, B, C, D = list(self.ihvs)
        for round_ in range(4):
            a, b, c, d, A, B, C, D = Ripemd128_u.round_f(round_, a, b, c, d, A, B, C, D, words)
        return a, b, c, d, A, B, C, D

    def combine(self, bhvs):
        a, b, c, d, A, B, C, D = bhvs
        h0, h1, h2, h3 = self.ihvs
        self.ihvs = h1 + c + D, h2 + d + A, h3 + a + B, h0 + b + C


class Ripemd256_u(Utility):
    """utility class for RIPEMD-256 cryptographic hash"""
    #initialization vectors are extended by nibble-mirroring
    IVs = list(Ripemd128_u.IVs) + [misc.nibbleswap(i, 4) for i in Ripemd128_u.IVs]

class Ripemd256(Ripemd128):
    """
    RIPEMD-256 is based on RIPEMD-128

     - instead of combining both sets of intermediate hash values at the end of each round,
    it stores them separately, with an extra swap at the end of each round
    thus, it doesn't increase security over RIPEMD-128, but just extends
    the size of the hash.
    """
    def __init__(self):
        Ripemd128.__init__(self)
        self.IVs = Ripemd256_u.IVs


    def combine(self, bhvs):
        """RIPEMD-256 uses standard sum combining, unlike L{RIPEMD-128<Ripemd128>}"""
        self.ihvs = [sum(i) for i in zip(self.ihvs, bhvs)]

    def rounds(self, words):
        a, b, c, d, A, B, C, D = self.ihvs
        # RIPEMD standard round...
        for round_ in range(4):
            a, b, c, d, A, B, C, D = Ripemd128_u.round_f(round_, a, b, c, d, A, B, C, D, words)
            # ...with an extra swap at the end of each round
            if round_ == 0:
                a, A = A, a
            elif round_ == 1:
                b, B = B, b
            elif round_ == 2:
                c, C = C, c
            elif round_ == 3:
                d, D = D, d
        return a, b, c, d, A, B, C, D

if __name__ == "__main__":
    import kbp.test.ripemd_test