#
#Kabopan - Readable Algorithms. Public Domain, 2009

from coder.lzw import *

assert compress("abracadabra") == (['a', 'r', 'b', 'c', 'd'],
                                   [0, 2, 1, 0, 3, 0, 4, 5, 7])

assert decompress(*compress("abracadabra")) == "abracadabra"

