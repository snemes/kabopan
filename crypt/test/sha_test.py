
#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python

from crypt.sha import *
from _misc import test_vector_strings, hex2bin, ass

IVs = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0]

class test(sha0):
    def __init__(self):
        sha0.__init__(self)
        assert [int(i) for i in self.IVs] == IVs
test()

hash = lambda x: sha0().compute(x).digest()

for i, tv in enumerate(test_vector_strings):
    assert hash(tv) == [
    0xf96cea198ad1dd5617ac084a3d92c6107708c0ef,
    0x37f297772fae4cb1ba39b6cf9cf0381180bd62f2,
    0x0164b8a914cd2a5e74c4f7ff082c4d97f1edf880,
    0xc1b0f222d150ebb9aa36a40cafdc8bcbed830b14,
    0xb40ce07a430cfd3c033039b9fe9afec95dc1bdcd,
    0x79e966f7a3a990df33e40e3d7f8f18d2caebadfa,
    0x4aa29d14d171522ece47bee8957e35a41f3e9cff][i], "Sha-0 test vectors"


#full collision, by Antoine Joux, Patrick Carribault, Christophe Lemuet, William Jalby
a = [
    "a766a602 b65cffe7 73bcf258 26b322b3 d01b1a97 2684ef53 3e3b4b7f 53fe3762",
    "24c08e47 e959b2bc 3b519880 b9286568 247d110f 70f5c5e2 b4590ca3 f55f52fe",
    "effd4c8f e68de835 329e603c c51e7f02 545410d1 671d108d f5a4000d cf20a439",
    "4949d72c d14fbb03 45cf3a29 5dcda89f 998f8755 2c9a58b1 bdc38483 5e477185",
    "f96e68be bb0025d2 d2b69edf 21724198 f688b41d eb9b4913 fbe696b5 457ab399",
    "21e1d759 1f89de84 57e8613c 6c9e3b24 2879d4d8 783b2d9c a9935ea5 26a729c0",
    "6edfc501 37e69330 be976012 cc5dfe1c 14c4c68b d1db3ecb 24438a59 a09b5db4",
    "35563e0d 8bdf572f 77b53065 cef31f32 dc9dbaa0 4146261e 9994bd5c d0758e3d"]
b = [
    "a766a602 b65cffe7 73bcf258 26b322b1 d01b1ad7 2684ef51 be3b4b7f d3fe3762",
    "a4c08e45 e959b2fc 3b519880 39286528 a47d110d 70f5c5e0 34590ce3 755f52fc",
    "6ffd4c8d 668de875 329e603e 451e7f02 d45410d1 e71d108d f5a4000d cf20a439",
    "4949d72c d14fbb01 45cf3a69 5dcda89d 198f8755 ac9a58b1 3dc38481 5e4771c5",
    "796e68fe bb0025d0 52b69edd a17241d8 7688b41f 6b9b4911 7be696f5 c57ab399",
    "a1e1d719 9f89de86 57e8613c ec9e3b26 a879d498 783b2d9e 29935ea7 a6a72980",
    "6edfc503 37e69330 3e976010 4c5dfe5c 14c4c689 51db3ecb a4438a59 209b5db4",
    "35563e0d 8bdf572f 77b53065 cef31f30 dc9dbae0 4146261c 1994bd5c 50758e3d"]

a, b = [hex2bin("".join(s).replace(" ", "")) for s in [a, b]]

assert hash(a) == hash(b)

def hash(msg):
    m = sha1()
    m.compute(msg)
    return m.digest()

assert [hash(s) for s in test_vector_strings] == [
    0xDA39A3EE5E6B4B0D3255BFEF95601890AFD80709,
    0x86F7E437FAA5A7FCE15D1DDCB9EAEAEA377667B8,
    0xA9993E364706816ABA3E25717850C26C9CD0D89D,
    0xC12252CEDA8BE8994D5FA0290A47231C1D16AAE3,
    0x32D10C7B8CF96570CA04CE37F2A19D84240D3A89,
    0x761C457BF73B14D27E9E9265C46F4B4DDA11F940,
    0x50ABF5706A150990A08B2C5EA40FA0E585554732]
