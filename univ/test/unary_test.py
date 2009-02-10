#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python

from unary import *

assert encode(0) == "1"
assert encode(1) == "01"
assert encode(5) == "000001"
assert encode(5, False) == "111110"

assert decode("1") == (0, 1)
assert decode("000001") == (5, 6)
