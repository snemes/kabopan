#Kabopan - Readable Algorithms. Public Domain, 2007-2009

from kbp.types import ( \
 sub_string, add_string, 
 Str, List, 
 BYTE, DWORD, WORD, QWORD, OWORD, DQWORD)

assert sub_string("abc", "aBc") == "_B_"
assert add_string("abc", "_B_") == "aBc"

s = Str("abcdefghij")
assert [ s,           s << 1,       s >> 1,       (s << 1) >> 1, s << 2,       s << 3,      s << 4] == \
       ['abcdefghij', 'bcdefghija', 'jabcdefghi', 'abcdefghij', 'cdefghijab', 'defghijabc', 'efghijabcd']

assert s.setstart("d") == "defghijabc"

s = Str('abcaba')
assert s.indexes("a") == [0, 3, 5]
assert s.indexes("d") == []

s = Str("abcdefghij")
import pprint
assert [s.insert("1", 2), s.insert("12", 2), s.overwrite("1", 2), s.overwrite("12", 2)] == \
       ['ab1cdefghij',   'ab12cdefghij',     'ab1defghij',        'ab12efghij']

assert [s.splitblock(2), s.splitblock(3)] == [['ab', 'cd', 'ef', 'gh', 'ij'], ['abc', 'def', 'ghi', 'j']]
 

assert List([1, 2, 3, 4]) >> 1 == [4, 1, 2, 3]
assert List([1, 2, 3, 4]) >> 4 == [1, 2, 3, 4]
assert List([1, 2, 3, 4]) << 1 == [2, 3, 4, 1]

assert 0xFFCD9AD6 == DWORD(251972843051734)
assert 0x9AD6 == WORD(251972843051734)
assert 0xD6 == BYTE(251972843051734)
assert str(QWORD(17)) == "0000000000000011"
assert 214 == BYTE(251972843051734)
assert BYTE(15 + 1)  == BYTE(15) + 1

# casting is important
assert BYTE(0xF) + DWORD(0xFFFFF00) == 0xF
assert DWORD(0xFFFFF00) + BYTE(0xF) == 0xFFFFF0F
assert DWORD(BYTE(0xF)) + DWORD(0xFFFFF00) == 0xFFFFF0F
assert int(BYTE(0xF)) + DWORD(0xFFFFF00) == 0xFFFFF0F
assert DQWORD(0xF) == OWORD(0xE) + 1

i = DWORD(0x4345669)
assert i[:3].concat(i[3:]) == i
