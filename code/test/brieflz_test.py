#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python

from code.brieflz import *

assert compress("aba").do()         == 'a\x00\x00ba'
assert compress("abababababa").do() == 'a\x00\x18bab\x03ba'
assert compress("abracadabra").do() == 'a\x00\x02bracad\x06'

assert decompress('a\x00\x00ba'        ).do() == ("aba", 5)
assert decompress('a\x00\x18bab\x03ba' ).do() == ("abababababa", 9)
assert decompress('a\x00\x02bracad\x06').do() == ("abracadabra", 10)
