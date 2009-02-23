#Kabopan - Readable Algorithms. Public Domain, 2007-2009

from kbp.crypt.Pad import *

assert [remaining(x, y) for x, y in [[0, 4], [1, 4],[2, 4], [3, 4], [4, 4]] ] \
 == [0, 3, 2, 1, 0]


assert zero("0000" + "0", 32)   == "\x00\x00\x00"
assert zero("0000" + "00", 32)  == "\x00\x00"
assert zero("0000" + "000", 32) == "\x00"
assert zero("0000" + "", 32)    == ""


assert pkcs7("0000" + "0", 32)    == "\x03\x03\x03"
assert pkcs7("0000" + "00", 32)   == "\x02\x02"
assert pkcs7("0000" + "000", 32)  == "\x01"
assert pkcs7("0000" + "0000", 32) == ""


assert bit("", 32)     =='\x80\x00\x00\x00'
assert bit("0", 32)    =='\x80\x00\x00'    
assert bit("00", 32)   =='\x80\x00'        
assert bit("000", 32)  =='\x80'            
assert bit("0000", 32) =='\x80\x00\x00\x00'

