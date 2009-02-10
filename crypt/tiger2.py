#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python

"""tiger2 is tiger, with sha-like padding (big-endian) instead of md4-like padding"""

from tiger import *

class tiger2(tiger):
    def __init__(self):
        tiger.__init__(self)
        self.pad_bit_7 = True

if __name__ == "__main__":
    import test.tiger2_test