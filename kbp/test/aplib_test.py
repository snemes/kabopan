#Kabopan - Readable Algorithms. Public Domain, 2007-2009
from kbp.coder.aplib import *

assert decompress(compress("a").do()).do() == ("a", 3)
assert decompress(compress("ababababababab").do()).do() == ('ababababababab', 9)
assert decompress(compress("aaaaaaaaaaaaaacaaaaaa").do()).do() == ('aaaaaaaaaaaaaacaaaaaa', 11)