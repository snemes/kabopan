#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python

from coder.ascii85 import *

assert ASCII85 == """!"#$%&'()*+,-./""" + DIGITS + ":;<=>?@" + ALPHABET + "[\]^_`" + char_range("a", "u")

assert merge([77, 97, 110, 32], 256) == 1298230816
assert split(1298230816, 85) == [24, 73, 80, 78, 61]
assert split(1298230816, 85, 7) == [0, 0, 24, 73, 80, 78, 61]

leviathan = "Man is distinguished, not only by his reason, " \
"but by this singular passion from other animals, which is a lust of the mind," \
" that by a perseverance of delight in the continued and indefatigable generation of knowledge," \
" exceeds the short vehemence of any carnal pleasure."
ascii85_leviathan = \
"<~9jqo^BlbD-BleB1DJ+*+F(f,q/0JhKF<GL>Cj@.4Gp$d7F!,L7@<6@)/0JDEF<G%<+EV:2F!," \
"O<DJ+*.@<*K0@<6L(Df-\\0Ec5e;DffZ(EZee.Bl.9pF\"AGXBPCsi+DGm>@3BB/F*&OCAfu2/AKY" \
"i(DIb:@FD,*)+C]U=@3BN#EcYf8ATD3s@q?d$AftVqCh[NqF<G:8+EV:.+Cf>-FD5W8ARlolDIa" \
"l(DId<j@<?3r@:F%a+D58'ATD4$Bl@l3De:,-DJs`8ARoFb/0JMK@qB4^F!,R<AKZ&-DfTqBG%G" \
">uD.RTpAKYo'+CT/5+Cei#DII?(E,9)oF*2M7/c~>"

for s in (DIGITS[:i] for i in range(8)):
    assert s == decode(encode(s))

assert encode(leviathan) == ascii85_leviathan
assert decode(ascii85_leviathan) == leviathan
