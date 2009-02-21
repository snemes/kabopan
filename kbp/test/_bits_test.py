#
#Kabopan - Readable Algorithms. Public Domain, 2007-2009

from kbp._bits import *

assert "".join(str(int(i)) for i in bits("AE")) == "01000001" + "01000101"
assert "".join(str(int(i)) for i in bits("AE",bit7_first=False)) == "10000010" + "10100010"

assert reverse(10341313, 32) == 2211690752
assert reverse(reverse(10341313, 32),32) == 10341313

c = compress(1);c.write_bit(1); assert c.getdata() == "\x80"
c = compress(2);c.write_bit(1); assert c.getdata() == "\x00\x80"
c = compress(2);c.write_variablenumber(109); assert c.getdata() == "`\xdf"
c = compress(2);c.write_fixednumber(109,9); assert c.getdata() == '\x806'
 
#c = compress(2);c.write_bit(1);c.write_fixednumber(15,5);c.write_variablenumber(2049);
#test = c.getdata()
test = 'U\xbd`U'
d = decompress(test, 2)
assert d.read_bit() == 1
assert d.read_fixednumber(5) == 15
assert d.read_variablenumber() == 2049