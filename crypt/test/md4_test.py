#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python

from _misc import rol, hex2bin
from crypt.md4 import *

from _misc import test_vector_strings

test_vectors = [
    0x31d6cfe0d16ae931b73c59d7e0c089c0,
    0xbde52cb31de33e46245e05fbdbd6fb24,
    0xa448017aaf21d8525fc10ae87aa6729d,
    0xd9130a8164549fe818874806e1c7014b,
    0xd79e1c308aa5bbcdeea8ed63df412da9,
    0x043f8582f241db351ce627e153e7f0e4,
    0xe33b4ddc9c38f2199c3e7b164fcc0536]

test_IVs = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476]
hash = lambda x: md4().compute(x).digest()
assert [hash(s) for s in test_vector_strings] == test_vectors

# collision, XiaoyunWang, Dengguo Feng, Xuejia Lai, Hongbo Yu, 2004

a = [
"839c7a4d 7a92cb56 78a5d5b9 eea5a757 3c8a74de b366c3dc 20a083b6 9f5d2a3b",
"b3719dc6 9891e9f9 5e809fd7 e8b23ba6 318edd45 e51fe397 08bf9427 e9c3e8b9"]

b = [
"839c7a4d 7a92cbd6 78a5d529 eea5a757 3c8a74de b366c3dc 20a083b6 9f5d2a3b",
"b3719dc6 9891e9f9 5e809fd7 e8b23ba6 318edc45 e51fe397 08bf9427 e9c3e8b9"]

a, b = [hex2bin("".join(s).replace(" ", "")) for s in [a, b]]


assert hash(a) == hash(b)
md4_rounds = [
    'A BCD 00 03 f 0x00000000',
    'D ABC 01 07 f 0x00000000',
    'C DAB 02 11 f 0x00000000',
    'B CDA 03 19 f 0x00000000',
    'A BCD 04 03 f 0x00000000',
    'D ABC 05 07 f 0x00000000',
    'C DAB 06 11 f 0x00000000',
    'B CDA 07 19 f 0x00000000',
    'A BCD 08 03 f 0x00000000',
    'D ABC 09 07 f 0x00000000',
    'C DAB 10 11 f 0x00000000',
    'B CDA 11 19 f 0x00000000',
    'A BCD 12 03 f 0x00000000',
    'D ABC 13 07 f 0x00000000',
    'C DAB 14 11 f 0x00000000',
    'B CDA 15 19 f 0x00000000',
    'A BCD 00 03 g 0x5A827999',
    'D ABC 04 05 g 0x5A827999',
    'C DAB 08 09 g 0x5A827999',
    'B CDA 12 13 g 0x5A827999',
    'A BCD 01 03 g 0x5A827999',
    'D ABC 05 05 g 0x5A827999',
    'C DAB 09 09 g 0x5A827999',
    'B CDA 13 13 g 0x5A827999',
    'A BCD 02 03 g 0x5A827999',
    'D ABC 06 05 g 0x5A827999',
    'C DAB 10 09 g 0x5A827999',
    'B CDA 14 13 g 0x5A827999',
    'A BCD 03 03 g 0x5A827999',
    'D ABC 07 05 g 0x5A827999',
    'C DAB 11 09 g 0x5A827999',
    'B CDA 15 13 g 0x5A827999',
    'A BCD 00 03 h 0x6ED9EBA1',
    'D ABC 08 09 h 0x6ED9EBA1',
    'C DAB 04 11 h 0x6ED9EBA1',
    'B CDA 12 15 h 0x6ED9EBA1',
    'A BCD 02 03 h 0x6ED9EBA1',
    'D ABC 10 09 h 0x6ED9EBA1',
    'C DAB 06 11 h 0x6ED9EBA1',
    'B CDA 14 15 h 0x6ED9EBA1',
    'A BCD 01 03 h 0x6ED9EBA1',
    'D ABC 09 09 h 0x6ED9EBA1',
    'C DAB 05 11 h 0x6ED9EBA1',
    'B CDA 13 15 h 0x6ED9EBA1',
    'A BCD 03 03 h 0x6ED9EBA1',
    'D ABC 11 09 h 0x6ED9EBA1',
    'C DAB 07 11 h 0x6ED9EBA1',
    'B CDA 15 15 h 0x6ED9EBA1']




class test(md4):
    def __init__(self):
        md4.__init__(self)
        assert [int(i) for i in self.IVs] == test_IVs

        # check that we generate the usual representation of md4 rounds
        l = list()
        ABCD = ["A", "B", "C", "D"]
        
        for r in range(3):  # rounds
            f, constant = self.functions[r], self.constants[r]
            for i in range(16): # iterations per round
                [a, b, c, d] = [((j - i) % 4) for j in range(4)]
                s = self.shifts[r][i % 4]
                k = self.r(i)[r]
        
                s = "%s %s%s%s %02i %02i %s 0x%08X" % (ABCD[a], ABCD[b], ABCD[c], ABCD[d], k, s, f.__name__, constant)
                l.append(s)
        
        assert l == md4_rounds

test()
