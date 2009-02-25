#
#Kabopan - Readable Algorithms. Public Domain, 2007-2009

from kbp.comp.brieflz import compress, decompress

assert compress("aba").do()         == 'a\x00\x00ba'
assert compress("abababababa").do() == 'a\x00\x18bab\x03ba'
assert compress("abracadabra").do() == 'a\x00\x02bracad\x06'

assert decompress('a\x00\x00ba'        ).do() == ("aba", 5)
assert decompress('a\x00\x18bab\x03ba' ).do() == ("abababababa", 9)
assert decompress('a\x00\x02bracad\x06').do() == ("abracadabra", 10)
