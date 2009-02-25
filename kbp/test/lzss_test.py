#
#Kabopan - Readable Algorithms. Public Domain, 2007-2009

from kbp.coder.lzss import compress, decompress

assert compress("abracadabra") == [
    {'literal': True, 'symbol': 'a'},
    {'literal': True, 'symbol': 'b'},
    {'literal': True, 'symbol': 'r'},
    {'literal': False, 'length': 1, 'offset': 3},
    {'literal': True, 'symbol': 'c'},
    {'literal': False, 'length': 1, 'offset': 2},
    {'literal': True, 'symbol': 'd'},
    {'literal': False, 'length': 4, 'offset': 7}]

assert decompress(compress("abracadabra")) == "abracadabra"

