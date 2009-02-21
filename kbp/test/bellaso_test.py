#
#Kabopan - Readable Algorithms. Public Domain, 2007-2009

from kbp.coder.bellaso import *

assert first_sifra("larmatatvrchescapa rtiraacinqvedilvgl io", "virtvtiomniaparent virtvtiomniaparent vi") == \
        "syboveyldanvofszlp iincvpnshmlrnxoizn rd"

assert second_sifra("giul ioce sare","qui confidunt in domino",
        "arma uirumque cano troie qui primus ab oris") == "nqhp msgn xdyt"

#this cipher is reciprocal
assert second_sifra("nqhp msgn xdyt","qui confidunt in domino",
        "arma uirumque cano troie qui primus ab oris") == "giul ioce sare"
