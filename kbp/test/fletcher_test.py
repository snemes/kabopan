#Kabopan - Readable Algorithms. Public Domain, 2007-2009

from kbp.checksum.fletcher import *
print "%x" % fletcher32("abracadabra")
#assert fletcher32("abracadabra") == 0x19E70454