#
#Kabopan - Readable Algorithms. Public Domain, 2009

from kbp.coder.lz78 import *

assert compress("abracadabra") == [
    {'index': 0, 'symbol': 'a'}, {'index': 0, 'symbol': 'b'}, {'index': 0, 'symbol': 'r'},
    {'index': 1, 'symbol': 'c'}, {'index': 1, 'symbol': 'd'},
    {'index': 1, 'symbol': 'b'}, {'index': 3, 'symbol': 'a'}]

assert decompress(compress("abracadabra")) == "abracadabra"
