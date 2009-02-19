#
#Kabopan - Readable Algorithms. Public Domain, 2009

from univ.fibonacci import *

assert number(20) == 6765

assert generate_numbers(20) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]

assert decompose(10) == [3,6]
assert decompose(6764) == [3, 5, 7, 9, 11, 13, 15, 17, 19]

assert recompose(decompose(6764)) == 6764

assert encode(7) == "001011"
assert encode(6764) ==  "00101010101010101011"

assert decode("01011") == 4
assert decode("001011") == 7
