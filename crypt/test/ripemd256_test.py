#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python

from crypt.ripemd256 import *
from _misc import test_vector_strings, ass

hash = lambda x: ripemd256().compute(x).digest()

IVs = [
    0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 
    0x76543210, 0xFEDCBA98, 0x89ABCDEF, 0x01234567]


test_vectors = [
    0x02ba4c4e5f8ecd1877fc52d64d30e37a2d9774fb1e5d026380ae0168e3c5522d,
    0xf9333e45d857f5d90a91bab70a1eba0cfb1be4b0783c9acfcd883a9134692925,
    0xafbd6e228b9d8cbbcef5ca2d03e6dba10ac0bc7dcbe4680e1e42d2e975459b65,
    0x87e971759a1ce47a514d5c914c392c9018c7c46bc14465554afcdf54a5070c0e,
    0x649d3034751ea216776bf9a18acc81bc7896118a5197968782dd1fd97d8d5133,
    0x5740a408ac16b720b84424ae931cbb1fe363d1d0bf4017f1a89f7ea6de77a0b8,
    0x06fdcc7a409548aaf91368c06a6275b553e3f099bf0ea4edfd6778df89a890dd]


ass(test_vectors, [hash(s) for s in test_vector_strings], "test vectors")

class test(ripemd256):
    def __init__(self):
        ripemd256.__init__(self)
        ass(self.IVs, IVs, "IVs")
test()
