#Kabopan - Readable Algorithms. Public Domain, 2009

from univ.elias import *

assert elias_split(1) == (0, "")
assert elias_split(14) == (3, "110")

assert gamma_encode(1) == "1"
assert gamma_encode(2) == "010"
assert gamma_encode(14) == "0001" + "110"

assert gamma_decode("000010001") == (17, 9)
assert gamma_decode("00001000100") == (17, 9)

assert interleaved_gamma_encode(14) == "101001"

assert interleaved_gamma_decode("101001") == (14, 6)

assert delta_encode(17) == "001010001"

assert delta_decode("001010001") == (17, 9)

assert [omega_encode(i) for i in range(1, 18)] ==  ['0', '100', '110', '101000', '101010', '101100', '101110', '1110000',
        '1110010', '1110100', '1110110', '1111000', '1111010', '1111100', '1111110', '10100100000', '10100100010']

assert omega_decode('10100100010') == (17, 11)
assert omega_decode('1010010001000') == (17, 11)
