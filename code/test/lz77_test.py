#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python

from code.lz77 import *

assert compress("abracadabra") == [
    {'length': 0, 'offset': 0, 'symbol': 'a'},
    {'length': 0, 'offset': 0, 'symbol': 'b'},
    {'length': 0, 'offset': 0, 'symbol': 'r'},
    {'length': 1, 'offset': 3, 'symbol': 'c'},
    {'length': 1, 'offset': 2, 'symbol': 'd'},
    {'length': 4, 'offset': 7, 'symbol': ''}] 

assert decompress(compress("abracadabra")) == "abracadabra"