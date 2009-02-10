#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python

from lzw import *

assert compress("abracadabra") == (['a', 'r', 'b', 'c', 'd'],
                                   [0, 2, 1, 0, 3, 0, 4, 5, 7])

assert decompress(*compress("abracadabra")) == "abracadabra"

