#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python
from code.aplib import *

assert decompress(compress("a").do()).do() == ("a", 3)
assert decompress(compress("ababababababab").do()).do() == ('ababababababab', 9)
assert decompress(compress("aaaaaaaaaaaaaacaaaaaa").do()).do() == ('aaaaaaaaaaaaaacaaaaaa', 11)