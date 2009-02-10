#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python

from _str import *

s = _str("abcdefghij")
assert [ s,           s << 1,       s >> 1,       (s << 1) >> 1, s << 2,       s << 3,      s << 4] == \
       ['abcdefghij', 'bcdefghija', 'jabcdefghi', 'abcdefghij', 'cdefghijab', 'defghijabc', 'efghijabcd']

assert s.setstart("d") == "defghijabc"

s = _str('abcaba')
assert s.indexes("a") == [0, 3, 5]
assert s.indexes("d") == []

s = _str("abcdefghij")
import pprint
assert [s.insert("1", 2), s.insert("12", 2), s.overwrite("1", 2), s.overwrite("12", 2)] == \
       ['ab1cdefghij',   'ab12cdefghij',     'ab1defghij',        'ab12efghij']

assert [s.splitblock(2), s.splitblock(3)] == [['ab', 'cd', 'ef', 'gh', 'ij'], ['abc', 'def', 'ghi', 'j']]
 
