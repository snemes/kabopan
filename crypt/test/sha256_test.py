#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python

from crypt.sha256 import *
from _misc import test_vector_strings

assert [sha256().compute(s).digest() for s in test_vector_strings] == [
    0xe3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855,
    0xca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb,
    0xba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad,
    0xf7846f55cf23e14eebeab5b4e1550cad5b509e3348fbc4efa3a1413d393cb650,
    0x71c480df93d6ae2f1efad1447c66c9525e316218cf51fc8d9ed832f2daf18b73,
    0xdb4bfcbd4da0cd85a60c3c37d3fbd8805c77f15fc6b1fdfe614ee0a7c8fdb4c0,
    0xf371bc4a311f2b009eef952dd83ca80e2b60026c8e935592d0f9c308453c813e]

IVs = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]
K = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]
    
class test(sha256):
    def __init__(self):
        sha256.__init__(self)
        assert [int(i) for i in self.IVs] == IVs
        assert self.K == K
test()