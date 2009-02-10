#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python

from code.rot import *

assert ASCII33_126  == "!\"#$%&'()*+,-./" + DIGITS  + ":;<=>?@" + ALPHABET  + \
    "[\\]^_`" + ALPHABET_LOWERCASE + "{|}~"

assert rot13("How can you tell an extrovert from an introvert at NSA?" 
    "Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.") ==  \
    "Ubj pna lbh gryy na rkgebireg sebz na vagebireg ng AFN?" \
    "In the elevators, the extrovert looks at the OTHER guy's shoes."

assert rot47("The Quick Brown Fox Jumps Over The Lazy Dog.") == \
    "%96 \"F:4< qC@H? u@I yF>AD ~G6C %96 {2KJ s@8]"

assert caesar_encode("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG") == \
    "WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ"

assert caesar_decode("WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ") == \
    "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"