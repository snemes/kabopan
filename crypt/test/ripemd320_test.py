#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python

from crypt.ripemd320 import *
from _misc import test_vector_strings, ass

hash = lambda x: ripemd320().compute(x).digest()

IVs = [
    0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476, 0xc3d2e1f0,
    0x76543210, 0xfedcba98, 0x89abcdef, 0x01234567, 0x3c2d1e0f]

test_vectors = [
    0x22d65d5661536cdc75c1fdf5c6de7b41b9f27325ebc61e8557177d705a0ec880151c3a32a00899b8,
    0xce78850638f92658a5a585097579926dda667a5716562cfcf6fbe77f63542f99b04705d6970dff5d,
    0xde4c01b3054f8930a79d09ae738e92301e5a17085beffdc1b8d116713e74f82fa942d64cdbc4682d,
    0x3a8e28502ed45d422f68844f9dd316e7b98533fa3f2a91d29f84d425c88d6b4eff727df66a7c0197,
    0xcabdb1810b92470a2093aa6bce05952c28348cf43ff60841975166bb40ed234004b8824463e6b009,
    0xed544940c86d67f250d232c30b7b3e5770e0c60c8cb9a4cafe3b11388af9920e1b99230b843c86a4,
    0x557888af5f6d8ed62ab66945c6d2a0a47ecd5341e915eb8fea1d0524955f825dc717e4a008ab2d42]

ass(test_vectors, [hash(s) for s in test_vector_strings], "test vectors")

class test(ripemd320):
    def __init__(self):
        ripemd320.__init__(self)
        ass(self.IVs, IVs, "IVs")
test()
