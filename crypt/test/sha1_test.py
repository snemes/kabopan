#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python

from crypt.sha1 import *
from _misc import test_vector_strings

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


