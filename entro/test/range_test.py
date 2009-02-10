#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python

from code.range import *

assert common_string(0.123,0.125) == "0.124"

assert do('b')   == (Fraction(0, 1), Fraction(1, 1))
assert do('ba')  == (Fraction(1, 2), Fraction(3, 4))
assert do('bab') == (Fraction(11, 27), Fraction(5, 9))
assert do('baba') == (Fraction(5, 8), Fraction(11, 16))
assert do("ABRACADABRA") == (Fraction(7231059615, 25937424601), Fraction(79541705765, 285311670611))
assert do("NMLNNNKKNML") == (Fraction(210964889166, 285311670611), Fraction(210965089166, 285311670611))