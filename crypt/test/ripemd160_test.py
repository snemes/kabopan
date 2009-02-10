#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python

from crypt.ripemd160 import *
from _misc import test_vector_strings, ass

hash = lambda x:ripemd160().compute(x).digest()

test_vectors = [
    0x9c1185a5c5e9fc54612808977ee8f548b2258d31,
    0x0bdc9d2d256b3ee9daae347be6f4dc835a467ffe,
    0x8eb208f7e05d987a9b044a8e98c6b087f15a0bfc,
    0x5d0689ef49d2fae572b881b123a85ffa21595f36,
    0xf71c27109c692c1b56bbdceb5b9d2865b3708dbc,
    0xb0e20b6e3116640286ed3a87a5713079b21f5189,
    0x9b752e45573d4b39f4dbd3323cab82bf63326bfb]


ass(test_vectors, [hash(s) for s in test_vector_strings], "test vectors")

k = [0x00000000, 0x5A827999, 0x6ED9EBA1, 0x8F1BBCDC, 0xA953FD4E]
K = [0x50A28BE6, 0x5C4DD124, 0x6D703EF3, 0x7A6D76E9, 0x00000000]
IVs = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0]


r = [
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
    (7, 4, 13, 1, 10, 6, 15, 3, 12, 0, 9, 5, 2, 14, 11, 8),
    (3, 10, 14, 4, 9, 15, 8, 1, 2, 7, 0, 6, 13, 11, 5, 12),
    (1, 9, 11, 10, 0, 8, 12, 4, 13, 3, 7, 15, 14, 5, 6, 2),
    (4, 0, 5, 9, 7, 12, 2, 10, 14, 1, 3, 8, 11, 6, 15, 13)]

R = [
    (5, 14, 7, 0, 9, 2, 11, 4, 13, 6, 15, 8, 1, 10, 3, 12),
    (6, 11, 3, 7, 0, 13, 5, 10, 14, 15, 8, 12, 4, 9, 1, 2),
    (15, 5, 1, 3, 7, 14, 6, 9, 11, 8, 12, 2, 10, 0, 4, 13),
    (8, 6, 4, 1, 3, 11, 15, 0, 5, 12, 2, 13, 9, 7, 10, 14),
    (12, 15, 10, 4, 1, 5, 8, 7, 6, 2, 13, 14, 0, 3, 9, 11)]


class test(ripemd160):
    def __init__(self):
        ripemd160.__init__(self)
        ass(self.IVs,IVs, "IVs")
        ass(self.ks, k , "K")
        ass(self.Ks, K, "K'")
        r_values = zip(*[self.rs(i) for i in range(16)])
        R_values = zip(*[self.Rs(i) for i in range(16)])
        ass(r_values, r, "r values")
        ass(R_values, R, "r' values")

#for s, S, r, R, f, F, k, K in rounds_parameters():
#    print "%02i" % s, "%02i" % r, f.__name__, "%08X" % k, "%02i" % S, "%02i" % R, F.__name__, "%08X" % K

test()