#
#Kabopan - Readable Algorithms. Public Domain, 2009

from kbp._misc import *

assert char_range("A", "Z") == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#gcd
#returns the greatest common divisor of both parameters
assert gcd(6, 8) == 2

#lcm
#returns the least common multiplier of both parameters
assert lcm(6,9) == 18
assert lcm(6,8) == 24

assert getbinlen(0) == 1
assert getbinlen(1) == 1
assert getbinlen(3) == 2

assert getvaluefrombinarystring("1000") == 8
assert getvaluefrombinarystring("001000") == 8

assert getpadbinstr(8, 8) == "00001000"

assert getunkbinstr(0,0,8) == "000000000"
assert getunkbinstr(1,0,8) == "000000001"
assert getunkbinstr(2,1,8) == "00000001x"
assert getunkbinstr(237,3,8) == "011101xxx"

assert gethexstr("\x00") == "00"
assert gethexstr("\x00\x01") == "00 01"
assert gethexstr("abcd") == "61 62 63 64"

assert int2lebin(1,2) == '\x01\x00'
assert int2lebin(65535,2) == "\xff\xff"
assert int2lebin(65535,3) == "\xff\xff\x00"

assert int2bebin(1,2) == '\x00\x01'

assert md5("") == "d41d8cd98f00b204e9800998ecf8427e"

assert modifystring("abcd","_",2) == "ab_d"
assert modifystring("abcde","=+",2) == "ab=+e"

assert getlongestcommon("31415926535", "31416")  == 4


assert gethyphenstr(r"c:\WINDOWS\system32\drivers\http.sys") == r"c:\WINDOW [...] \http.sys"

assert getbinstr(0) == "0"
assert getbinstr(8) == "1000"

assert countmissing(0,8) == 0
assert countmissing(3,8) == 5
assert countmissing(8,8) == 0

assert insert_string("abcd", 2, "1") == "ab1cd"

assert zip([1,2], [0]) == [(1,0)]
assert zip_extend([1,2], [0], 0) == [(1,0), (2,0)]
assert zip_extend([0], [1,2], 0) == [(1,0), (2,0)]

assert rorstr("abc") == "cab"
assert [rorstr("abc", i) for i in range(4)] == ['abc', 'cab', 'bca', 'abc']

assert setstr("abcde","d") == "deabc"

