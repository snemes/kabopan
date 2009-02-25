#
#Kabopan - Readable Algorithms. Public Domain, 2007-2009

from kbp.comp.lz77 import compress, decompress

assert compress("abracadabra") == [
    {'length': 0, 'offset': 0, 'symbol': 'a'},
    {'length': 0, 'offset': 0, 'symbol': 'b'},
    {'length': 0, 'offset': 0, 'symbol': 'r'},
    {'length': 1, 'offset': 3, 'symbol': 'c'},
    {'length': 1, 'offset': 2, 'symbol': 'd'},
    {'length': 4, 'offset': 7, 'symbol': ''}] 

assert decompress(compress("abracadabra")) == "abracadabra"