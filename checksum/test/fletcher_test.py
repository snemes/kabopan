#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python

from checksum.fletcher import *
print "%x" % fletcher32("abracadabra")
assert fletcher32("abracadabra") == 0x19E70454