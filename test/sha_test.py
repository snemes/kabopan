#Kabopan - Readable Algorithms. Public Domain, 2009
"""tests for sha-0 and sha-1"""

from crypt.sha import *
from _misc import test_vector_strings, hex2bin, ass
from _int import add_string

hash0 = lambda x: sha0().compute(x).digest()

IVs = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0]

sha0_test_vectors = [
    0xf96cea198ad1dd5617ac084a3d92c6107708c0ef,
    0x37f297772fae4cb1ba39b6cf9cf0381180bd62f2,
    0x0164b8a914cd2a5e74c4f7ff082c4d97f1edf880,
    0xc1b0f222d150ebb9aa36a40cafdc8bcbed830b14,
    0xb40ce07a430cfd3c033039b9fe9afec95dc1bdcd,
    0x79e966f7a3a990df33e40e3d7f8f18d2caebadfa,
    0x4aa29d14d171522ece47bee8957e35a41f3e9cff]

ass(IVs, IVs, "sha-0 IVs")
ass(sha0_test_vectors, [hash0(s) for s in test_vector_strings], "sha-0 test vectors")

#full collision, by Antoine Joux, Patrick Carribault, Christophe Lemuet, William Jalby
a = \
 "a766a602 b65cffe7 73bcf258 26b322b3 d01b1a97 2684ef53 3e3b4b7f 53fe3762"\
 "24c08e47 e959b2bc 3b519880 b9286568 247d110f 70f5c5e2 b4590ca3 f55f52fe"\
 "effd4c8f e68de835 329e603c c51e7f02 545410d1 671d108d f5a4000d cf20a439"\
 "4949d72c d14fbb03 45cf3a29 5dcda89f 998f8755 2c9a58b1 bdc38483 5e477185"\
 "f96e68be bb0025d2 d2b69edf 21724198 f688b41d eb9b4913 fbe696b5 457ab399"\
 "21e1d759 1f89de84 57e8613c 6c9e3b24 2879d4d8 783b2d9c a9935ea5 26a729c0"\
 "6edfc501 37e69330 be976012 cc5dfe1c 14c4c68b d1db3ecb 24438a59 a09b5db4"\
 "35563e0d 8bdf572f 77b53065 cef31f32 dc9dbaa0 4146261e 9994bd5c d0758e3d"

delta = \
 "________ ________ ________ _______1 ______d_ _______1 b_______ d_______"\
 "a______5 ______f_ ________ 3_____2_ a______d _______0 3_____e_ 7______c"\
 "6______d 6_____7_ _______e 4_______ d_______ e_______ ________ ________"\
 "________ _______1 ______6_ _______d 1_______ a_______ 3______1 ______c_"\
 "7_____f_ _______0 5______d a_____d_ 7______f 6______1 7_____f_ c_______"\
 "a_____1_ 9______6 ________ e______6 a_____9_ _______e 2______7 a_____8_"\
 "_______3 ________ 3______0 4_____5_ _______9 5_______ a_______ 2_______"\
 "________ ________ ________ _______0 ______e_ _______c 1_______ 5_______" 

a = a.replace(" ","")
delta = delta.replace(" ","")
b = add_string(a, delta)
a, b = [hex2bin("".join(s).replace(" ", "")) for s in [a, b]]

ass(hash0(a), hash0(b), "sha-0 collision")

#sha-1
hash1 = lambda x: sha1().compute(x).digest()


sha1_test_vectors = [
    0xDA39A3EE5E6B4B0D3255BFEF95601890AFD80709,
    0x86F7E437FAA5A7FCE15D1DDCB9EAEAEA377667B8,
    0xA9993E364706816ABA3E25717850C26C9CD0D89D,
    0xC12252CEDA8BE8994D5FA0290A47231C1D16AAE3,
    0x32D10C7B8CF96570CA04CE37F2A19D84240D3A89,
    0x761C457BF73B14D27E9E9265C46F4B4DDA11F940,
    0x50ABF5706A150990A08B2C5EA40FA0E585554732]

ass(sha1_test_vectors, [hash1(s) for s in test_vector_strings], "sha-1 test vectors")

#70 rounds collision,
#Collisions for 70-step SHA-1: On the Full Cost of Collision Search
#Christophe De Canniere, Florian Mendel, and Christian Rechberger, 2007

class sha1_70r(sha1):
    def rounds(self, words):
        [a, b, c, d, e] = list(self.ihvs)
        for round_ in range(4):
            f = sha_u.functions[round_]
            k = sha_u.constants[round_]
            ranges = [20,20,20,10][round_]
            for i in range(ranges):
                [a, b, c, d, e] = sha_u.round_f(a, b, c, d, e, f, 5, 30, words, i + 20 * round_, k)
        return [a, b, c, d, e]

a = \
 "3bb33aae 85aecbbb 57a88417 8137cb9c 4de99220 5b6f12c7 726bd948 e3f6e9b8"\
 "23607799 239b2f1d aac76b94 e8009a1e c24de871 5b7c30d8 000359f5 90f9ed31"\
 "abddbee2 42a20ac7 a915e04d 5063b027 4ddf989a e0020cf7 7ffdc0f4 efefe0a7"\
 "0ffbc2f0 c8de16bf 81bbe675 254429cb 5f37a2c6 cd1963d3 ffca1cb9 9642cb56"

delta = \
 "a_____d_ 3_____e8 6______f ______df 9_____52 e_____d_ 8_____2a 2_____fa"\
 "______a_ c_____5f 8_____f_ 0_____5f e_____2_ 9_____99 e_____87 3______2"\
 "3_____9_ f_____94 9______5 ______64 9_____e8 5_____e_ 8_____96 2_____e5"\
 "______c_ 2_____fd a_____1_ c_____8a 7_____9_ 0_____92 1_____cb 3______5"

a = a.replace(" ","")
delta = delta.replace(" ","")
b = add_string(a, delta)
a, b = [hex2bin("".join(s).replace(" ", "")) for s in [a, b]]

hash1_70r = lambda x: sha1_70r().compute(x).digest()
assert hash1_70r(a) == hash1_70r(b)
