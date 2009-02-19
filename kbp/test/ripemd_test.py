#Kabopan - Readable Algorithms. Public Domain, 2009
"""tests for ripemd-160, ripemd-128, ripemd-256 and ripemd-320"""

from kbp.crypt.ripemd import *
from kbp._misc import test_vector_strings, ass, nibbleswap

k = [0x00000000, 0x5A827999, 0x6ED9EBA1, 0x8F1BBCDC, 0xA953FD4E]
K = [0x50A28BE6, 0x5C4DD124, 0x6D703EF3, 0x7A6D76E9, 0x00000000]

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

r_values = zip(*[ripemd160_u.rs[i] for i in range(16)])
R_values = zip(*[ripemd160_u.Rs[i] for i in range(16)])

ripemd160_test_vectors = [
    0x9c1185a5c5e9fc54612808977ee8f548b2258d31,
    0x0bdc9d2d256b3ee9daae347be6f4dc835a467ffe,
    0x8eb208f7e05d987a9b044a8e98c6b087f15a0bfc,
    0x5d0689ef49d2fae572b881b123a85ffa21595f36,
    0xf71c27109c692c1b56bbdceb5b9d2865b3708dbc,
    0xb0e20b6e3116640286ed3a87a5713079b21f5189,
    0x9b752e45573d4b39f4dbd3323cab82bf63326bfb]


ripemd320_IVs = [
    0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476, 0xc3d2e1f0,
    0x76543210, 0xfedcba98, 0x89abcdef, 0x01234567, 0x3c2d1e0f]

ripemd320_test_vectors = [
    0x22d65d5661536cdc75c1fdf5c6de7b41b9f27325ebc61e8557177d705a0ec880151c3a32a00899b8,
    0xce78850638f92658a5a585097579926dda667a5716562cfcf6fbe77f63542f99b04705d6970dff5d,
    0xde4c01b3054f8930a79d09ae738e92301e5a17085beffdc1b8d116713e74f82fa942d64cdbc4682d,
    0x3a8e28502ed45d422f68844f9dd316e7b98533fa3f2a91d29f84d425c88d6b4eff727df66a7c0197,
    0xcabdb1810b92470a2093aa6bce05952c28348cf43ff60841975166bb40ed234004b8824463e6b009,
    0xed544940c86d67f250d232c30b7b3e5770e0c60c8cb9a4cafe3b11388af9920e1b99230b843c86a4,
    0x557888af5f6d8ed62ab66945c6d2a0a47ecd5341e915eb8fea1d0524955f825dc717e4a008ab2d42]


ripemd128_IVs = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476]

ripemd128_test_vectors = [
    0xcdf26213a150dc3ecb610f18f6b38b46,
    0x86be7afa339d0fc7cfc785e72f578d33,
    0xc14a12199c66e4ba84636b0f69144c77,
    0x9e327b3d6e523062afc1132d7df9d1b8,
    0xfd2aa607f71dc8f510714922b371834e,
    0xd1e959eb179c911faea4624c60c5c702,
    0x3f45ef194732c2dbb2c4a2c769795fa3]


ripemd256_IVs = [
    0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 
    0x76543210, 0xFEDCBA98, 0x89ABCDEF, 0x01234567]

ripemd256_test_vectors = [
    0x02ba4c4e5f8ecd1877fc52d64d30e37a2d9774fb1e5d026380ae0168e3c5522d,
    0xf9333e45d857f5d90a91bab70a1eba0cfb1be4b0783c9acfcd883a9134692925,
    0xafbd6e228b9d8cbbcef5ca2d03e6dba10ac0bc7dcbe4680e1e42d2e975459b65,
    0x87e971759a1ce47a514d5c914c392c9018c7c46bc14465554afcdf54a5070c0e,
    0x649d3034751ea216776bf9a18acc81bc7896118a5197968782dd1fd97d8d5133,
    0x5740a408ac16b720b84424ae931cbb1fe363d1d0bf4017f1a89f7ea6de77a0b8,
    0x06fdcc7a409548aaf91368c06a6275b553e3f099bf0ea4edfd6778df89a890dd]

hash160 = lambda x:ripemd160().compute(x).digest()
hash128 = lambda x:ripemd128().compute(x).digest()
hash320 = lambda x:ripemd320().compute(x).digest()
hash256 = lambda x:ripemd256().compute(x).digest()

ass(ripemd160_u.ks, k , "ripemd160 K")
ass(ripemd160_u.Ks, K, "ripemd160 K'")
ass(r_values, r, "ripemd160 r")
ass(R_values, R, "ripemd160 r'")
ass(ripemd160_test_vectors, [hash160(s) for s in test_vector_strings], "ripemd160 test vectors")

ass(ripemd320_IVs, ripemd320_u.IVs, "ripemd320 IVs")
ass(ripemd320_test_vectors, [hash320(s) for s in test_vector_strings], "ripemd320 test vectors")

ass(ripemd128_u.IVs, ripemd128_IVs, "ripemd128 IVs")
ass(ripemd128_u.ks, [0x00000000, 0x5A827999, 0x6ED9EBA1, 0x8F1BBCDC], "ripemd128 K")
ass(ripemd128_u.Ks, [0x50A28BE6, 0x5C4DD124, 0x6D703EF3, 0x00000000], "ripemd128 K'")
ass(ripemd128_test_vectors, [hash128(s) for s in test_vector_strings], "ripemd128 test vectors")

ass(ripemd256_u.IVs, ripemd256_IVs, "ripemd256 IVs")
ass(ripemd256_test_vectors, [hash256(s) for s in test_vector_strings], "ripemd256 test vectors")

#for s, S, r, R, f, F, k, K in rounds_parameters():
#    print "%02i" % s, "%02i" % r, f.__name__, "%08X" % k, "%02i" % S, "%02i" % R, F.__name__, "%08X" % K
