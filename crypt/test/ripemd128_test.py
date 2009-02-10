#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python

from crypt.ripemd128 import *
from _misc import test_vector_strings, ass

hash = lambda x:ripemd128().compute(x).digest()

test_vectors = [
    0xcdf26213a150dc3ecb610f18f6b38b46,
    0x86be7afa339d0fc7cfc785e72f578d33,
    0xc14a12199c66e4ba84636b0f69144c77,
    0x9e327b3d6e523062afc1132d7df9d1b8,
    0xfd2aa607f71dc8f510714922b371834e,
    0xd1e959eb179c911faea4624c60c5c702,
    0x3f45ef194732c2dbb2c4a2c769795fa3]

ass(test_vectors, [hash(s) for s in test_vector_strings], "test vectors")

IVs = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476]
class test(ripemd128):
    def __init__(self):
        ripemd128.__init__(self)
        ass(self.IVs, IVs, "IVs")

        ass(self.ks, [0x00000000, 0x5A827999, 0x6ED9EBA1, 0x8F1BBCDC], "K")
        ass(self.Ks, [0x50A28BE6, 0x5C4DD124, 0x6D703EF3, 0x00000000], "K'")

test()