#
#Kabopan - Readable Algorithms. Public Domain, 2007-2009

from kbp.checksum.crc import *


assert or_all ([1, 1 << 31]) == 0x80000001

tests = [
    # polynom name exponents                                               root        reversed    width
    ["CRC32_IEEE", [32, 26, 23, 22, 16, 12, 11, 10, 8, 7, 5, 4, 2, 1, 0], (0x04C11DB7, 0xEDB88320, 32)]
    ]
for polynom_name, exponents, info in tests:
    polynom = CRCs[polynom_name]["polynom"]
    assert exponents == get_exponents(polynom)
    assert generate_root(polynom) == info

test_strings = ["", "123456789", "abracadabra"]
tests = [
    [crc32_ieee, [0x00000000, 0xCBF43926, 0x17EAF9B7]]
    ]

for function, values in tests:
    for i, s in enumerate(test_strings):
        expected_value = values[i]
        test_value = function(s)
        try:
            assert expected_value == test_value
        except:
            print "function %s, string %s: expected %x, got %x" % (function.__name__, s, expected_value, test_value)